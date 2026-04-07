# Encapsulamiento

Le pondremos un candado a la informacion y crearemos "ventanillas de atencion ( getters y setters) con guardias de seguridad qu validaran quien entra y que datos se pueden modificar. 

**sintaxis** Para convertir 


```python
class Cuenta:
    def __init__ (self, saldo_inicial):
        self.nombre= "Publica"
        self._saldo=saldo_inicial



mi_cuenta=Cuenta(1000)
print(mi_cuenta.nombre)
print(mi_cuenta._saldo)

```

```python
class UsuarioBancario:
    def __init__(self, nombre_ingresado, pin_ingresado):
        self.nombre