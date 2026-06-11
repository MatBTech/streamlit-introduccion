import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# Configuración de la página
st.set_page_config(
    page_title="Reportes",
    page_icon="📊"
)

# Título principal
st.title("📊 Dashboards y Reportes")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Ventas Totales",
        value="$125,000",
        delta="+12%"
    )

with col2:
    st.metric(
        label="Clientes Activos",
        value="850",
        delta="+45"
    )

with col3:
    st.metric(
        label="Productos Vendidos",
        value="3,250",
        delta="+8%"
    )

st.divider()

# Selector de rango de fechas
st.subheader("📅 Seleccionar rango de fechas")

rango_fechas = st.date_input(
    "Rango de fechas",
    value=(date(2025, 1, 1), date(2025, 12, 31))
)

st.write("Fechas seleccionadas:", rango_fechas)

st.divider()

# Datos de ejemplo para ventas por mes
ventas = pd.DataFrame({
    "Mes": [
        "Ene", "Feb", "Mar", "Abr",
        "May", "Jun", "Jul", "Ago",
        "Sep", "Oct", "Nov", "Dic"
    ],
    "Ventas": [
        12000, 15000, 18000, 17000,
        22000, 25000, 24000, 26000,
        28000, 30000, 32000, 35000
    ]
})

# Gráfico de líneas
st.subheader("📈 Ventas por Mes")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(
    ventas["Mes"],
    ventas["Ventas"],
    marker="o",
    linewidth=2
)
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas ($)")
ax.set_title("Evolución de Ventas")
ax.grid(True)

st.pyplot(fig)

st.divider()

# Descarga de reporte
st.subheader("📥 Descargar Reporte")

csv = ventas.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Descargar reporte CSV",
    data=csv,
    file_name="reporte_ventas.csv",
    mime="text/csv"
)