from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


df = pd.read_csv('stemmed_reviews.csv')

kolom_target = 'stemmed_review' 

# Jika ada baris kosong (NaN), paksa menjadi string kosong
df[kolom_target] = df[kolom_target].fillna('')

# Ubah kolom DataFrame kembali menjadi format list yang dipahami TfidfVectorizer
dokumen = df[kolom_target].tolist()

# Inisialisasi model TF-IDF
vectorizer = TfidfVectorizer(lowercase=False)

# Fit (pelajari kosakata) dan Transform (hitung bobot TF-IDF)
tfidf_matrix = vectorizer.fit_transform(dokumen)

# Ambil daftar kata unik yang berhasil diekstrak (sebagai header kolom)
kata_kunci = vectorizer.get_feature_names_out()

# Ubah hasil (sparse matrix) menjadi array biasa dan masukkan ke DataFrame Pandas
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=kata_kunci)

print(f"Berhasil memproses {len(dokumen)} dokumen.")

print("\n== MATRIKS TF-IDF 5 Baris Pertama ==")
print(df_tfidf.head())
