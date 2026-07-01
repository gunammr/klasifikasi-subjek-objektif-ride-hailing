import streamlit as st

st.set_page_config(
    page_title="Klasifikasi Subjek-Objektif Ride-Hailing",
    page_icon="🚕",
    layout="wide"
)

st.title("🚕 Klasifikasi Ulasan Ride-Hailing")

st.markdown("""
Selamat datang pada sistem klasifikasi ulasan ride-hailing menggunakan
algoritma **Support Vector Machine (SVM)** dan ekstraksi fitur **TF-IDF**.

### Menu Sistem

📊 Dashboard  
Menampilkan statistik hasil klasifikasi.

✍️ Input Ulasan  
Melakukan prediksi terhadap ulasan baru.

📄 Hasil Analisis  
Menampilkan riwayat hasil prediksi yang telah dilakukan.

---

Silakan pilih menu pada sidebar sebelah kiri.
""")