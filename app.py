from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesion_ad_portal"

# Catálogo de 10 materiales educativos
MATERIALES = [
    {
        "id": 1,
        "titulo": "Las Vocales: Fichas Didácticas (PDF)",
        "descripcion": "Recurso pedagógico ilustrado para la iniciación en la lectoescritura. Incluye ejercicios de discriminación visual, asociación de sonido inicial y trazo guiado.",
        "url_descarga": "https://drive.google.com/file/d/1ZmbVq4PViwcZKEA4zzjRHceQhOc1SMo0/view?usp=drive_link"
    },
    {
        "id": 2,
        "titulo": "Repaso Práctico de las Sílabas",
        "descripcion": "Cuadernillo de reforzamiento enfocado en la combinación fonética de consonantes y vocales. Contiene ejercicios dinámicos para afianzar el proceso lector.",
        "url_descarga": "https://drive.google.com/file/d/1A8Qa1PR5aiC1RW0lPUymJEt1Z2cvYeqa/view?usp=drive_link"
    },
    {
        "id": 3,
        "titulo": "Fichas Ilustradas del Abecedario",
        "descripcion": "Colección completa de fichas visuales que cubren de la A a la Z. Diseñadas para favorecer el reconocimiento gráfico-fonémico y ampliar el vocabulario infantil.",
        "url_descarga": "https://drive.google.com/file/d/14Kog8-8olCtHalZN11IURkEtHXrCCUP0/view?usp=drive_link"
    },
    {
        "id": 4,
        "titulo": "Aprendamos a Leer con Sílabas",
        "descripcion": "Guía didáctica progresiva para el desarrollo de la fluidez lectora mediante el método silábico. Incluye lecturas cortas y ejercicios de identificación.",
        "url_descarga": "https://drive.google.com/file/d/1h_brFpBAHEDTtaNITGmMDw5C2d9LG7Pa/view?usp=drive_link"
    },
    {
        "id": 5,
        "titulo": "Actividades de Técnicas Grafoplásticas",
        "descripcion": "Manual práctico de psicomotricidad fina que integra técnicas artísticas como rasgado, arrugado, trozado y dactilopintura previo al trazo de letras.",
        "url_descarga": "https://drive.google.com/file/d/1NOGgSLiYBOXTxOC5c-BryQKoCPVetp_B/view?usp=drive_link"
    },
    {
        "id": 6,
        "titulo": "Ejercicios con Palabras de 3 Sílabas",
        "descripcion": "Cuaderno de trabajo estructurado para el análisis silábico de palabras trisílabas. Desarrolla la conciencia fonológica y el enriquecimiento de vocabulario.",
        "url_descarga": "https://drive.google.com/file/d/11TXViQI88CZqPv-z687hvpr9KA82bh8Q/view?usp=drive_link"
    },
    {
        "id": 7,
        "titulo": "Abecedario Completo de Aprendizaje",
        "descripcion": "Material de consulta y referencia alfabética completa con letras en mayúscula y minúscula para la ambientación del rincón de lectura.",
        "url_descarga": "https://drive.google.com/file/d/1x31RWetfeVk1QeLPtCytengiQlrbXCkx/view?usp=drive_link"
    },
    {
        "id": 8,
        "titulo": "Abecedario Didáctico Para Colorear",
        "descripcion": "Colección de láminas creativas que combinan el aprendizaje alfabético con la expresión artística y el coloreado para la retención visual.",
        "url_descarga": "https://drive.google.com/file/d/1tywEYzkOMXzh27PAE2DONkbdmU8bXK11/view?usp=drive_link"
    },
    {
        "id": 9,
        "titulo": "Abecedario con Trazos y Dibujos",
        "descripcion": "Cuadernillo de grafomotricidad para el trazo correcto de las letras del abecedario, con guías direccionales e ilustraciones temáticas.",
        "url_descarga": "https://drive.google.com/file/d/1HNp17tHEDRjVyQ3uC5v5TbKRXA5LF-aQ/view?usp=drive_link"
    },
    {
        "id": 10,
        "titulo": "Cuadernillo de Fábulas Infantiles y Valores",
        "descripcion": "Compilación de relatos breves y tradicionales acompañados de preguntas simples de comprensión lectora para fomentar el análisis y los valores.",
        "url_descarga": "https://drive.google.com/file/d/1YEfd4ywdLL-8Qhh4D5rkeGr77zOXB8YB/view?usp=drive_link"
    }
]

# Configuración del Perfil
PERFIL_DATOS = {
    "nombre": "Siente y Aprende",
    "subtitulo": "Creación de Material Didáctico y Recursos Educativos",
    "descripcion": "Bienvenido a Siente y Aprende. Diseñamos recursos didácticos, guías de lectoescritura, canciones educativas y cuadernillos de actividades pensados para acompañar el desarrollo pedagógico en la educación infantil y primaria.",
    "foto": "/static/img/logo.jpeg",
    "portada": "/static/img/portada.jpeg",
    "redes": [
        {
            "id": "youtube",
            "nombre": "YouTube",
            "usuario": "@SienteyAprende",
            "url": "https://www.youtube.com/@SienteyAprende",
            "color": "hover:border-red-500 hover:bg-red-50 group-hover:text-red-600"
        },
        {
            "id": "facebook",
            "nombre": "Facebook",
            "usuario": "Siente y Aprende",
            "url": "https://www.facebook.com/sienteyaprend",
            "color": "hover:border-blue-500 hover:bg-blue-50 group-hover:text-blue-600"
        },
        {
            "id": "instagram",
            "nombre": "Instagram",
            "usuario": "@Sientey_Aprende",
            "url": "https://www.instagram.com/sientey_aprende?srtk=MTJiNHIzazJpem05OQ==",
            "color": "hover:border-pink-500 hover:bg-pink-50 group-hover:text-pink-600"
        },
        {
            "id": "tiktok",
            "nombre": "TikTok",
            "usuario": "@sienteyaprende",
            "url": "tiktok.com/@sienteyaprende",
            "color": "hover:border-black hover:bg-gray-100 group-hover:text-black"
        },
        {
            "id": "eduki",
            "nombre": "Eduki",
            "usuario": "Siente y Aprende",
            "url": "https://eduki.com/es/autor/3771705/siente-y-aprende",
            "color": "hover:border-teal-500 hover:bg-teal-50 group-hover:text-teal-600"
        },
        {
            "id": "paypal",
            "nombre": "Apoya el Proyecto (PayPal)",
            "usuario": "@Padrestea",
            "url": "https://www.paypal.com/paypalme/padrestea",
            "color": "hover:border-sky-500 hover:bg-sky-50 group-hover:text-sky-600"
        }
    ]
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        materiales=MATERIALES
    )


@app.route("/perfil")
def perfil():
    return render_template(
        "perfil.html",
        perfil=PERFIL_DATOS
    )


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
