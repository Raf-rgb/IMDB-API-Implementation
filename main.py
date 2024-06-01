import streamlit as st
import utils.utils as utils
from streamlit_image_select import image_select

st.set_page_config(
    page_title="Movie Details",
    page_icon="🎥",
    layout="wide"
)

if "title" not in st.session_state:
    st.session_state["title"] = {}

if "movies" not in st.session_state:
    st.session_state["movies"] = []

if "id_movie" not in st.session_state:
    st.session_state["id_movie"] = ""

def main():
    title = st.text_input("Ingrese el titulo", key="id")
    
    if st.button("Buscar", type="primary", key="search_btn") and title != "":
        st.session_state.movies = utils.search_movie(title)

    if len(st.session_state.movies) > 0:
        img = image_select(
            "Selecciona una pelicula",
            images=[movie["titlePosterImageModel"]["url"] for movie in st.session_state.movies],
            captions=[movie["titleNameText"] + f"({movie["titleReleaseText"]})" for movie in st.session_state.movies],
            return_value="index"
        )

        if st.button("Ver detalles", key="details_btn"):
            st.session_state.id_movie = st.session_state.movies[img]["id"]
            st.switch_page("pages/0_Movie_Details.py")
    else:
        st.text("Sin resultados :c")
if __name__ == "__main__":
    main()