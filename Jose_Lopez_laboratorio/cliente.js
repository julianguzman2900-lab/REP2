const recurso = process.argv[2];
const peso = Number(process.argv[3]);

if (!recurso || isNaN(peso)) {
    process.exit(1);
}

const prepararPaquete = (nombre, kg, callback) => {
    console.log(`1. Empacando ${nombre}...`);
    callback();
};

prepararPaquete(recurso, peso, () => {
    console.log("2. Enviando datos al servidor central...");

    setTimeout(() => {
        if (peso > 500) {
            console.log(`[LOG] Recibido pedido de ${recurso} (${peso}kg).`);
            console.log("Estado: RECHAZADO.");
            console.log('Respuesta del Servidor: { "error": "Capacidad de hangar excedida" }');
        } else {
            console.log(`[LOG] Recibido pedido de ${recurso} (${peso}kg).`);
            console.log("Estado: ACEPTADO.");
            console.log('Respuesta del Servidor: { "mensaje": "Despacho programado", "id": "A-102" }');
        }
    }, 1500);
});
