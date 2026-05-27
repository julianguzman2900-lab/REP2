import dotenv from 'dotenv'
dotenv.config

const mysql = require("mysql2") 


const conexion = mysql.createConnection({ 
  host: process.env.DB_HOST|| 'localhost', 
  user: process.env.DB_USER, 
  password: process.env.DB_PASSWORD, 
  database: process.env.DB_NAME 
}) 


conexion.connect((err) => { 
  if(err) { 
    console.log("Error al conectar con mysql: ", err.message) 
  } else { 
    console.log("Conexion a mysql desde el modelo exitosa") 
  } 
}) 

const Usuario = { 
  obtenerTodos: (callback) => { 
    
    const sql = "SELECT * FROM usuarios" 
    conexion.query(sql, callback) 
  }, 
  
  obtenerPorId: (id, callback) => { 
    
    const sql = "SELECT * FROM usuarios WHERE id = ?" 
    conexion.query(sql, [id], callback) 
  }, 
  
  crear: (datos, callback) => { 
    
    const sql = `INSERT INTO usuarios (nombre, edad, altura, correo, empresa_id, foto_url) VALUES (?, ?, ?, ?, ?, ?)` 
    const valores = [ 
      datos.nombre, 
      datos.edad || 0, 
      datos.altura || 0.0, 
      datos.correo || null, 
      datos.empresa_id || null, 
      datos.foto_url || null 
    ] 
    conexion.query(sql, valores, callback) 
  }, 
  
  actualizar: (id, datos, callback) => { 
    const sql = `UPDATE usuarios SET nombre=?, edad=?, altura=?, correo=?, empresa_id=?, foto_url=? WHERE id=?` 
    const valores = [ 
      datos.nombre, 
      datos.edad || 0, 
      datos.altura || 0.0, 
      datos.correo || null, 
      datos.empresa_id || null, 
      datos.foto_url || null,
      id 
    ] 
    conexion.query(sql, valores, callback) 
  }, 
  
  eliminar: (id, callback) => { 
    const sql = `DELETE FROM usuarios WHERE id = ?` 
    
    conexion.query(sql, [id], callback) 
  } 
} 


module.exports = Usuario
