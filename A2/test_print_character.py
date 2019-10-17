from unittest import TestCase
from unittest.mock import patch
from lab05 import print_character
import io


class TestPrint_character(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_no_bag(self, mock_output):
        character = ["Bahedi", ["Strength", 3], ["Dexterity", 6], ["Constitution", 9],
                     ["Intelligence", 12], ["Wisdom", 15], ["Charisma", 18]]
        expected_output = f"Your character's name is {character[0]}.\n" \
                          f"\n" \
                          f"--Attributes--\n" \
                          f"{character[1][0]}: {character[1][1]}\n" \
                          f"{character[2][0]}: {character[2][1]}\n" \
                          f"{character[3][0]}: {character[3][1]}\n" \
                          f"{character[4][0]}: {character[4][1]}\n" \
                          f"{character[5][0]}: {character[5][1]}\n" \
                          f"{character[6][0]}: {character[6][1]}\n"
        print_character(character)
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_empty_bag(self, mock_output):
        character = ["Bahedi", ["Strength", 3], ["Dexterity", 6], ["Constitution", 9],
                     ["Intelligence", 12], ["Wisdom", 15], ["Charisma", 18], []]
        expected_output = f"Your character's name is {character[0]}.\n" \
                          f"\n" \
                          f"--Attributes--\n" \
                          f"{character[1][0]}: {character[1][1]}\n" \
                          f"{character[2][0]}: {character[2][1]}\n" \
                          f"{character[3][0]}: {character[3][1]}\n" \
                          f"{character[4][0]}: {character[4][1]}\n" \
                          f"{character[5][0]}: {character[5][1]}\n" \
                          f"{character[6][0]}: {character[6][1]}\n" \
                          f"\n--Inventory--\n" \
                          f"You have no items...\n"
        print_character(character)
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_bag_with_items(self, mock_output):
        character = ["Bahedi", ["Strength", 3], ["Dexterity", 6], ["Constitution", 9],
                     ["Intelligence", 12], ["Wisdom", 15], ["Charisma", 18],
                     ["Boots of Swiftness", "Boots of Lucidity"]]
        expected_output = f"Your character's name is {character[0]}.\n" \
                          f"\n" \
                          f"--Attributes--\n" \
                          f"{character[1][0]}: {character[1][1]}\n" \
                          f"{character[2][0]}: {character[2][1]}\n" \
                          f"{character[3][0]}: {character[3][1]}\n" \
                          f"{character[4][0]}: {character[4][1]}\n" \
                          f"{character[5][0]}: {character[5][1]}\n" \
                          f"{character[6][0]}: {character[6][1]}\n" \
                          f"\n--Inventory--\n" \
                          f"Boots of Swiftness\n" \
                          f"Boots of Lucidity\n"
        print_character(character)
        self.assertEqual(expected_output, mock_output.getvalue())
