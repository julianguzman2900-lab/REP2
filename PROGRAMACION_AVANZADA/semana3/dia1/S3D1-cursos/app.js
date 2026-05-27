const express = require('express');
const app = express();
const puerto = 3000;

app.use(express.json());


const rutasCursos = require('./cursos');



app.use('/cursos', rutasCursos);


app.get('/', (req, res) => {
    res.send('Servidor funcionando correctamente');
});


app.listen(puerto, () => {
    console.log(`Servidor escuchando en http://localhost:${puerto}`);
});
