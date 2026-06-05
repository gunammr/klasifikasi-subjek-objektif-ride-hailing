from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

dokumen = [
    "Kucing itu tidur di atas meja.",
    "Anjing itu mengejar kucing di taman.",
    "Kucing dan anjing adalah hewan peliharaan."
]

# 2. Inisialisasi model TF-IDF

vectorizer = TfidfVectorizer(lowercase=False)

# Fit (pelajari kosakata) dan Transform (hitung bobot TF-IDF)
tfidf_matrix = vectorizer.fit_transform(dokumen)

# Ambil daftar kata unik yang berhasil diekstrak (sebagai header kolom)
kata_kunci = vectorizer.get_feature_names_out()

# Ubah hasil (sparse matrix) menjadi array biasa dan masukkan ke DataFrame Pandas
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=kata_kunci)

print("DAFTAR KATA (VOCABULARY)")
print(kata_kunci)

print("\nMATRIKS TF-IDF")
print(df_tfidf)
