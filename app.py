from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "clave_secreta_siente_y_aprende"

# Catálogo con descripciones pedagógicas detalladas
MATERIALES = [
    {
        "id": 1,
        "titulo": "Las Vocales: Fichas Didácticas e Ilustradas (PDF)",
        "descripcion": "Recurso pedagógico completo diseñado para niños de 3 a 5 años. Incluye actividades de discriminación auditiva y visual de las vocales A, E, I, O, U, trazos guiados para fortalecer la psicomotricidad fina y láminas de asociación de sonido inicial con ilustraciones coloridas. Ideal para iniciar la lectoescritura en el aula o en el hogar.",
        "url_descarga": "https://drive.google.com/file/d/1ZmbVq4PViwcZKEA4zzjRHceQhOc1SMo0/view?usp=drive_link"
    },
    {
        "id": 2,
        "titulo": "Repaso Práctico de las Sílabas Simple y Compuestas",
        "descripcion": "Cuadernillo de reforzamiento estructurado para afianzar la combinación fonética de consonantes y vocales. Contiene ejercicios de segmentación silábica, sopa de letras infantiles y lecturas guiadas de oraciones cortas, favoreciendo la fluidez lectora y el reconocimiento ortográfico temprano.",
        "url_descarga": "https://drive.google.com/file/d/1A8Qa1PR5aiC1RW0lPUymJEt1Z2cvYeqa/view?usp=drive_link"
    },
    {
        "id": 3,
        "titulo": "Fichas Ilustradas del Abecedario Completo",
        "descripcion": "Colección interactiva que abarca desde la letra A hasta la Z. Cada ficha cuenta con letras en tamaño grande para colorear, palabras de referencia con imágenes representativas y renglones de caligrafía con líneas guía. Excelente material para la ambientación del rincón de lectura escolar.",
        "url_descarga": "https://drive.google.com/file/d/14Kog8-8olCtHalZN11IURkEtHXrCCUP0/view?usp=drive_link"
    },
    {
        "id": 4,
        "titulo": "Guía Didáctica: Aprendamos a Leer con Sílabas",
        "descripcion": "Guía pedagógica progresiva basada en el método silábico sintético. Permite a los estudiantes avanzar gradualmente desde sílabas directas hasta lecturas comprensivas cortas. Incluye actividades de autoevaluación y preguntas sencillas de comprensión de lectura.",
        "url_descarga": "https://drive.google.com/file/d/1h_brFpBAHEDTtaNITGmMDw5C2d9LG7Pa/view?usp=drive_link"
    },
    {
        "id": 5,
        "titulo": "Manual de Técnicas Grafoplásticas y Psicomotricidad Fina",
        "descripcion": "Compendio de actividades prácticas enfocado en el desarrollo muscular de las manos previo a la escritura. Incluye guías paso a paso para técnicas de rasgado, arrugado de papel, trozado, dactilopintura y entorchado, fundamentales para la pinza digital en educación inicial.",
        "url_descarga": "https://drive.google.com/file/d/1NOGgSLiYBOXTxOC5c-BryQKoCPVetp_B/view?usp=drive_link"
    },
    {
        "id": 6,
        "titulo": "Cuaderno de Análisis Silábico con Palabras Trisílabas",
        "descripcion": "Material de trabajo diseñado para fortalecer la conciencia fonológica en niños de nivel preescolar y primaria. Presenta dinámicas de conteo de sílabas, identificación de sílaba tónica y ordenamiento de palabras para construir oraciones simples.",
        "url_descarga": "https://drive.google.com/file/d/11TXViQI88CZqPv-z687hvpr9KA82bh8Q/view?usp=drive_link"
    },
    {
        "id": 7,
        "titulo": "Mural y Cartilla de Referencia del Abecedario",
        "descripcion": "Recurso gráfico en alta resolución para impresión en formato póster o cartilla individual. Presenta la tipografía adecuada para el aprendizaje infantil con distinción clara entre mayúsculas y minúsculas acompañadas de pictogramas de fácil asociación.",
        "url_descarga": "https://drive.google.com/file/d/1x31RWetfeVk1QeLPtCytengiQlrbXCkx/view?usp=drive_link"
    },
    {
        "id": 8,
        "titulo": "Abecedario Didáctico Creativo Para Colorear",
        "descripcion": "Cuaderno de expresión artística y aprendizaje alfabético. Combina el refuerzo de la memoria visual de las letras con dibujos detallados para colorear, favoreciendo la concentración, la relajación y el reconocimiento gráfico en los primeros años escolares.",
        "url_descarga": "https://drive.google.com/file/d/1tywEYzkOMXzh27PAE2DONkbdmU8bXK11/view?usp=drive_link"
    },
    {
        "id": 9,
        "titulo": "Cuadernillo de Grafomotricidad y Trazos Guiados",
        "descripcion": "Manual de ejercitación caligráfica que orienta la dirección correcta de cada trazo mediante flechas explicativas. Ayuda a prevenir problemas de inversión de letras y mejora el control visomotriz en el proceso de enseñanza de la escritura.",
        "url_descarga": "https://drive.google.com/file/d/1HNp17tHEDRjVyQ3uC5v5TbKRXA5LF-aQ/view?usp=drive_link"
    },
    {
        "id": 10,
        "titulo": "Compilación de Fábulas Infantiles con Preguntas de Comprensión",
        "descripcion": "Antología de relatos breves con enseñanzas morales y éticas adaptadas para niños. Cada lectura viene acompañada de ejercicios de comprensión lectora, preguntas de reflexión y actividades de dibujo para incentivar el hábito de la lectura analítica.",
        "url_descarga": "https://drive.google.com/file/d/1YEfd4ywdLL-8Qhh4D5rkeGr77zOXB8YB/view?usp=drive_link"
    }
]

