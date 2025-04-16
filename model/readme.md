# PersonaAI Model Training

## Deskripsi
Proyek ini mengembangkan model pembelajaran mesin untuk mengklasifikasikan teks aktivitas pengguna dalam dua kategori:
1. **Persona**: Mengklasifikasikan teks ke dalam kategori seperti Guts, Health, Kindness, Knowledge, Proficiency, dan Charm.
2. **Tingkat Aktivitas**: Mengklasifikasikan tingkat aktivitas pengguna ke dalam kategori Berat, Menengah, dan Ringan.

Model menggunakan **BERT IndoBERT** dan dilatih dengan **Stratified K-Fold Cross Validation**.

## Dataset
Dataset berisi teks aktivitas pengguna dengan label kategori Persona dan Tingkat Aktivitas, yang terdiri dari file CSV:
- `guts_dataset.csv`, `health_dataset.csv`, `kindness_dataset.csv`, dll.

## Metodologi
- **Preprocessing**: Label encoding, TF-IDF Vectorization, dan resampling (SMOTE).
- **Model**: TFBertForSequenceClassification dari Hugging Face.
- **Evaluasi**: Cross-validation, akurasi, precision, recall, dan F1-score.

## Hasil
**Model Persona (Akurasi: 98.94%)**
**Model Tingkat Aktivitas (Akurasi: 84.62%)**

## Poin Perbaikan yang Diperlukan

### 1. Menambah Dataset
Model yang digunakan saat ini dilatih dengan dataset yang terbatas. Untuk meningkatkan performa dan generalisasi model, sangat disarankan untuk menambah dataset yang lebih beragam dan berkualitas.
### 2. Meningkatkan Akurasi Model Tingkat Aktivitas (>90%)
Model saat ini mencapai akurasi 84,62% untuk klasifikasi Tingkat Aktivitas, yang masih kurang dari target >90%.

## Download Model
- [Download Model Persona (Fold 3)]([Here](https://drive.google.com/drive/folders/1BKakPl7nb4rCx7kssn9hS5blkA3YWtHG?usp=sharing))
- [Download Model Tingkat Aktivitas (Fold 3)]([Here](https://drive.google.com/drive/folders/1WrYlbvqBIRNQOXUO_B3u2Tm7JGvknTYm?usp=sharing))
