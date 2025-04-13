# 🧠 Self-Tracking AI System

Sebuah sistem self-tracking berbasis AI yang membantu pengguna melacak dan mengembangkan diri melalui aktivitas sehari-hari secara otomatis dan menyenangkan.

## 🔭 Visi & Tujuan

### 🎯 Visi
Membangun sistem self-tracking yang fleksibel dan berbasis AI untuk membantu pengguna melacak perkembangan aktivitas mereka secara otomatis tanpa batasan jenis kegiatan.

### 🎯 Tujuan
- Menggunakan AI untuk mengklasifikasikan dan memberikan poin berdasarkan aktivitas pengguna.
- Menganalisis pola aktivitas dan memberikan statistik perkembangan.
- Mengintegrasikan sistem dengan UI berbasis web untuk pengalaman pengguna yang mudah.
- Memungkinkan AI untuk mengenali konsumsi (misal: membaca buku tertentu meningkatkan stats tertentu).

---

## 🚀 Fitur Utama

### 📝 Input Aktivitas
- Pengguna dapat memasukkan aktivitas dalam bentuk teks bebas.
- AI akan membaca input dan mengkategorikan aktivitas secara otomatis.

**Contoh:**
- `"Saya membaca 30 halaman Atomic Habits."` → + Knowledge 📖  
- `"Saya jogging selama 20 menit."` → + Health 💪  
- `"Saya berbicara di depan umum hari ini!"` → + Guts 🔥  
- `"Saya membantu teman dengan tugasnya."` → + Kindness 💙  

---

### ⚙️ Klasifikasi Aktivitas & Poin Otomatis
- Menggunakan NLP (Natural Language Processing) untuk memahami teks aktivitas.
- AI menentukan kategori dan memberikan poin berdasarkan bobot aktivitas.

| Tingkat Aktivitas | Poin        |
|-------------------|-------------|
| Ringan            | 5 - 10 XP   |
| Menengah          | 15 - 25 XP  |
| Berat             | 30 - 50 XP  |

---

### 📊 Statistik & Perkembangan
- **Dashboard visualisasi:** radar chart, pie chart, trend perkembangan.
- **Leveling system:** Setiap kategori memiliki XP & Level.
- **Title:** Setiap milestone level mendapatkan gelar khusus.
- **Level Maksimum:** 21+ → status "Master".

#### 📖 Knowledge
| Level     | Title         | Deskripsi                                       |
|-----------|---------------|-------------------------------------------------|
| 1 - 5     | Beginner       | Baru mulai membaca dan belajar.                |
| 6 - 10    | Learner        | Memahami konsep dasar.                         |
| 11 - 15   | Scholar        | Bisa membagikan pengetahuan.                   |
| 16 - 20   | Expert         | Pemahaman mendalam, riset sendiri.             |
| 21+       | Mastermind     | Pakar dalam bidang tertentu.                   |

#### 🔥 Guts
| Level     | Title         | Deskripsi                                       |
|-----------|---------------|-------------------------------------------------|
| 1 - 5     | Timid          | Ragu dan takut mencoba hal baru.               |
| 6 - 10    | Brave          | Mulai hadapi tantangan.                        |
| 11 - 15   | Fearless       | Mengatasi ketakutan, lebih tegas.              |
| 16 - 20   | Daredevil      | Langkah besar tanpa ragu.                      |
| 21+       | Unbreakable    | Mental baja, siap tantangan besar.             |

#### 🛠️ Proficiency
| Level     | Title         | Deskripsi                                       |
|-----------|---------------|-------------------------------------------------|
| 1 - 5     | Novice         | Baru mulai keterampilan.                       |
| 6 - 10    | Apprentice     | Mahir tugas dasar.                             |
| 11 - 15   | Craftsman      | Mulai efisien dan mahir.                       |
| 16 - 20   | Specialist     | Keahlian solid.                                |
| 21+       | Master of Craft| Diakui sebagai ahli.                           |

