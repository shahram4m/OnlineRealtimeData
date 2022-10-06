from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from django.conf import settings
from assignment.models import Information
from assignment.serializers import InformationSerializer
from helper.Validator import ValidatUrl
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class GetAllInformationFromCSVAPIView(APIView):

    def get(self, request, format=None):
        try:
            if settings.CSVURL and ValidatUrl(settings.CSVURL):
                #do process
                #data = read_csv_data()

                return Response({'data': "jdata"}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Bad Request, url Not Found.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetInformationByPredicateView(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            print(query)
            informations = Information.objects.filter(Q(description__icontains=query))
            data = []
            for intormation in informations:
                data.append({
                    "title": intormation.title,
                    "image": intormation.image if intormation.image else None,
                    "description": intormation.description,
                })

            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAllInformationPagingView(APIView):
    def get(self, request, format=None):
        try:
            informations = Information.objects.all()
            pagination_class = LimitOffsetPagination
            data = []
            for intormation in informations:
                data.append({
                    "title": intormation.title,
                    "image": intormation.image if intormation.image else None,
                    "description": intormation.description,
                })

            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InfoList(APIView):
    def get(self, request):
        info = Information.objects.all().order_by('created_at')
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(info, request)
        serializer = InformationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)