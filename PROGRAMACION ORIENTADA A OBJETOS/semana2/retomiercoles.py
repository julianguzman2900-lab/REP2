# 1. Crea la clase `CuentaBancaria`.
class CuentaBancaria:
# 2. **Atributos Compartidos**
#      El banco maneja una `tasa_interes_global` que nace en `0.05`
    tasa_interes_global= 0.05
#      El banco lleva un registro de `total_cuentas_creadas` que nace en `0`.
    total_cuentas_creada= 0
# 3. **El Constructor**
#      Pide un parámetro: `nombre_titular`.
    def __init__(self,nombre_titular):
#      Crea el atributo privado `__titular` usando el parámetro.
        self.__titular=nombre_titular
#      Crea el atributo privado `__saldo` e inicialízalo por defecto en `0.0`.
        self.__saldo=0.0
#      Súmale 1 al atributo de clase `total_cuentas_creadas`
        CuentaBancaria.total_cuentas_creada+=1
# 4. **Seguridad**
#      Crea un `@property` llamado `saldo` que actúe como Getter
    @property
    def saldo(self):
        return self.__saldo
#        OJO:** No hagas el Setter para el saldo, el saldo no se debe poder sobrescribir con un `=`, solo debe cambiar mediante depósitos y retiros.
#      Crea un `@property` llamado `titular` (Getter).
    @property
    def titular(self):
        return self.__titular
# Crea su respectivo `@titular.setter`. La validación debe asegurar que el nombre no esté en blanco
    @titular.setter
    def titular(self,nuevo_titular):
        if nuevo_titular == "":
            print("[ERROR] El nombre del titular no puede estar vacio: ")

        else:
            self.__titular=nuevo_titular
            print("El nuevo titular de la cuenta es:",self.titular)
# 5. **Métodos de Instancia**
#      Crea un método `depositar(self, cantidad)`. Si la cantidad es mayor a 0, súmala al saldo 
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("[SISTEMA] Deposito exitoso. Tu saldo es de:",self.saldo)
        else:
            print("[ERROR] La cantidad a depositar debe ser mayor a 0.")
#      Crea un método `retirar(self, cantidad)`. Solo permite el retiro si hay suficiente dinero en la cuenta.
    def retirar(self,cantidad):
        if cantidad <= self.__saldo:
            self.__saldo-=cantidad
            print("[SISTEMA] Retiro exitoso. Tu saldo es de:", self.saldo)

        else:
            print("[ERROR] Su cuenta no tiene saldo suficiente para realizar el retiro")
#      Crea un método `proyectar_interes(self)`. Este método debe multiplicar el saldo privado actual por la `tasa_interes_global` de la clase e imprimir cuánto dinero ganará el cliente este *año*.

    def proyectar_intereses(self):
        interes=self.__saldo*CuentaBancaria.tasa_interes_global
        print("La cantidad de intereses que ganara este año sera:",interes)
# 6. **Método de Clase:**
 #Crea un `@classmethod` llamado `modificar_tasa_interes(cls, nueva_tasa)`. Este método debe actualizar la tasa global del banco.
    @classmethod
    def modificar_tasa_intereses(cls, nueva_tasa):
        cls.tasa_interes_global= nueva_tasa
        print("[SISTEMA] La tasas de interes anual se ha actualizado a:", cls.tasa_interes_global)

#Simulación en el programa principal:**
#  Crea dos cuentas 
print("\n ===== SISTEMA BANCARIO====")
cuenta1=CuentaBancaria("CARLOS")
cuenta2=CuentaBancaria("SOFIA")

#  Imprime cuántas cuentas existen a nivel global.
print(f"El total de cuentas existentes es de: {CuentaBancaria.total_cuentas_creada}")

#  Deposítale 10,000 a cuenta1
cuenta1.depositar(10000)

#  Proyecta el interés de cuenta1 con la tasa actual del 5%
cuenta1.proyectar_intereses()
#  Usa el método de clase para que el Banco suba la tasa de interés a 0.10 (10%).
cuenta1.retirar(2000)

CuentaBancaria.modificar_tasa_intereses(0.10)
#  Vuelve a proyectar el interés de cuenta1 para ver cómo la ganancia se duplicó automáticamente.
cuenta1.proyectar_intereses()
#  Intenta cambiar el nombre de Sofía a un texto en blanco `""` para comprobar que el setter la bloquea.
cuenta1.titular="MARIA"