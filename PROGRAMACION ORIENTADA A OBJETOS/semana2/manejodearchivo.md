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
 