async function obtenerUsuario() {
    try{
        console.log("solicitar datos...")
        const respuesta = await fetch("https://jsonplaceholder.typicode.com/users")

        if(!respuesta.ok)
            throw new Error("Error HTTP:", respuesta.status)

        const usuarios = await respuesta.json()
        console.log("Usuarios recibidos: ", usuarios)
    }
    catch(error){
        console.error("Hubo un problema con la solicitud", error.message)
    }
}

obtenerUsuario()



// Enviar datos con un post

async function crearUsuario(){
    const nuevoUsuario = {
        name:"Julian Guzman",
        email:"julianj@gmail.com"
    }

    try{
        const respuesta = await fetch("https://jsonplaceholder.typicode.com/users", {
            method: "POST",
            header:{
                "Content-Type": "application/json"
            },                  
            body: JSON.stringify(nuevoUsuario)                                                          
        })
        const data= await respuesta.json()
        console.log("Usuario creado:", data)
    }
    catch (error){
        console.log("Hubo un problema con la creacion", error.message)
    }
}

crearUsuario()


const res = await fetch("")
const html = await res.text()
console.log(html)
//-----------------
<img id = "imagen" width = "300"/>
async function cargarImagen(){
    try{
      const rest = await fetch("https://pluhe.com")

      const blob = await res.blob();
      const urlTemporal = URL.createObjectURL(blob)

        document.getElementById("imagen").src = urlTemporal

        console.log("La imagen esta cargada en memoria")
    }
    catch(error){
        console.error("Error al desgargar", error)
    }
}