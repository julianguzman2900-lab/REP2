const pool = require('./db');

// Verificar inicio de sesión
async function verificarLogin(usuario, contrasena) {
  try {
    const [rows] = await pool.query(
      'SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?',
      [usuario, contrasena]
    );
    return rows.length > 0 ? rows[0] : null;
  } catch (error) {
    console.error('Error en login:', error);
    return null;
  }
}

module.exports = { verificarLogin };