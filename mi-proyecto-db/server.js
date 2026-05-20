const express = require('express');
const path = require('path');
const mysql = require('mysql2');

const app = express();
const PORT = 3000;

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'julian28',
    database: 'ecoeventos_db'
});

app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {

    res.sendFile(path.join(__dirname, 'views/index.html'));

});

app.post('/confirmar', (req, res) => {

    const { nombre, correo } = req.body;

    const querySQL = `
        INSERT INTO asistentes (nombre, correo)
        VALUES (?, ?)
    `;

    db.query(querySQL, [nombre, correo], (err, results) => {

        if (err) {
            return res.send('Error');
        }

        res.send(`
            <!DOCTYPE html>
            <html lang="es">

            <head>
                <meta charset="UTF-8">
                <title>Registro</title>
            </head>

            <body>

                <h1>Registro guardado</h1>

                <p>${nombre} fue registrado correctamente</p>

            </body>

            </html>
        `);

    });

});

app.get('/asistencias', (req, res) => {

    const querySQL = 'SELECT * FROM asistentes';

    db.query(querySQL, (err, resultado) => {

        if (err) {
            return res.send('Error');
        }

        let filasHTML = '';

        resultado.forEach((asistente) => {

            filasHTML += `
                <tr>
                    <td>${asistente.id}</td>
                    <td>${asistente.nombre}</td>
                    <td>${asistente.correo}</td>
                </tr>
            `;

        });

        res.send(`
            <!DOCTYPE html>
            <html lang="es">

            <head>
                <meta charset="UTF-8">
                <title>Asistencias</title>
                <link rel="stylesheet" href="/css/estilos.css">
            </head>

            <body>

                <h1>Lista de asistentes</h1>

                <table>

                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Correo</th>
                    </tr>

                    ${filasHTML}

                </table>

            </body>

            </html>
        `);

    });

});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});