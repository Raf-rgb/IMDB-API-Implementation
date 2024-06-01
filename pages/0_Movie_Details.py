import streamlit as st
import utils.utils as utils
from streamlit_image_select import image_select

st.set_page_config(
    page_title="Movie Details",
    page_icon="🎥",
    layout="wide"
)

if "details" not in st.session_state:
    st.session_state["details"] = utils.get_details(st.session_state.id_movie)

if "show_details" not in st.session_state:
    st.session_state["show_details"] = False

st.title(f"{st.session_state.details["title"]} ({st.session_state.details["year"]})")

if st.button("Regresar",type="primary", key="back_btn"):
    del st.session_state["details"]
    del st.session_state["show_details"]

    st.switch_page("main.py")

if st.session_state.details:
    data = st.session_state.details

    st.divider()

    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.header("Portada")
        st.image(data["poster"], width=300)
        st.code(data["poster"])
    
    with col2:
        st.header("Detalles")

        st.text("Título:")
        st.code(data["title"], language="text")

        st.text("Director(es):")
        st.code(data["directors"], language="text")

        st.text("Año:")
        st.code(data["year"], language="text")

        st.text("Género(s):")
        st.code(data["genres"], language="text")

    st.header("Imagenes de fondo")

    img_index = image_select(
        label="Selecciona una imagen de fondo",
        images=data["background"],
        return_value="index"
    )

    st.text("Imagen seleccionada:")
    st.code(data["background"][img_index])