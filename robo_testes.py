import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def test_carregar(self):
        megaman = Robo('Mega Man', bateria=50)
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)


if __name__ == '__main__':
    unittest.main()
