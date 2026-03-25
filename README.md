# El mundo del revés

Aventura de texto interactiva con estética de Stranger Things, construida con Python y Streamlit.
Desarrollada como demostración para alumnos de secundaria de cómo los conceptos de
Programación Orientada a Objetos (POO) y herencia pueden materializarse en una
interfaz web real.

---

## Qué contiene el proyecto

```
stranger_things_app/
├── app.py              # Aplicación principal (lógica + interfaz)
├── requirements.txt    # Librerías necesarias
└── README.md           # Este archivo
```

---

## Conceptos de programación que implementa

- **Clase padre** `Personaje` con atributos `nombre` y `vida`
- **Clases hijas** `Heroe` y `Monstruo` que heredan de `Personaje` usando `super()`
- **Polimorfismo** a través del método `hablar()`, sobrescrito en cada clase hija
- **Estado de sesión** con `st.session_state` para mantener el progreso entre pantallas
- **Enrutador de pantallas** que dirige al jugador según sus decisiones

---

## Ejecutar en local

### Requisitos previos

- Python 3.9 o superior
- pip

### Pasos

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/stranger-things-app.git
cd stranger-things-app
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Lanza la aplicación:

```bash
streamlit run app.py
```

4. Abre el navegador en `http://localhost:8501`

---

## Desplegar en Streamlit Community Cloud

1. Sube el repositorio a GitHub (debe ser público).
2. Entra en [share.streamlit.io](https://share.streamlit.io) con tu cuenta de GitHub.
3. Haz clic en **New app**.
4. Selecciona el repositorio, la rama (`main`) y el archivo principal (`app.py`).
5. Haz clic en **Deploy**.

Streamlit Cloud detecta automáticamente el archivo `requirements.txt` e instala
las dependencias. En menos de dos minutos la app estará disponible en una URL pública.

---

## Personalización sugerida para el aula

Estos son los puntos del código más sencillos de modificar para mostrar a los alumnos
cómo pequeños cambios tienen efecto inmediato en la interfaz:

- **Cambiar los personajes disponibles**: busca el diccionario `personajes` dentro
  de `pantalla_inicio()` y añade o modifica entradas.
- **Cambiar el daño del Demogorgon**: modifica `nivel_demogorgon` al crear el objeto
  `Monstruo` en `init_state()`.
- **Añadir un tercer personaje con su propia clase**: crea una clase `Aliado` que
  herede de `Personaje` y sobrescriba `hablar()`.
- **Añadir una tercera decisión**: crea una función `pantalla_decision_3()` siguiendo
  el mismo patrón que las existentes y añádela al diccionario `pantallas`.

---

## Tecnologías utilizadas

| Tecnología | Versión mínima | Uso |
|---|---|---|
| Python | 3.9 | Lenguaje base |
| Streamlit | 1.35.0 | Interfaz web |

---

## Licencia

MIT — libre para uso educativo y modificación.
