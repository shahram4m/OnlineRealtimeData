from django.apps import AppConfig
from helper.csvDataHelper import IntialDb


class AssignmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assignment'

    def ready(self):
        IntialDb()
        from helper import SyncDbAndCsv_Job
        SyncDbAndCsv_Job.start()