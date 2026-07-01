import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from pathlib import Path
from io import BytesIO

st.set_page_config(
    page_title="Input Ulasan",
    page_icon="✍️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "svc_model_norm1.pkl"
VECTORIZER_PATH = BASE_DIR / "model" / "tfidf_vectorizer_norm1.pkl"
CSV_PATH = BASE_DIR / "dataset" / "hasil_prediksi.csv"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

st.title("Input Ulasan")

st.caption(
    "Masukkan ulasan secara manual atau upload file CSV untuk prediksi massal."
)

tab1, tab2 = st.tabs([
    "Input Manual",
    "Upload CSV"
])

with tab1:

    ulasan = st.text_area(
        "Masukkan Ulasan",
        height=200,
        placeholder="Contoh: Aplikasi sering mengalami error saat pembayaran..."
    )

    col1, col2 = st.columns(2)

    prediksi_btn = col1.button(
        "Prediksi",
        use_container_width=True
    )

    reset_btn = col2.button(
        "Reset",
        use_container_width=True
    )

    if reset_btn:
        st.rerun()

    if prediksi_btn:

        if ulasan.strip() == "":
            st.warning(
                "Masukkan ulasan terlebih dahulu."
            )

        else:

            ulasan_tfidf = vectorizer.transform(
                [ulasan]
            ).toarray()

            hasil = model.predict(
                ulasan_tfidf
            )[0]

            probabilitas = model.predict_proba(
                ulasan_tfidf
            )[0]

            confidence = max(
                probabilitas
            )

            label = (
                "Subjektif"
                if hasil == 1
                else "Objektif"
            )

            st.success(
                f"Hasil Prediksi : {label}"
            )

            st.metric(
                "Confidence Score",
                f"{confidence * 100:.2f}%"
            )

            data_baru = pd.DataFrame([
                {
                    "review": ulasan,
                    "label": label,
                    "confidence": round(confidence, 4),
                    "tanggal": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }
            ])

            if CSV_PATH.exists():

                df_lama = pd.read_csv(
                    CSV_PATH
                )

                df_baru = pd.concat(
                    [
                        df_lama,
                        data_baru
                    ],
                    ignore_index=True
                )

            else:

                df_baru = data_baru

            df_baru.to_csv(
                CSV_PATH,
                index=False
            )

with tab2:

    st.subheader(
        "Upload CSV untuk Prediksi Massal"
    )

    st.info(
        "File CSV harus memiliki kolom bernama 'review'"
    )

    uploaded_file = st.file_uploader(
        "Pilih File CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        df_upload = pd.read_csv(
            uploaded_file
        )

        st.write(
            "Preview Data:"
        )

        st.dataframe(
            df_upload.head(),
            use_container_width=True
        )

        if "review" not in df_upload.columns:

            st.error(
                "Kolom 'review' tidak ditemukan."
            )

        else:

            if st.button(
                "Prediksi Semua Data",
                use_container_width=True
            ):

                hasil_prediksi = []

                for review in df_upload["review"]:

                    review = str(review)

                    review_tfidf = vectorizer.transform(
                        [review]
                    ).toarray()

                    hasil = model.predict(
                        review_tfidf
                    )[0]

                    probabilitas = model.predict_proba(
                        review_tfidf
                    )[0]

                    confidence = max(
                        probabilitas
                    )

                    label = (
                        "Subjektif"
                        if hasil == 1
                        else "Objektif"
                    )

                    hasil_prediksi.append(
                        {
                            "review": review,
                            "label": label,
                            "confidence": round(
                                confidence,
                                4
                            ),
                            "tanggal": datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S"
                            )
                        }
                    )

                hasil_df = pd.DataFrame(
                    hasil_prediksi
                )

                if CSV_PATH.exists():

                    df_lama = pd.read_csv(
                        CSV_PATH
                    )

                    df_final = pd.concat(
                        [
                            df_lama,
                            hasil_df
                        ],
                        ignore_index=True
                    )

                else:

                    df_final = hasil_df

                df_final.to_csv(
                    CSV_PATH,
                    index=False
                )

                st.success(
                    f"{len(hasil_df)} ulasan berhasil diprediksi."
                )

                st.dataframe(
                    hasil_df,
                    use_container_width=True
                )
                excel_buffer = BytesIO()

                with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
                    hasil_df.to_excel(
                    writer,
                    index=False,
                    sheet_name="Hasil Prediksi"
                )

                excel_buffer.seek(0)

                st.download_button(
                label="Download Hasil Prediksi (.xlsx)",
                data=excel_buffer,
                file_name="hasil_prediksi.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )