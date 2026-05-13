const piloto = process.argv[2]
const carga = parseFloat(process.argv[3])
const capacidad = parseFloat(process.argv[4])

if (isNaN(carga) || isNaN(capacidad) || carga < 0 || capacidad <= 0) {
    console.error("Error: Los datos de carga y capacidad deben ser números válidos.")
    process.exit(1)
}

const calcularPorcentaje = (carga, capacidad) => (carga / capacidad) * 100
const porcentaje = calcularPorcentaje(carga, capacidad)

let estado;
if (porcentaje > 90) {
    estado = "Peligro"
} else {
    estado = "Seguro"
}

const reporte = {
    "piloto": piloto,
    "carga": carga,
    "capacidad": capacidad,
    "porcentaje": porcentaje,
    "estado": estado
}

console.log("Analizando despacho para: " + piloto + "...")
console.log(reporte)

if (estado === "Peligro") {
    console.log("¡ALERTA!: Peso excedido, despegue abortado.")
}