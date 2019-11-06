from unittest import TestCase
from sud import roll_hp


squishy = ["sorcerer", "wizard"]
light = ["bard", "cleric", "druid", "monk", "rogue", "warlock"]
medium = ["fighter", "paladin", "ranger"]
heavy = ["barbarian"]

class TestRoll_hp(TestCase):

    # Roll HP for squishy classes
    def test_roll_hp_squishy(self):
        for char in squishy:
            hp = roll_hp(char)
            self.assertTrue(1 <= hp[0] <= 6)

    # Roll HP for light armor classes
    def test_roll_hp_light(self):
        for char in light:
            hp = roll_hp(char)
            self.assertTrue(1 <= hp[0] <= 8)

    # Roll HP for medium armor classes
    def test_roll_hp_medium(self):
        for char in medium:
            hp = roll_hp(char)
            self.assertTrue(1 <= hp[0] <= 10)

    # Roll HP for heavy armor classes
    def test_roll_hp_heavy(self):
        for char in heavy:
            hp = roll_hp(char)
            self.assertTrue(1 <= hp[0] <= 12)
