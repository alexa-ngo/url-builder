from url_lib.url_builder import dict_to_str
import unittest


class TestUrlBuilder(unittest.TestCase):

    def test_no_path(self):
        input_dict = {'path': '12', 'scheme': 'http', 'hostname': 'rainforest.com', 'port': '22', 'params': {'vegetation': 'herbs', 'flowers': 'wildflowers'}}

        my_result = dict_to_str(input_dict)
        self.assertEqual("http://rainforest.com:22/12?vegetation=herbs&flowers=wildflowers", my_result)

    def test_no_port_and_params(self):
        input_dict = {'scheme': 'mailto', 'hostname': 'gold.ai', 'port': '888', 'path': 'find-location', 'params': {}}

        my_result = dict_to_str(input_dict)
        self.assertEqual("mailto://gold.ai:888/find-location", my_result)

    def test_no_params(self):
        input_dict = {'scheme': 'ftp', 'hostname': 'green.com', 'port': '4040', 'path': 'garden', 'params': {}}

        my_result = dict_to_str(input_dict)
        self.assertEqual("ftp://green.com:4040/garden", my_result)

    def test_no_scheme(self):
        input_dict = {'scheme': 'mailserver', 'hostname': 'ruby.ai', 'port': '992', 'path': 'development', 'params': {'game': 'server'}}
        my_result = dict_to_str(input_dict)
        self.assertEqual('mailserver://ruby.ai:992/development?game=server', my_result)


if __name__ == '__main__':
    unittest.main()
