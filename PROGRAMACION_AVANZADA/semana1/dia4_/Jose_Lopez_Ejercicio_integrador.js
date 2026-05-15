const libros = [
    { id: 1, titulo: "Cien años de soledad", disponible: true },
    { id: 2, titulo: "Don Quijote de la Mancha", disponible: false },
    { id: 3, titulo: "El Principito", disponible: true },
    { id: 4, titulo: "1984", disponible: true },
    { id: 5, titulo: "La Odisea", disponible: false }
]

function filtrarDisponibles(listaLibros, criterio) {

    let librosFiltrados = []

    listaLibros.forEach(libro => {

        if (criterio(libro)) {
            librosFiltrados.push(libro)
        }

    })

    return librosFiltrados
}

function obtenerLibrosServidor(callback) {

    console.log("Buscando libros en el servidor...")

    setTimeout(() => {

        const servidorCaido = Math.random() <0.2

        if (servidorCaido)
            return callback(
                "Error: Fallo en la comunicación con el servidor",
                null
            )

        callback(null, libros)

    }, 2000)
}

obtenerLibrosServidor((mensajeError, listaLibros) => {

    if (mensajeError)
        return console.log(mensajeError)

    const librosDisponibles = filtrarDisponibles(
        listaLibros,
        libro => libro.disponible
    )

    console.log("Libros disponibles:")

    librosDisponibles.forEach(libro => {
        console.log(libro.titulo)
    })

})