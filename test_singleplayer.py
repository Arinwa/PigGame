"""
Module dedicated for testing singleplayer module.
"""

import unittest
from unittest import mock
from unittest.mock import patch, mock_open
import singleplayer


class TestSingleplayer(unittest.TestCase):
    """Singleplayer test class"""

    @patch('builtins.input', return_value="n")
    def test_init_(self, mock_const):
        """Test init object"""
        s_obj = singleplayer.Singleplayer()
        e_obj = singleplayer.Singleplayer
        self.assertIsInstance(s_obj, e_obj)

    @patch('builtins.input', return_value="n")
    @patch("player.Player.set_name")
    def test_do_set_name(self, mock_set, mock_const):
        """Test dosetname method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_set_name(self)
        self.assertTrue(mock_set.called)

    @patch("bot.Bot.bot_turn")
    @patch('builtins.input', return_value="n")
    def test_do_hold(self, mock_turn, mock_const):
        """Test do_hold method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_hold(self)
        self.assertTrue(mock_turn.called)

    @patch('builtins.input', return_value="n")
    @patch("player.Player.cheat")
    def test_do_cheat(self, mock_cheat, mock_const):
        """Test do cheat method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_cheat(self)
        self.assertTrue(mock_cheat)

    @patch("player.Player.is_winner")
    @patch("dice.Dice.roll")
    @patch('builtins.input', return_value="n")
    def test_do_roll(self, mock_roll, mock_winner, mock_const):
        """Test do roll method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_roll(self)
        inst = mock_winner.return_value
        inst.score = 100  # set score True so isWinner() to return True
        self.assertTrue(mock_roll.called)

    @patch("singleplayer.Singleplayer.do_exit")
    @patch("player.Player.update_score")
    @patch('builtins.input', return_value="n")
    @patch("player.Player.is_winner")
    def test_update_score_check_winner(
            self, mock_win, mock_update, mock_exit, mock_const):
        """Test updating player score"""
        inst = mock_win.return_value
        inst.score = 100    # set score True so isWinner() to return True
        s_obj = singleplayer.Singleplayer()
        s_obj.update_score_check_winner(6)
        self.assertTrue(mock_update.called)
        self.assertTrue(mock_exit.called)

    @patch("player.Player.remove_points")
    @patch('builtins.input', return_value="n")
    def test_remove_points_switch_turn(
            self, mock_called, mock_const):
        """Test remove points and switch turn methods"""
        s_obj = singleplayer.Singleplayer()
        s_obj.remove_points_switch_turn()
        self.assertTrue(mock_called.called)

    def test_dump_high_score(self):
        """Test writing player scores to file"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open('singlepl_high_scores.txt').read() == "data"
        mock_file.assert_called_with("singlepl_high_scores.txt")

    def test_do_show_scores(self):
        """Test show scores method"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open('singlepl_high_scores.txt').read() == "data"
        mock_file.assert_called_with("singlepl_high_scores.txt")

    @mock.patch("builtins.print")
    @patch('builtins.input', return_value="n")
    def test_do_start(self, mock_const, mock1):
        """Test do start method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_start(self)
        str_1 = "Difficulty set to NORMAL.\n"
        mock1.assert_called_with(str_1)
