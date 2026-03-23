import streamlit as st

# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Stranger Things — El mundo del revés",
    page_icon="🔦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# ESTILOS CSS PERSONALIZADOS — Estética Stranger Things
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Benguiat:wght@400;700&family=Share+Tech+Mono&family=Cinzel:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

/* Reset y fondo principal */
.stApp {
    background-color: #0a0a0f;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(180, 0, 0, 0.07) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 100, 180, 0.05) 0%, transparent 50%),
        url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    color: #e8e0d0;
    font-family: 'Crimson Text', serif;
}

/* Ocultar elementos por defecto de Streamlit */
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 2rem; max-width: 780px;}

/* Título principal */
.titulo-principal {
    font-family: 'Share Tech Mono', monospace;
    font-size: 2.6rem;
    font-weight: 700;
    color: #cc1a1a;
    text-align: center;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-shadow:
        0 0 20px rgba(200, 20, 20, 0.8),
        0 0 40px rgba(200, 20, 20, 0.4),
        0 0 80px rgba(200, 20, 20, 0.2);
    margin-bottom: 0.2rem;
    animation: flicker 4s infinite;
}

.subtitulo {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.95rem;
    color: #888;
    text-align: center;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
}

@keyframes flicker {
    0%, 95%, 100% { opacity: 1; }
    96% { opacity: 0.7; }
    97% { opacity: 1; }
    98% { opacity: 0.5; }
    99% { opacity: 1; }
}

/* Separador decorativo */
.separador {
    border: none;
    border-top: 1px solid rgba(200, 20, 20, 0.3);
    margin: 1.5rem 0;
}

/* Caja de narración */
.caja-narracion {
    background: linear-gradient(135deg, rgba(20,10,10,0.95), rgba(10,10,20,0.95));
    border: 1px solid rgba(180, 20, 20, 0.25);
    border-left: 3px solid #cc1a1a;
    border-radius: 4px;
    padding: 1.4rem 1.6rem;
    margin: 1rem 0;
    font-family: 'Crimson Text', serif;
    font-size: 1.15rem;
    line-height: 1.75;
    color: #d4cfc5;
    box-shadow: 0 4px 24px rgba(0,0,0,0.5), inset 0 0 40px rgba(180,20,20,0.03);
}

/* Caja de diálogo del personaje */
.caja-dialogo {
    background: rgba(15, 8, 8, 0.9);
    border: 1px solid rgba(200, 160, 60, 0.2);
    border-radius: 4px;
    padding: 1rem 1.4rem;
    margin: 0.6rem 0;
    font-family: 'Crimson Text', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #c8b870;
}

.nombre-personaje {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    font-style: normal;
    color: #888;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    display: block;
    margin-bottom: 0.3rem;
}

/* Caja de stats del personaje */
.caja-stats {
    background: rgba(10, 10, 20, 0.8);
    border: 1px solid rgba(60, 100, 200, 0.2);
    border-radius: 4px;
    padding: 0.9rem 1.2rem;
    margin: 0.5rem 0;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.82rem;
    color: #7090cc;
}

.stat-label {
    color: #506090;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 0.7rem;
}

/* Caja de resultado / evento */
.caja-evento {
    background: rgba(180, 20, 20, 0.08);
    border: 1px solid rgba(180, 20, 20, 0.3);
    border-radius: 4px;
    padding: 1.1rem 1.4rem;
    margin: 1rem 0;
    font-family: 'Crimson Text', serif;
    font-size: 1.1rem;
    color: #e8d8c8;
    line-height: 1.7;
}

/* Final victorioso */
.caja-victoria {
    background: rgba(20, 80, 20, 0.12);
    border: 1px solid rgba(40, 160, 40, 0.3);
    border-radius: 4px;
    padding: 1.4rem 1.8rem;
    margin: 1rem 0;
    text-align: center;
}

