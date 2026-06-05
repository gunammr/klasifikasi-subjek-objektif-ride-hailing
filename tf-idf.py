from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


df = pd.read_csv('stemmed_reviews.csv')

kolom_target = 'stemmed_review' 

df[kolom_target] = df[kolom_target].fillna('')

dokumen = df[kolom_target].tolist()

vectorizer = TfidfVectorizer(lowercase=False)

tfidf_matrix = vectorizer.fit_transform(dokumen)

kata_kunci = vectorizer.get_feature_names_out()

df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=kata_kunci)

print(f"Berhasil memproses {len(dokumen)} dokumen.")

print("\n== MATRIKS TF-IDF 5 Baris Pertama ==")
print(df_tfidf.head())
