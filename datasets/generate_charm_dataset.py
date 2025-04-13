import csv
import random

# Template aktivitas dalam bentuk kalimat dengan placeholder { ... }
templates = [
    "Saya berusaha menjaga sikap yang santai dan percaya diri saat berbicara di depan orang banyak dengan {cara_menarik_perhatian}.",
    "Saya memberikan perhatian penuh pada percakapan sehingga orang merasa dihargai dengan {bahasa_tubuh}.",
    "Saya berusaha untuk membuat orang lain merasa nyaman dengan cara berbicara yang ramah, sambil {humor}.",
    "Saya menjaga sikap tubuh yang rileks dan terbuka agar orang merasa nyaman berada di sekitar saya dengan {penampilan_terbaik}.",
    "Saya berusaha tampil percaya diri tanpa terkesan sombong, dengan {pujian}.",
    "Saya menggunakan bahasa tubuh yang terbuka untuk membuat orang merasa lebih nyaman di sekitar saya dengan {bahasa_tubuh}.",
    "Saya mengungkapkan rasa terima kasih kepada orang lain secara terbuka untuk mempererat hubungan, sambil {humor}.",
    "Saya selalu berbicara dengan empati agar orang merasa dimengerti dan dihargai, sambil memperhatikan {penampilan_terbaik}.",
    "Saya memperhatikan penampilan saya agar bisa membuat kesan pertama yang baik dengan {cara_menarik_perhatian}.",
    "Saya sering mengungkapkan pujian yang tulus kepada orang lain untuk membuat mereka merasa dihargai, seperti {pujian}.",
    "Saya berusaha menghibur orang-orang di sekitar saya dengan cerita yang menarik sambil {humor}.",
    "Saya menggunakan sikap percaya diri untuk mempengaruhi orang lain secara positif dengan {bahasa_tubuh}.",
    "Saya mencoba untuk menjadi orang yang menyenangkan untuk diajak berbicara dengan {cara_menarik_perhatian}.",
    "Saya berusaha untuk selalu menjaga bahasa tubuh yang positif dan ramah dengan {penampilan_terbaik}.",
    "Saya berusaha untuk menjadi pendengar yang baik saat berbicara dengan orang lain, sambil {humor}.",
    "Saya berusaha untuk menunjukkan rasa hormat dan ketulusan dalam setiap pertemuan dengan {pujian}.",
    "Saya selalu memberi senyuman kepada orang yang saya temui, meskipun dalam situasi sulit, dan {cara_menarik_perhatian}.",
    "Saya percaya bahwa setiap orang berhak untuk dihargai dan merasa penting, yang saya tunjukkan dengan {bahasa_tubuh}.",
    "Saya menunjukkan ketertarikan yang tulus terhadap orang lain melalui pertanyaan dan perhatian, serta {pujian}.",
    "Saya mengusahakan untuk menjadi orang yang penuh semangat agar orang merasa terinspirasi dengan {humor}.",
    "Saya berusaha menjadi orang yang dapat dipercaya dan dapat membuat orang merasa nyaman berbicara dengan saya, dengan {penampilan_terbaik}.",
    "Saya berusaha untuk mengerti perasaan orang lain dan memberikan dukungan melalui kata-kata yang positif, serta {cara_menarik_perhatian}.",
    "Saya menggunakan humor untuk mencairkan suasana dan membuat orang merasa lebih dekat dengan {humor}.",
    "Saya berusaha memperlihatkan sikap yang menyenangkan agar orang merasa senang berada di sekitar saya, sambil {penampilan_terbaik}.",
    "Saya menciptakan suasana yang menyenangkan dengan sikap positif dan penuh semangat, yang bisa dilihat dari {bahasa_tubuh}.",
    "Saya percaya bahwa melalui kata-kata yang baik, kita bisa menciptakan koneksi yang kuat dengan orang lain, dengan {pujian}.",
    "Saya berbicara dengan nada suara yang menyenangkan agar orang merasa dihargai dan diperhatikan, dengan {cara_menarik_perhatian}.",
    "Saya selalu berusaha untuk tampil dengan senyuman yang memikat di setiap kesempatan, yang saya tunjukkan dengan {penampilan_terbaik}.",
    "Saya berusaha untuk membuat orang merasa istimewa dengan mendengarkan mereka dengan penuh perhatian, sambil {humor}.",
    "Saya menunjukkan empati kepada orang lain agar mereka merasa dihargai dan diterima dengan {bahasa_tubuh}.",
    "Saya mencoba untuk selalu memperlihatkan sikap yang positif dan optimis, sambil {pujian}.",
    "Saya berusaha untuk memberi perhatian lebih kepada orang yang saya temui, sehingga mereka merasa spesial, dengan {cara_menarik_perhatian}.",
    "Saya selalu menjaga kontak mata untuk menunjukkan perhatian dan rasa hormat, serta {bahasa_tubuh}.",
    "Saya selalu berusaha untuk memberikan kesan yang baik dengan sikap santun dan ramah, serta {penampilan_terbaik}.",
    "Saya mengenal orang-orang dengan cepat dan berusaha untuk menarik perhatian mereka dengan karisma saya, melalui {humor}."
]

