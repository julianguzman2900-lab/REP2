const express = require("express")
const router = express.Router()

// CORREGIDO: Ahora coincide exactamente con tu archivo real
const productosController = require("../controllers/productosControllers")

router.get("/", productosController.obtenerTodos)
router.get("/:id", productosController.obtenerPorId)
router.post("/", productosController.crear)

module.exports = router



