import csv
import random

# Template aktivitas dalam bentuk kalimat
templates = [
    "Saya mengambil langkah besar dalam hidup saya dengan {keputusan_besar}.",
    "Saya menghadapi tantangan besar dengan penuh keberanian ketika {keputusan_besar}.",
    "Saya memutuskan untuk keluar dari zona nyaman dengan {keputusan_besar}.",
    "Saya mengatasi ketakutan saya ketika {keputusan_besar}.",
    "Saya mengambil risiko besar dalam hidup saya ketika {keputusan_besar}.",
    "Saya memilih untuk terus berjuang meski {tantangan}.",
    "Saya menghadapi ketidakpastian dengan keyakinan karena {keputusan_besar}.",
    "Saya berani berbicara di depan umum meski {ketakutan}.",
    "Saya mengambil keputusan besar meski ada banyak keraguan karena {keputusan_besar}.",
    "Saya menghadapi ketakutan saya dengan penuh keberanian dan {keputusan_besar}.",
    "Saya keluar dari zona nyaman saya dan {keputusan_besar}.",
    "Saya menghadapi kegagalan dengan kepala tegak setelah {keputusan_besar}.",
    "Saya berani mengubah hidup saya dengan {keputusan_besar}.",
    "Saya memilih untuk bertahan dalam kesulitan dengan tekad karena {keputusan_besar}.",
    "Saya mengambil langkah besar menuju impian saya meski {rintangan}.",
    "Saya memutuskan untuk mengejar tujuan saya meski {tantangan}.",
    "Saya menghadapi risiko besar karena {keputusan_besar}.",
    "Saya berani menerima tantangan baru meski {ketakutan}.",
    "Saya melangkah maju meskipun saya merasa takut dengan {keputusan_besar}.",
    "Saya memilih untuk berkembang dengan mengambil {keputusan_besar}.",
    "Saya melangkah lebih jauh meski ada ketidakpastian dengan {keputusan_besar}.",
    "Saya percaya bahwa langkah besar saya akan membawa perubahan setelah {keputusan_besar}.",
    "Saya memilih untuk menjadi lebih berani dan mengambil {keputusan_besar}.",
    "Saya memilih untuk berdiri teguh meski {rintangan}.",
    "Saya mengambil keputusan besar dan melangkah maju dengan penuh keyakinan."
]

keputusan_besar_list = [
    "berpindah ke kota baru", "memulai usaha sendiri", "berbicara di depan umum", 
    "meninggalkan pekerjaan yang aman", "memutuskan untuk melanjutkan pendidikan", 
    "mengambil pekerjaan baru di luar negeri", "menyelesaikan masalah besar dalam hubungan pribadi", 
    "menghadapi ketakutan terbesar saya", "memulai petualangan baru", "mengambil keputusan yang tidak populer"
]

tantangan_list = [
    "saya tidak yakin dengan hasilnya", "banyak orang meragukan kemampuan saya", 
    "saya belum tahu apakah itu benar-benar tepat untuk saya", "ada banyak ketidakpastian di depan", 
    "saya takut gagal", "saya tidak tahu apakah ini akan berhasil", "saya merasa tidak siap", 
    "saya merasa tidak punya cukup pengalaman"
]

ketakutan_list = [
    "saya merasa gugup", "saya takut orang akan menilai saya", "saya merasa tidak bisa melakukannya", 
    "saya merasa tidak siap", "saya takut gagal", "saya takut mengecewakan orang lain"
]

rintangan_list = [
    "ada banyak rintangan di depan", "saya tidak tahu apakah saya bisa menghadapinya", "banyak halangan yang harus diatasi", 
    "saya khawatir dengan konsekuensinya", "perjalanan ini penuh dengan tantangan", "saya tidak tahu apakah ini keputusan yang tepat"
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

# Generate 1000 aktivitas Guts yang unik
data = []
for _ in range(1000):
    # Pilih template secara acak
    template = random.choice(templates)
    
    # Format kalimat dengan pilihan acak dari daftar
    kalimat = template.format(
        keputusan_besar=random.choice(keputusan_besar_list),
        tantangan=random.choice(tantangan_list),
        ketakutan=random.choice(ketakutan_list),
        rintangan=random.choice(rintangan_list)
    )
    
    # Cek jika kalimat sudah ada, jika belum tambahkan ke set dan list data
    if kalimat not in kalimat_unik:
        kalimat_unik.add(kalimat)
        tingkat = pilih_tingkat()
        data.append([kalimat, "Guts", tingkat])

# Simpan ke CSV
with open("persona-ai/dataset/guts_dataset.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text_aktivitas", "kategori", "tingkat_aktivitas"])
    writer.writerows(data)