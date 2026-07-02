import streamlit as st
from streamlit_option_menu import option_menu

from pages.dashboard import show_dashboard
from pages.hasil_analisis import show_hasil_analisis
from pages.input_ulasan import show_input_ulasan

st.set_page_config(
    page_title="Klasifikasi Subjek-Objektif Ride-Hailing",
    page_icon="car",
    layout="wide"
)

st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu Sistem", 
        options=["Home", "Dashboard", "Hasil Analisis", "Input Ulasan"], 
        icons=["house", "bar-chart", "clipboard-data", "pencil-square"],
        menu_icon="cast", 
        default_index=0,

        styles={
            "container": {"padding": 0, "vertical-align": "top", "background-color": "transparent"},
        } 
    )


if selected == "Home":
    st.title(":material/local_taxi: Klasifikasi Ulasan Ride-Hailing")

    st.markdown("""
    Selamat datang pada sistem klasifikasi ulasan ride-hailing menggunakan
    algoritma **Support Vector Machine (SVM)** dan ekstraksi fitur **TF-IDF**.

    ### Menu Sistem

    :material/bar_chart: **Dashboard**  
    Menampilkan statistik hasil klasifikasi.

    :material/edit: **Input Ulasan**  
    Melakukan prediksi terhadap ulasan baru.

    :material/assignment: **Hasil Analisis**  
    Menampilkan riwayat hasil prediksi yang telah dilakukan.

    ---

    Silakan pilih menu pada sidebar sebelah kiri.
    """)

elif selected == "Dashboard":
    show_dashboard()

elif selected == "Hasil Analisis":
    show_hasil_analisis()

elif selected == "Input Ulasan":
    show_input_ulasan()