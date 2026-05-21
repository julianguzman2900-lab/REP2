

function prepararCafe(tipoDeCafe, ms) {
    return new Promise((resolve) => {
    
        console.log(`Barista: Iniciando preparacion de ${tipoDeCafe}`);
        
        setTimeout(() => {
            resolve(`Su ${tipoDeCafe} esta listo `);
        }, ms);
    });
}

function prepararPastel(tipoDePastel, ms){
    return new Promise((resolve)=>{
    console.log(`preparando pastel ${tipoDePastel}`);
    setTimeout(()=>{
        resolve(`Su pastel de ${tipoDePastel} fue entregado  `)
    }, ms);
    })
}


async function atenderCliente() {
    console.log("Inicio de atencion");

    const r1 = await prepararCafe("Capuccino", 3000);
    console.log(r1);

    const rp = await prepararPastel("Selva negra", 4000);
    console.log(rp)

    const r2 = await prepararCafe("Espresso", 6000);
    console.log(r2);

    const rp2 = await prepararPastel("Frutos del bosque", 7000);
    console.log(rp2);
   
    console.log("Fin de atencion");
}


atenderCliente();
