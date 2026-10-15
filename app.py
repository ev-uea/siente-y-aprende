from flask import Flask, render_template, session, jsonify, request

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesion_ad_portal"

# Catálogo de materiales educativos (10 Espacios)
MATERIALES = [
    {
        "id": 1,
        "titulo": "Las Vocales (PDF)",
        "descripcion": "Recurso pedagógico ilustrado para la iniciación en la lectoescritura. Incluye fichas de asociación de sonido e imagen, incluye todas las vocales (A, E, I, O, U) ideal para educación inicial y preescolar.",
        "tipo": "gratis",
        "url_descarga": "https://drive.google.com/file/d/1ZmbVq4PViwcZKEA4zzjRHceQhOc1SMo0/view?usp=drive_link"
    },
    {
        "id": 2,
        "titulo": "Repaso Práctico de las Sílabas",
        "descripcion": "Cuadernillo de reforzamiento enfocado en la combinación fonética de consonantes y vocales. Contiene ejercicios dinámicos de completación, separación silábica y lectura guiada para afianzar el proceso lector en los primeros años de primaria.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1A8Qa1PR5aiC1RW0lPUymJEt1Z2cvYeqa/view?usp=drive_link"
    },
    {
        "id": 3,
        "titulo": "Fichas Ilustradas del Abecedario",
        "descripcion": "Colección completa de fichas visuales que cubren de la A a la Z. Diseñadas para favorecer el reconocimiento gráfico-fonémico, ampliar el vocabulario infantil y servir como material de apoyo multisensorial en el aula de clases.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/14Kog8-8olCtHalZN11IURkEtHXrCCUP0/view?usp=drive_link"
    },
    {
        "id": 4,
        "titulo": "Aprendamos a Leer con Sílabas",
        "descripcion": "Guía didáctica progresiva para el desarrollo de la fluidez lectora mediante el método silábico. Incluye lecturas cortas, construcción de palabras sencillas y actividades de comprensión adaptadas a niños en etapa de iniciación.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1h_brFpBAHEDTtaNITGmMDw5C2d9LG7Pa/view?usp=drive_link"
    },
    {
        "id": 5,
        "titulo": "Actividades de Técnicas Grafoplásticas",
        "descripcion": "Manual práctico de psicomotricidad fina que integra técnicas artísticas tradicionales como arrugado, rasgado, trozado, dactilopintura y puntillismo. Ideal para estimular la coordinación visomotriz y la preparación previa al trazo de letras.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1NOGgSLiYBOXTxOC5c-BryQKoCPVetp_B/view?usp=drive_link"
    },
    {
        "id": 6,
        "titulo": "Ejercicios con Palabras de 3 Sílabas",
        "descripcion": "Cuaderno de trabajo estructurado para el análisis silábico de palabras trisílabas. Desarrolla la conciencia fonológica mediante actividades de conteo de sílabas, ordenamiento, lectura y formación de vocabulario intermedio.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/11TXViQI88CZqPv-z687hvpr9KA82bh8Q/view?usp=drive_link"
    },
    {
        "id": 7,
        "titulo": "Abecedario Completo de Aprendizaje",
        "descripcion": "Material de consulta y referencia alfabética completa con letras en mayúscula y minúscula. Un recurso indispensable para la ambientación del rincón de lectura y el fortalecimiento continuo del reconocimiento de las letras.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1x31RWetfeVk1QeLPtCytengiQlrbXCkx/view?usp=drive_link"
    },
    {
        "id": 8,
        "titulo": "Abecedario Didáctico Para Colorear",
        "descripcion": "Colección de láminas creativas que combinan el aprendizaje alfabético con la expresión artística y el coloreado. Promueve la retención visual, la concentración y la motricidad fina a través del juego y el arte.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1tywEYzkOMXzh27PAE2DONkbdmU8bXK11/view?usp=drive_link"
    },
    {
        "id": 9,
        "titulo": "Abecedario con Trazos y Dibujos",
        "descripcion": "Cuadernillo de grafomotricidad y lectoescritura enfocado en el trazo correcto de las letras del abecedario. Incluye guías direccionales de trazado junto a ilustraciones temáticas para asociar la grafía con su correspondiente sonido inicial.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1HNp17tHEDRjVyQ3uC5v5TbKRXA5LF-aQ/view?usp=drive_link"
    },
    {
        "id": 10,
        "titulo": "Cuadernillo de Fábulas Infantiles y Valores",
        "descripcion": "Recurso de lectura comprensiva que reúne relatos cortos y tradicionales acompañados de preguntas de reflexión y actividades didácticas. Diseñado para fomentar la fluidez lectora, el pensamiento crítico y el desarrollo de valores morales.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1YEfd4ywdLL-8Qhh4D5rkeGr77zOXB8YB/view?usp=drive_link"
    }
]

