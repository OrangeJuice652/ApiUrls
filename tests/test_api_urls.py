from api_urls import ApiUrlsMeta
from sub_directories import SubDirecotries
from unittest import TestCase


class TestNewApiUrlsMeta(TestCase):

    def test_new_api_urls_is_success(self):
        class TestApiUrls(metaclass=ApiUrlsMeta):
            __protocol = 'https'
            __domain = 'test.co.jp'
            __sub_directories = SubDirecotries(
                {
                    'test_api':'/test',
                }
            )
    
    def test_new_api_urls_dont_define_protocol(self):
        with self.assertRaises(ValueError) as e:
            class TestApiUrls(metaclass=ApiUrlsMeta):
                __domain = 'test.co.jp'
                __sub_directories = SubDirecotries(
                    {
                        'test_api':'/test',
                    }
                )

            self.assertEqual(
                e.message,
                'ApiProtocol is required',
            )

    def test_new_api_urls_dont_define_domain(self):
        with self.assertRaises(ValueError) as e:
            class TestApiUrls(metaclass=ApiUrlsMeta):
                __protocol = 'https'
                __sub_directories = SubDirecotries(
                    {
                        'test_api':'/test',
                    }
                )

            self.assertEqual(
                e.message,
                'ApiDomain is required',
            )

    def test_new_api_urls_dont_define_subdirs(self):
        with self.assertRaises(ValueError) as e:
            class TestApiUrls(metaclass=ApiUrlsMeta):
                __protocol = 'https'
                __domain = 'test.co.jp'

            self.assertEqual(
                e.message,
                'SubDirectories is required',
            )
    
    def test_new_api_urls_has_invalid_subdirs(self):
        with self.assertRaises(TypeError) as e:
            class TestApiUrls(metaclass=ApiUrlsMeta):
                __protocol = 'https'
                __domain = 'test.co.jp'
                __sub_directories = {
                    'test_api':'/test',
                }

            self.assertEqual(
                e.message,
                '__sub_directories is not SubDirecotries',
            )


class TestInitApiUrls(metaclass=ApiUrlsMeta):
            __protocol = 'https'
            __domain = 'test.co.jp'
            __sub_directories = SubDirecotries(
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
