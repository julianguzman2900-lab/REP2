const num1 = Number (process.argv[2])
const num2 = Number (process.rgv[3])
const altura =parseFloat(process.argv[4])
const edad= parseFloat(process.argv[5],10)
if (isNaN(num1) || isNaN(num2)){
    console.error("Por favor, proporciona dos numeros con argumentos validos")
    console.log("Uso: node.suma.js <num1> <num2>");
    process.exit(1);

}