# Catálogo de Canciones Infantiles (Desbloqueables con anuncios)
CANCIONES_INFANTILES = [
    {
        "id": 201,
        "titulo": "Canción: Los Colores Primarios (MP3 / Video)",
        "descripcion": "Audio pedagógico en alta calidad con letra para cantar en el aula o en casa.",
        "tipo": "desbloqueable",
        "url_descarga": "https://youtu.be/KxiRAw3VgsU?si=GbyDAXXVUsDNJn2N"
    },
    {
        "id": 202,
        "titulo": "Canción: Las Vocales Cantando (MP3)",
        "descripcion": "Pista musical divertida para el aprendizaje de las vocales en educación inicial.",
        "tipo": "desbloqueable",
        "url_descarga": "https://drive.google.com/file/d/1ndai2OwL2C_J8UBB5tDJ7xbUdvrL4RJd/view?usp=sharing"
    }
]

# Catálogo de Libros Exclusivos (Venta Individual)
LIBROS_EXCLUSIVOS = [
    {
        "id": 101,
        "titulo": "Libro no disponible",
        "descripcion": "No disponible",
        "precio": "$0.00",
        "imagen": "/static/img/portada.jpeg",
        "link_compra": "No disponible",
        "url_descarga": ""
    },
    {
        "id": 102,
        "titulo": "Libro no disponible",
        "descripcion": "No disponible",
        "precio": "$0.00",
        "imagen": "/static/img/portada.jpeg",
        "link_compra": "No disponible",
        "url_descarga": ""
    }
]


@app.route("/")
def index():
    desbloqueados = session.get("desbloqueados", [])
    comprados = session.get("comprados", [])

    return render_template(
        "index.html",
        materiales=MATERIALES,
        canciones=CANCIONES_INFANTILES,
        libros=LIBROS_EXCLUSIVOS,
        desbloqueados=desbloqueados,
        comprados=comprados
    )


@app.route("/api/desbloquear/<int:material_id>", methods=["POST"])
def api_desbloquear(material_id):
    """Registra cualquier material o canción como desbloqueado tras ver el anuncio."""
    desbloqueados = session.get("desbloqueados", [])
    if material_id not in desbloqueados:
        desbloqueados.append(material_id)
        session["desbloqueados"] = desbloqueados
    return jsonify({"success": True, "message": "Recurso desbloqueado con éxito."})


@app.route("/api/comprar-libro/<int:libro_id>", methods=["POST"])
def api_comprar_libro(libro_id):
    """Registra la compra individual del libro en la sesión."""
    comprados = session.get("comprados", [])
    if libro_id not in comprados:
        comprados.append(libro_id)
        session["comprados"] = comprados
    return jsonify({"success": True, "message": "¡Libro comprado y desbloqueado con éxito!"})


# --- RUTAS OBLIGATORIAS PARA GOOGLE ADSENSE ---

@app.route("/privacidad")
def privacidad():
    return render_template("privacidad.html")


@app.route("/terminos")
def terminos():
    return render_template("terminos.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)