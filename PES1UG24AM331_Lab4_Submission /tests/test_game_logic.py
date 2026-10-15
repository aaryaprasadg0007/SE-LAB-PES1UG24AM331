"""Focused unit tests for the four tasks in the Galaga Repair Lab."""
import sys
import types
import unittest

# Pygame is a runtime dependency for the game. The pure logic tests can still
# run in CI without a display or an installed Pygame package using this tiny
# Vector2 substitute; actual gameplay should be tested with requirements.txt.
try:
    import pygame  # noqa: F401
except ModuleNotFoundError:
    fake_pygame = types.ModuleType("pygame")

    class Vector2:
        def __init__(self, x=0, y=None):
            if y is None:
                x, y = x
            self.x = float(x)
            self.y = float(y)

        def __iter__(self):
            yield self.x
            yield self.y

    fake_pygame.Vector2 = Vector2
    sys.modules["pygame"] = fake_pygame

import game


class BezierTests(unittest.TestCase):
    def test_curve_starts_and_ends_at_control_endpoints(self):
        p0, p1, p2, p3 = (0, 0), (10, 20), (30, 40), (50, 60)
        start = game.bezier(p0, p1, p2, p3, 0)
        end = game.bezier(p0, p1, p2, p3, 1)
        self.assertAlmostEqual(start.x, p0[0])
        self.assertAlmostEqual(start.y, p0[1])
        self.assertAlmostEqual(end.x, p3[0])
        self.assertAlmostEqual(end.y, p3[1])

    def test_midpoint_uses_squared_t_for_second_control_point(self):
        points = ((0, 0), (10, 0), (20, 0), (30, 0))
        midpoint = game.bezier(*points, 0.5)
        # Standard cubic Bézier weights at t=0.5 are 1/8, 3/8, 3/8, 1/8.
        expected_x = 0.125 * 0 + 0.375 * 10 + 0.375 * 20 + 0.125 * 30
        self.assertAlmostEqual(midpoint.x, expected_x)


class FeatureTests(unittest.TestCase):
    def test_wave_one_uses_default_enemy_colours_and_later_wave_changes_palette(self):
        game.on_wave_start(1)
        self.assertIsNone(game.enemy_tint("red"))
        game.on_wave_start(2)
        self.assertEqual(game.enemy_tint("red"), (255, 100, 120))
        self.assertIsNone(game.enemy_tint("not-an-enemy"))

    def test_wave_start_sets_banner_and_short_timer(self):
        game.on_wave_start(7)
        self.assertEqual(game._wave_banner_text, "WAVE 7")
        self.assertAlmostEqual(game._wave_banner_timer, 1.5)
        self.assertEqual(game._current_wave, 7)

    def test_shield_is_granted_every_third_wave(self):
        self.assertEqual([game.shield_charges(w) for w in range(1, 10)], [0, 0, 1, 0, 0, 1, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
