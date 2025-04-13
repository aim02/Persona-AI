import csv
import random

# Template aktivitas dalam bentuk kalimat dengan placeholder { ... }
templates = [
    "Saya berusaha menjaga pola makan sehat dengan {kegiatan_aktif}.",
    "Saya menjaga kesehatan tubuh dengan rutin melakukan {kegiatan_aktif}.",
    "Saya selalu memastikan untuk tidur cukup dengan {kegiatan_aktif}.",
    "Saya berusaha menjaga keseimbangan tubuh dengan melakukan {kegiatan_aktif}.",
    "Saya mengikuti pola hidup sehat dengan melakukan {kegiatan_aktif} setiap hari.",
    "Saya menghindari makanan tidak sehat dengan {kegiatan_aktif}.",
    "Saya memperhatikan kesehatan mental dengan cara {kegiatan_aktif}.",
    "Saya menjaga kebugaran tubuh dengan {kegiatan_aktif}.",
    "Saya menjaga pola tidur yang baik dengan {kegiatan_aktif}.",
    "Saya selalu menjaga hidrasi tubuh dengan {kegiatan_aktif}.",
    "Saya berusaha menjaga berat badan yang ideal dengan {kegiatan_aktif}.",
    "Saya berusaha mengurangi stres dengan {kegiatan_aktif}.",
    "Saya menjaga kesehatan dengan melakukan aktivitas fisik yang rutin seperti {kegiatan_aktif}.",
    "Saya berusaha menjaga kebugaran dengan kegiatan {kegiatan_aktif}.",
    "Saya selalu meluangkan waktu untuk menjaga kesehatan dengan {kegiatan_aktif}.",
    "Saya berusaha menjaga kebugaran tubuh dengan mengikuti program {kegiatan_aktif}.",
    "Saya berkomitmen untuk hidup sehat dengan melakukan {kegiatan_aktif} setiap hari.",
    "Saya memilih aktivitas yang mendukung kesehatan tubuh, seperti {kegiatan_aktif}.",
    "Saya menjaga pola hidup sehat dengan melakukan {kegiatan_aktif} secara teratur.",
    "Saya berusaha menjaga pola hidup sehat dengan melakukan {kegiatan_aktif} secara konsisten."
]

# Expanded lists for the Health category
kegiatan_aktif_list = [
    "berolahraga secara rutin", "berjalan kaki setiap pagi", "mengikuti kelas yoga", "berenang di kolam renang", 
    "bersepeda di sekitar rumah", "berjalan kaki setelah makan", "makan makanan sehat dan bergizi", "minum air putih yang cukup", 
    "beristirahat dengan cukup setiap malam", "melakukan meditasi untuk meredakan stres", "melakukan latihan pernapasan dalam-dalam", 
    "menjaga pola tidur dengan tidur pada waktu yang sama setiap malam", "menghindari konsumsi makanan yang mengandung banyak gula", 
    "memilih makanan rendah lemak", "menerapkan pola makan dengan porsi kecil namun sering", "melakukan stretching setiap pagi"
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

# Generate 1000 aktivitas Health yang unik
data = []
for _ in range(1000):
    # Pilih template secara acak
    template = random.choice(templates)
    
    # Format kalimat dengan pilihan acak dari daftar
    kalimat = template.format(
        kegiatan_aktif=random.choice(kegiatan_aktif_list)
    )
    
    # Cek jika kalimat sudah ada, jika belum tambahkan ke set dan list data
    if kalimat not in kalimat_unik:
        kalimat_unik.add(kalimat)
        tingkat = pilih_tingkat()
        data.append([kalimat, "Health", tingkat])

# Simpan ke CSV
with open("persona-ai/dataset/health_dataset.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text_aktivitas", "kategori", "tingkat_aktivitas"])
    writer.writerows(data)