from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse
import datetime

from clientdb.models import Client
from clientdb.views import ClientList

class ClientListPaginationTestCase(TestCase):

    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Client.objects.create(
                client_ref = 'N{}'.format(n),
                dob = datetime.date.today(),
                full_name = 'Person {}'.format(n),
                hk_id = 'X123456({})'.format(n),
                sex = 'O',
                tel = '123456{}'.format(n),
            )

    def testFirstPage(self):
        client_list_path = reverse('clientdb:ClientList')
        request = RequestFactory().get(path=client_list_path)
        response = ClientList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                client_list_path, 1, 1),
            response.rendered_content)