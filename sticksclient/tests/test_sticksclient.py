#
#   Copyright (c) 2015 EUROGICIEL
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

"""
test_python-sticksclient
----------------------------------

Tests for `python-sticksclient` module.
"""
import mock

from sticksclient import client
from sticksclient.tests import base
from sticksclient.v1 import tickets


def my_mock(*a, **b):
    return [a, b]


def my_mock_ticket(*a, **b):
    b['ticket'] = b
    return [a, b]


api = mock.MagicMock(json_request=my_mock)


class TestSticksclient(base.TestCase):

    def test_create_client_instance(self):
        endpoint = 'http://no-resolved-host:8001'
        test_client = client.Client('1', endpoint=endpoint,
                                    token='1', timeout=10)
        self.assertIsNotNone(test_client.tickets)

    def test_ticket_manager_list(self):
        manager = tickets.TicketManager(api)
        result = manager.list(data={})
        self.assertEqual([], result)

    def test_ticket_manager_get(self):
        api = mock.MagicMock(json_request=my_mock_ticket)
        manager = tickets.TicketManager(api)
        result = manager.get('test')
        self.assertIsNotNone(result.manager)

    def test_ticket_manager_create(self):
        api = mock.MagicMock(json_request=my_mock_ticket)
        manager = tickets.TicketManager(api)
        result = manager.create('{foo:bar}')
        self.assertIsNotNone(result.manager)
