from django.apps import AppConfig

class AssignmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assignment'

    def ready(self):
        from helper import SyncDbAndCsv_Job
        SyncDbAndCsv_Job.start()