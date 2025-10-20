# 🌾 Sistem Pakar Rekomendasi Tanaman Berdasarkan Kondisi Lingkungan

## 📖 Deskripsi Proyek

Sistem ini merupakan **sistem pakar berbasis aturan (rule-based expert system)** yang berfungsi untuk memberikan **rekomendasi jenis tanaman** yang sesuai dengan kondisi lingkungan tertentu.
Sistem menerima input berupa parameter lingkungan seperti **jenis tanah**, **curah hujan**, dan **iklim**, kemudian menghasilkan rekomendasi tanaman yang cocok melalui proses inferensi berbasis *forward chaining*.

Tujuan utama dari sistem ini adalah untuk membantu pengguna — terutama petani atau pelajar — memahami hubungan antara faktor lingkungan dengan kesesuaian tanaman menggunakan pendekatan kecerdasan buatan berbasis pengetahuan (*knowledge-based system*).

---

## 🧠 Komponen Sistem Pakar

| Komponen                  | Deskripsi                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Knowledge from Expert** | Pengetahuan diperoleh dari literatur agronomi dan penelitian mengenai kesesuaian lahan dan tanaman.                    |
| **Knowledge Base**        | Berisi kumpulan aturan (*if–then rules*) yang menghubungkan kondisi lingkungan dengan tanaman yang sesuai.             |
| **Inference Engine**      | Mesin inferensi yang menggunakan metode *forward chaining* untuk menelusuri aturan berdasarkan fakta yang diberikan.   |
| **User Interface**        | Antarmuka berbasis web yang memungkinkan pengguna memasukkan kondisi lingkungan dan melihat hasil rekomendasi tanaman. |

---

## ⚙️ Cara Kerja Sistem

1. **Input Data Lingkungan**
   Pengguna memasukkan kondisi seperti jenis tanah, curah hujan, dan iklim melalui antarmuka sistem.

2. **Proses Inferensi**
   Mesin inferensi mencocokkan fakta input dengan aturan dalam *knowledge base* menggunakan metode *forward chaining*.

3. **Output Rekomendasi**
   Sistem menampilkan tanaman yang paling sesuai dengan kondisi lingkungan yang dimasukkan pengguna.

---

## 🪴 Contoh Aturan (Rule Base)

Contoh penerapan aturan dalam sistem pakar:

```
    {"if": {"tanah_gembur", "curah_hujan_rendah"}, "then": "cocok_jagung"},
    {"if": {"tanah_liat", "curah_hujan_sedang"}, "then": "cocok_singkong"},
    {"if": {"tanah_berpasir", "curah_hujan_rendah"}, "then": "cocok_kacang_tanah"},
```

Aturan di atas disusun berdasarkan prinsip agronomi umum dan literatur ilmiah mengenai kesesuaian lahan dan tanaman.

---

## 📘 Sumber Pengetahuan (Knowledge Source / Rule Base Reference)

Aturan dalam sistem pakar ini disusun berdasarkan prinsip agronomi dan penelitian terkait evaluasi kesesuaian lahan terhadap jenis tanaman.

Referensi utama:

1. **Kalogirou, S. (2002).** *Expert Systems and GIS: An Application of Land Suitability Evaluation.*
   — Menjelaskan penerapan sistem pakar berbasis aturan untuk menentukan kesesuaian lahan menggunakan data lingkungan.

2. **AbdelRahman, M.A.E., Natarajan, A., & Hegde, R. (2022).** *Assessment of Land Suitability Using a Soil-Indicator-Based Approach.*
   — Menjabarkan hubungan antara karakteristik tanah (tekstur, drainase) dengan tanaman yang cocok ditanam.

3. **FAO (1985).** *Guidelines: Land Evaluation for Rainfed Agriculture.*
   — Panduan internasional mengenai kriteria kesesuaian tanah, iklim, dan topografi terhadap tanaman.

4. **Prinsip Agronomi Umum.**
   — Pengetahuan dasar yang menjelaskan bahwa kesesuaian tanaman bergantung pada:

   * Jenis dan tekstur tanah
   * Curah hujan
   * Suhu dan iklim

---


## 🧪 Teknologi yang Digunakan

* **Python** untuk pemrosesan logika dan inferensi
* **Fast API** (opsional) untuk membuat Rest API sederhana
* **HTML / Tailwind / JavaScript** untuk tampilan antarmuka pengguna
* **Rule-based reasoning (Forward Chaining)** untuk sistem inferensi

---

## 💬 Cara Menjalankan

1. Clone repository:

   ```bash
   git clone https://github.com/raihants/Sistem-pakar-rekomendasi-tanaman-berdasarkan-kondisi-lingkungan.git
   cd Sistem-pakar-rekomendasi-tanaman-berdasarkan-kondisi-lingkungan
   ```

2. Jalankan program:

   ```bash
   docker compose up --build

   lalu jalankan di docker desktop 
   ```

3. Masukkan kondisi lingkungan sesuai instruksi di terminal atau antarmuka web.

---
