require('dotenv').config();
const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static('public'));


const rutaIdentificar = require('./routes/identificar');
app.use('/identificar', rutaIdentificar);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => { 
  console.log(`Servidor corriendo en http://localhost:${PORT}`); 
});
