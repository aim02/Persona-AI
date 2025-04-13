import csv
import random

# Template aktivitas dalam bentuk kalimat
templates = [
    "Saya mempelajari {topik} dengan cara {metode_pembelajaran}.",
    "Saya meningkatkan kemampuan saya dalam {topik} melalui {aktivitas_praktik}.",
    "Saya berlatih {topik} setiap hari dengan fokus pada {area_spesifik}.",
    "Saya mengikuti kursus {topik} untuk meningkatkan pemahaman saya.",
    "Saya membaca buku tentang {topik} untuk memperluas pengetahuan saya.",
    "Saya berusaha untuk mencapai {tujuan_pembelajaran} dalam bidang {topik}.",
    "Saya melatih diri dengan {aktivitas_praktik} untuk meningkatkan keterampilan saya di {topik}.",
    "Saya mencoba menyelesaikan tantangan dalam {topik} untuk menguji kemampuan saya.",
    "Saya mengikuti ujian atau tes dalam {topik} untuk menilai kemajuan saya.",
    "Saya melibatkan diri dalam proyek nyata yang berkaitan dengan {topik} untuk meningkatkan pengalaman saya.",
    "Saya berpartisipasi dalam komunitas online mengenai {topik} untuk berdiskusi dan berbagi ide.",
    "Saya membuat rencana pembelajaran untuk menguasai {topik} dalam waktu {jangka_waktu}.",
    "Saya menyusun materi ajar mengenai {topik} untuk lebih memahami konsep-konsep penting.",
    "Saya mencoba mengajar orang lain tentang {topik} untuk memperdalam pengetahuan saya.",
    "Saya menyusun portfolio yang menunjukkan kemajuan saya dalam {topik}.",
    "Saya berlatih menggunakan {alat_teknologi} untuk meningkatkan keterampilan praktis saya dalam {topik}.",
    "Saya mencari mentor dalam {topik} untuk mendapatkan bimbingan yang lebih mendalam.",
    "Saya menggunakan aplikasi atau platform online untuk meningkatkan keterampilan saya dalam {topik}.",
    "Saya menganalisis masalah dalam {topik} untuk menemukan solusi terbaik.",
    "Saya menantang diri saya untuk memecahkan masalah yang lebih sulit dalam {topik}.",
    "Saya mengikuti seminar atau webinar tentang {topik} untuk memperoleh wawasan baru.",
    "Saya membaca artikel ilmiah terkait {topik} untuk mengikuti perkembangan terbaru di bidang tersebut.",
    "Saya berkolaborasi dalam proyek yang berhubungan dengan {topik} untuk meningkatkan keterampilan tim saya."
]

topik_list = [
    "pemrograman", "data science", "matematika", "bahasa Inggris", "musik", "fotografi", "desain grafis", "teknologi informasi", "manajemen", "kepemimpinan"
]

metode_pembelajaran_list = [
    "membaca buku", "mengikuti tutorial online", "berlatih secara langsung", "bergabung dengan komunitas", "mengikuti kelas",
    "menggunakan aplikasi pembelajaran", "mencari mentor", "menonton video pembelajaran"
]

aktivitas_praktik_list = [
    "menyelesaikan soal latihan", "mengerjakan proyek", "membuat kode", "berlatih instrumen musik", "melakukan eksperimen", 
    "mengambil foto", "desain grafis", "menganalisis data", "berbicara dalam bahasa Inggris", "mengatur acara"
]

area_spesifik_list = [
    "algoritma", "statistik", "komunikasi lisan", "penulisan kode", "komposisi musik", "pengeditan foto", "modeling 3D", "analisis pasar", "negosiasi", "presentasi"
]

tujuan_pembelajaran_list = [
    "menguasai dasar-dasar", "menyelesaikan proyek kecil", "mendapatkan sertifikat", "mencapai level mahir", "memahami konsep-konsep utama",
    "menjadi ahli di bidang ini", "mampu mengajarkan orang lain", "menjadi profesional di industri ini"
]

jangka_waktu_list = [
    "satu bulan", "tiga bulan", "enam bulan", "satu tahun", "dua tahun"
]

alat_teknologi_list = [
    "Python", "R", "Adobe Photoshop", "Premiere Pro", "Final Cut Pro", "AutoCAD", "Excel", "Microsoft Word", "Google Analytics"
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

# Generate 1000 aktivitas Proficiency yang unik
data = []
for _ in range(1000):
    # Pilih template secara acak
    template = random.choice(templates)
    
    # Format kalimat dengan pilihan acak dari daftar
    kalimat = template.format(
        topik=random.choice(topik_list),
        metode_pembelajaran=random.choice(metode_pembelajaran_list),
        aktivitas_praktik=random.choice(aktivitas_praktik_list),
        area_spesifik=random.choice(area_spesifik_list),
        tujuan_pembelajaran=random.choice(tujuan_pembelajaran_list),
        jangka_waktu=random.choice(jangka_waktu_list),
        alat_teknologi=random.choice(alat_teknologi_list)
    )
    
    # Cek jika kalimat sudah ada, jika belum tambahkan ke set dan list data
    if kalimat not in kalimat_unik:
        kalimat_unik.add(kalimat)
        tingkat = pilih_tingkat()
        data.append([kalimat, "Proficiency", tingkat])

# Simpan ke CSV
with open("persona-ai/dataset/proficiency_dataset.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text_aktivitas", "kategori", "tingkat_aktivitas"])
    writer.writerows(data)