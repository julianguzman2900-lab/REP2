const express = require('express');
const router = express.Router();
const identificarController = require('../controllers/identificarController');

router.post('/', identificarController.procesarFormulario);

module.exports = router;
