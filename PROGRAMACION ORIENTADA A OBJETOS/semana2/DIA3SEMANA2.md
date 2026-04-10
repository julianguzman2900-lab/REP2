# El estilo profesional de python(`@property`)

`cliente.pin= 1234`
property se le llama usar Decoradores


# Sintaxis del decorador
*  **Para el getter**: Escribimos `@property` justo encima del metodo. El DEBE y TIENE que llamarse exactamente igual que el atributo (sin los guiones bajos)
* **Para el Setter**: Escribamos `@nombre_del_metodo.setter` justo encima del metodo modificador 

##  micro ejemplo

```python
class Temperatura:
    def __init__(self):
    self.grados= 20

    

    @property
    def grados(self):
        return self._grados
       
    
     @grados.setter
    def grados(self,nuevo_grado):
        if nuevo_grado <0:
            print("Temperatura invalida")
        else:
            self.__grados = nuevo_grado 



clima = Temperatura()
clima._grados = 50
print(clima.grados)
```

# Ejercicio 1
```python
class Empleado:
    def __init__(self):
     self.__salario= 300


    @property
    def salario(self):
       return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
       if nuevo_salario  <=300:
          print("Salario invalido")
       else:
          self.__salario = nuevo_salario
          print("tu nuevo salario es:")
          

salario1= Empleado()

print(salario1.salario)

salario1.salario= 500
print(salario1.salario)
```

# Ejercicio 2
```python


```


# Atributos y metodos de clase
## Atributo de clase
```python
class Tienda:

    #atributo de la clase (APLICA A TODOS)

    impuesto_iva= 0.13

    def __init__(self,productos):
        self.productos=productos
```


# metododos de la clase

`@classmethod`->`cls`
self->objeto
cls->clas

se usa exclusivamente para leer o modificar los atributos de una clase

```python
class Tienda:

    #atributo de la clase (APLICA A TODOS)

    impuesto_iva= 0.13

    def __init__(self,productos):
        self.productos=productos

    @classmethod
    def cambiar_impuesto(cls, nuevo_impuesto):
        cls.impuesto_iva = nuevo_impuesto


Tienda.cambiar_impuesto(0.15)
```


```PYTHON
class RegistroVisitantes:

    total_personas=0

    def __init__(self, nombre_visitante):
        self.nombre=nombre_visitante

        RegistroVisitantes.total_personas+=1
        
        print(f"{self.nombre} ha ingresado. La pizarra global ahora marca : {RegistroVisitantes.total_personas} ")



persona1=RegistroVisitantes("Maria") 

persona2= RegistroVisitantes("Carlos")

persona3=RegistroVisitantes("Julian")

print(f"\nTotal final del dia de personas es: {RegistroVisitantes.total_personas}")
```



# Reto integrador
4. **Seguridad**
    * Crea un `@propertyPS 
` llamado `saldo` que actúe como Getter 
      * **OJO:** No hagas el Setter para el saldo, el saldo no se debe poder sobrescribir con un `=`, solo debe cambiar mediante depósitos y retiros.
    * Crea un `@property` llamado `titular` (Getter).
    * Crea su respectivo `@titular.setter`. La validación debe asegurar que el nombre no esté en blanco
5. **Métodos de Instancia**
    * Crea un método `depositar(self, cantidad)`. Si la cantidad es mayor a 0, súmala al saldo 
    * Crea un método `retirar(self, cantidad)`. Solo permite el retiro si hay suficiente dinero en la cuenta.
    * Crea un método `proyectar_interes(self)`. Este método debe multiplicar el saldo privado actual por la `tasa_interes_global` de la clase e imprimir cuánto dinero ganará el cliente este *año*.
6. **Método de Clase:**
    * Crea un `@classmethod` llamado `modificar_tasa_interes(cls, nueva_tasa)`. Este método debe actualizar la tasa global del banco.
**Simulación en el programa principal:**
* Crea dos cuentas 
* Imprime cuántas cuentas existen a nivel global.
* Deposítale 10,000 a cuenta1
* Proyecta el interés de cuenta1 con la tasa actual del 5%
* Usa el método de clase para que el Banco suba la tasa de interés a 0.10 (10%).
* Vuelve a proyectar el interés de cuenta1 para ver cómo la ganancia se duplicó automáticamente.
* Intenta cambiar el nombre de Sofía a un texto en blanco `""` para comprobar que el setter la bloquea.