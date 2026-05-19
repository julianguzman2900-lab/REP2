const express = require('express');
const path = require('path')
const app = express();
const PORT = 4000;

// Middleware para servir archivos estáticos desde la carp
app.use(express.static('public'));
// permite que express lea y procese los datos enviados a
app.use(express.urlencoded({ extended: true }));


app.post('/enviar_datos', (req, res) => {
    const { nombre, id } = req.body;
    console.log(`Nombre: ${nombre}, ID: ${id}`);
        // res.send('
//     <!DOCTYPE html>
//     <html lang="es">
//     <head>
//         <title>Datos Recibidos</title>
//     </head>
//     <body>
//         <p>Datos recibidos <strong>correctamente</strong>
//     </body>
//     </html>');
res.sendFile(path.join(__dirname, 'public', 'agradecimiento.html'));
});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
