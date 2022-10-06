from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^information/all/$', views.GetAllInformationFromCSVAPIView.as_view(), name='all_informations'),
    re_path(r'^information/getByPredicate/$', views.GetInformationByPredicateView.as_view(), name='predicate_information'),
    re_path(r'^information/getByPaging/$', views.GetAllInformationPagingView.as_view(), name='predicate_paging'),
    re_path(r'^information/list/$', views.InfoList.as_view(), name='list_paging'),


]