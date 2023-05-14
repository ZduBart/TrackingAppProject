from django.apps import AppConfig

# from main.publisher import PublisherThread


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    """
    Uncomment if using threads
    """
    # def ready(self):
    #     super().ready()
    #     publisher = PublisherThread()
    #     publisher.start()
