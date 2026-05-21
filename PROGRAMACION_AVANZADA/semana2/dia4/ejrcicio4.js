// function tarea(ms, nombre) { 
//     return new Promise( resolve => { 
//         setTimeout( () => resolve(`${nombre} lista en ${ms} ms`), ms ) 
//     } ) 
// } 

// async function ejemploAll() { 
//     const promesa1 = tarea(5000, "Lavar"); 
//     const promesa2 = tarea(3000, "Cocinar"); 
//     const promesa3 = tarea(6000, "Limpiar"); 
//     const promesa4 = tarea(2000, "Aplanchar"); 
    
//     const [prom1, prom2, prom3, prom4] = await Promise.all([promesa1, promesa2, promesa3, promesa4]) 
    
//     console.log(promesa1) 
//     console.log(promesa2) 
//     console.log(promesa3) 
//     console.log(promesa4) 
// }


// ejemploAll(); 







function prepararCafe(tipoDeCafe, ms) { 
  return new Promise((resolve) => { 
    console.log(`Barista: Iniciando preparacion de ${tipoDeCafe}`); 
    setTimeout(() => { 
      resolve(tipoDeCafe); 
    }, ms); 
  }); 
} 

function prepararPastel(tipoDePastel, ms){ 
  return new Promise((resolve)=>{ 
    console.log(`preparando pastel ${tipoDePastel}`); 
    setTimeout(()=>{ 
      resolve(tipoDePastel); 
    }, ms); 
  }) 
} 

async function atenderCliente() { 
  console.log("Inicio de atencion"); 


  const promesaCafe1 = prepararCafe("Capuccino", 3000); 
  const promesaPastel1 = prepararPastel("Selva negra", 4000); 
  const [cafe1, pastel1] = await Promise.allSettled([promesaCafe1, promesaPastel1]); 
 
  console.log(`Combo entregado: ${cafe1} y ${pastel1}`); 


  const promesaCafe2 = prepararCafe("Espresso", 6000); 
  const promesaPastel2 = prepararPastel("Frutos del bosque", 7000); 
  const [cafe2, pastel2] = await Promise.allSettled([promesaCafe2, promesaPastel2]); 

  console.log(`Combo entregado: ${cafe2} y ${pastel2}`); 

  console.log("Fin de atencion"); 
} 

atenderCliente();
