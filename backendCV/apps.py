from django.apps import AppConfig

class BackendcvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backendCV'

    def ready(self) -> None:
        import backendCV.signals #Añadimos esta para poder enviar emails

