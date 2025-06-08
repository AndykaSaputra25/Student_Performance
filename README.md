
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meskipun memiliki reputasi baik dan banyak lulusan berkualitas, institusi ini menghadapi tantangan serius terkait angka mahasiswa yang tidak menyelesaikan studinya alias dropout.

### Permasalahan Bisnis

Angka dropout yang tinggi berisiko merusak reputasi institusi, menurunkan efektivitas operasional, serta berpengaruh terhadap pendanaan dan akreditasi. Oleh karena itu, institusi memerlukan sistem yang mampu:
- Memprediksi kemungkinan dropout sejak dini.
- Memberikan wawasan faktor-faktor utama yang mempengaruhi performa mahasiswa.
- Memonitor performa dan status mahasiswa secara visual melalui dashboard.

### Cakupan Proyek

1. Membersihkan dan menyiapkan data performa mahasiswa.
2. Melakukan eksplorasi data dan feature selection.
3. Membangun model klasifikasi status mahasiswa (Dropout, Enrolled, Graduate).
4. Mengembangkan dashboard interaktif di Metabase.
5. Deploy prototype sistem prediksi ke Streamlit Cloud.

### Persiapan

**Sumber data:** [Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Setup environment:**
```bash
pip install -r requirements.txt
```

---

## Business Dashboard

Dashboard telah dibuat menggunakan **Metabase** dengan koneksi ke database Supabase. Dashboard mencakup:

- Total Students : Jumlah seluruh mahasiswa yang terdapat dalam database (4,424 mahasiswa). Menunjukkan cakupan analisis.
- Average Age of Enrollment : Usia rata-rata mahasiswa saat mendaftar. Usia bisa memengaruhi performa dan risiko dropout.
- Dropout Rate : Persentase mahasiswa yang tidak menyelesaikan studi. Ini adalah salah satu indikator keberhasilan institusi.
- Average Admission Grade : Rata-rata nilai penerimaan masuk (seleksi awal). Bisa menggambarkan kualitas awal input mahasiswa.
- Average Previous Qualification Grade : Nilai pendidikan terakhir sebelum masuk kampus. Penting untuk melihat pengaruh latar belakang akademik.
- Total Students by Status : Donut chart yang membagi mahasiswa menjadi: Graduate, Enrolled, dan Dropout. Penting untuk melihat proporsi performa akademik.
- Total Students by Gender : Visualisasi proporsi laki-laki vs perempuan. Bisa digunakan untuk menganalisis apakah ada perbedaan tren dropout antar gender.
- Total Students by Marital Status : Bar chart yang menunjukkan status pernikahan (Lajang, Menikah, Bercerai) per kategori status mahasiswa. Menarik untuk melihat apakah status pernikahan berkorelasi dengan kelulusan/dropout.
- Scholarship Holder : Donut chart yang menunjukkan proporsi mahasiswa penerima beasiswa.
- Debtor : Visualisasi proporsi mahasiswa yang memiliki tunggakan pembayaran. Ini berkaitan langsung dengan potensi risiko dropout.
- Displaced : Apakah mahasiswa berasal dari wilayah yang terkena relokasi/geografis tertentu. Bisa dikaitkan dengan akses dan performa.
- Students Performance Grade per Semester : Grouped bar chart yang membandingkan rata-rata nilai semester pertama dan kedua berdasarkan status mahasiswa. Terlihat bahwa mahasiswa Dropout memiliki rata-rata nilai yang lebih rendah.
- Average Enrolled Curriculum : Jumlah mata kuliah yang diambil (enrolled) di semester 1 dan 2. Menunjukkan tingkat partisipasi mahasiswa.
- Average Approved Curriculum : Mata kuliah yang disetujui/lulus (approved). Bisa digunakan untuk mengukur keberhasilan per semester.
- Average Evaluation Curriculum : Mata kuliah yang diikuti ujian/penilaian. Membantu mengetahui aktivitas akademik mahasiswa.
- Attendance Time : Bar chart menunjukkan jumlah mahasiswa berdasarkan waktu kuliah (Siang atau Malam). Bisa dibandingkan dengan proporsi dropout.
- Total Age at Enrollment : Horizontal bar chart dengan bin usia (16–25, 26–35, dst). Membantu mengetahui rentang usia dominan saat masuk kuliah. Berguna untuk analisis kelompok rentan terhadap dropout.

🔗 Akses dashboard:  
```bash
docker run -p 3000:3000 --name metabase metabase/metabase
username : root@mail.com
password : root123
```

---

## Menjalankan Sistem Machine Learning

Model klasifikasi telah dibangun dengan algoritma Random Forest dan disimpan dalam format `.joblib`. Prototype berbasis Streamlit memungkinkan input data mahasiswa secara manual dan menampilkan prediksi status mereka (Dropout, Graduate, Enrolled).

**Menjalankan secara lokal:**
```bash
streamlit run app.py
```

**Link Deploy Streamlit Cloud:**  
🔗 `https://studentperformancebyandyka.streamlit.app/`

---

## Conclusion

Proyek ini berhasil membangun sistem prediktif berbasis machine learning untuk mengklasifikasikan status mahasiswa berdasarkan data demografi dan akademik. Selain itu, dashboard analitik interaktif juga telah disiapkan untuk memberikan insight visual kepada manajemen.

Akurasi model terbaik mencapai >75% dan mampu membantu mengidentifikasi potensi dropout secara dini.

Insight berdasarkan dataset performance students.

1. Nilai akademik pada semester pertama memiliki pengaruh paling signifikan terhadap potensi dropout. Mahasiswa dengan performa rendah cenderung tidak menyelesaikan studi.
2. Mahasiswa dengan status Debtor dan tanpa beasiswa memiliki tingkat dropout yang lebih tinggi, kemungkinan karena beban finansial.
3. Mahasiswa kelas malam menunjukkan kecenderungan dropout lebih besar dibanding kelas siang.
4. Dashboard interaktif efektif untuk memantau faktor-faktor yang mempengaruhi performa mahasiswa.
---

### Rekomendasi Action Items

- Buat program remedial, tutoring, atau pendampingan untuk mahasiswa dengan nilai semester 1 yang rendah.
- Sediakan program beasiswa berbasis risiko dropout dan layanan konseling keuangan bagi Debtor.
- Evaluasi ulang sistem pembelajaran malam dengan memberi fleksibilitas akses materi atau hybrid class.
- Gunakan dashboard secara berkala untuk mendeteksi tren dropout berdasarkan jurusan, gender, dan faktor akademik.

---
