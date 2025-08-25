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
            "Kebab", "AbulleKebab", "Lorusso Jr.", "Bernardeschi", "엉덩이에 섹스"
        ],
        "Numero": [
            1, 12, 3, 14, 6,
            4, 19, 10, 22, 95,
            78, 11, 18, 17, 7,
            11, 29, 49, 49, 69
        ]
    })
    st.dataframe(giocatori, use_container_width=True)

# --- Partite ---
elif sezione == "Partite":
    st.header("📅 Partite della Stagione")
    st.info("Le partite devono ancora essere decise... ⏳")

# --- Info ---
elif sezione == "Info":
    st.header("ℹ️ Info sulla Squadra")
    st.write("""
    La **ABSA** è una squadra di calcio creata per divertimento e passione.  
    Questa web app mostra la rosa, le partite e tutte le novità della squadra.
    """)
    st.success("💡 Segui questa pagina per restare aggiornato!")
