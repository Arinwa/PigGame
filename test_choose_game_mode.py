"""
Module dedicated for testing chooseGameMode module.
"""
import unittest
from unittest import mock
import cmd
import choosegamemode


class TestChooseGameMode(unittest.TestCase):
    """"Script for testing the choose game mode"""

    def test_choosegamemode(self):
        """Test instantiation of an object"""
        res = choosegamemode.ChooseGameMode(cmd.Cmd)
        exp = choosegamemode.ChooseGameMode
        self.assertIsInstance(res, exp)

    # make a mock of the function
    @mock.patch("singleplayer.Singleplayer.cmdloop")
    # that you want to check if it was called
    def test_do_s(self, mock1):
        """Testing do_s() executes with cmdloop() the singleplayer module"""
        choose_game_obj = choosegamemode.ChooseGameMode(
            cmd.Cmd)  # instance of the ChooseGameMode class
        choose_game_obj.do_s(self)
        self.assertTrue(mock1.called)

    # make a mock of the function
    @mock.patch("multiplayer.Multiplayer.cmdloop")
    # that you want to check if it was called
    def test_do_m(self, mock1):
        """Testing do_m() executes with cmdloop() the multiplayer module"""
        choose_game_obj = choosegamemode.ChooseGameMode(
            cmd.Cmd)  # instance of the chooseGameMode class
        choose_game_obj.do_m(self)
        self.assertTrue(mock1.called)
