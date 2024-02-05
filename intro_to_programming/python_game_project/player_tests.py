# import pygame
# import unittest
# from unittest.mock import Mock, patch
# from player import Player
#
# class TestPlayer(unittest.TestCase):
#
#     def setUp(self):
#         self.screen_mock = Mock(spec=pygame.Surface)
#         self.player = Player(self.screen_mock)
#
#     def test_init(self):
#         self.assertEqual(self.player.size, 101)
#         self.assertIsNotNone(self.player.image)
#         self.assertIsNotNone(self.player.rect)
#         self.assertEqual(self.player.rect.center, (self.screen_mock.get_width() // 2, self.screen_mock.get_height() // 2))
#         self.assertEqual(self.player.jump_height, 10)
#         self.assertEqual(self.player.velocity_y, 0)
#         self.assertEqual(self.player.gravity, 1)
#         self.assertTrue(self.player.is_jumping)
#         self.assertEqual(self.player.direction, 1)
#         self.assertFalse(self.player.flip)
#         self.assertEqual(self.player.arrow_size, (25, 10))
#         self.assertEqual(self.player.arrow_color, (255, 255, 255))
#         self.assertIsNone(self.player.arrow_start_pos)
#         self.assertIsNone(self.player.arrow_end_pos)
#         self.assertFalse(self.player.is_shooting)
#
#     @patch('pygame.mouse.get_pos', return_value=(50, 50))
#     def test_update_arrow(self, mock_mouse_pos):
#         self.player.update_arrow()
#         self.assertEqual(self.player.arrow_start_pos, self.player.rect.center)
#         self.assertEqual(self.player.arrow_end_pos, (50, 50))
#
#     @patch('pygame.draw.lines')
#     def test_shoot_arrow(self, mock_draw_lines):
#         self.player.arrow_start_pos = (100, 100)
#         self.player.arrow_end_pos = (200, 200)
#         self.player.is_shooting = True
#         self.player.shoot_arrow()
#         mock_draw_lines.assert_called_once_with(self.screen_mock, self.player.arrow_color, False, mock_draw_lines.ANY, 2)
#
#     def test_move_not_shooting(self):
#         keys = {pygame.K_w: True}
#         self.player.is_shooting = False
#         self.player.move(keys)
#         self.assertTrue(self.player.is_jumping)
#
#     def test_move_shooting(self):
#         keys = {pygame.K_w: True}
#         self.player.is_shooting = True
#         self.player.move(keys)
#         self.assertFalse(self.player.is_jumping)
#
#     def test_move_jump_height(self):
#         keys = {pygame.K_w: True}
#         self.player.is_jumping = False
#         self.player.move(keys)
#         self.assertEqual(self.player.velocity_y, self.player.jump_height)
#
#     def test_move_gravity(self):
#         keys = {pygame.K_w: True}
#         self.player.is_jumping = True
#         self.player.move(keys)
#         self.assertTrue(self.player.rect.y < self.screen_mock.get_height())
#
#     def test_draw(self):
#         with patch.object(self.screen_mock, 'blit') as mock_blit:
#             self.player.draw()
#             mock_blit.assert_called_once_with(pygame.transform.flip(self.player.image, self.player.flip, False), self.player.rect)
#
# if __name__ == '__main__':
#     unittest.main()