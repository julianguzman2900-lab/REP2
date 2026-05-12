# ¿Qué es Node.js?
- Node.js es un **entorno de ejecución** de JavaScript fuera del navegador, construido sobre **V8**
- Es **multiplataforma**, **open-source** y está orientado a un **modelo de eventos** (event loop).No es un lenguaje, ni un servidor web por sí mismo.
- **Limitación:** No es ideal para tareas muy **CPU intensive (intensivas en CPU)**.

## Que es im rutime eviroment
Un **ritime** es el entorno que provee todas las herramientas para ejecutar un lenguaje. En los navegadores: El entorno incluye objetos como `window` o `document` .En Node.js: El entorno incluye objetos propios para interactuar con el sistema, como:`global` `process` ` fs` (file system) `http`, etc 


## Event Loop y asincroníaNode
js funciona con un **único hilo de ejecución (single-thread)**.Su capacidad para manejar múltiples tareas concurrentes (sin bloquearse) se debe al **Event Loop**.



## El objeto global es Node.js y navegadores: `window`, `global` y `globalThis`

En un navegador web sl objeti global se llama **`window`**

- en **navegadores**: `globalThis=== ` `window`
- en **Nose.js** : 

## Extenciones 