# Artículos de alto valor pedagógico para cumplimiento estricto con AdSense
ARTICULOS = [
    {
        "id": 1,
        "slug": "importancia-grafomotricidad-educacion-inicial",
        "titulo": "La Importancia de la Grafomotricidad en la Educación Inicial",
        "resumen": "Descubre cómo las actividades de trazo y coordinación visomotriz preparan la mano del niño para la escritura y previenen dificultades futuras.",
        "contenido": """
        La grafomotricidad es el conjunto de habilidades motoras finas que permiten al niño controlar los movimientos de la mano y los dedos para realizar trazos, formas y, eventualmente, letras. En la etapa de educación inicial (de 3 a 6 años), el desarrollo grafomotor es un pilar fundamental para garantizar una transición fluida hacia el aprendizaje formal de la escritura.

        Antes de sostener un lápiz y escribir una palabra, el niño necesita ejercitar los músculos pequeños de la mano. Las técnicas grafoplásticas como el rasgado de papel, el moldeado de plastilina, el trozado y el uso de punzones no solo estimulan la fuerza muscular, sino también la coordinación ojo-mano (visomotriz) y la precisión en el agarre de la pinza digital.

        Implementar cuadernillos de trazos verticales, horizontales, curvos y en espiral permite que el niño adquiera control sobre la presión y dirección de sus movimientos. Al ofrecer un entorno lúdico con materiales interactivos, fortalecemos su confianza y prevenimos tensiones o fatiga muscular asociadas con una mala postura o un agarre deficiente.
        """
    },
    {
        "id": 2,
        "slug": "metodo-silabico-lectoescritura-guia",
        "titulo": "Estrategias Clave para Enseñar a Leer con el Método Silábico",
        "resumen": "Una guía completa sobre el método silábico, sus etapas y cómo combinarlo con recursos didácticos ilustrados para agilizar el aprendizaje.",
        "contenido": """
        El método silábico es una de las metodologías tradicionales más efectivas y estructuradas para el proceso de enseñanza de la lectoescritura en español. A diferencia de otros enfoques, parte de las unidades vocálicas simples para luego combinarlas con consonantes y formar sílabas, palabras y oraciones completas de manera progresiva.

        El proceso inicia con la enseñanza y memorización de las vocales (a, e, i, o, u) mediante canciones, pictogramas y ejercicios de asociación fonética. Una vez consolidadas las vocales, se introducen las consonantes más accesibles como la M, P, S y L, formando las primeras sílabas directas (ma, me, mi, mo, mu).

        El valor de este método radica en la construcción lógica de la lectura. Los niños aprenden a decodificar palabras combinando las sílabas aprendidas (por ejemplo, 'ma-má' o 'só-pa'), lo que les otorga una sensación inmediata de logro. Acompañar estas lecciones con fichas didácticas ilustradas asegura que el aprendizaje no sea memorístico, sino verdaderamente significativo.
        """
    }
]

# Perfil del Creador
PERFIL_DATOS = {
    "nombre": "Siente y Aprende",
    "subtitulo": "Creación de Material Didáctico y Recursos Educativos",
    "descripcion": "Bienvenido a Siente y Aprende. Diseñamos recursos didácticos, guías de lectoescritura, canciones educativas y artículos pedagógicos pensados para acompañar el desarrollo en la educación infantil.",
    "foto": "/static/img/logo.jpeg",
    "portada": "/static/img/portada.jpeg",
    "redes": [
        {"id": "youtube", "nombre": "YouTube", "usuario": "@SienteyAprende", "url": "https://www.youtube.com/@SienteyAprende", "color": "hover:border-red-500 hover:bg-red-50 group-hover:text-red-600"},
        {"id": "facebook", "nombre": "Facebook", "usuario": "Siente y Aprende", "url": "https://www.facebook.com/", "color": "hover:border-blue-500 hover:bg-blue-50 group-hover:text-blue-600"},
        {"id": "instagram", "nombre": "Instagram", "usuario": "@SienteyAprende", "url": "https://www.instagram.com/", "color": "hover:border-pink-500 hover:bg-pink-50 group-hover:text-pink-600"},
        {"id": "tiktok", "nombre": "TikTok", "usuario": "@SienteyAprende", "url": "https://www.tiktok.com/", "color": "hover:border-black hover:bg-gray-100 group-hover:text-black"},
        {"id": "eduki", "nombre": "Eduki", "usuario": "Siente y Aprende", "url": "https://eduki.com/", "color": "hover:border-teal-500 hover:bg-teal-50 group-hover:text-teal-600"},
        {"id": "paypal", "nombre": "Apoya el Proyecto (PayPal)", "usuario": "Donaciones y Aportes", "url": "https://paypal.me/", "color": "hover:border-sky-500 hover:bg-sky-50 group-hover:text-sky-600"}
    ]
}


@app.route("/")
def index():
    return render_template("index.html", materiales=MATERIALES, articulos=ARTICULOS)


@app.route("/articulo/<int:articulo_id>")
def ver_articulo(articulo_id):
    articulo = next((a for a in ARTICULOS if a["id"] == articulo_id), None)
    return render_template("articulo.html", articulo=articulo)


@app.route("/perfil")
def perfil():
    return render_template("perfil.html", perfil=PERFIL_DATOS)


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
