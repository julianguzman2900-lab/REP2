const express = require('express');
const router = express.Router();

router.post('/', async (req, res) => {
  try {
    const { nombre, apellido } = req.body;

    const [respuestaActividad, respuestaImagen] = await Promise.all([
      fetch('https://bored-api.appbrewery.com/random'),
      fetch('https://dog.ceo/api/breeds/image/random')
    ]);

    const datosActividad = await respuestaActividad.json();
    const datosImagen = await respuestaImagen.json();

    const actividad = datosActividad.activity;
    const linkImagen = datosImagen.message;

    res.send(`
        <!DOCTYPE html>
      <html lang="es">
      <head>
        <meta charset="UTF-8">
        <title>Actividad del día</title>
        <style>
          body {
            font-family: Monaco, Monospace;
            background-color: #120b1ddf;
            margin: 0;
            padding: 0;
            text-align: center;
          }
          header {
            background-color: rgba(28, 8, 61, 0.671);
            color: rgb(199, 199, 199);
            padding: 20px;
            margin-bottom: 25px;
          }
          section {
            background-color: rgb(26, 16, 41);
            color: rgb(255, 255, 255);
            width: 300px;
            padding: 20px;
            margin: auto;
            border-radius: 7px;
          }
          button {
            width: 100%;
            padding: 10px;
            background-color: rgba(1, 3, 15, 0.781);
            color: rgb(255, 255, 255);
            border-radius: 15px;
          
          }
          img {
            display: block;
            margin: 20px auto;
            border-radius: 7px;
          }
        </style>
      </head>
      <body>
        <header>
          <h2>Generador Web de Actividades y Contenido Dinámico</h2>
        </header>
        
        <section>
          <h3>¡Hola, ${nombre} ${apellido}!</h3>
          <p>¿Qué haremos hoy?</p>
          <p>${actividad}</p>
          
          
          <img src="${linkImagen}" width="300" height="240" alt="Fotos de Perritos">
          
          <a href="/index.html"><button>Volver</button></a>
        </section>
      </body>
      </html>
    `);

  } catch (error) {
    console.error(error);
    res.status(500).send("<h1>Error en el Servidor</h1>");
  }
});

module.exports = router;
