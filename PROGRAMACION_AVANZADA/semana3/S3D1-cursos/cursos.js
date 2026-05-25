const express = require('express');
const router = express.Router();


router.get('/', async (req, res) => {
    try {
        res.status(200).json({ mensaje: "Lista de todos los cursos" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

router.post('/crear', (req, res) => {
    try {
        const infoCurso = req.body;
        res.status(201).json({ 
            mensaje: "Curso creado con éxito", 
            datosRecibidos: infoCurso 
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});


router.put('/:id', (req, res) => {
    try {
        const idCurso = req.params.id;
        const nuevaInformacion = req.body;

        res.status(200).json({ 
            mensaje: `El curso ${idCurso} fue actualizado con informacion nueva`, actualizacion: nuevaInformacion 
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
}); 

module.exports = router;
