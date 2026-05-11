# PREPARACION DEL ENTORNO (INSTALACION DE Node.JS)
# Nuestro primer programa de node "hola mundo"

En JavaEscript


## VARIABLES
Tenemos dos formas de crear una variable
- **`let` (variable mutable)**
- **`const`(constantes)**
```javascript
let edad =30
edad = 40
console.log(edad)
const impuestos = 013

```
Conenciones: **camelcase**
- totalPrecio
-userName
Tipos primitivos: `number`, `string`, `boolean`, `null`, `undefined`, `bigint,` `symbol`; y estructurados como `object` y `function`

```js
const curso = "Programación avanzada"
let inscritos = 15
inscritos = inscritos + 1

const precio = 10.99       // number
const nombre = "Diego"      // string
const activo = true         // boolean
const nada = null           // null
let indefinido;             // undefined

console.log(precio)
console.log(typeof precio)


console.log(nombre)
console.log(typeof nombre)
```

## Ejercicio de practica
const se utiliza para variables que no queremos que se puedan editar y let las que si queremos que cambien

## Operadores aritmeticos, comparacion y logicos

* **Aritmeticos:** `+` `-` `*` `/` `%` `**`
* **Comparación:** `===`,`!==`, `<, >`, `<=`, `>=`
                  (evitar `==`,`!=`)
* **Lógicos:** `&&` (AND), `||` (OR), `!` (NOT)

```js
let num1 = 10
let num2 = 5

console.log(num1 + num2)  // Suma: 15
console.log(num1 - num2)  // Resta: 5
console.log(num1 * num2)  // Multiplicación: 50
console.log(num1 / num2)  // División: 2
console.log(num1 % num2)  // Módulo (resto): 0
console.log(num1 ** num2) // Potencia: 100000

console.log(5=="5") //True
console.log(5==="5") // False



const edad= 20

const puedeVolar = edad >= 18 && edad <65
console.log(puedeVotar)


```



## Condicionales
`if / else if/ else`
` Switvh(valor) {case...}`

use `if/else` para logica general y `Switch` para multiples casos de un mism valor


```js
// const nota= 13
// let letra

// if(nota>= 90) {letra="A"}

// else if (nota>= 80) {letra = "B"}

// else if (nota >= 70) {letra = "C"}
// else {letra = "D"}
// console.log(letra)
// ```


// - `Switch`
// ```js

// const dia = martes 
// switch(dia){
//     case "Lunes":
//         console.log("Clase teorica")
//     break    
//     case console.log




const temperatura= 10


switch(True){
    case temperatura < 15:
        console.log("Frio")
        break
    case temperatura > 15 && <25:
        console.log("Templado")
        break
    default:
        console.log("Caliente")
        

}
```

## Ciclosfor 
(`inicialización`; `condición; `actualización)` { ... }while (condición) { ... }do { ... } while (condición)javascript

`ciclo for`
```js


let suma = 0

for (let index = 0; index <= 5; index++) {
    suma += index
}

console.log(suma)
```

`ciclo while`
```js
let energia = 3

while (energia > 0) {
    console.log("Saltando... Energia restante:" + energia )
    energia --;

}

```

- `ciclo do while`: Hazlo al menos una vez
```js 
const passCorrecta = "1234"

let passIngresada =""

do{
    passIngresada = "1234"
    consol.log("Validando contrasena...")
} while (passIngreada!== passCorrecta);

console.log("Acceso concedido")
```

- `For...of` sobre un array
```js 
const frutas = ["Manzanas", "Pera", "Uvas"]
for (const fruta of frutas) {
    console.log(fruta)
}
```
# Ejercicio


```js
const nums =[2,5,7,10,11]
```

### Subrutinas(funciones)

- **Declaracion:** `funcion nombre(params) {...}`
- **Expresion:** ` const nombre= function(params) {...}`
- **Flecha:** `const nombre= (params) => {...}`. callbacks
- **Parametros por defecto:** ` function f(a = 0) {...}`
- **Retorno:** `return valor;`
``` js
// declaraciones tradicionales 
function alCuadrado(num){
    return num * num
}

// funcion flecha
const esPar = (num) => num %2===0


// funcion con parametros por defecto 

function saludar(nombre = "Estudiante"){
    return `hola ${nombre}!`
}
console.log (alCuadrado(5))
console.log(esPar(4))
console.log(esPar(5))
console.log(saludar())
console.log(saludar("Julian"))


```


## Areglos y matrices 
```js
const array = [1,2,3]
const matriz = [
    [1,2,3],
    [9,8,7]
]
console.log(matriz[1][2])

```
## JSON - JavaScript Object Notation 
### Reglas 
1. **Las Claves (Keys):** Deben ser obligatoriamente cadenas de texto encerradas en **Comillas dobles** (`""`). Laas comillas simples estan prohibidas (`''`)



### Traduccion a JSON
```json
{
    "nombre": "Ana",
    "edad": 28,
    "activo": true,
    "habilidades":[
        "Python",
        "SQL"
    ],
    "vehiculo":null
}
