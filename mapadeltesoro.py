import streamlit as st
import pandas as pd

st.title("🗺️ Tesoro Mundial")

# Pistas + tesoro
data = pd.DataFrame({
    "lat": [-3.5, 27.9, 29.9, 64.9, -19.5],
    "lon": [-60.5, 86.9, 31.1, -19.0, -57.5],
})

# Mapa
st.map(data)

# Info
st.markdown("🟠 pistas → 🏆 tesoro final")
st.success("Sigue la ruta hasta encontrar el tesoro")