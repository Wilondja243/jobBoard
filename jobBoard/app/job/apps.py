from django.apps import AppConfig


class JobConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobBoard.app.job'

    def ready(self):
        import jobBoard.app.job.signals
