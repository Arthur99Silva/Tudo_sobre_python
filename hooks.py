"""
Antes e após hooks - Unittest

São os testes em si, execução.

setup() -> é excutado antes de cada método de teste. E util para criarmos instâncias de objetos e outros dados;
tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com
ancos de dados,

"""
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Config do setUp()
        pass

    def test_primeiro(self):
        # setUp() roda antes do teste
        # tearDown() roda depois do teste
        pass

    def test_segundo(self):
        # setUp() roda antes do teste
        # tearDown() roda depois do teste
        pass

    def tearDown(self):
        # Config do tearDown()
        pass