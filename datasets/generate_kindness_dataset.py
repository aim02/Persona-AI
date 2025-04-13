import csv
import random

# Template aktivitas dalam bentuk kalimat
templates = [
    "Saya menunjukkan kasih sayang kepada {orang_terdekat} dengan cara {cara_menunjukkan}.",
    "Saya merayakan momen spesial dengan {orang_terdekat} pada {tanggal_spesial}.",
    "Saya memberikan kejutan manis kepada {orang_terdekat} berupa {hadiah}.",
    "Saya meluangkan waktu untuk {kegiatan_bersama} dengan {orang_terdekat}.",
    "Saya menulis surat untuk {orang_terdekat}.",
    "Saya membuatkan makanan favorit untuk {orang_terdekat}.",
    "Saya memberi dukungan emosional kepada {orang_terdekat} saat {situasi_difficult}.",
    "Saya mengungkapkan perasaan saya kepada {orang_terdekat} melalui {cara_ungkapan}.",
    "Saya merawat hewan peliharaan saya dengan penuh kasih sayang.",
    "Saya berusaha menjaga hubungan dengan {orang_terdekat} meski ada perbedaan.",
    "Saya membantu {orang_terdekat} dengan {bantuan_kebaikan} ketika mereka dalam kesulitan.",
    "Saya memberikan hadiah kejutan berupa {hadiah_kebaikan} untuk {orang_terdekat}.",
    "Saya memaafkan orang lain meski mereka {kesalahan_mereka}.",
    "Saya berusaha mendengarkan keluhan orang lain dengan penuh perhatian.",
    "Saya membantu seseorang yang sedang dalam kesulitan dengan memberi {bantuan_kebaikan}.",
    "Saya memberikan senyuman dan kata-kata penyemangat untuk orang yang saya temui hari ini.",
    "Saya menolong orang yang membutuhkan dengan cara {bantuan_kebaikan}.",
    "Saya memberikan waktu saya untuk membantu {kegiatan_sosial} tanpa mengharapkan imbalan.",
    "Saya percaya bahwa setiap orang berhak untuk merasa bahagia dan dihargai.",
    "Saya berharap bisa memberikan lebih banyak kebaikan kepada orang-orang di sekitar saya.",
    "Saya yakin bahwa dunia ini masih penuh harapan dan kebaikan.",
    "Saya berusaha menjadi sumber harapan bagi orang-orang yang sedang mengalami kesulitan.",
    "Saya percaya bahwa dengan kebaikan, kita bisa mengubah dunia menjadi lebih baik.",
    "Saya membantu orang lain dengan harapan bahwa mereka akan melakukan hal yang sama suatu hari nanti.",
    "Saya memberikan dukungan dengan keyakinan bahwa itu akan membantu orang lain pulih dan berkembang.",
    "Saya menginspirasi orang lain untuk tetap berharap meskipun menghadapi kesulitan.",
    "Saya merasa bahwa harapan adalah kunci untuk bertahan dan tumbuh dalam hidup."
]

orang_terdekat_list = [
    "pasangan", "orang tua", "teman terbaik", "saudara", "anak", "hewan peliharaan"
]

cara_menunjukkan_list = [
    "memberikan pelukan", "mengucapkan kata-kata manis", "memberikan perhatian lebih",
    "meluangkan waktu bersama", "membantu dalam kesulitan"
]

tanggal_spesial_list = [
    "ulang tahun", "hari jadian", "perayaan hari jadi pernikahan", "Hari Valentine", "hari libur keluarga"
]

hadiah_list = [
    "kalung", "boneka", "tiket konser", "bunga", "hadiah buatan tangan", "surat cinta"
]

kegiatan_bersama_list = [
    "berjalan-jalan di taman", "berkumpul di rumah", "menonton film bersama", "memasak bersama", "bermain permainan"
]

situasi_difficult_list = [
    "kesulitan pekerjaan", "masalah pribadi", "ketika sedang sakit", "ketika merasa cemas"
]

cara_ungkapan_list = [
    "surat", "puisi", "percakapan hati ke hati", "pesan teks", "video call"
]

bantuan_kebaikan_list = [
    "membantu membersihkan rumah", "menyediakan makanan", "menawarkan bantuan finansial", "mendengarkan keluhan", "membantu membawa barang"
]

hadiah_kebaikan_list = [
    "buku motivasi", "bunga segar", "tiket untuk aktivitas yang disukai", "handmade gifts", "parfum favorit"
]

kesalahan_mereka_list = [
    "telah membuat saya kecewa", "tidak menghargai waktu saya", "melakukan sesuatu yang salah", "melupakan janji"
]

kegiatan_sosial_list = [
    "penggalangan dana", "bantuan bencana", "pendampingan anak-anak", "membersihkan lingkungan", "kegiatan bakti sosial"
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

# Generate 1000 aktivitas Hope dan Kindness yang unik
data = []
for _ in range(1000):
    # Pilih template secara acak
    template = random.choice(templates)
    
    # Format kalimat dengan pilihan acak dari daftar
    kalimat = template.format(
        orang_terdekat=random.choice(orang_terdekat_list),
        cara_menunjukkan=random.choice(cara_menunjukkan_list),
        tanggal_spesial=random.choice(tanggal_spesial_list),
        hadiah=random.choice(hadiah_list),
        kegiatan_bersama=random.choice(kegiatan_bersama_list),
        situasi_difficult=random.choice(situasi_difficult_list),
        cara_ungkapan=random.choice(cara_ungkapan_list),
        bantuan_kebaikan=random.choice(bantuan_kebaikan_list),
        hadiah_kebaikan=random.choice(hadiah_kebaikan_list),
        kesalahan_mereka=random.choice(kesalahan_mereka_list),
        kegiatan_sosial=random.choice(kegiatan_sosial_list)
    )
    
    # Cek jika kalimat sudah ada, jika belum tambahkan ke set dan list data
    if kalimat not in kalimat_unik:
        kalimat_unik.add(kalimat)
        tingkat = pilih_tingkat()
        data.append([kalimat, "Kindness", tingkat])

# Simpan ke CSV
with open("persona-ai/dataset/kindness_dataset.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text_aktivitas", "kategori", "tingkat_aktivitas"])
    writer.writerows(data)