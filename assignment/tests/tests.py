import requests
from rest_framework.test import APITestCase
from elements import settings
import csv

class InformationAPITest(APITestCase):
    """ Test module for GET all information API """

    def setUp(self):
        pass

    def test_get_Information_by_Predicate_without_predict(self):
        # get API response
        response = requests.get('http://127.0.0.1:801/information/getByPredicate/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 24)

    def test_get_Information_by_Predicate_with_predicate(self):
        # get API response getByPredicate
        payload = {'limit': '5', 'offset': '0', 'description': 'Description 1', 'title': '1'}
        response = requests.get('http://127.0.0.1:801/information/getByPredicate/', params=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 11)
        self.assertEqual(len(response.json()['results']), 5)

    def test_get_Information_all_by_Paging(self):
        # get API response getAllItems
        payload = {'limit': '5', 'offset': '0'}
        response = requests.get('http://127.0.0.1:801/information/getAllItems/', params=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 24)
        self.assertEqual(len(response.json()['results']), 5)

    def test_get_FileInformation_all_by_Paging(self):
        # get API response getAllItems
        payload = {'limit': '5', 'offset': '0'}
        response = requests.get('http://127.0.0.1:801/fileInformation/getAllItems/', params=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 24)
        self.assertEqual(len(response.json()['results']), 5)

    def test_post_FileInformation_all_by_Paging(self):
        # get API response getAllItems
        payload = {
                "url": "www.newcsvfile.com/csvfile",
            }
        response = requests.post('http://127.0.0.1:801/fileInformation/create/', payload)
        self.assertEqual(response.status_code, 200)

    def test_valid_url_and_haveContentTypeCsv(self):
        # test valid url and have csv contact
        headers = requests.head(settings.CSVURL, allow_redirects=True).headers
        self.assertEqual(headers.get('content-type'), 'text/csv')

    def test_if_file_len(self):
        # test len csv contact
        reader = csv.reader(settings.CSVURL, delimiter=',', quotechar='"')
        self.assertEqual(len(list(reader)), 0)
