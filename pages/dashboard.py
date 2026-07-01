import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / 'dataset' / 'hasil_prediksi.csv'
)

total_ulasan = len(df)

jumlah_subjektif = len(
    df[df['label'] == 'Subjektif']
)

jumlah_objektif = len(
    df[df['label'] == 'Objektif']
)

if total_ulasan > 0:
    avg_confidence = (
        df['confidence'].mean() * 100
    )
else:
    avg_confidence = 0

st.title(
    "Dashboard Sistem Analisis Ulasan"
)

st.caption(
    "Overview analisis dan statistik ulasan"
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Ulasan",
    total_ulasan
)

col2.metric(
    "Subjektif",
    jumlah_subjektif
)

col3.metric(
    "Objektif",
    jumlah_objektif
)

col4.metric(
    "Confidence",
    f"{avg_confidence:.2f}%"
)

chart_data = pd.DataFrame({
    'Label': [
        'Subjektif',
        'Objektif'
    ],
    'Jumlah': [
        jumlah_subjektif,
        jumlah_objektif
    ]
})

fig = px.pie(
    chart_data,
    names='Label',
    values='Jumlah',
    hole=0.6
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader(
    "Ulasan Terbaru"
)
if df.empty:
    st.info(
        "Belum ada hasil prediksi."
    )
else:

    data_terbaru = df.tail(5)

    st.dataframe(
        data_terbaru[
            [
                'review',
                'label',
                'confidence',
                'tanggal'
            ]
        ],
        use_container_width=True
    )