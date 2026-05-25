const mysql = require('mysql2');

const conexion = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'puja'
});

conexion.connect((error) => {
    if (error) {
        console.log('Error de conexion', error);
    } else {
        console.log("Mysql esta conectado");
    }
});


module.exports = conexion;
