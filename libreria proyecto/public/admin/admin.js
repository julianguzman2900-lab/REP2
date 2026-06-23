// Verificar si está logueado
document.addEventListener('DOMContentLoaded', () => {
    if (!localStorage.getItem('adminLogueado')) {
        window.location.href = 'login.html';
        return;
    }

    // Mostrar nombre e inicial
    const nombre = localStorage.getItem('adminNombre');
    document.getElementById('nombreAdmin').textContent = nombre;
    document.getElementById('inicialUsuario').textContent = nombre.charAt(0).toUpperCase();

    cargarLibrosAdmin();
    configurarEventos();
});

let modoEdicion = false;
let librosGlobales = [];

// Elementos
const tablaLibros = document.getElementById('tablaLibros');
const btnAgregar = document.getElementById('btnAgregar');
const modalFormulario = document.getElementById('modalFormulario');
const modalContenido = document.getElementById('modalContenido');
const cerrarModal = document.getElementById('cerrarModal');
const formLibro = document.getElementById('formLibro');
const tituloModal = document.getElementById('tituloModal');
const alerta = document.getElementById('alerta');
const btnCerrar = document.getElementById('btnCerrar');
const estadisticasDiv = document.getElementById('estadisticas');

function configurarEventos() {
    // Abrir modal agregar
    btnAgregar.addEventListener('click', () => {
        modoEdicion = false;
        tituloModal.textContent = 'Agregar Nuevo Libro';
        formLibro.reset();
        document.getElementById('libroId').value = '';
        abrirModal();
    });

    // Cerrar modal
    cerrarModal.addEventListener('click', cerrarModalFunc);
    modalFormulario.addEventListener('click', (e) => {
        if(e.target === modalFormulario) cerrarModalFunc();
    });
    
    // Guardar formulario
    formLibro.addEventListener('submit', guardarLibro);

    // Cerrar sesión
    btnCerrar.addEventListener('click', () => {
        localStorage.removeItem('adminLogueado');
        localStorage.removeItem('adminNombre');
        window.location.href = 'login.html';
    });
}

// 🚀 Funciones MODAL con animación
function abrirModal() {
    modalFormulario.classList.remove('hidden');
    setTimeout(() => {
        modalContenido.classList.remove('scale-95', 'opacity-0');
        modalContenido.classList.add('scale-100', 'opacity-100');
    }, 10);
    document.body.style.overflow = 'hidden';
}

function cerrarModalFunc() {
    modalContenido.classList.remove('scale-100', 'opacity-100');
    modalContenido.classList.add('scale-95', 'opacity-0');
    setTimeout(() => {
        modalFormulario.classList.add('hidden');
    }, 300);
    document.body.style.overflow = 'auto';
}

// 📊 CARGAR DATOS
async function cargarLibrosAdmin() {
    try {
        const res = await fetch('/api/libros');
        librosGlobales = await res.json();
        
        actualizarEstadisticas(librosGlobales);
        renderizarTabla(librosGlobales);

    } catch (error) {
        tablaLibros.innerHTML = `
            <tr>
                <td colspan="6" class="px-6 py-12 text-center text-danger">
                    <i class="fa fa-exclamation-triangle fa-2x mb-3"></i>
                    <p>Error al cargar los datos. Intenta recargar.</p>
                </td>
            </tr>
        `;
    }
}

