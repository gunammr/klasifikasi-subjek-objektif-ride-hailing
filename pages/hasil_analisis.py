import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Hasil Analisis",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "dataset" / "hasil_prediksi.csv"

# ==========================
# LOAD DATA
# ==========================

if CSV_PATH.exists():

    df = pd.read_csv(CSV_PATH)

else:

    df = pd.DataFrame(
        columns=[
            "review",
            "label",
            "confidence",
            "tanggal"
        ]
    )

# ==========================
# HEADER
# ==========================

st.title("Hasil Analisis")

st.caption(
    "Tabel lengkap hasil prediksi dan klasifikasi ulasan"
)

# ==========================
# EXPORT
# ==========================

if not df.empty:

    st.download_button(
        label="📥 Export Data",
        data=df.to_csv(index=False),
        file_name="hasil_analisis.csv",
        mime="text/csv"
    )

# ==========================
# STATISTIK
# ==========================

total_ulasan = len(df)

jumlah_subjektif = len(
    df[
        df["label"] == "Subjektif"
    ]
)

jumlah_objektif = len(
    df[
        df["label"] == "Objektif"
    ]
)

if total_ulasan > 0:

    avg_confidence = (
        df["confidence"].mean()
        * 100
    )

else:

    avg_confidence = 0

# ==========================
# INFO BOX
# ==========================

st.info(
    f"Menampilkan {total_ulasan} dari {total_ulasan} ulasan"
)

# ==========================
# CARD STATISTIK
# ==========================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Ulasan Subjektif",
        jumlah_subjektif
    )

with col2:

    st.metric(
        "Ulasan Objektif",
        jumlah_objektif
    )

with col3:

    st.metric(
        "Avg. Confidence",
        f"{avg_confidence:.2f}%"
    )

# ==========================
# FILTER
# ==========================

filter_label = st.selectbox(
    "Filter Label",
    [
        "Semua",
        "Subjektif",
        "Objektif"
    ]
)

df_tampil = df.copy()

if filter_label != "Semua":

    df_tampil = df_tampil[
        df_tampil["label"]
        == filter_label
    ]

# ==========================
# FORMAT DATA
# ==========================

df_tampil = df_tampil.reset_index(
    drop=True
)

if not df_tampil.empty:

    df_tampil.insert(
        0,
        "ID",
        [
            f"#{i+1}"
            for i in range(
                len(df_tampil)
            )
        ]
    )

    df_tampil["confidence"] = (
        df_tampil["confidence"]
        * 100
    ).round(2)

    df_tampil["confidence"] = (
        df_tampil["confidence"]
        .astype(str)
        + "%"
    )

# ==========================
# TABEL HASIL
# ==========================

st.subheader(
    "Hasil Analisis Ulasan"
)

if df_tampil.empty:

    st.warning(
        "Belum ada data hasil prediksi."
    )

else:

    st.dataframe(
        df_tampil[
            [
                "ID",
                "review",
                "label",
                "confidence",
                "tanggal"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

# ==========================
# FOOTER
# ==========================

st.caption(
    f"Total: {len(df_tampil)} ulasan ditampilkan"
)