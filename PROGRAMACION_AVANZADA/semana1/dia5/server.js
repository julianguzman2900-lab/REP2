const express = require('express');
const app = express();

const PORT = 3000;
app.get(`/hola`,(req, res)=> {
    res.send("<h1>¡Hola Estudiantes!</h1><p>El servidor responde")
});
app.get (`/contscto`, (req, res)=>{
    res.json({
        nombre: "Soporte Tecnico",
        email: "ayuda@irsi.com",
        extension: 2205
    });
});

app.listen(PORT, () => {
 console.log("Servidor activo en el puerto " + PORT);
});

