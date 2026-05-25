const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.status(200).json({ mensaje: "Lista de todos los productos" });
});

router.post('/agregar', (req, res) => {
    res.status(201).json({ mensaje: "Producto agregado correctamente" });
});

module.exports = router;
