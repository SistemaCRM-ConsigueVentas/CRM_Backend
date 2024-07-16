import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.paginator import Paginator
from api.model.NotificationModel import Notification
from api.model.UserModel import User

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'notifications'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.list_notifications({'page': 1})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            action = data.get('action')

            if action == 'create':
                await self.create_notification(data)
            elif action == 'update':
                await self.update_notification(data)
            elif action == 'delete':
                await self.delete_notification(data['id'])
            elif action == 'list':
                await self.list_notifications(data)
            elif action == 'archive':
                await self.archive_notification(data['notification_id'], data['user_id'])
            elif action == 'unarchive':
                await self.unarchive_notification(data['notification_id'], data['user_id'])
        
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON'
            }))
        except KeyError as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': f'Missing key: {str(e)}'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def create_notification(self, data):
        try:
            user = await sync_to_async(User.objects.get)(id=data['user_id'])
            notification = await sync_to_async(Notification.objects.create)(
                title=data['title'],
                description=data['description'],
                date=data['date'],
                user_id=user
            )

            notification_data = {
                'id': notification.id,
                'title': notification.title,
                'description': notification.description,
                'date': notification.date,
                'user_id': notification.user_id.id,
                'status': notification.status,
                'list_archives': json.loads(notification.list_archives)
            }

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'notification_message',
                    'message': notification_data
                }
            )
        except User.DoesNotExist:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'User does not exist'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))    

    async def update_notification(self, data):
        try:
            notification = await sync_to_async(Notification.objects.get)(id=data['id'])
            notification.title = data['title']
            notification.description = data['description']
            notification.date = data['date']
            await sync_to_async(notification.save)()

            await self.list_notifications({'type': 'replace-list'})            
        
        except Notification.DoesNotExist:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Notification does not exist'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def delete_notification(self, notification_id):
        try:
            notification = await sync_to_async(Notification.objects.get)(id=notification_id)
            await sync_to_async(notification.delete)()
            
            await self.list_notifications({'page': 1, 'type': 'replace-list'})
            
        except Notification.DoesNotExist:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Notification does not exist'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def list_notifications(self, data):
        try: 
            page_number = data.get('page', 1)       
            type_message = data.get('type', 'list-all')     
            notifications = await sync_to_async(list)(Notification.objects.all().order_by('-date'))
            paginator = Paginator(notifications, 10)                        
            page_obj = paginator.get_page(page_number)            

            notifications_data = []
            for notification in page_obj.object_list:
                notification_data = await sync_to_async(lambda n: {
                    'id': n.id,
                    'title': n.title,
                    'description': n.description,
                    'date': n.date.isoformat(),
                    'user_id': n.user_id.id,
                    'status': n.status,
                    'list_archives': json.loads(n.list_archives)
                })(notification)
                notifications_data.append(notification_data)
            
            await self.send(text_data=json.dumps({
                'type': type_message,
                'notifications': notifications_data,
                'has_next': page_obj.has_next(),
                'has_previous': page_obj.has_previous(),
                'page': page_number,
                'total_pages': paginator.num_pages
            }))
        except Exception as e: 
            print(f'Error al enviar lista: {e}')
            pass
    
    async def archive_notification(self, notification_id, user_id):
        try:            
            notification = await sync_to_async(Notification.objects.get)(id=notification_id)    
            
            await sync_to_async(notification.add_to_archived)(user_id)        
            await self.list_notifications({'type': 'replace-list'})

        except Notification.DoesNotExist:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Notification does not exist'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def unarchive_notification(self, notification_id, user_id):
        try:
            notification = await sync_to_async(Notification.objects.get)(id=notification_id)
            
            await sync_to_async(notification.remove_from_archived)(user_id)
            await self.list_notifications({'type': 'replace-list'})

        except Notification.DoesNotExist:
            pass

    async def notification_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'single-list',
            'data': event['message']
        }))
        