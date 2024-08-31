from apiurls.api_urls import ApiUrlsMixin
from apiurls.sub_directories import SubDirecotries
from unittest import TestCase


class TestNewApiUrlsMixin(TestCase):
    def test_new_api_urls_is_success(self):
        class TestApiUrls(ApiUrlsMixin):
            _protocol = 'https'
            _domain = 'test.co.jp'
            _sub_directories = SubDirecotries(
                {
                    'test_api':'/test',
                }
            )

    def test_new_api_urls_dont_define_protocol(self):
        with self.assertRaises(ValueError) as e:
            class TestApiUrls(ApiUrlsMixin):
                _domain = 'test.co.jp'
                _sub_directories = SubDirecotries(
                    {
                        'test_api':'/test',
                    }
                )

        self.assertEqual(
            str(e.exception),
            'ApiProtocol is required',
        )

    def test_new_api_urls_dont_define_domain(self):
        with self.assertRaises(ValueError) as e:
            class TestApiUrls(ApiUrlsMixin):
                _protocol = 'https'
                _sub_directories = SubDirecotries(
                    {
                        'test_api':'/test',
                    }
                )

            self.assertEqual(
                str(e.exception),
                'ApiDomain is required',
            )

    def test_new_api_urls_dont_define_subdirs(self):
        with self.assertRaises(ValueError) as e:
            class TestApiUrls(ApiUrlsMixin):
                _protocol = 'https'
                _domain = 'test.co.jp'

            self.assertEqual(
                str(e.exception),
                'SubDirectories is required',
            )

    def test_new_api_urls_has_invalid_subdirs(self):
        with self.assertRaises(TypeError) as e:
            class TestApiUrls(ApiUrlsMixin):
                _protocol = 'https'
                _domain = 'test.co.jp'
                _sub_directories = {
                    'test_api':'/test',
                }

            self.assertEqual(
                str(e.exception),
                '_sub_directories is not SubDirecotries',
            )
