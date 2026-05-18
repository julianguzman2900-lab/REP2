const express = require('express');
const path = require('path')
const app = express();
const PORT = 3000;

// Middleware para servir archivos estáticos desde la carp
app.use(express.static('public'));
// permite que express lea y procese los datos enviados a
app.use(express.urlencoded({ extended: true }));


app.post('/enviar_datos', (req, res) => {
    const { nombre, id } = req.body;
    console.log(`Nombre: ${nombre}, ID: ${id}`);
    res.send('Datos recibidos correctamente');
});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
