# Herencia basica 

## Principio DRY: (Don't Repeat yourself)|No te repitas|
## Micro ejemplo
```python
class perro:
    def __init__(self, nombre):
        self.nombre= nombre
    def comer(Self):
        print("Comiendo...")

class gato:
    def __init__(self, nombre):
        self.nombre= nombre
    def comer(self):
        print("Comiendo...")
```

### Solucion usano herencia
```python
class animal:
    def comer(self):
        print("El animal esta comiendo...")

class perro(animal):
pass 

mi_mascota= perro()
mi_mascota.comer()
```




### Agregando habilidades exclusivas al hijo 
```python
# La superclase (el padre)
class vehiculo:
    def encender_motor(self):
        print("[SITEMA] | EL MOTOR SE HA ENCENDIDO.")

    def apagar_motor(self):
        print("[SITEMA] | EL MOTOR SE HA APAGADO.")

#subclase 1(hijo)
class Auto(vehiculo):
    def encender_aire(self):
        print("[AUTO] | Aire acondicionado esata encendido.")

class Moto(vehiculo):
    def hacer_acrobacia(self):
        print("[MOTO] | Levantando la rueda delantera.")
    
carro= Auto()
moto=   Moto()


print("Acciones del auto")
carro.encender_motor()
carro.encender_aire()

print("\nAcciones de la moto")
moto.encender_motor()
moto.hacer_acrobacia()
```

# Ejercicio practico: Heroes con habilidades unicas 

```python
class PersonajeBase:
    def caminar(self):
        print("El personaje esta avanzando por el mapa.")
    
    def descansar(self):
        print("El personaje esta recuperando energia.")


class Mago(PersonajeBase):
    def lanzar_hechizo(self):
        print("El mago lanza una bola de fuego.")

class Guerrero(PersonajeBase):
    def bloquear_ataque(Self):
        print("El guerrero levanta su escudo de metal")


mi_mago= Mago()
mi_guerrero= Guerrero()

print("\nAcciones del mago")
mi_mago.caminar()
mi_mago.descansar()
mi_mago.lanzar_hechizo()

print("\nAcciones del guerrero")

mi_guerrero.caminar()
mi_guerrero.descansar()
mi_guerrero.bloquear_ataque()
```

## Constructor del hijo 
```python
class Padre:
    def __init__(self, apellido):
        self.apellido = apellido


class Hijo(Padre):
    def __init__(self, nombre):
        self.nombre=nombre

chico= Hijo("Carlos")
```

### Solucion
`super()`. Significa literalmente "Superclase" o "padre". Dentro del `__init__` del hijo llamamos a `super().`
`__init__()` y le pasamos los ingrediebtes que le corresponden al padre.

```python
class Persona:
    def __init__(self, nombre):
        
        self.nombre = nombre

class Estudianye(Persona):
    def __init__(self,nombre_ingresado,nota_ingresada):
        super().__init__(nombre_ingresado)
        self.nota= nota_ingresada

    def mostrar_info(self):
    print(f"Hola mi nombre es: {self.nombre} y mi nota es: {self.nota}")

estudiante1= Estudiante("Juan", 8.5)
estudiante1.mostrar_info()
```


## Polimorfismo: "Muchas formas"


**SOLID**
1. **S - Single responsibility (Responsabilidad unica)**
2. **O - open/closed (Abierto/cerrado)**
3. **L - Liskov substitution (Sustitucion de Liskov)**
4. **I - Interfaces segregation (Segregacion de interfaces)**
5. **D - Dependency inversion (Inversion de dependencias)**

```python
class EmpleadoDios:
    def __init__(self, nombre,salario):
        self.nombre= nombre
        self.salario= salario

class CalculadoraFinanciera:
    def calcular_impuestos(self,empleado):
        return empleado.salario * 0.13

class RepositorioEmpleados:
    def guardar_empleado(self,empleado):
        print(f"Guardando empleado: {empleado.nombre} con salario: {empleado.salario}")

```

## La rebelion del Hijo (Sobrescritura de metodos)
```python

class PersonaMayor:
    def saludar(self):
        print("Bienas tardes, estimado, como se encuentra usted el dia de hoy?")


class Adolescente(PersonaMayor):
    def saludar(self):
        print("Hola, todo bien")

senor= PersonaMayor()
chico= Adolescente()

senor.saludar()
chico.saludar()
```

### El poder del polimorfismo

perros, gatos y vacas, y quiere que todos hagan un sonido, escribir algo asi:
`if tipo =="perro": ladrar()`
`elif tipo=="gato": maullar()`
`elif tipo =="vaca": mugir()`


### Ejemplo | Simulacion granja
```python

class Animal:
    def __init__(self,nombre)
    self.nombre= nombre

def __str__(self):
        return f"Animal: {self.nombre}"

    def hacer_sonido(self):

class perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El perro hace: Guauu, Guauu!")
    

class gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El gato hace: Miau, Miau!")

class pato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El pato hace: Cuac, Cuac!")

animal1 = Perro("Pochiberto")
animal2 = Gato("Porfirio")
animal3 = Pato("Pancracio")

lista_granja= [animal1,animal2]
lista_granja.append(animal3)

animal_desconocido= Animal("Extraterrestre")
lista_granja.append(animal_desconocido)

print(lista_granja)
```
## Combinando lo viejo y lo nuevo:
### 1. Usar `super()` en metodos normales

```python
class EmpleadoBase:
    def iniciar_rutina(self):
        print("1. Llego a la oficina a las 9:00 am.")
        print("2. Reviso mis correos electronicos.")
        print("3. Planifico mis tareas.")
        
class Programador(EmpleadosBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()

        print("4. Escribo codigo y resuelvo problemas tecnicos.")

trabajador1= Programador()
trabajador1.iniciar_rutina()
```