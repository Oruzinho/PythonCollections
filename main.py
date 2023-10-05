from abc import ABCMeta, abstractmethod
from functools import total_ordering


@total_ordering
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    @property
    def codigo(self):
        return self._codigo

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"[codigo {self._codigo} saldo {self._saldo}]\n"

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo


class contaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class contaPoupança(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class contaInvestimento(Conta):
    def passa_o_mes(self):
        self._saldo *= 2.01
        self._saldo -= 5


class contaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @property
    def codigo(self):
        return self._codigo

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"[codigo {self._codigo} saldo {self._saldo}]\n"

    def __eq__(self, other):
        if type(other) != contaSalario:
            return False


conta1 = contaCorrente(1)
conta2 = contaPoupança(2)
# conta3 = Conta(3)
conta4 = contaInvestimento(4)

contas = [conta1, conta2]

print(contas[0], contas[1])

for conta in contas:
    print(f"Opa! Caiu dinheiro na conta {conta.codigo}")
    conta.deposita(1000)
    print(conta)

for conta in contas:
    print("Passou o mês...")
    conta.passa_o_mes()
    print(conta)

print("Mostrando por ordem do saldo")

for conta in sorted(contas):
    print(conta)

print(conta1 >= conta2)
