# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SyncListItemTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_list_items(index=1).fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Sync/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Lists/ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Items/1',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "data": {},
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "index": 100,
                "list_sid": "ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/100"
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_list_items(index=1).fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_list_items(index=1).delete(if_match="if_match")

        headers = {'If-Match': "if_match", }
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/Sync/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Lists/ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Items/1',
            headers=headers,
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_list_items(index=1).delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_list_items.create(data={})

        values = {'Data': serialize.object({}), }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Sync/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Lists/ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Items',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "data": {},
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "index": 100,
                "list_sid": "ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/100"
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_list_items.create(data={})

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_list_items.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Sync/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Lists/ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Items',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "items": [],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?From=from&Bounds=inclusive&Order=asc&PageSize=50&Page=0",
                    "key": "items",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?From=from&Bounds=inclusive&Order=asc&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_list_items.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "items": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "created_by": "created_by",
                        "data": {},
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "index": 100,
                        "list_sid": "ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "revision": "revision",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/100"
                    }
                ],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?From=from&Bounds=inclusive&Order=asc&PageSize=50&Page=0",
                    "key": "items",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?From=from&Bounds=inclusive&Order=asc&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_list_items.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .sync_list_items(index=1).update(data={}, if_match="if_match")

        values = {'Data': serialize.object({}), }

        headers = {'If-Match': "if_match", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Sync/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Lists/ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Items/1',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Sync/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Lists/ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Items/1',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "data": {},
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "index": 100,
                "list_sid": "ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Lists/ESaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/100"
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_lists(sid="ESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .sync_list_items(index=1).update(data={})

        self.assertIsNotNone(actual)
