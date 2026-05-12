function saludo(nombre){
    console.log(`Hola ${nombre}, bienvenido a la programacion avanzada`)
}


saludo("Juan");

const nombre = process.argv[2] ;

if (!nombre){
    console.error("Por favor, proporciona un nombre como argumento")
    console.log ("Uso: node dia2.js <nombre>");
    process.exit(1)
}

console.log(globalThis)


