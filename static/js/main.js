let materialActualId = null;
let urlDescargaActual = "";

function iniciarDesbloqueo(id, titulo, url) {
    materialActualId = id;
    urlDescargaActual = url;

    const modal = document.getElementById("modalAnuncio");
    const contadorEl = document.getElementById("contador");
    const areaContador = document.getElementById("areaContador");
    const areaDescarga = document.getElementById("areaDescarga");
    const btnDescarga = document.getElementById("btnDescargaFinal");

    // Reiniciar interfaz del modal
    modal.classList.remove("hidden");
    modal.classList.add("flex");
    areaDescarga.classList.add("hidden");
    areaContador.classList.remove("hidden");

    let segundos = 10;
    contadorEl.innerText = segundos;

    const temporizador = setInterval(() => {
        segundos--;
        contadorEl.innerText = segundos;

        if (segundos <= 0) {
            clearInterval(temporizador);
            areaContador.classList.add("hidden");
            btnDescarga.href = urlDescargaActual;
            areaDescarga.classList.remove("hidden");
        }
    }, 1000);
}

function confirmarDesbloqueoServidor() {
    if (!materialActualId) return;

    fetch(`/api/desbloquear/${materialActualId}`, { method: "POST" })
        .then(res => res.json())
        .then(data => {
            setTimeout(() => {
                location.reload();
            }, 1000);
        });
}

function procesarPagoVIP() {
    const linkDePago = "https://paypal.me/tuusuario/4.99USD";
    window.open(linkDePago, "_blank");

    if (confirm("¿Completaste el pago en la pasarela? Haz clic en Aceptar para activar tu acceso VIP.")) {
        fetch("/api/pago-premium", { method: "POST" })
            .then(res => res.json())
            .then(data => {
                alert("¡Felicidades! Tu cuenta ahora es Premium y no verás anuncios.");
                location.reload();
            });
    }
}

function procesarCompraLibro(libroId, linkCompra) {
    window.open(linkCompra, "_blank");

    if (confirm("Se ha abierto la pasarela de pago. ¿Completaste la compra del libro?")) {
        fetch(`/api/comprar-libro/${libroId}`, { method: "POST" })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("¡Gracias por tu compra! Tu libro ha sido desbloqueado.");
                    location.reload();
                }
            })
            .catch(err => console.error("Error al registrar la compra:", err));
    }
}