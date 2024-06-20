from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.urls import reverse
from django.db.models import Sum
from django_rest_passwordreset.signals import reset_password_token_created
from decimal import Decimal
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Sale, SaleDetailsService, SaleDetailsProduct

# Para enviar un correo electronico de recuperación de contraseña
@receiver(reset_password_token_created)
def password_reset_token_created(sender,instance,reset_password_token,*args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.email,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }
    email_html_message = """<p>Hola,</p>
        <p>Hemos recibido una solicitud para restablecer tu contraseña. Por favor, haz clic en el enlace de abajo para restablecer tu contraseña:</p>
        <p><a href="""+context['reset_password_url'] +""">Restablecer Contraseña</a></p>
        <p>Si no solicitaste este restablecimiento de contraseña, puedes ignorar de forma segura este correo electrónico.</p>"""
            # message:
    email_plaintext_message="message test" #Si no colocamos esto el correo no se enviara luego se cambiara el mensaje por el html
    msg = EmailMultiAlternatives(
        # title:
        "Recuperar contraseña de {title}".format(title="CRM"),
        # message:
        email_plaintext_message,
        # from:
        "cmr.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message,"text/html") #Enviar html
    msg.send()

@receiver([post_save, post_delete], sender=SaleDetailsService)
@receiver([post_save, post_delete], sender=SaleDetailsProduct)
def update_sale_total(sender, instance, **kwargs):
    sale = instance.sale  # Obtener instancia de Sale asociada

    # Calcular nuevo total de Sale basado en SaleDetailsService y SaleDetailsProduct
    total_sale_details_service = SaleDetailsService.objects.filter(sale=sale).aggregate(total_amount=Sum('total_item_amount'))['total_amount'] or Decimal('0.00')
    total_sale_details_product = SaleDetailsProduct.objects.filter(sale=sale).aggregate(total_amount=Sum('total_item_amount'))['total_amount'] or Decimal('0.00')

    sale.total = total_sale_details_service + total_sale_details_product
    sale.save()