# Expanded lists for the Charm category
cara_menarik_perhatian_list = [
    "senyuman tulus", "berbicara dengan nada suara yang lembut", "menunjukkan ketertarikan pada cerita mereka",
    "menggunakan bahasa tubuh yang ramah", "memberikan pujian yang tulus", "mendengarkan dengan perhatian penuh",
    "menghargai setiap percakapan", "menggunakan humor untuk mencairkan suasana", "menunjukkan rasa hormat dalam setiap kata",
    "memiliki sikap percaya diri yang tidak berlebihan", "memberikan perhatian yang penuh dalam setiap interaksi"
]

penampilan_terbaik_list = [
    "menjaga penampilan dengan pakaian yang rapi dan sopan", "memakai pakaian yang cocok dengan suasana", "berpakaian dengan cara yang memancarkan kepercayaan diri",
    "memilih aksesori yang sederhana namun elegan", "memperhatikan detail kecil dalam penampilan", "menjaga kebersihan dan kerapian diri"
]

bahasa_tubuh_list = [
    "sikap tubuh yang terbuka", "menjaga kontak mata dengan orang yang diajak bicara", "postur tubuh yang tegak dan percaya diri", "gerakan tangan yang natural saat berbicara",
    "senyum yang ramah dan tulus", "berdiri dengan cara yang menunjukkan kepercayaan diri", "mempertahankan ekspresi wajah yang ramah dan penuh perhatian"
]

humor_list = [
    "menceritakan cerita lucu untuk menghibur orang lain", "menggunakan lelucon ringan untuk mencairkan suasana", "menggunakan humor situasional", "bercanda dengan cara yang ramah dan tidak menyinggung",
    "memberikan komentar lucu yang membuat orang tertawa", "bermain-main dengan kata-kata untuk membuat orang tersenyum"
]

pujian_list = [
    "memberikan pujian tentang penampilan mereka", "mengungkapkan penghargaan terhadap usaha mereka", "memuji keahlian mereka dalam sesuatu", "memberikan pujian atas sifat baik mereka",
    "memberikan pujian tulus atas kebaikan hati mereka", "memuji ide-ide atau kreativitas mereka", "memberikan pujian tentang bagaimana mereka membuat orang lain merasa dihargai"
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

# Generate 1000 aktivitas Charm yang unik
data = []
for _ in range(1000):
    # Pilih template secara acak
    template = random.choice(templates)
    
    # Format kalimat dengan pilihan acak dari daftar
    kalimat = template.format(
        cara_menarik_perhatian=random.choice(cara_menarik_perhatian_list),
        penampilan_terbaik=random.choice(penampilan_terbaik_list),
        bahasa_tubuh=random.choice(bahasa_tubuh_list),
        humor=random.choice(humor_list),
        pujian=random.choice(pujian_list)
    )
    
    # Cek jika kalimat sudah ada, jika belum tambahkan ke set dan list data
    if kalimat not in kalimat_unik:
        kalimat_unik.add(kalimat)
        tingkat = pilih_tingkat()
        data.append([kalimat, "Charm", tingkat])

# Simpan ke CSV
with open("persona-ai/dataset/charm_dataset.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text_aktivitas", "kategori", "tingkat_aktivitas"])
    writer.writerows(data)
