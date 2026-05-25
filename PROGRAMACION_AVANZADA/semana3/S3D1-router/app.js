const express = require("express")
const app = express()

const rutasUsuarios = require('./routes/usuarios')

app.use(express.json())

app.use('/usuarios', rutasUsuarios)

app.listen(3000,()=>{
    console.log("Servidor corriendo en el puerto 3000")
})