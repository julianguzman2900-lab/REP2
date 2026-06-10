require('dotenv').config();
const express = require('express');
const cors = require('cors');
const pool = require('./db');
const { verificarLogin } = require('./auth');

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// ------------------- RUTAS PÚBLICAS -------------------
app.get('/api/libros', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM libros');
    res.json(rows);
  } catch (error) {
    console.error('Error al obtener libros:', error);
    res.status(500).json({ error: 'Error del servidor' });
  }
});

app.get('/api/libros/:id', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM libros WHERE id = ?', [req.params.id]);
    if (rows.length === 0) return res.status(404).json({ error: 'Libro no encontrado' });
    res.json(rows[0]);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Error del servidor' });
  }
});

app.get('/api/libros/genero/:genero', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM libros WHERE genero = ?', [req.params.genero]);
    res.json(rows);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Error del servidor' });
  }
});

app.get('/api/buscar/:termino', async (req, res) => {
  const termino = `%${req.params.termino}%`;
  try {
    const [rows] = await pool.query(
      'SELECT * FROM libros WHERE titulo LIKE ? OR autor LIKE ? OR genero LIKE ?',
      [termino, termino, termino]
    );
    res.json(rows);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Error del servidor' });
  }
});

// ------------------- RUTAS DE ADMINISTRACIÓN -------------------

// Iniciar sesión
app.post('/api/admin/login', async (req, res) => {
  const { usuario, contrasena } = req.body;
  const admin = await verificarLogin(usuario, contrasena);
  
  if (admin) {
    res.json({ exito: true, mensaje: 'Bienvenido', usuario: admin.nombre });
  } else {
    res.status(401).json({ exito: false, mensaje: 'Usuario o contraseña incorrectos' });
  }
});

// Agregar nuevo libro
app.post('/api/admin/libros', async (req, res) => {
  try {
    const { titulo, autor, genero, precio, imagen, descripcion, stock } = req.body;
    const [resultado] = await pool.query(
      'INSERT INTO libros (titulo, autor, genero, precio, imagen, descripcion, stock) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [titulo, autor, genero, precio, imagen, descripcion, stock]
    );
    res.json({ exito: true, id: resultado.insertId, mensaje: 'Libro agregado correctamente' });
  } catch (error) {
    console.error('Error al agregar:', error);
    res.status(500).json({ exito: false, mensaje: 'Error al agregar el libro' });
  }
});

// Editar libro
app.put('/api/admin/libros/:id', async (req, res) => {
  try {
    const { titulo, autor, genero, precio, imagen, descripcion, stock } = req.body;
    await pool.query(
      'UPDATE libros SET titulo=?, autor=?, genero=?, precio=?, imagen=?, descripcion=?, stock=? WHERE id=?',
      [titulo, autor, genero, precio, imagen, descripcion, stock, req.params.id]
    );
    res.json({ exito: true, mensaje: 'Libro actualizado correctamente' });
  } catch (error) {
    console.error('Error al editar:', error);
    res.status(500).json({ exito: false, mensaje: 'Error al editar el libro' });
  }
});

// Eliminar libro
app.delete('/api/admin/libros/:id', async (req, res) => {
  try {
    await pool.query('DELETE FROM libros WHERE id = ?', [req.params.id]);
    res.json({ exito: true, mensaje: 'Libro eliminado correctamente' });
  } catch (error) {
    console.error('Error al eliminar:', error);
    res.status(500).json({ exito: false, mensaje: 'Error al eliminar el libro' });
  }
});

app.listen(PORT, () => {
  console.log(`✅ Servidor corriendo en http://localhost:${PORT}`);
});