.texto-victoria {
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.3rem;
    color: #40c040;
    text-shadow: 0 0 15px rgba(40,180,40,0.5);
    letter-spacing: 0.08em;
}

/* Final alternativo */
.caja-derrota {
    background: rgba(80, 10, 10, 0.15);
    border: 1px solid rgba(180, 20, 20, 0.4);
    border-radius: 4px;
    padding: 1.4rem 1.8rem;
    margin: 1rem 0;
    text-align: center;
}

.texto-derrota {
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.2rem;
    color: #cc3030;
    text-shadow: 0 0 15px rgba(180,20,20,0.5);
    letter-spacing: 0.08em;
}

/* Título de sección */
.titulo-seccion {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    margin: 1.8rem 0 0.6rem 0;
}

/* Barra de vida */
.barra-vida-container {
    background: rgba(255,255,255,0.05);
    border-radius: 2px;
    height: 6px;
    margin-top: 6px;
    overflow: hidden;
}

/* Botones Streamlit — override */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(180, 20, 20, 0.5) !important;
    color: #cc4040 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    border-radius: 2px !important;
    padding: 0.5rem 1.2rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}

.stButton > button:hover {
    background: rgba(180, 20, 20, 0.15) !important;
    border-color: rgba(200, 40, 40, 0.9) !important;
    color: #ff6060 !important;
    box-shadow: 0 0 12px rgba(180,20,20,0.3) !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: rgba(15, 8, 8, 0.9) !important;
    border: 1px solid rgba(180, 20, 20, 0.3) !important;
    color: #d4cfc5 !important;
    font-family: 'Crimson Text', serif !important;
    border-radius: 2px !important;
}

/* Radio buttons */
.stRadio > div {
    gap: 0.5rem !important;
}

.stRadio > div > label {
    background: rgba(15, 8, 8, 0.8) !important;
    border: 1px solid rgba(100, 100, 100, 0.2) !important;
    border-radius: 3px !important;
    padding: 0.6rem 1rem !important;
    font-family: 'Crimson Text', serif !important;
    font-size: 1.05rem !important;
    color: #b0a898 !important;
    transition: all 0.15s ease !important;
    cursor: pointer !important;
}

.stRadio > div > label:hover {
    border-color: rgba(180, 20, 20, 0.5) !important;
    color: #e8d8c8 !important;
}

/* Progress bar de vida */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #cc1a1a, #ff4040) !important;
}

