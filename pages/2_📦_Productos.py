import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Productos",
    page_icon="📦"
)

# Título principal
st.title("📦 Catálogo de Productos")

# Imagen relacionada con productos
st.image(
    "https://images.unsplash.com/photo-1563013544-824ae1b704d",
    caption="Catálogo de productos",
    use_container_width=True
)

# DataFrame de productos
df = pd.DataFrame({
    "Nombre": [
        "Laptop",
        "Mouse",
        "Teclado",
        "Monitor",
        "Auriculares"
    ],
    "Categoría": [
        "Electrónica",
        "Accesorios",
        "Accesorios",
        "Electrónica",
        "Audio"
    ],
    "Precio": [
        1200,
        25,
        45,
        300,
        80
    ],
    "Stock": [
        10,
        50,
        30,
        15,
        40
    ]
})

# Filtro por categoría
categorias = st.multiselect(
    "Selecciona categorías",
    options=df["Categoría"].unique(),
    default=df["Categoría"].unique()
)

df_filtrado = df[df["Categoría"].isin(categorias)]

# Métrica: total de productos
st.metric(
    label="Total de productos",
    value=len(df_filtrado)
)

# Mostrar tabla
st.subheader("Lista de Productos")
st.dataframe(df_filtrado)

# Gráfico de barras: precio por producto
st.subheader("Precio por Producto")

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df_filtrado["Nombre"], df_filtrado["Precio"])
ax.set_xlabel("Producto")
ax.set_ylabel("Precio")
ax.set_title("Precio por Producto")
plt.xticks(rotation=45)

st.pyplot(fig)