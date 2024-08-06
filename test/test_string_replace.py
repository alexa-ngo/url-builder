from url_lib.url_builder_string_replace import get_params
import unittest


class TestStringReplace(unittest.TestCase):

    def test_space_octo_rightbrace_carrot(self):

        input = {'current-location': 'los angeles', 'destination': 'fra#nce', 'numbers': 'the-dictionary-}', 'celebname': 'marykate&ashley', 'shop-name': 'the-carrot-^-shop'}
        expected_results = get_params(input)
        self.assertEqual("?current-location=los%20angeles&destination=fra%23nce&numbers=the-dictionary-%7D&celebname=marykate%26ashley&shop-name=the-carrot-%5E-shop", expected_results)

    def test_rightbracket_leftcarrot_percent_pipe(self):

        input = {'style': 'rightbracket]', 'money_amount': 'dollars<greater', 'numbers': 'discount-of10%-off', 'chores': 'fixing-the-pipe|here'}
        expected_results = get_params(input)
        self.assertEqual("?style=rightbracket%5D&money_amount=dollars%3Cgreater&numbers=discount-of10%25-off&chores=fixing-the-pipe%7Chere", expected_results)

    def test_tilde_greaterthan_leftbrace_backslash(self):

        input = {'estimate': '~75', 'money_amount': 'dollars>greater', 'dict': 'thewordsdict{', 'relax': 'thebackslashes\\'}
        expected_results = get_params(input)
        self.assertEqual("?estimate=%7E75&money_amount=dollars%3Egreater&dict=thewordsdict%7B&relax=thebackslashes%5C", expected_results)

    def test_leftbracket_semicolon_forwardslash_at(self):

        input = {'bracket': 'leftbracket[', 'working-list': 'longlist;', 'slashes': 'forwards/', 'email-address': 'alexa@hello.com'}
        expected_results = get_params(input)
        self.assertEqual("?bracket=leftbracket%5B&working-list=longlist%3B&slashes=forwards%2F&email-address=alexa%40hello.com", expected_results)

    def test_question_equal_colon_ampersand(self):

        input = {'asking': 'a-question?', 'checking-fair': 'data-is-equal=', 'another-list': 'the-semi-colon:', 'more-information': 'the-ampersand&'}
        expected_results = get_params(input)
        self.assertEqual("?asking=a-question%3F&checking-fair=data-is-equal%3D&another-list=the-semi-colon%3A&more-information=the-ampersand%26", expected_results)


if __name__ == '__main__':
    unittest.main()