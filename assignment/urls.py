from django.urls import include, re_path
from . import views

app_name = 'assignment'

urlpatterns = [
    re_path(r'^information/getByPredicate/$', views.GetInformationByPredicateView.as_view(), name='predicate_information'),
    re_path(r'^information/getAllItems/$', views.GetAllInformationView.as_view(), name='getAllItems_information'),
    re_path(r'^fileInformation/create/$', views.CreateFileInformationView.as_view(), name='create_fileInformation'),
    re_path(r'^fileInformation/getAllItems/$', views.GetAllFileInformationView.as_view(), name='getAllItems_fileInformation'),
]