/* Línea decorativa luces */
.luces-hawkins {
    text-align: center;
    font-size: 1.4rem;
    letter-spacing: 0.5rem;
    margin: 0.5rem 0;
    opacity: 0.6;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# CLASES POO — Misma lógica que el ejercicio de secundaria
# ============================================================

class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida

    def hablar(self):
        return f"{self.nombre} no dice nada..."

    def porcentaje_vida(self):
        return max(0, self.vida / self.vida_max)


class Heroe(Personaje):
    def __init__(self, nombre, vida, poder_psiquico, inventario):
        super().__init__(nombre, vida)
        self.poder_psiquico = poder_psiquico
        self.inventario = inventario

    def hablar(self):
        frases = {
            "Eleven":  "— No me rindo. Voy a cerrar la puerta del Mundo del Revés.",
            "Mike":    "— ¡Juntos podemos con esto! Somos el Partido Dungeon.",
            "Hopper":  "— Llevo años protegiéndoos. No voy a parar ahora.",
        }
        return frases.get(self.nombre, "— ¡No me rindo, protegeré Hawkins!")


class Monstruo(Personaje):
    def __init__(self, nombre, vida, nivel_demogorgon):
        super().__init__(nombre, vida)
        self.nivel_demogorgon = nivel_demogorgon

    def hablar(self):
        return f"*GRRRRAAAAWWWL* — Nivel de amenaza: {self.nivel_demogorgon}/5"

    def dano(self):
        return self.nivel_demogorgon * 10


# ============================================================
# INICIALIZACIÓN DEL ESTADO DE SESIÓN
# Streamlit rerenderiza en cada interacción, necesitamos
# guardar el estado entre pantallas con st.session_state
# ============================================================

def init_state():
    defaults = {
        "pantalla": "inicio",
        "heroe": None,
        "monstruo": None,
        "resultado_d1": None,
        "vida_tras_d1": 100,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ============================================================
# COMPONENTES DE UI REUTILIZABLES
# ============================================================

def mostrar_cabecera():
    st.markdown('<div class="titulo-principal">Stranger Things</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo">El mundo del revés</div>', unsafe_allow_html=True)
    st.markdown('<div class="luces-hawkins">💡 💡 💡 💡 💡 💡 💡</div>', unsafe_allow_html=True)
    st.markdown('<hr class="separador">', unsafe_allow_html=True)


def mostrar_stats(heroe):
    vida_pct = heroe.porcentaje_vida()
    color_vida = "#40c040" if vida_pct > 0.6 else "#e0a020" if vida_pct > 0.3 else "#cc2020"
    inventario_str = " · ".join(heroe.inventario)
    poder_str = "Sí" if heroe.poder_psiquico else "No"

    st.markdown(f"""
    <div class="caja-stats">
        <span class="stat-label">Personaje</span> &nbsp; {heroe.nombre}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <span class="stat-label">Vida</span> &nbsp; {heroe.vida} / {heroe.vida_max}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <span class="stat-label">Poderes</span> &nbsp; {poder_str}
        <br><br>
        <span class="stat-label">Inventario</span> &nbsp; {inventario_str}
    </div>
    """, unsafe_allow_html=True)
    st.progress(vida_pct)


def mostrar_dialogo(personaje, texto=None):
    frase = texto if texto else personaje.hablar()
    st.markdown(f"""
    <div class="caja-dialogo">
        <span class="nombre-personaje">{personaje.nombre}</span>
        {frase}
    </div>
    """, unsafe_allow_html=True)


def narracion(texto):
    st.markdown(f'<div class="caja-narracion">{texto}</div>', unsafe_allow_html=True)


def evento(texto):
    st.markdown(f'<div class="caja-evento">{texto}</div>', unsafe_allow_html=True)


# ============================================================
# PANTALLAS DEL JUEGO
# ============================================================

def pantalla_inicio():
    mostrar_cabecera()

    narracion(
        "Es 1985. Hawkins, Indiana. Las luces del laboratorio parpadean sin control. "
        "Algo ha cruzado de nuevo desde el Mundo del Revés, y solo tú puedes detenerlo. "
        "<br><br>"
        "Elige a tu personaje y prepárate. No hay tiempo que perder."
    )

    st.markdown('<p class="titulo-seccion">Selecciona tu personaje</p>', unsafe_allow_html=True)

    personajes = {
        "Eleven — Poderes psíquicos. Inventario: gofre":
            ("Eleven", 100, True,  ["gofre"]),
        "Mike Wheeler — Sin poderes. Inventario: walkie-talkie, mapa":
            ("Mike",   100, False, ["walkie-talkie", "mapa"]),
        "Hopper — Sin poderes. Inventario: pistola, linterna":
            ("Hopper", 120, False, ["pistola", "linterna"]),
    }

    eleccion = st.radio("", list(personajes.keys()), label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Comenzar la aventura"):
        datos = personajes[eleccion]
        st.session_state.heroe = Heroe(*datos)
        st.session_state.monstruo = Monstruo("Demogorgon", 80, 3)
        st.session_state.pantalla = "presentacion"
        st.rerun()


def pantalla_presentacion():
    mostrar_cabecera()
    heroe = st.session_state.heroe
    monstruo = st.session_state.monstruo

    mostrar_stats(heroe)

    narracion(
        f"Las puertas del laboratorio se cierran de golpe. {heroe.nombre} está atrapado/a dentro. "
        f"Al fondo del pasillo, una figura enorme avanza lentamente entre las sombras. "
        f"El <strong>Demogorgon</strong> ha encontrado su presa."
    )

    st.markdown('<p class="titulo-seccion">Los personajes hablan</p>', unsafe_allow_html=True)
    mostrar_dialogo(heroe)
    mostrar_dialogo(monstruo)

    st.markdown("""
    <div class="caja-stats" style="margin-top:1rem; border-color: rgba(80,80,200,0.2); color: #6080aa; font-size: 0.78rem;">
        <span class="stat-label">Nota POO</span> &nbsp;
        Ambos personajes usan el método <code>hablar()</code>, pero cada clase lo tiene definido
        de forma diferente. Esto es <strong>polimorfismo</strong>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Continuar →"):
        st.session_state.pantalla = "decision_1"
        st.rerun()


def pantalla_decision_1():
    mostrar_cabecera()
    heroe = st.session_state.heroe
    monstruo = st.session_state.monstruo

    mostrar_stats(heroe)

    narracion(
        f"El Demogorgon bloquea completamente la única puerta de salida. "
        f"Su nivel de amenaza es <strong>{monstruo.nivel_demogorgon}/5</strong>. "
        f"Atacar de frente sería suicida. {heroe.nombre} mira a su alrededor buscando opciones."
    )

    st.markdown('<p class="titulo-seccion">Primera decisión</p>', unsafe_allow_html=True)

    opciones = {
        "A — Usar tus habilidades para apartarlo":  "A",
        "B — Escapar corriendo hacia los conductos de ventilación": "B",
    }
    eleccion = st.radio("¿Qué hace tu personaje?", list(opciones.keys()), label_visibility="visible")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Confirmar decisión"):
        letra = opciones[eleccion]
        if letra == "A":
            if heroe.poder_psiquico:
                st.session_state.resultado_d1 = "poder_exito"
            else:
                dano = monstruo.dano()
                heroe.vida -= dano
                st.session_state.resultado_d1 = "poder_fallo"
        else:
            heroe.vida -= 20
            st.session_state.resultado_d1 = "huida"

        st.session_state.vida_tras_d1 = heroe.vida
        st.session_state.pantalla = "resultado_1"
        st.rerun()


def pantalla_resultado_1():
    mostrar_cabecera()
    heroe = st.session_state.heroe
    resultado = st.session_state.resultado_d1

    mostrar_stats(heroe)

    if resultado == "poder_exito":
        evento(
            f"<strong>Eleven</strong> cierra los ojos. Las luces del pasillo estallan una a una. "
            f"El Demogorgon sale despedido contra la pared con un impacto brutal. "
            f"La puerta queda libre. Ha funcionado."
        )
        mostrar_dialogo(heroe, "— Lo sabía. Siempre lo supe.")

    elif resultado == "poder_fallo":
        monstruo = st.session_state.monstruo
        evento(
            f"<strong>{heroe.nombre}</strong> intenta resistir, pero sin poderes psíquicos "
            f"no puede detener al Demogorgon. La criatura golpea y "
            f"<strong>{heroe.nombre} pierde {monstruo.dano()} puntos de vida</strong>. "
            f"Hay que encontrar otra salida."
        )
    else:
        evento(
            f"<strong>{heroe.nombre}</strong> corre hacia los conductos de ventilación. "
            f"El Demogorgon ruge y golpea la rejilla, arrancándole "
            f"<strong>20 puntos de vida</strong> antes de que logre entrar. "
            f"Dentro de los conductos, el silencio. Por ahora, está a salvo."
        )

    if heroe.vida <= 0:
        st.session_state.pantalla = "fin_derrota"
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Continuar →"):
            st.session_state.pantalla = "decision_2"
            st.rerun()


def pantalla_decision_2():
    mostrar_cabecera()
    heroe = st.session_state.heroe

    mostrar_stats(heroe)

    narracion(
        f"{heroe.nombre} llega jadeando a la sala de control del laboratorio. "
        f"Frente a él/ella hay dos puertas. Una conduce al exterior y a la seguridad. "
        f"La otra... emana un frío extraño y las luces a su alrededor parpadean con violencia. "
        f"Es la puerta al <strong>Mundo del Revés</strong>."
    )

    st.markdown('<p class="titulo-seccion">Segunda decisión</p>', unsafe_allow_html=True)

    opciones = {
        "1 — Abrir la puerta de salida al exterior": "1",
        "2 — Abrir la puerta al Mundo del Revés":   "2",
    }
    eleccion = st.radio("¿Qué puerta abre tu personaje?", list(opciones.keys()), label_visibility="visible")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Abrir la puerta"):
        letra = opciones[eleccion]
        if letra == "1":
            st.session_state.pantalla = "fin_victoria"
        else:
            st.session_state.pantalla = "fin_alternativo"
        st.rerun()


def pantalla_fin_victoria():
    mostrar_cabecera()
    heroe = st.session_state.heroe

    mostrar_stats(heroe)

    st.markdown(f"""
    <div class="caja-victoria">
        <div class="texto-victoria">— Hawkins está a salvo —</div>
        <br>
        <div style="font-family: 'Crimson Text', serif; font-size: 1.1rem; color: #a0d0a0; line-height: 1.8;">
            {heroe.nombre} cruza la puerta y sale al exterior. El aire frío de la noche de Indiana
            nunca había sabido tan bien. A lo lejos, las luces del laboratorio se apagan para siempre.
            <br><br>
            El Mundo del Revés puede esperar.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="caja-stats" style="margin-top:1.5rem; font-size: 0.82rem;">
        <span class="stat-label">Resumen de partida</span><br><br>
        Personaje &nbsp;·&nbsp; {heroe.nombre}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        Vida final &nbsp;·&nbsp; {heroe.vida} / {heroe.vida_max}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        Inventario &nbsp;·&nbsp; {" · ".join(heroe.inventario)}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Volver a empezar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


def pantalla_fin_alternativo():
    mostrar_cabecera()
    heroe = st.session_state.heroe

    mostrar_stats(heroe)

    st.markdown(f"""
    <div class="caja-derrota">
        <div class="texto-derrota">— El Mundo del Revés te ha reclamado —</div>
        <br>
        <div style="font-family: 'Crimson Text', serif; font-size: 1.1rem; color: #c08080; line-height: 1.8;">
            {heroe.nombre} abre la puerta equivocada. La oscuridad del Mundo del Revés
            se expande a su alrededor. Las esporas llenan el aire. La puerta se cierra sola.
            <br><br>
            Hawkins tendrá que esperar a otro héroe.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Intentarlo de nuevo"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


def pantalla_fin_derrota():
    mostrar_cabecera()
    heroe = st.session_state.heroe

    st.markdown(f"""
    <div class="caja-derrota">
        <div class="texto-derrota">— {heroe.nombre} ha caído —</div>
        <br>
        <div style="font-family: 'Crimson Text', serif; font-size: 1.1rem; color: #c08080; line-height: 1.8;">
            Los puntos de vida llegaron a cero. El Demogorgon ha ganado esta vez.
            Hawkins necesita un héroe más fuerte, o decisiones más inteligentes.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Intentarlo de nuevo"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


# ============================================================
# ENRUTADOR PRINCIPAL
# Muestra la pantalla correcta según st.session_state.pantalla
# ============================================================

pantallas = {
    "inicio":       pantalla_inicio,
    "presentacion": pantalla_presentacion,
    "decision_1":   pantalla_decision_1,
    "resultado_1":  pantalla_resultado_1,
    "decision_2":   pantalla_decision_2,
    "fin_victoria":    pantalla_fin_victoria,
    "fin_alternativo": pantalla_fin_alternativo,
    "fin_derrota":     pantalla_fin_derrota,
}

pantallas[st.session_state.pantalla]()
