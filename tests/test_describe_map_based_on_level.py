from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import describe_map_based_on_level


class TestDescribeMapBasedOnLevel(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_map_based_on_level_character_level_1(self, mockup_output):
        character = {"Stat": {"Level": 1}}
        describe_map_based_on_level(character)
        print_result = mockup_output.getvalue()
        expected_result = ("\n🕸️ UNDERGROUND - THE GARAGE 🕸️\n"
                           "A dark space is filled with stacked boxes, tools, and the smell of dust. It is dead quiet, \n"
                           "but you know you are not alone. You can sense some sneaky creatures watching your every move.\n")
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_map_based_on_level_character_level_2(self, mockup_output):
        character = {"Stat": {"Level": 2}}
        describe_map_based_on_level(character)
        print_result = mockup_output.getvalue()
        expected_result = ("\n🏠 GROUND FLOOR - LIVING ROOM 🏠\n"
                           "The once lively living room now feels quiet. Stay alert for obstacles that will try to keep you away.\n")
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_map_based_on_level_character_level_3(self, mockup_output):
        character = {"Stat": {"Level": 3}}
        describe_map_based_on_level(character)
        print_result = mockup_output.getvalue()
        expected_result = ("\n🚪 UPPER FLOOR - THE ATTIC 🚪\n"
                           "The attic is filled with forgotten toys and old memories. Someone seems to be standing guard,\n"
                           "ready to protect these treasures. Proceed with caution.\n")
        self.assertEqual(print_result, expected_result)
