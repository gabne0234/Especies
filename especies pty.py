import pandas as pd
import plotly.graph_objects as go

# Datos
df = pd.DataFrame({
    'Grupo': ['Anfibios🐸', 'Reptiles🦎', 'Aves🦜', 'Mamíferos🦥', 'Peces de agua dulce🐟', 'Peces marinos🌊🐠', 'Plantas🌱'],
    'Endemicas': [49, 33, 8, 16, 64, 0, 1176],
    'Porcentaje_mundial': [3.4, 2.3, 9, 4.8, 1.47, 5.79, 3.3]
})

# Crear figura
fig = go.Figure()

# Barras: especies endémicas
fig.add_trace(go.Bar(
    x=df['Grupo'],
    y=df['Endemicas'],
    name='Especies endémicas',
    marker_color='darkgreen',
    text=df['Endemicas'],
    textposition='auto'
))

# Línea: porcentaje mundial en eje secundario
fig.add_trace(go.Scatter(
    x=df['Grupo'],
    y=df['Porcentaje_mundial'],
    name='% de especies a nivel mundial en Panamá',
    mode='lines+markers+text',
    text=df['Porcentaje_mundial'].apply(lambda x: f"{x}%\n"),
    textposition='top center',
    marker=dict(color='orange', size=14),
    line=dict(dash='dot', width=2),
    yaxis='y2'
))

# Layout con eje secundario y grilla
fig.update_layout(
    title='<u>Biodiversidad en Panamá: Especies endémicas y % de especies a nivel mundial en Panamá<u>',
    title_x=0.5,
    xaxis_title='Grupo de especies',
    yaxis=dict(title='Número de especies endémicas', showgrid=True, gridcolor='lightgray'),
    yaxis2=dict(title='% de especies a nivel mundial en Panamá', overlaying='y', side='right', showgrid=False),
    legend=dict(x=0.5, y=0.95),
    paper_bgcolor='lightyellow',   # Fondo completo
    plot_bgcolor='lightyellow'           # Fondo del área del gráfico
)

# Mostrar en navegador
fig.show(renderer="browser")