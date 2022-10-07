from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from django.conf import settings
from assignment.models import Information
from assignment.serializers import InformationSerializer
from helper.Validator import ValidatUrl
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

#get data by predicate and paging
#url sample like (http://127.0.0.1:8000/information/getByPredicate/?limit=5&offset=0&description=Description 1&title=1)
class GetInformationByPredicateView(APIView):

    # With cookie: cache requested url for each user for 1 hours
    @method_decorator(cache_page(60*2))
    @method_decorator(vary_on_cookie)
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            informations = Information.objects.all()
            title_query = self.request.query_params.get('title', None)
            description_query = self.request.query_params.get('description', None)

            if title_query:
                informations = informations.filter(Q(title__icontains=title_query))

            if description_query:
                informations = informations.filter(Q(description__contains=description_query))

            if len(informations) > 0:
                # using LimitOffsetPagination
                paginator = LimitOffsetPagination()
                result_page = paginator.paginate_queryset(informations, request)
                serializer = InformationSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#get all data by paging
#url sample like (http://127.0.0.1:8000/information/getAllItems/?limit=5&offset=5)
class GetAllInformationView(APIView):

    # With cookie: cache requested url for each user for 1 hours
    @method_decorator(cache_page(60*2))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        try:
            informations = Information.objects.all().order_by('created_at')
            if len(informations) > 0:
                #using LimitOffsetPagination
                paginator = LimitOffsetPagination()
                result_page = paginator.paginate_queryset(informations, request)
                serializer = InformationSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)