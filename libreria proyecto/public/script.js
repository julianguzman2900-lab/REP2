let libros = [];
let carrito = [];

const grillaLibros = document.getElementById('grillaLibros');
const buscador = document.getElementById('buscador');
const filtrosBtns = document.querySelectorAll('.filtro-btn');
const carritoBtn = document.getElementById('carritoBtn');
const carritoDesplegable = document.getElementById('carritoDesplegable');
const contadorCarrito = document.getElementById('contadorCarrito');
const listaCarrito = document.getElementById('listaCarrito');
const totalCarrito = document.getElementById('totalCarrito');
const modalLibro = document.getElementById('modalLibro');
const cerrarModal = document.getElementById('cerrarModal');
const contenidoModal = document.getElementById('contenidoModal');
const formContacto = document.getElementById('formContacto');

document.addEventListener('DOMContentLoaded', () => {
    cargarLibros();
    configurarFiltros();
    configurarBuscador();
    configurarCarrito();
    configurarModal();
    configurarFormulario();
});

async function cargarLibros(genero = 'todos') {
    try {
        let url = '/api/libros';
        if (genero !== 'todos') url = `/api/libros/genero/${genero}`;
        
        const respuesta = await fetch(url);
        libros = await respuesta.json();
        mostrarLibros(libros);
    } catch (error) {
        console.error('Error al cargar libros:', error);
        grillaLibros.innerHTML = '<p class="col-span-full text-center text-red-500 py-10">Error al cargar los libros</p>';
    }
}

function mostrarLibros(lista) {
    grillaLibros.innerHTML = '';
    
    if(lista.length === 0) {
        grillaLibros.innerHTML = '<p class="col-span-full text-center text-gray-500 py-10">No se encontraron libros</p>';
        return;
    }

    lista.forEach(libro => {
        const tarjeta = document.createElement('div');
        tarjeta.className = 'bg-white rounded-lg shadow-md overflow-hidden card-hover';
        tarjeta.innerHTML = `
            <img src="${libro.imagen}" alt="${libro.titulo}" class="w-full h-64 object-cover">
            <div class="p-4">
                <h3 class="font-bold text-lg mb-1 text-primary">${libro.titulo}</h3>
                <p class="text-gray-600 text-sm mb-2">${libro.autor}</p>
                <p class="font-bold text-secondary text-xl mb-3">$${parseFloat(libro.precio).toFixed(2)}</p>
                <div class="flex gap-2">
                    <button class="ver-detalles flex-1 bg-light hover:bg-gray-200 py-2 rounded transition-colors" data-id="${libro.id}">Ver más</button>
                    <button class="agregar-carrito flex-1 bg-accent text-white hover:bg-opacity-90 py-2 rounded transition-colors" data-id="${libro.id}">Agregar</button>
                </div>
            </div>
        `;
        grillaLibros.appendChild(tarjeta);
    });

    document.querySelectorAll('.agregar-carrito').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = parseInt(e.target.dataset.id);
            agregarAlCarrito(id);
        });
    });

    document.querySelectorAll('.ver-detalles').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = parseInt(e.target.dataset.id);
            abrirModal(id);
        });
    });
}

function configurarFiltros() {
    filtrosBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filtrosBtns.forEach(b => {
                b.classList.remove('active', 'bg-primary', 'text-white');
                b.classList.add('bg-white', 'border', 'border-gray-300');
            });
            btn.classList.add('active', 'bg-primary', 'text-white');
            btn.classList.remove('bg-white', 'border', 'border-gray-300');

            const genero = btn.dataset.genero;
            cargarLibros(genero);
            buscador.value = '';
        });
    });
}

function configurarBuscador() {
    buscador.addEventListener('input', async (e) => {
        const termino = e.target.value.trim();
        if (termino === '') {
            cargarLibros();
            return;
        }
        try {
            const res = await fetch(`/api/buscar/${termino}`);
            const resultados = await res.json();
            mostrarLibros(resultados);
            
            filtrosBtns.forEach(b => {
                b.classList.remove('active', 'bg-primary', 'text-white');
                b.classList.add('bg-white', 'border', 'border-gray-300');
            });
            document.querySelector('[data-genero="todos"]').classList.add('active', 'bg-primary', 'text-white');
        } catch (error) {
            console.error('Error en búsqueda:', error);
        }
    });
}

function configurarCarrito() {
    carritoBtn.addEventListener('click', () => {
        carritoDesplegable.classList.toggle('translate-x-96');
        carritoDesplegable.classList.toggle('opacity-0');
    });

    document.addEventListener('click', (e) => {
        if(!carritoBtn.contains(e.target) && !carritoDesplegable.contains(e.target)) {
            carritoDesplegable.classList.add('translate-x-96', 'opacity-0');
        }
    });
}

