"""
Module dedicated for testing player module.
"""
import unittest
from unittest.mock import patch
import player


class TestPlayerClass(unittest.TestCase):
    """Test script for the player class."""

    @patch('builtins.input', return_value="Arinze")
    def test_set_name(self, mock_input):
        """"Tests set name"""
        player_obj = player.Player(1)
        player_obj.set_name()
        exp = player_obj.name == "Arinze"
        self.assertTrue(exp)

    def test_update_score(self):
        """Test update_score() method."""
        player_obj = player.Player(1)
        add = 6
        res = player_obj.score + add
        player_obj.update_score(add)
        exp = player_obj.score
        self.assertEqual(res, exp)

    def test_is_winner(self):
        """Test is_winner method."""
        player_obj = player.Player(1)
        player_obj.score = 100
        res = player_obj.is_winner()
        exp = True
        self.assertEqual(res, exp)

    def test_remove_points(self):
        """Test remove points from turn"""
        player_obj = player.Player(1)
        player_obj.score = 10
        player_obj.score_turn = 4
        res = player_obj.score - player_obj.score_turn
        exp = player_obj.remove_points()
        self.assertEqual(res, exp)

    def test_cheat(self):
        """Test cheat method"""
        player_obj = player.Player(1)
        player_obj.cheat()
        self.assertEqual(player_obj.is_cheater, True)