function actualizarEstadisticas(libros) {
    const total = libros.length;
    const precioMax = Math.max(...libros.map(l => l.precio), 0);
    const totalStock = libros.reduce((acc, l) => acc + l.stock, 0);
    const generos = [...new Set(libros.map(l => l.genero))].length;

    estadisticasDiv.innerHTML = `
        <div class="bg-white rounded-2xl shadow-card p-5 border-l-4 border-primary">
            <div class="flex justify-between items-start">
                <div>
                    <p class="text-gray-500 text-sm font-medium">Total Libros</p>
                    <h3 class="text-[clamp(1.5rem,2vw,2rem)] font-bold text-dark mt-1">${total}</h3>
                </div>
                <div class="w-10 h-10 rounded-lg bg-primary/10 text-primary flex items-center justify-center">
                    <i class="fa fa-book"></i>
                </div>
            </div>
        </div>
        <div class="bg-white rounded-2xl shadow-card p-5 border-l-4 border-success">
            <div class="flex justify-between items-start">
                <div>
                    <p class="text-gray-500 text-sm font-medium">En Inventario</p>
                    <h3 class="text-[clamp(1.5rem,2vw,2rem)] font-bold text-dark mt-1">${totalStock}</h3>
                </div>
                <div class="w-10 h-10 rounded-lg bg-success/10 text-success flex items-center justify-center">
                    <i class="fa fa-cubes"></i>
                </div>
            </div>
        </div>
        <div class="bg-white rounded-2xl shadow-card p-5 border-l-4 border-info">
            <div class="flex justify-between items-start">
                <div>
                    <p class="text-gray-500 text-sm font-medium">Géneros</p>
                    <h3 class="text-[clamp(1.5rem,2vw,2rem)] font-bold text-dark mt-1">${generos}</h3>
                </div>
                <div class="w-10 h-10 rounded-lg bg-info/10 text-info flex items-center justify-center">
                    <i class="fa fa-tags"></i>
                </div>
            </div>
        </div>
        <div class="bg-white rounded-2xl shadow-card p-5 border-l-4 border-warning">
            <div class="flex justify-between items-start">
                <div>
                    <p class="text-gray-500 text-sm font-medium">Precio Máx.</p>
                    <h3 class="text-[clamp(1.5rem,2vw,2rem)] font-bold text-dark mt-1">$${precioMax.toFixed(2)}</h3>
                </div>
                <div class="w-10 h-10 rounded-lg bg-warning/10 text-warning flex items-center justify-center">
                    <i class="fa fa-dollar"></i>
                </div>
            </div>
        </div>
    `;
}

function renderizarTabla(libros) {
    tablaLibros.innerHTML = '';

    libros.forEach((libro, index) => {
        const fila = document.createElement('tr');
        fila.className = 'hover:bg-gray-50 transition-custom';
        fila.style.animationDelay = `${index * 50}ms`;
        fila.innerHTML = `
            <td class="px-6 py-4 text-gray-500 font-mono">${libro.id}</td>
            <td class="px-6 py-4">
                <div class="flex items-center gap-3">
                    <img src="${libro.imagen}" alt="${libro.titulo}" class="w-12 h-16 object-cover rounded-lg shadow">
                    <div>
                        <h4 class="font-semibold text-gray-800 line-clamp-1">${libro.titulo}</h4>
                        <p class="text-xs text-gray-500">${libro.autor}</p>
                    </div>
                </div>
            </td>
            <td class="px-6 py-4">
                <span class="px-3 py-1 bg-primary/10 text-primary text-xs rounded-full font-medium">${libro.genero.charAt(0).toUpperCase() + libro.genero.slice(1)}</span>
            </td>
            <td class="px-6 py-4 text-center font-medium text-gray-800">$${parseFloat(libro.precio).toFixed(2)}</td>
            <td class="px-6 py-4 text-center">
                <span class="font-semibold ${libro.stock > 10 ? 'text-success' : libro.stock > 0 ? 'text-warning' : 'text-danger'}">
                    ${libro.stock}
                </span>
            </td>
            <td class="px-6 py-4 text-right">
                <div class="flex justify-end gap-2">
                    <button class="editar-btn p-2 text-info hover:bg-info/10 rounded-lg transition-custom" data-id="${libro.id}" title="Editar">
                        <i class="fa fa-pencil"></i>
                    </button>
                    <button class="eliminar-btn p-2 text-danger hover:bg-danger/10 rounded-lg transition-custom" data-id="${libro.id}" title="Eliminar">
                        <i class="fa fa-trash"></i>
                    </button>
                </div>
            </td>
        `;
        tablaLibros.appendChild(fila);
    });

    // Eventos
    document.querySelectorAll('.editar-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const id = e.currentTarget.dataset.id;
            await abrirEdicion(id);
        });
    });

    document.querySelectorAll('.eliminar-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const id = e.currentTarget.dataset.id;
            if(confirm('¿Estás seguro? Esta acción no se puede deshacer.')) {
                await eliminarLibro(id);
            }
        });
    });
}

