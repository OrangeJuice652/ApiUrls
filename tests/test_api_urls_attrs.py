from apiurls.api_urls import ApiUrlsMixin
from apiurls.sub_directories import SubDirecotries
from unittest import TestCase


class TestInitApiUrls(ApiUrlsMixin):
    _protocol = 'https'
    _domain = 'test.co.jp'
    _sub_directories = SubDirecotries(
        {
            'test_api_1':'/test/1',
            'test_api_2': '/test/2',
        }
    )


class TestApiUrlsAttrs(TestCase):
    def test_init_api_urls(self):
        api_urls = TestInitApiUrls()
        self.assertEqual(
            api_urls.test_api_1,
            'https://test.co.jp/test/1',
        )
        self.assertEqual(
            api_urls.test_api_2,
            'https://test.co.jp/test/2',
        )
