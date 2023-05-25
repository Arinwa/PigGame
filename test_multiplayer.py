"""
Module dedicated for testing multiplayer module.
"""
from unittest.mock import patch, mock_open
import unittest
from unittest import mock
import multiplayer


class TestMultiplayer(unittest.TestCase):
    """Test script for the multiplayer class."""

    def test_init_obj(self):
        """Test constructor"""
        res = multiplayer.Multiplayer()
        exp = multiplayer.Multiplayer
        self.assertIsInstance(res, exp)

    @patch("player.Player.set_name")
    def test_do_set_name(self, mock1):
        """Test set_name method call"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_set_name(self)
        self.assertTrue(mock1.called)
        mult_obj.turn_index = 2  # check if it works for player 2
        mult_obj.do_set_name(self)
        self.assertTrue(mock1.called)

    def test_do_hold(self):
        """Test hold hand method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_hold(self)
        self.assertEqual(mult_obj.turn_index, 2)
        # now check if the index changes to point to value 1
        mult_obj.turn_index = 2
        mult_obj.do_hold(self)
        self.assertEqual(mult_obj.turn_index, 1)

    @patch('builtins.input', return_value="l")
    @patch("player.Player.cheat")
    def test_do_cheat(self, mock1, mock_input):
        """Test cheat method call and then do_exit"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_cheat(self)
        self.assertTrue(mock1.called)
        mult_obj.turn_index = 2  # check if it works for player 2
        mult_obj.do_cheat(self)
        self.assertTrue(mock1.called)
        # mock the input when do_exit method gets called
        mult_obj.do_exit(self)
        exp = 'l'
        self.assertTrue(exp)

    @patch('builtins.input', return_value="l")
    @patch("player.Player.is_winner")
    @patch("dice.Dice.roll")
    def test_do_roll(self, mock_roll, mock_win, mock_input):
        """Test roll method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_roll(self)
        inst = mock_win.return_value
        inst.score = 100  # set score so is_winner() to return True
        self.assertTrue(mock_roll.called)

    @patch('builtins.input', return_value="l")  # patch for automatic input
    @patch("player.Player.is_winner")
    def test_update_score_check_winner(self, mock_win, mock_input):
        """Test update_score method for player 1"""
        inst = mock_win.return_value
        inst.score = 100  # set score True so is_winner() to return True
        mult_obj = multiplayer.Multiplayer()
        mult_obj.update_score_check_winner(6)
        self.assertTrue(mock_win.called)

    @patch('builtins.input', return_value="l")  # patch for automatic input
    @patch("player.Player.is_winner")
    def test_update_score_check_winner2(self, mock_is_winner, mock_input):
        """Test update_score method for player 2"""
        inst = mock_is_winner.return_value
        inst.score = 100  # set score True so isWinner() to return True
        mult_obj = multiplayer.Multiplayer()
        mult_obj.turn_index = 2
        mult_obj.update_score_check_winner(6)
        self.assertTrue(mock_is_winner.called)

    @patch("player.Player.remove_points")
    def test_remove_points_switch_turn1(self, mock_remove):
        """Test remove points for 1st player"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.remove_points_switch_turn()
        self.assertTrue(mock_remove.called)

    @patch("player.Player.remove_points")
    def test_remove_points_switch_turn2(self, mock_remove):
        """Test remove points for 2nd player"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.turn_index = 2
        mult_obj.remove_points_switch_turn()
        self.assertTrue(mock_remove.called)

    def test_dump_high_score(self):
        """Test writing player scores to file"""
        with patch('builtins.open', mock_open(read_data="data")) as mock_file:
            assert open('multiple_high_scores.txt').read() == "data"
        mock_file.assert_called_with("multiple_high_scores.txt")

    def test_do_show_scores(self):
        """Test show scores method"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open('multiple_high_scores.txt').read() == "data"
        mock_file.assert_called_with("multiple_high_scores.txt")

    @mock.patch("builtins.print")
    def test_do_start(self, mock1):
        """Test start of new game"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_start(self)
        str_1 = "You have started a new game.\n"
        mock1.assert_called_with(str_1)

    @patch("builtins.print")
    def test_do_restart(self, mock1):
        """Test restart method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_restart(self)
        str_1 = "Game has been restarted.\n"
        mock1.assert_called_with(str_1)

    @patch('builtins.input', return_value="s")  # patch for automatic input
    def test_do_exit(self, mock_input):
        """Test exit game method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_exit(self)
        exp = 'l'
        self.assertTrue(exp)
