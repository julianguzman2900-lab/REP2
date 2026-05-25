const express = require("express")
const app = express()

const rutasProductos = require('./productos')


app.use(express.json())

app.use('/productos', rutasProductos)

app.listen(3000,()=>{
    console.log("Servidor corriendo en el puerto 3000")
})