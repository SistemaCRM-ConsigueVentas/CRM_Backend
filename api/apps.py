from django.apps import AppConfig

class apiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self) -> None:
        import api.signals #Añadimos esta para poder enviar emails

