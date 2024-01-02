"""
Unittest

Testes unitários - Teste é a forma de se testar unidades individuais de código fonte.
Unidades individuais podem ser: funções, métodos, classes, módulos etc.Não é especifico do Python.

Para criar nossos testes, criamos classes que herdam de unittest. TestCase
e a partir de então ganhamos todos 05 'assertions' presentes no módulo.
Para rodar os testes, utili:amos unittest.main()

TestCase -> Casos de teste para sua unidade
# Conhecendo as assertions

Método
assertEqual (a, b)          a == b
assertNotEqual (a, b)       a != b
assertTrue(x)               x verdadeiro
assertFalse(x)              x falso
assertls(a, b)              a é b
assertrsNot(a, b)           a não é b
assertIfNone(x)             x None
assertrsNotNone (x)         x não None
assertln(a, b)              a está em b
assertNotIn(a, b)           a não está em b
assertIsIstance(a, b)       a instãncia de b
assertNotIsInstance(a, b)   a não instãncia de b



"""
# TDD

class TestCase:
    pass