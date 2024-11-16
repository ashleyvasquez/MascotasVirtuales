const API_URL = "http://127.0.0.1:5002";

document.getElementById('form-adoptar').addEventListener('submit', async (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const especie = document.getElementById('especie').value;

    const response = await fetch(`${API_URL}/mascotas/adoptar`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, especie, usuario_id: "user_123" })
    });

    if (response.ok) {
        const nuevaMascota = await response.json();
        agregarMascota(nuevaMascota);
    }
});

const cargarMascotas = async () => {
    const response = await fetch(`${API_URL}/mascotas/listar?usuario_id=user_123`);
    const mascotas = await response.json();

    mascotas.forEach(mascota => agregarMascota(mascota));
};

const agregarMascota = (mascota) => {
    const lista = document.getElementById('lista-mascotas');

    const card = document.createElement('div');
    card.className = 'mascota-card';
    card.innerHTML = `
        <h3>${mascota.nombre} (${mascota.especie})</h3>
        <p>Felicidad: ${mascota.felicidad}</p>
        <p>Hambre: ${mascota.hambre}</p>
        <p>Salud: ${mascota.salud}</p>
    `;

    lista.appendChild(card);
};

cargarMascotas();
