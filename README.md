import streamlit as st
import pandas as pd

# --- Configurazione ---
st.set_page_config(page_title="ABSA ⚽", page_icon="⚽", layout="centered")

st.title("⚽ ABSA – Pagina Ufficiale")
st.subheader("Benvenuto nella web app ufficiale della squadra ABSA!")

# --- Menu laterale ---
sezione = st.sidebar.radio("Naviga", ["Componenti Squadra", "Partite", "Info"])

# --- Componenti Squadra ---
if sezione == "Componenti Squadra":
    st.header("👥 Rosa Ufficiale ABSA")
    giocatori = pd.DataFrame({
        "Nome": [
            "Temu Jr.", "LeKebab", "Alibaba", "Swaagie", "Chorfene",
            "Lorusso", "Abdullah", "Zlatan Jr.", "Abullah", "Temu Jr.",
            "ፊክ ጄር", "Abdul", "Abdul II", "Neymar Nip.", "Abdullah Jr. Jr.",
