function getFlag(name){
    const idx = process.argv.indexOf(`--${name}`);


    

    if (idx !== -1 && 
        idx + 1 < process.argv.length && 
        process.argv[idx + 1] &&
        !process.argv[idx +1].startsWith("--")) {
        return process.argv[idx + 1];

        }

        return "Invitado";

}


const name = getFlag("name")
const times = Number (getFlag("times")) || 1;


if (!Number.isInteger(times) || times <= 0) {
    console.error("El valor de times debe ser un numero entero y positivo ")
    console.exit(1);
}



for (let index = 0; index < times; index ++) {
    console.log(`Hola ${name}, bienvenido a la programacion avanzada!`);
}

const help= Number(getFlag("help"))

if (help === 1){
    console.log("HOLA ")
}
