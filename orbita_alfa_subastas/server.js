const express = require('express'); 
const path = require('path'); 
const db = require('./db'); 

const app = express(); 
const PORT = 3000; 

app.use(express.urlencoded({ extended: true })); 
app.use(express.static(path.join(__dirname, 'public'))); 

app.get('/', (req, res) => { 
    res.sendFile(path.join(__dirname, 'public/index.html')); 
}); 

app.post('/subasta', (req, res) => { 
    const idLote = req.body.idLote;
    const comerciante = req.body.comerciante;
    const oferta = Number(req.body.oferta);

    let loteEncontrado = undefined;
    let usuarioEncontrado = undefined;

    const consultaLote = new Promise((resolve, reject) => {
        db.query('SELECT * FROM lotes WHERE id = ?', [idLote], (err, filas) => {
            if (err) return reject(err);
            
            if (filas.length > 0) {
                loteEncontrado = Object.assign({}, filas.item || filas.fields || filas.rows || filas);
                filas.forEach((elemento) => { loteEncontrado = elemento; });
            }
            resolve();
        });
    });

    const consultaUsuario = new Promise((resolve, reject) => {
        db.query('SELECT * FROM comerciantes WHERE nombre = ?', [comerciante], (err, filas) => {
            if (err) return reject(err);
            
            if (filas.length > 0) {
                usuarioEncontrado = Object.assign({}, filas.item || filas.fields || filas.rows || filas);
                filas.forEach((elemento) => { usuarioEncontrado = elemento; });
            }
            resolve();
        });
    });

    Promise.all([consultaLote, consultaUsuario])
    .then(() => {
        if (loteEncontrado === undefined || usuarioEncontrado === undefined) {
            return res.send('<h1>Error de Validación</h1><p>El ID del lote o el nombre de comerciante no están registrados en el sistema.</p>');
        }

        if (oferta > usuarioEncontrado.saldo) {
            return res.send('<h1>Fallo de Fondos</h1><p>Saldo insuficiente.</p>');
        }

        if (oferta <= loteEncontrado.puja_acutual) {
            return res.send('<h1>Puja Rechazada</h1><p>Tu oferta debe ser mayor a la actual.</p>');
        }

        const actualizaUsuario = new Promise((resolve, reject) => {
            db.query('UPDATE comerciantes SET saldo = saldo - ? WHERE nombre = ?', [oferta, comerciante], (err) => {
                if (err) return reject(err);
                resolve();
            });
        });

        const actualizaLote = new Promise((resolve, reject) => {
            db.query('UPDATE lotes SET puja_acutual = ?, lider = ? WHERE id = ?', [oferta, comerciante, idLote], (err) => {
                if (err) return reject(err);
                resolve();
            });
        });

        return Promise.all([actualizaUsuario, actualizaLote]);
    })
    .then(() => {
        res.send('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Operación Exitosa</title></head><body><h1>¡Operación Exitosa!</h1><p>Puja registrada correctamente.</p><br><a href="/consultar">Ver Estado</a></body></html>');
    })
    .catch((error) => {
        res.send('<h1>Error en el sistema:</h1><p>' + error.message + '</p>');
    });
});

app.get('/consultar', (req, res) => {
    let listaDeLotes = undefined;
    let listaDeComerciantes = undefined;

    const traerLotes = new Promise((resolve, reject) => {
        db.query('SELECT * FROM lotes', (err, filas) => {
            if (err) return reject(err);
            listaDeLotes = filas;
            resolve();
        });
    });

    const traerComerciantes = new Promise((resolve, reject) => {
        db.query('SELECT * FROM comerciantes', (err, filas) => {
            if (err) return reject(err);
            listaDeComerciantes = filas;
            resolve();
        });
    });

    Promise.all([traerLotes, traerComerciantes])
    .then(() => {
        let filasLotesHTML = '';
        if (listaDeLotes) {
            listaDeLotes.forEach((lote) => {
                filasLotesHTML = filasLotesHTML + '<tr><td>' + lote.id + '</td><td>' + lote.puja_acutual + '</td><td>' + lote.lider + '</td></tr>';
            });
        }

        let filasComerciantesHTML = '';
        if (listaDeComerciantes) {
            listaDeComerciantes.forEach((comerciante) => {
                filasComerciantesHTML = filasComerciantesHTML + '<tr><td>' + comerciante.nombre + '</td><td>' + comerciante.saldo + '</td></tr>';
            });
        }

        res.send('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Estado de la Subasta</title><link rel="stylesheet" href="/css/estilos.css"></head><body><h1>Estado de la Subasta</h1><h3>Tabla de Lotes</h3><table border="1"><tr><th>ID</th><th>Puja Actual</th><th>Líder</th></tr>' + filasLotesHTML + '</table><br><h3>Tabla de Comerciantes</h3><table border="1"><tr><th>Nombre</th><th>Saldo</th></tr>' + filasComerciantesHTML + '</table></body></html>');
    })
    .catch((error) => {
        res.send('<h1>Error al consultar el mercado:</h1><p>' + error.message + '</p>');
    });
});

app.listen(PORT, () => { 
    console.log('Servidor escuchando en http://localhost:' + PORT); 
});



