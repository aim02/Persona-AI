import csv
import random

# Template aktivitas dalam bentuk kalimat
templates = [
    "Saya menghabiskan waktu untuk membaca buku tentang {topik}.",
    "Saya memutuskan untuk belajar tentang {topik} agar bisa meningkatkan pemahaman saya.",
    "Saya mengikuti kursus online tentang {topik} untuk mengembangkan keterampilan saya.",
    "Saya berbagi pengetahuan saya tentang {topik} dengan orang lain.",
    "Saya meluangkan waktu untuk mempelajari {topik} dengan lebih mendalam.",
    "Saya membuat catatan untuk membantu diri saya sendiri memahami lebih baik tentang {topik}.",
    "Saya berusaha untuk menguasai {topik} melalui praktik dan pembelajaran.",
    "Saya belajar tentang {topik} agar dapat memperluas wawasan saya.",
    "Saya mencari referensi tambahan tentang {topik} untuk memperdalam pemahaman saya.",
    "Saya berdiskusi dengan teman-teman saya mengenai {topik} untuk saling berbagi pengetahuan.",
    "Saya menonton video pendidikan tentang {topik} untuk memperkaya wawasan saya.",
    "Saya menghadiri seminar tentang {topik} untuk mendapatkan informasi terbaru.",
    "Saya menyelesaikan latihan tentang {topik} untuk menguji pengetahuan saya.",
    "Saya menyusun rencana pembelajaran tentang {topik} untuk meningkatkan keterampilan saya.",
    "Saya mencoba untuk menguasai {topik} dengan cara membaca buku-buku tentangnya.",
    "Saya mengumpulkan artikel-artikel tentang {topik} untuk memperluas pengetahuan saya.",
    "Saya memanfaatkan sumber daya online untuk memahami lebih dalam mengenai {topik}.",
    "Saya membuat presentasi untuk berbagi pengetahuan tentang {topik} dengan orang lain.",
    "Saya menulis blog tentang {topik} untuk membagikan pengetahuan saya.",
    "Saya berpartisipasi dalam diskusi kelompok mengenai {topik} untuk saling belajar.",
    "Saya mempelajari {topik} untuk memperkaya wawasan saya tentang dunia sekitar.",
    "Saya menggunakan aplikasi belajar untuk memperdalam pengetahuan tentang {topik}.",
    "Saya berusaha menguasai {topik} agar dapat mengaplikasikannya dalam kehidupan sehari-hari.",
    "Saya membuat tutorial tentang {topik} untuk membantu orang lain belajar.",
    "Saya memperdalam pemahaman saya tentang {topik} dengan eksperimen langsung.",
    "Saya membaca artikel-artikel tentang {topik} untuk tetap up-to-date."
]

topik_list = [
    "Artificial Intelligence", "Machine Learning", "Deep Learning", "Matematika", "Fisika", 
    "Biologi", "Teknologi", "Filsafat", "Psikologi", "Ekonomi", "Seni", "Sejarah", "Literasi Digital", 
    "Pengembangan Diri", "Bahasa Pemrograman", "Game Development", "Desain Grafis", "Ekologi", 
    "Pendidikan", "Kewirausahaan", "Manajemen Waktu", "Produktivitas", "Kepemimpinan", "Inovasi Teknologi"
]

# Menentukan tingkat aktivitas berdasarkan probabilitas
def pilih_tingkat():
    return random.choices(
        population=["Ringan", "Menengah", "Berat"],
        weights=[0.5, 0.3, 0.2],
        k=1
    )[0]

# Set untuk menyimpan kalimat yang sudah digunakan
kalimat_unik = set()

# Generate 1000 aktivitas Knowledge yang unik
data = []
for _ in range(1000):
    # Pilih template secara acak
    template = random.choice(templates)
    
    # Format kalimat dengan pilihan acak dari daftar
    kalimat = template.format(
        topik=random.choice(topik_list)
    )
    
    # Cek jika kalimat sudah ada, jika belum tambahkan ke set dan list data
    if kalimat not in kalimat_unik:
        kalimat_unik.add(kalimat)
        tingkat = pilih_tingkat()
        data.append([kalimat, "Knowledge", tingkat])

# Simpan ke CSV
with open("persona-ai/dataset/knowledge_dataset.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text_aktivitas", "kategori", "tingkat_aktivitas"])
    writer.writerows(data)