function agregarAlCarrito(idLibro) {
    const libro = libros.find(l => l.id === idLibro);
    const itemExistente = carrito.find(item => item.libro.id === idLibro);

    if(itemExistente) {
        itemExistente.cantidad++;
    } else {
        carrito.push({libro: libro, cantidad: 1});
    }
    
    actualizarCarritoUI();
    mostrarNotificacion(`"${libro.titulo}" agregado al carrito`);
}

function actualizarCarritoUI() {
    const totalItems = carrito.reduce((acc, item) => acc + item.cantidad, 0);
    contadorCarrito.textContent = totalItems;

    if(carrito.length === 0) {
        listaCarrito.innerHTML = '<p class="text-gray-500 text-center">Tu carrito está vacío</p>';
        totalCarrito.textContent = '$0.00';
        return;
    }

    listaCarrito.innerHTML = '';
    let total = 0;

    carrito.forEach((item, index) => {
        const subtotal = item.libro.precio * item.cantidad;
        total += subtotal;

        const elemento = document.createElement('div');
        elemento.className = 'flex justify-between items-center py-2 border-b';
        elemento.innerHTML = `
            <div class="flex-1">
                <h4 class="font-medium text-sm">${item.libro.titulo}</h4>
                <p class="text-xs text-gray-600">$${parseFloat(item.libro.precio).toFixed(2)} x ${item.cantidad}</p>
            </div>
            <div class="flex items-center gap-2">
                <button class="text-gray-500 hover:text-dark px-1" onclick="cambiarCantidad(${index}, -1)">-</button>
                <span>${item.cantidad}</span>
                <button class="text-gray-500 hover:text-dark px-1" onclick="cambiarCantidad(${index}, 1)">+</button>
                <button class="text-red-500 hover:text-red-700 ml-2" onclick="eliminarDelCarrito(${index})">
                    <i class="fa fa-trash"></i>
                </button>
            </div>
        `;
        listaCarrito.appendChild(elemento);
    });

    totalCarrito.textContent = `$${total.toFixed(2)}`;
}

function cambiarCantidad(indice, cambio) {
    carrito[indice].cantidad += cambio;
    if(carrito[indice].cantidad <= 0) {
        carrito.splice(indice, 1);
    }
    actualizarCarritoUI();
}

function eliminarDelCarrito(indice) {
    carrito.splice(indice, 1);
    actualizarCarritoUI();
}

function configurarModal() {
    cerrarModal.addEventListener('click', () => {
        modalLibro.classList.add('hidden');
    });
    modalLibro.addEventListener('click', (e) => {
        if(e.target === modalLibro) modalLibro.classList.add('hidden');
    });
}

function abrirModal(idLibro) {
    const libro = libros.find(l => l.id === idLibro);
    contenidoModal.innerHTML = `
        <div>
            <img src="${libro.imagen}" alt="${libro.titulo}" class="w-full h-auto rounded-lg shadow-md">
            <p class="text-sm text-gray-500 mt-2">Stock disponible: ${libro.stock}</p>
        </div>
        <div>
            <h2 class="text-2xl font-bold text-primary mb-2">${libro.titulo}</h2>
            <p class="text-gray-600 mb-4"><strong>Autor:</strong> ${libro.autor}</p>
            <p class="text-gray-600 mb-4"><strong>Género:</strong> ${libro.genero.charAt(0).toUpperCase() + libro.genero.slice(1)}</p>
            <p class="text-xl font-bold text-secondary mb-4">$${parseFloat(libro.precio).toFixed(2)}</p>
            <p class="mb-6 text-gray-700 leading-relaxed">${libro.descripcion}</p>
            <button class="w-full bg-accent text-white py-3 rounded-lg hover:bg-opacity-90 transition-colors agregar-carrito" data-id="${libro.id}">Agregar al carrito</button>
        </div>
    `;
    
    contenidoModal.querySelector('.agregar-carrito').addEventListener('click', () => {
        agregarAlCarrito(libro.id);
        modalLibro.classList.add('hidden');
    });

    modalLibro.classList.remove('hidden');
}

function mostrarNotificacion(mensaje) {
    const notif = document.createElement('div');
    notif.className = 'fixed bottom-4 right-4 bg-primary text-white px-6 py-3 rounded-lg shadow-lg transform transition-all duration-500 translate-y-20 opacity-0';
    notif.textContent = mensaje;
    document.body.appendChild(notif);

    setTimeout(() => notif.classList.remove('translate-y-20', 'opacity-0'), 10);
    setTimeout(() => {
        notif.classList.add('translate-y-20', 'opacity-0');
        setTimeout(() => notif.remove(), 500);
    }, 3000);
}

function configurarFormulario() {
    formContacto.addEventListener('submit', (e) => {
        e.preventDefault();
        mostrarNotificacion('¡Mensaje enviado con éxito! Te responderemos pronto.');
        formContacto.reset();
    });
}