#### 💙 Kindness
| Level     | Title         | Deskripsi                                       |
|-----------|---------------|-------------------------------------------------|
| 1 - 5     | Casual Helper  | Suka membantu sesekali.                        |
| 6 - 10    | Caring Friend  | Peduli secara aktif.                          |
| 11 - 15   | Compassionate  | Sosok yang baik hati.                         |
| 16 - 20   | Philanthropist | Dampak sosial besar.                          |
| 21+       | Saint          | Empati luar biasa.                            |

#### ✨ Charm
| Level     | Title            | Deskripsi                                         |
|-----------|------------------|---------------------------------------------------|
| 1 - 5     | Shy               | Kurang percaya diri.                             |
| 6 - 10    | Friendly          | Nyaman berinteraksi.                             |
| 11 - 15   | Charming          | Menarik & membangun hubungan baik.               |
| 16 - 20   | Charismatic Leader| Menginspirasi banyak orang.                      |
| 21+       | Legendary Figure  | Sosok ikonik dan menginspirasi.                  |

#### 💪 Health
| Level     | Title         | Deskripsi                                       |
|-----------|---------------|-------------------------------------------------|
| 1 - 5     | Unfit          | Kurang bugar.                                   |
| 6 - 10    | Active         | Rutin olahraga.                                 |
| 11 - 15   | Athletic       | Stamina meningkat.                              |
| 16 - 20   | Peak Condition | Kondisi fisik sangat baik.                      |
| 21+       | Iron Body      | Ketahanan luar biasa.                           |

---

### 🤖 AI untuk Rekomendasi & Evaluasi
- Memberi saran berdasarkan statistik pengguna.
- Menjaga keseimbangan pertumbuhan seluruh stats.

**Contoh:**
- `"Health rendah → Mungkin kamu butuh olahraga ringan hari ini?"`
- `"Charm rendah → Coba berinteraksi lebih banyak dengan orang lain!"`
- `"Kamu banyak belajar, tapi kurang olahraga. Jangan lupa jaga kesehatan!"`

---

## 🧩 Arsitektur Sistem

| Komponen     | Teknologi                          |
|--------------|------------------------------------|
| Frontend     | ReactJS / Streamlit / Next.js (?)  |
| Backend API  | FastAPI / Flask (?)                |
| AI Model     | spaCy / OpenAI / NLP Custom        |
| Database     | SQLite / PostgreSQL / Firebase (?) |
| Hosting      | Vercel (Frontend), Render (API)    |

---

## ⚙️ Alur Kerja Sistem

1. User input aktivitas → Teks bebas.
2. AI klasifikasikan → Menentukan kategori & poin.
3. Data disimpan → Statistik diperbarui.
4. Dashboard → Visualisasi progres & level.


---

## 🖼️ Wireframe UI

### 🏠 Halaman Utama
- Input aktivitas (text box)
- Statistik singkat (XP, level, radar chart)
- Rekomendasi AI
- Profil / foto pengguna

### 📈 Halaman Statistik Detail
- Breakdown XP per kategori
- Riwayat aktivitas pengguna
- Grafik perkembangan per waktu

---

## 📅 Roadmap Pengembangan

### 🔹 Phase 1: MVP
- [ ] Model AI sederhana untuk klasifikasi
- [ ] API backend untuk input dan XP
- [ ] UI dasar (input + statistik singkat)

### 🔹 Phase 2: AI & Database
- [ ] Model NLP lebih fleksibel
- [ ] Integrasi database (history & XP)
- [ ] Sistem level-up

### 🔹 Phase 3: UI & Rekomendasi
- [ ] Dashboard interaktif
- [ ] Rekomendasi AI berbasis pola
- [ ] Notifikasi & tantangan harian

---

> 📌 Dibuat dengan semangat self-growth dan teknologi ✨  
> Powered by Python, NLP, and your real-life efforts.

![Preview](https://i.redd.it/gyimgw5nm4f61.png)

