import random
import time
import sys
import unittest
from PyQt6.QtWidgets import QApplication
from constants import STATUS_ICONS, Status
from main import MainWindow, QIcon

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.window = MainWindow()

    def tearDown(self):
        self.window.close()

    def test_initial_status(self):
        self.assertEqual(self.window.status, Status.READY)

    def test_mines_label(self):
        self.assertEqual(self.window.mines.text(), f"{self.window.n_mines:03d}")

    def test_clock_label(self):
        self.assertEqual(self.window.clock.text(), "000")

    def test_button_icon(self):
        self.assertEqual(self.window.button.icon().name(), QIcon("./images/smiley.png").name())

    def test_reset_map(self):
        self.window.reset_map()
        mine_count = sum(1 for x in range(self.window.b_size) for y in range(self.window.b_size) if self.window.grid.itemAtPosition(y, x).widget().is_mine)
        self.assertEqual(mine_count, self.window.n_mines)

    def test_update_status(self):
        self.window.update_status(Status.PLAYING)
        self.assertEqual(self.window.status, Status.PLAYING)
        self.assertEqual(self.window.button.icon().name(), QIcon(STATUS_ICONS[Status.PLAYING]).name())

    def test_update_timer(self):
        self.window.update_status(Status.PLAYING)
        self.window._timer_start_nsecs = int(time.time()) - 5
        self.window.update_timer()
        self.assertEqual(self.window.clock.text(), "005")

    def test_game_over(self):
        self.window.game_over()
        self.assertEqual(self.window.status, Status.FAILED)
        self.assertEqual(self.window.button.icon().name(), QIcon(STATUS_ICONS[Status.FAILED]).name())
   
    def test_reset_map_b_size(self):
        self.window.reset_map()
        for x in range(self.window.b_size):
            for y in range(self.window.b_size):
                self.assertIsNotNone(self.window.grid.itemAtPosition(y, x))

    def test_reset_map_no_out_of_bounds(self):
        self.window.reset_map()
        for x in range(self.window.b_size):
            for y in range(self.window.b_size):
                w = self.window.grid.itemAtPosition(y, x).widget()
                self.assertFalse(w.is_mine and w.is_start)
                
    def test_get_surrounding(self):
        self.window.reset_map()
        x, y = 1, 1
        surrounding_positions = self.window.get_surrounding(x, y)
        expected_positions = [
            self.window.grid.itemAtPosition(yi, xi).widget()
            for xi in range(max(0, x - 1), min(x + 2, self.window.b_size))
            for yi in range(max(0, y - 1), min(y + 2, self.window.b_size))
        ]
        self.assertEqual(surrounding_positions, expected_positions)

    def test_game_success(self):
        self.window.reset_map()
        for x in range(self.window.b_size):
            for y in range(self.window.b_size):
                w = self.window.grid.itemAtPosition(y, x).widget()
                if not w.is_mine:
                    w.click()
        self.assertEqual(self.window.status, Status.SUCCESS)
        self.assertEqual(self.window.button.icon().name(), QIcon(STATUS_ICONS[Status.SUCCESS]).name())
        
    def test_button_pressed_reset(self):
        self.window.update_status(Status.READY)
        self.window.button_pressed()
        self.assertEqual(self.window.status, Status.READY)
        mine_count = sum(1 for x in range(self.window.b_size) for y in range(self.window.b_size) if self.window.grid.itemAtPosition(y, x).widget().is_mine)
        self.assertEqual(mine_count, self.window.n_mines)

    def test_button_pressed_failed(self):
        self.window.update_status(Status.FAILED)
        self.window.button_pressed()
        self.assertEqual(self.window.status, Status.FAILED)
        for x in range(self.window.b_size):
            for y in range(self.window.b_size):
                w = self.window.grid.itemAtPosition(y, x).widget()
                self.assertTrue(w.is_revealed)


if __name__ == "__main__":
    unittest.main()