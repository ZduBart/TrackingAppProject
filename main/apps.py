from django.apps import AppConfig

# from main.publisher import PublisherThread


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    # def ready(self):
    #     super().ready()
    #     publisher = PublisherThread()
    #     publisher.start()