// ✏️ EDITAR
async function abrirEdicion(id) {
    try {
        const res = await fetch(`/api/libros/${id}`);
        const libro = await res.json();

        modoEdicion = true;
        tituloModal.textContent = 'Editar Libro';
        
        // Llenar formulario
        document.getElementById('libroId').value = libro.id;
        document.getElementById('titulo').value = libro.titulo;
        document.getElementById('autor').value = libro.autor;
        document.getElementById('genero').value = libro.genero;
        document.getElementById('precio').value = libro.precio;
        document.getElementById('stock').value = libro.stock;
        document.getElementById('imagen').value = libro.imagen;
        document.getElementById('descripcion').value = libro.descripcion;

        abrirModal();
    } catch (error) {
        mostrarAlerta('Error al cargar datos', 'error');
    }
}

// 💾 GUARDAR
async function guardarLibro(e) {
    e.preventDefault();
    
    const datosLibro = {
        titulo: document.getElementById('titulo').value,
        autor: document.getElementById('autor').value,
        genero: document.getElementById('genero').value,
        precio: parseFloat(document.getElementById('precio').value),
        stock: parseInt(document.getElementById('stock').value),
        imagen: document.getElementById('imagen').value,
        descripcion: document.getElementById('descripcion').value
    };

    try {
        let url, metodo;

        if (modoEdicion) {
            const id = document.getElementById('libroId').value;
            url = `/api/admin/libros/${id}`;
            metodo = 'PUT';
        } else {
            url = '/api/admin/libros';
            metodo = 'POST';
        }

        const res = await fetch(url, {
            method: metodo,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(datosLibro)
        });

        const respuesta = await res.json();

        if (respuesta.exito) {
            mostrarAlerta(respuesta.mensaje, 'exito');
            cerrarModalFunc();
            cargarLibrosAdmin();
            formLibro.reset();
        } else {
            mostrarAlerta(respuesta.mensaje, 'error');
        }

    } catch (error) {
        mostrarAlerta('Error de conexión', 'error');
    }
}

// 🗑️ ELIMINAR
async function eliminarLibro(id) {
    try {
        const res = await fetch(`/api/admin/libros/${id}`, { method: 'DELETE' });
        const respuesta = await res.json();
        
        if (respuesta.exito) {
            mostrarAlerta(respuesta.mensaje, 'exito');
            cargarLibrosAdmin();
        } else {
            mostrarAlerta(respuesta.mensaje, 'error');
        }
    } catch (error) {
        mostrarAlerta('Error al eliminar', 'error');
    }
}

// 🔔 ALERTA
function mostrarAlerta(mensaje, tipo) {
    alerta.textContent = mensaje;
    alerta.classList.remove('hidden', 'bg-green-100', 'text-green-800', 'bg-red-100', 'text-red-800');
    
    if (tipo === 'exito') {
        alerta.classList.add('bg-green-100', 'text-green-800');
    } else {
        alerta.classList.add('bg-red-100', 'text-red-800');
    }

    alerta.classList.remove('translate-y-2', 'opacity-0');
    alerta.classList.add('translate-y-0', 'opacity-100');

    setTimeout(() => {
        alerta.classList.add('translate-y-2', 'opacity-0');
        setTimeout(() => alerta.classList.add('hidden'), 300);
    }, 4000);
}