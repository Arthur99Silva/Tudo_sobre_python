
from entidade import Entidade, Cliente, Conta, Transacao

class Persistente:
    def __init__(self):
        self._entidades = []
    
    def inserir(self, entidade):
        self._entidades.append(entidade)
    
    def alterar(self, entidade):
        for i, e in enumerate(self._entidades):
            if e.get_id() == entidade.get_id():
                self._entidades[i] = entidade
                return
        raise EntidadeNaoEncontradaError(f"Entidade com id {entidade.get_id()} não encontrada")
    
    def excluir(self, entidade):
        try:
            self._entidades.remove(entidade)
        except ValueError:
            raise EntidadeNaoEncontradaError(f"Entidade com id {entidade.get_id()} não encontrada")
    
    def buscar_por_id(self, id):
        for entidade in self._entidades:
            if entidade.get_id() == id:
                return entidade
        raise EntidadeNaoEncontradaError(f"Entidade com id {id} não encontrada")
    
    def __str__(self):
        return "\n".join(str(e) for e in self._entidades)


class BancoDados:
    def __init__(self):
        self._clientes = Persistente()
        self._contas = Persistente()
        self._transacoes = Persistente()
    
    def get_clientes(self):
        return self._clientes
    
    def set_clientes(self, clientes):
        self._clientes = clientes
    
    def get_contas(self):
        return self._contas
    
    def set_contas(self, contas):
        self._contas = contas
    
    def get_transacoes(self):
        return self._transacoes
    
    def set_transacoes(self, transacoes):
        self._transacoes = transacoes


class EntidadeNaoEncontradaError(Exception):
    pass
