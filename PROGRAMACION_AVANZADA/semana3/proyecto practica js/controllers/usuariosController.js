const { request } = require("node:http") 
const Usuario = require("../model/usuarioModel") 

function validarPeticion(res, body){ 
  let vacios=[] 
  if(!body.nombre) vacios.push("nombre") 
  if (vacios.length) return res.status(400).json({ error:`Bad Request`, message:`Error, nombre no puede estar vacio` }) 
} 
exports.obtenerTodos = (req, res) => {
  Usuario.obtenerTodos((err, filas) => {
    if (err) {
      console.error(err)
      return res.status(500).send("Error al obtener los usuarios")
    }
    res.json(filas)
  })
}

exports.obtenerPorId = (req, res) => { 
  const id = req.params.id 
  Usuario.obtenerPorId(id, (err, filas) => { 
    if(err) { 
      console.error(err) 
      return res.status(500).send("Error al obtener el usuario") 
    } 
    if (filas.length === 0) return res.status(404).send("Usuario no encontrado") 
    res.json(filas[0]) 
  }) 
} 

exports.crear = (req, res) => { 
  if (validarPeticion(res, req.body)) return 

  Usuario.crear(req.body, (err, resultado) => { 
    if (err) { 
      console.error(err) 
      return res.status(500).send("Error al crear el usuario") 
    } 
    res.status(201).send("Usuario creado con éxito") 
  }) 
} 

exports.actualizar = (req, res) => { 
  const id = req.params.id 
  
  
  if (validarPeticion(res, req.body)) return 

  Usuario.actualizar(id, req.body, (err, resultado) => { 
    if (err) { 
      console.error(err) 
      return res.status(500).send("Error al actualizar el usuario") 
    } 
    res.status(200).send("Usuario actualizado correctamente") 
  }) 
} 

exports.eliminar = (req, res) => { 
  const id = req.params.id 
  Usuario.eliminar(id, (err, resultado) => { 
    if (err) { 
      console.error(err) 
      return res.status(500).send("Error al eliminar el usuario") 
    } 
    res.status(200).send("Usuario eliminado correctamente") 
  }) 
}




