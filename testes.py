import unittest

from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    def test_comer(self):
        self.assertEqual(
            comer('quiabo', True),
            'Comendo quiabo agora, pois faz bem.'
        )

        self.assertEqual(
            comer('pizza', False),
            'Comendo pizza agora, pois quero morrer.'
        )



if __name__ == '__main--':
    unittest.main()

