import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from api.model.NotificationModel import Notification
from api.model.UserModel import User

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')
        title = data.get('title')
        description = data.get('description')
        user_id = data.get('user_id')
        date = data.get('date')
        
        if action == 'create':
            await self.create_notification(title, description, date, user_id)
        elif action == 'update':
            await self.update_notification(data)
        elif action == 'delete':
            await self.delete_notification(data['id'])
        
        # Respuesta al cliente
        await self.send(text_data=json.dumps({
            'message': 'Notification handled successfully'
        }))

    async def create_notification(self, title, description, date, user_id):
        try:
            user = await sync_to_async(User.objects.get)(id=user_id)
            notification = await sync_to_async(Notification.objects.create)(
                title=title,
                description=description,
                date=date,
                user_id=user
            )
        except User.DoesNotExist:
            # Si no se encuentra el usuario
            pass

    async def update_notification(self, data):
        try:
            notification = await sync_to_async(Notification.objects.get)(id=data['id'])
            notification.title = data['title']
            notification.description = data['description']
            notification.date = data['date']
            await sync_to_async(notification.save)()
        except Notification.DoesNotExist:
            # En caso no se encuentra la notificación
            pass

    async def delete_notification(self, notification_id):
        try:
            notification = await sync_to_async(Notification.objects.get)(id=notification_id)
            await sync_to_async(notification.delete)()
        except Notification.DoesNotExist:
            # En caso no se encuentra la notificación
            pass
