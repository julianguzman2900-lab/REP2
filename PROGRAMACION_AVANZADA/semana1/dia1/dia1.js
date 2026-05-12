// console.log("Hola Mundo");

// const pi = 3.14159
// let radio = 7
// let area = pi*radio*radio
// console.log(area)


// const numero= 20

// let esValido = numero > 10 && numero % 2==0
// console.log(esValido)


// const temperatura= 20



// switch(true){
//     case temperatura < 15:
//         console.log("Frio")
//         break
//     case temperatura > 15 && temperatura <25:
//         console.log("Templado")
//         break
//     default:
//             console.log("Caliente")
        

// // }
    

// const temperatura = 14;
// let resultado;

// if (temperatura < 15) {
//     resultado = "Frio";
// } else if (temperatura >= 15 && temperatura < 25) { 
//     resultado = "Templado";
// } else {
//     resultado = "Caliente";
// }

// console.log(re
 function maximo(a,b,c){
    if (a>=b && a>=c){
        return a;

    } else if (b>=a && b>=c){
        return b;
    }
    else{
        return c;
    }

 }
console.log("El mayor del primer conjunto (10, 25, 15) es:", maximo(10, 25, 15));
console.log("El mayor del segundo conjunto (100, 50, 80) es:", maximo(100, 50, 80));


