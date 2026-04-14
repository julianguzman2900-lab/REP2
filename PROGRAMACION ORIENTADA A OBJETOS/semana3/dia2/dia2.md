# Sobrecarga de operadores
+ 
5+5, 10 (Matematica)
"Hola" + "Mundo"+, "Hola Mundo" (concatenado)

billetera1+ billetera2,
- el `+`, sobreescribimos `__add__(self, otro_objeto)` (sumar)
- el `-` sobreescribimos `__sub__(self, otro_objeto)` (resta)
- el `>`,Sobreescribimos `__gt__(self, otro_objeto)` (greater than | mayor que )
- el `<`, sobreescribimos `__lt__(self,otro_objeto)` (less than | menos que )
- el `==`, sobreescribimos `__eq__(self,otro_objeto)` (equal | igual)


```python
class Billetera:
    def __init__(self, propietario, monto):
        self.propietario=propietario
        self.monto=monto


    def __add__(self, otra_billetera):
        suma_total = self.monto + otra_billetera.monto
        nuevo_propietario = f"Fondo en conjunto de {self.propietario} y {otra_billetera.propietario}"

        return Billetera(nuevo_propietario, suma total )

    def __gt__(self,otra_billetera)

        return self.monto> otra_billetera.monto



    billetera1= Billetera("Luis",1000)
    billetera2= Billetera("Juan", 500)

    if billetera1 > billetera2
    print("La billetera1 tiene mas efectivo" )
    else("La billetera2 tiene mas efectivo")
```


## La bodega de herramientas
### Modulos o librerias
### Importando cajas
Vamos a usar la palabra reservada `import` Seguida del nombre de la caja 
- Esto trae la caja entera a nuestra mesa. Para usar una herramienta que esta adentro, debemos escribir el nombre de la caja, un punti `.` y luego el nombre de la herramienta 

```python
#traemos la caja entera desde la bodega
import math
print("---- Forma 1----")

raiz= math.sqrt(5000)
```
# Forma 2

- Usamos la sintaxis `from[nombre_caja] [nombre_herramienta]`

```python
from math import pi,pow

area_circulo= pi *pow(5,2)
print(f"El area del circulo es: {area_circulo}")

```
# Forma 3
python nos permite ponerle un apodo a 


