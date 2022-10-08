from unittest import TestCase

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from assignment.models import Information
from assignment.serializers import InformationSerializer


class GetAllInformationTest(APITestCase):
    """ Test module for GET all information API """

    def setUp(self):
        pass

    def test_get_all_information(self):
        # get API response
        url = reverse("assignment:getAllItems_information")
        print(url)
        response = self.client.get(url)
        print(response)
        # get data from db
        informations = Information.objects.all()
        serializer = InformationSerializer(informations, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_By_Predicate(self):
        # get API response
        from rest_framework.test import RequestsClient
        client = RequestsClient()
        response = client.get('http://testserver:801/information/getAllItems/?limit=5&offset=5', format='json')
        assert response.status_code == 200
        self.assertEqual(len(response.data), 5)