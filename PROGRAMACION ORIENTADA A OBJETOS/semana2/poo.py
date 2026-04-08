class Cuenta:
    def __init__ (self, saldo_inicial):
        self.nombre= "Publica"
        self._saldo=saldo_inicial



mi_cuenta=Cuenta(1000)
print(mi_cuenta.nombre)
print(mi_cuenta._saldo)
