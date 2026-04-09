# Atributos:
```python
class producto:
    pass


#fabricar dos objetos fidsicos e indepenfientes

articulo_1= producto()
articulo_2= producto()

# les vamos a asignar atributos (caracteristicas) a cda uno 
#sintaxis: objeto.atributo=valor
articulo_1.nombre= "camiseta"
articulo_1.precio= 19.99
articulo_1.cantidad= 10

articulo_2. nombre= "pantalon"
articulo_2. precio= 39.99
articulo_2.cantidad= 5

# imprimimos 
print(f"articulo 1: {articulo_1.nombre}, precio: {articulo_1.precio}, cantidad: {articulo_1.cantidad}")
print(f"articulo 2: {articulo_2.nombre}, precio: {articulo_2.precio}, cantidad: {articulo_2.cantidad}")


#ejercicio
class Empleado:
    pass

empleado_1= Empleado()
empleado_2= Empleado()
empleado_3= Empleado()

empleado_1.nombre= "Carlos"
empleado_1.cargo= "Gerente"
empleado_1.salario= 8000

empleado_2.nombre= "Marcos"
empleado_2.cargo= "Auxiliar contable"
empleado_2.salario= 4500

empleado_3.nombre= "sofia"
empleado_3.cargo= "CEO"
empleado_3.salario= 20000

print(f"empleado 1: {empleado_1.nombre}, Cargo: {empleado_1.cargo}, Salario: {empleado_1.salario}")
print(f"empleado 2: {empleado_2.nombre}, Cargo: {empleado_2.cargo}, Salario: {empleado_2.salario}")
print(f"empleado 3: {empleado_3.nombre}, Cargo: {empleado_3.cargo}, Salario: {empleado_3.salario}")

```
# metodos:
`def`
Cuando creamos un metodo (funcion) dentro de una Clase **el primer parametro siempre `self`

```python
class Empleado:
    def saludar_cliente(self):
        print(f"Hola me llamo {self.nombre}, bienvenido a nuestra tienda ")


# fabricamos el objeto
cajero=Empleado()
bodeguero= Empleado()

cajero.nombre= "Julian"
bodeguero.nombre= "carlos"


cajero.saludar_cliente()
bodeguero.saludar_cliente()
```

# EJERCICIO2
```PYTHON
class Cajaregistradora:
    def mostrar_dinero_actual(self):
        print(f"DINERO Q.{self.dinero}")
    def procesar_ventas(self):
        print("Se realizo una venta de Q.500")
        self.dinero=self.dinero+500
        print("venta procesada")

caja_registradora1= Cajaregistradora()


caja_registradora1.dinero= 500



caja_registradora1.mostrar_dinero_actual()
caja_registradora1.procesar_ventas()
caja_registradora1.mostrar_dinero_actual()
```
# EJERCICIO 3
```python
class TarjetaVIP:
    def mostrar_puntos(self):
        print(f"Sus puntos son: {self.puntos}")
    
    def sumar_puntos(self):
        self.puntos += 50
        print("Se han sumado 50 puntos por su compra")
        



tarjeta_carlos= TarjetaVIP()

tarjeta_carlos.puntos = 100

tarjeta_carlos.mostrar_puntos()
tarjeta_carlos.sumar_puntos()
tarjeta_carlos.mostrar_puntos()
```