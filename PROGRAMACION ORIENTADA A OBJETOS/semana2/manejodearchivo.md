# MANEJO DE ARCHIVOS

## metodos de apertura
`open()`

esta funcion requiere dos argumentos obligatorios: El nombre y el "Modo" en el que queremos abrirlo.
\
### Modos de apertura

1. **modo `w`** (write/escribir).
   * Crea un archivo nuevo
   * **Advertencia**: Si el archivo ya existia , el modo `'w'` lo destruye por completo y lo sobre escribe desde cero
2. **Modo`a`** (append/anadir)
   * Abre un archivo existente y coloca el cursor al final.
   * Todo lo que escrbamos se agregara sin borrar lo anterior

3. **Modo `r`** (read/leer)
   * Solo nos permite ver el contenido.
   * NO podemos modificar o agregar al archivo
   * Si el archivo no existe, el programa se detendra con un error


SIEMPRE que abro un archivo, hay que cerrar el archivo 
`close()`

Para escribir en mi archivo, usamos la funcion `write`

```python
archivo_prueba= open("archivo.text", "a")

archivo_prueba.write("Hoy aprendi a escribir a un archivo")

archivo_prueba.close()
```


## administrador de contexto `whit open`

```python
with open("archivo.text", "a")as archivo_prueba:
    archivo_prueba.write("hoy aprendi a escribir en un archivo\n")
    archivo_prueba.write("Ahora puedo escribir varias lineas\n")
```


## Leer nuestros archivos
```python
with open("archivo.text","a") as archivo_prueba:
   print("contenido del archivo")

      for linea in archivo_prueba:

         texto_limpio= linea.strip()
         print(f"{texto_limpio}")
 ```


 ## El metodo read `read()`

 python tomara todo el contenido del archivo y lo guardara en una sola variable de tipo cadena de texto (string)

 ```python
 with open("cuento.txt","r") as archivo:
   contenido= archivo.read()
   print("contenido completo:")
   print(contenido)
   ```


## metodo `readline()`

```python
with open("lista_alumnos.txt","r")as archivo: