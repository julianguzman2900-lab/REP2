exports.procesarFormulario = async (req, res) => {
    try {
        const { nombre, apellido } = req.body;

        const [respuestaActividad, respuestaImagen] = await Promise.all([
            fetch('https://bored-api.appbrewery.com/random'),
            fetch('https://dog.ceo/api/breeds/image/random')
        ]);

        const datosActividad = await respuestaActividad.json();
        const datosImagen = await respuestaImagen.json();

        const textoActividad = datosActividad.activity;
        const urlImagen = datosImagen.message;

        console.log(textoActividad);
        console.log(urlImagen);

        res.send(`
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Tu Actividad Dinámica</title>
            </head>
            <body>
                <h2>¡Hola, ${nombre} ${apellido}!</h2>
                <p>Que haremos hoy?:</p>
                <div>
                    "${textoActividad}"
                </div>
                <br>
                <img src="${urlImagen}" width="300" height="250" alt="Ilustración Animal">
                <br><br>
                <a href="/index.html">← Volver</a>
            </body>
            </html>
        `);

    } catch (error) {
        console.error(error);
        res.status(500).send("<h1>Error en el Servidor</h1>");
    }
};
