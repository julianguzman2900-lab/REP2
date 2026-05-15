//ejercicio 1
const express = require('express');
const app = express();
const PORT = 3000;

//paso 2.1
app.use(express.json());


//ejercicio 1.2
app.get(`/hola`,(req, res)=> {
    res.send("<h1>¡Hola Estudiantes!</h1><p>El servidor responde")
});


//ejercicio 1.3
app.get (`/contacto`, (req, res)=>{
    res.json({
        nombre: "Soporte Tecnico",
        email: "ayuda@irsi.com",
        extension: 2205
    });
});

//ejercicio 3======================
function procesarEstudiantes(lista, callback) {
    if (!Array.isArray(lista) || lista.length === 0) {
        return callback(new Error("La lista esta vacia o no es un arreglo valido"));
    }

    const aprobados = [];
    const reprobados = [];

    lista.forEach(estudiante => {
        if (estudiante.nota >= 70) {
            aprobados.push(estudiante.nombre);
        } else {
            reprobados.push(estudiante.nombre);
        }
    });

    callback(null, { 
        aprobados, 
        reprobados, 
        total: lista.length 
    });
}

app.post('/analizar-clase', (req, res) => {
    const { estudiantes } = req.body; 

    procesarEstudiantes(estudiantes, (error, resultado) => {
        if (error) {
            return res.status(400).json({ error: error.message });
        }
        res.json({
            status: "success",
            reporte: resultado
        });
    });
});



//========================================

//paso 2.2
app.post(`/registrar`, (req, res)=> {
    const infoEstudiante = req.body;

    console.log("Datos recibidos:", infoEstudiante);

    res.status(201). json({
        mensaje: "Estudiante registradi con exito",
        datos_recibidos: infoEstudiante
    });
});

app.get('/buscar', (req, res) => {
    const nombre = req.query.nombre;
    const rol = req.query.rol;

    if (!nombre) {
        return res.status(400).json({
            error: "Error: El parámetro 'nombre' es obligatorio para la búsqueda."
        });
    }

    res.status(200).json({
        mensaje: `Resultado: Se ha encontrado al ${rol} ${nombre} en la base de datos.`
    });
});


app.listen(PORT, () => {
    console.log(`Servidor activo en: http://localhost:${PORT}`);
});




//ejercicio 4 ================================================================
const express = require('express');
const app = express();
const PORT = 4000;
app.use(express.json())

app.post(`/despacho`,(req,res)=>{
    const {recurso, peso} = req.body

    setTimeout(()=>{
        console.log(`Pedido recibido de ${recurso} (${peso}kg)`)

        if(peso > 500) {
            console.log("Estado: RECHAZADO")
            return res.status(400).json({
                error: "Capacidad de hangar excedida"
            })
        }

        console.log("Estado: ACEPTADO")
        res.json({
            mensaje: "Despacho programado",
            id: "A-102"
        })
    }, 1500)

})

app.listen(PORT, ()=>{
    console.log(`servidor activo en el puerto ${PORT}`)
})


//cliente.js=========================================================
const recurso = process.argv[2];
const peso = Number(process.argv[3]);

if (!recurso || isNaN(peso)) {
    process.exit(1);
}

const prepararPaquete = (nombre, kg, callback) => {
    console.log(`1. Empacando ${nombre}...`);
    callback();
};

prepararPaquete(recurso, peso, () => {
    console.log("2. Enviando datos al servidor central...");

    setTimeout(() => {
        if (peso > 500) {
            console.log(`[LOG] Recibido pedido de ${recurso} (${peso}kg).`);
            console.log("Estado: RECHAZADO.");
            console.log('Respuesta del Servidor: { "error": "Capacidad de hangar excedida" }');
        } else {
            console.log(`[LOG] Recibido pedido de ${recurso} (${peso}kg).`);
            console.log("Estado: ACEPTADO.");
            console.log('Respuesta del Servidor: { "mensaje": "Despacho programado", "id": "A-102" }');
        }
    }, 1500);
});