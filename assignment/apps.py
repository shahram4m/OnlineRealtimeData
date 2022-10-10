from django.apps import AppConfig
from assignment.services import IntialDb


class AssignmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assignment'

    def ready(self):
        IntialDb()
        from share import scheduler
        scheduler.start()