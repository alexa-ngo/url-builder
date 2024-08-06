from url_lib.url_builder_logic import Url
import unittest


class TestUrlBuilderLogic(unittest.TestCase):

    def test_no_params_1(self):
        hostname = "google.com"
        path = "maps"
        port = "1234"
        params = {}
        scheme = "http"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://google.com:1234/maps", expected_results)

    def test_no_params_and_input(self):
        hostname = "abcmouse.com"
        path = "education"
        port = "88"
        scheme = "http"

        my_url = Url(hostname, path, port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://abcmouse.com:88/education", expected_results)

    def test_no_params_one_input(self):
        hostname = "minniemouse.com"
        path = "teaparty"
        port = "4321"
        scheme = "https"

        my_url = Url(hostname, path, port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://minniemouse.com:4321/teaparty", expected_results)

    def test_no_params_and_path(self):
        hostname = "gym.com"
        path = None
        port = "11"
        params = None
        scheme = "http"

        try:
            my_url = Url(hostname, path, port, params, scheme)
            my_url.get_url()
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_no_param_google_123(self):
        hostname = "google.com"
        path = "maps"
        port = "123"
        params = {}
        scheme = "https"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://google.com:123/maps", expected_results)

    def test_no_port_path_params_petco(self):
        hostname = "petco.com"
        path = None
        port = None
        params = {}
        scheme = "http"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://petco.com", expected_results)

    def test_no_host_name_and_params(self):
        hostname = None
        path = "lost&found"
        port = "80"
        params = {}
        scheme = "http"

        try:
            my_url = Url(hostname, path, port, params, scheme)
            my_url.get_url()
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_no_scheme_path_params(self):
        hostname = "hawaii.com"
        path = None
        port = "80"
        params = {}
        scheme = None

        try:
            my_url = Url(hostname, path, port, params, scheme)
            my_url.get_url()
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_no_params_japan(self):
        hostname = "japan"
        path = "museums"
        port = "6000"
        params = None
        scheme = "https"

        try:
            my_url = Url(hostname, path, port, params, scheme)
            my_url.get_url()
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_all_attribute_none(self):

        try:
            my_url = Url()
            my_url.get_url()
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_no_scheme_uniqlo(self):
        hostname = "uniqlo.com"
        port = "88"
        path = "jackets"

        my_url = Url(hostname, path, port)
        expected_results = my_url.get_url()
        self.assertEqual("https://uniqlo.com:88/jackets", expected_results)

    def test_ideal_url(self):
        hostname = "theCoolClub.com"
        port = "443"
        path = "wall"

        my_url = Url(hostname, path, port)
        expected_results = my_url.get_url()
        self.assertEqual("https://theCoolClub.com/wall", expected_results)

    def test_no_port(self):
        scheme = "http"
        hostname = "bookstore.com"
        port = "80"
        path = "weekly-meetings"

        my_url = Url(hostname, path, port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://bookstore.com/weekly-meetings", expected_results)

    def test_http_netflix(self):
        hostname = "netflix.com"
        path = "home"
        port = "80"
        scheme = "http"

        my_url = Url(hostname, path, port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://netflix.com/home", expected_results)

    def test_https_facebook(self):
        scheme = "https"
        hostname = "facebook.com"
        port = "443"
        path = "wall-post"

        my_url = Url(hostname, path, port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://facebook.com/wall-post", expected_results)

    def test_facebook_hn_only(self):
        hostname = "facebook.com"

        my_url = Url(hostname)
        expected_results = my_url.get_url()
        self.assertEqual("https://facebook.com", expected_results)

    def test_https_scheme_params(self):
        hostname = "amazon.com"
        path = "books"
        port = "5000"
        params = {"availability": "True", "price": "$5"}

        my_url = Url(hostname, path, port, params)
        expected_results = my_url.get_url()
        self.assertEqual("https://amazon.com:5000/books?availability=True&price=$5", expected_results)

    def test_ideal_http_usa_4(self):
        hostname = "usa.whitehouse"
        path = "presidents"
        port = "1400"
        params = {"approvedBills": "20"}
        scheme = "http"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://usa.whitehouse:1400/presidents?approvedBills=20", expected_results)

# Test if one attribute is missing

    def test_no_port_two_params(self):
        hostname = "ebay.com"
        path = "accounting"
        params = {"availability": "True", "price": "$5"}
        scheme = "mailto"

        my_url = Url(hostname, path=path, params=params, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("mailto://ebay.com/accounting?availability=True&price=$5", expected_results)

    def test_parmas_not_in_order(self):
        hostname = "cafe.com"
        path = "accounting"
        port = "454"
        params = {"availability": "True", "price": "$5"}

        my_url = Url(hostname, path, port, params)
        expected_results = my_url.get_url()
        self.assertEqual("https://cafe.com:454/accounting?availability=True&price=$5", expected_results)

    def test_ftp_params(self):
        hostname = "disneyland.com"
        path = "attractions"
        port = "900"
        params = {"availability": "True", "price": "$5"}
        scheme = "ftp"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("ftp://disneyland.com:900/attractions?availability=True&price=$5", expected_results)

    def test_ftp_empty_params(self):
        hostname = "disney.com"
        path = "parks"
        port = "600"
        params = {"characters": "7", "height": "4 feet", "travel": "true"}
        scheme = "ftp"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("ftp://disney.com:600/parks?characters=7&height=4%20feet&travel=true", expected_results)

    def test_http_one_params(self):
        hostname = "target.com"
        path = "plants"
        port = "10"
        params = {"items": "2"}
        scheme = "http"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://target.com:10/plants?items=2", expected_results)

    def test_param_out_of_order(self):
        hostname = "cafe.com"
        path = "nowhere"
        port = "44"
        params = {"stretch": "goals", "height": "tooshort"}

        my_url = Url(hostname, path, port, params)
        expected_results = my_url.get_url()
        self.assertEqual("https://cafe.com:44/nowhere?stretch=goals&height=tooshort", expected_results)

    def test_path_no_port(self):
        hostname = "gardenshop.com"
        scheme = "ftp"
        path = "flowers"
        params = {"items": "2"}

        my_url = Url(hostname, path, params=params, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("ftp://gardenshop.com/flowers?items=2", expected_results)

    def test_params_three_values(self):
        hostname = "fly.com"
        port = "11"
        params = {"current-location": "losangeles", "destination": "france", "hi": "value"}

        my_url = Url(hostname, port=port, params=params)
        expected_results = my_url.get_url()
        self.assertEqual("https://fly.com:11/?current-location=losangeles&destination=france&hi=value", expected_results)
#
    def test_http_university(self):
        hostname = "university.com"
        path = "study"
        port = "443"
        params = {"attendants": "2000"}
        scheme = "http"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://university.com/study?attendants=2000", expected_results)

    def test_no_path_params_port_80(self):
        hostname = "university.com"
        port = "80"
        params = {"international": "1000", "pilots": "54", "suitcase": "100"}
        scheme = "http"

        my_url = Url(hostname, port=port, params=params, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://university.com/?international=1000&pilots=54&suitcase=100", expected_results)

    def test_no_path_params_library(self):
        hostname = "library.com"
        port = "443"
        scheme = "https"

        my_url = Url(hostname, port=port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://library.com", expected_results)

    def test_no_path_whitehouse(self):
        hostname = "usa.whitehouse"
        port = "1111"
        params = {"approvedBills": "20"}
        scheme = "http"

        my_url = Url(hostname, port=port, params=params, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("http://usa.whitehouse:1111/?approvedBills=20", expected_results)

    def test_google_key_value(self):
        hostname = "google.com"
        scheme = "https"
        params = {"current-location": "losangeles", "destination": "france"}

        my_url = Url(hostname, scheme=scheme, params=params)
        expected_results = my_url.get_url()
        self.assertEqual("https://google.com/?current-location=losangeles&destination=france", expected_results)

    def test_no_param_path_dogworld(self):
        hostname = "dogworld.com"
        port = "11"
        scheme = "https"

        my_url = Url(hostname, port=port, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://dogworld.com:11", expected_results)

    def test_no_port_path_dog(self):
        hostname = "dog.com"
        scheme = "https"

        my_url = Url(hostname, scheme=scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://dog.com", expected_results)

    def test_only_hostname(self):
        hostname = "lion.com"

        my_url = Url(hostname)
        expected_results = my_url.get_url()
        self.assertEqual("https://lion.com", expected_results)

    def test_no_scheme_port_path(self):
        hostname = "hi.com"
        params = {"stretch": "goals", "height": "tooshort", "mouse": "trap"}

        my_url = Url(hostname, params=params)
        expected_results = my_url.get_url()
        self.assertEqual("https://hi.com/?stretch=goals&height=tooshort&mouse=trap", expected_results)

    def test_hostname_path_port_params_scheme(self):
        hostname = "amazon.com"
        path = "kitchen-supplies"
        port = "1100"
        params = {"items": "2", "inventory": "True"}
        scheme = "https"

        my_url = Url(hostname, path, port, params, scheme)
        expected_results = my_url.get_url()
        self.assertEqual("https://amazon.com:1100/kitchen-supplies?items=2&inventory=True", expected_results)


if __name__ == '__main__':
    unittest.main()


