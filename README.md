---

# Proyek Analisis Data Produksi dan Penjualan

## Deskripsi

Proyek ini bertujuan untuk menganalisis dan memprediksi data produksi dan penjualan dari beberapa produk menggunakan berbagai teknik analisis statistik dan machine learning. Data yang dianalisis mencakup informasi tentang persediaan, produksi, dan penjualan produk dari minggu ke minggu. Analisis ini mencakup visualisasi tren, analisis korelasi, forecasting, pengujian hipotesis, clustering, dan modeling dengan machine learning.

## Tabel Data

Proyek ini menggunakan tiga set data utama:

1. **Persediaan**: Data mengenai jumlah produk yang tersedia.
2. **Produksi**: Data mengenai jumlah produk yang diproduksi.
3. **Penjualan**: Data mengenai jumlah produk yang terjual.

Struktur dari masing-masing file CSV adalah sebagai berikut:

- `Minggu`: Minggu ke-n (angka)
- `Produk A`, `Produk B`, `Produk C`, `Produk D`: Jumlah produk (angka)

## Langkah-Langkah Analisis

1. **Pembersihan Data**:
   - Mengimputasi nilai NaN pada data produksi menggunakan rata-rata.

2. **Deskriptif Statistik**:
   - Menampilkan deskriptif statistik untuk setiap dataset (persediaan, produksi, penjualan).

3. **Visualisasi Tren Waktu**:
   - Menggambar tren waktu untuk persediaan, produksi, dan penjualan.

4. **Analisis Korelasi**:
   - Menghitung dan memvisualisasikan korelasi antara produk dalam persediaan.
   - Menilai korelasi antara produksi dan penjualan untuk setiap produk.

5. **Analisis Moving Average**:
   - Menggunakan moving average untuk analisis tren pada data produksi.

6. **Forecasting**:
   - **Holt-Winters**: Peramalan untuk data produksi.
   - **ARIMA**: Peramalan untuk data penjualan.

7. **Pengujian Hipotesis**:
   - Menguji perbedaan rata-rata penjualan antara dua periode waktu.

8. **Clustering**:
   - Menggunakan K-Means untuk melakukan clustering pada data produksi.

9. **Modeling dengan Machine Learning**:
   - Membangun model regresi random forest untuk memprediksi produksi.

10. **Visualisasi Analisis Deskriptif**:
    - Membuat visualisasi untuk analisis deskriptif setiap produk.

## Analisis dan Hasil

- **Tren Waktu**: Tren untuk setiap produk menunjukkan pola musiman dan peningkatan atau penurunan secara umum dalam waktu.
- **Korelasi**: Analisis korelasi menunjukkan adanya hubungan antara produksi dan penjualan, namun dengan variasi yang signifikan untuk setiap produk.
- **Moving Average**: Moving average menunjukkan fluktuasi yang lebih halus dalam tren produksi.
- **Peramalan**:
  - **Holt-Winters**: Memberikan peramalan yang stabil untuk produksi dengan tren musiman.
  - **ARIMA**: Memberikan peramalan yang akurat untuk penjualan dengan mempertimbangkan fluktuasi musiman.
- **Pengujian Hipotesis**: Hasil pengujian hipotesis menunjukkan bahwa ada perbedaan signifikan antara dua periode penjualan.
- **Clustering**: Clustering mengidentifikasi kelompok produk dengan pola produksi yang mirip.
- **Model Machine Learning**: Model regresi random forest memberikan R-squared score yang baik, menunjukkan kemampuan model untuk memprediksi produksi.

## Interpretasi

- **Produksi dan Penjualan**: Ada potensi untuk meningkatkan akurasi peramalan dengan menyesuaikan model ARIMA dan Holt-Winters.
- **Clustering**: Kelompok produk yang teridentifikasi dapat membantu dalam strategi pengelolaan persediaan dan produksi yang lebih efisien.
- **Hipotesis**: Perbedaan dalam penjualan dapat digunakan untuk merencanakan promosi atau penyesuaian strategi pemasaran.

## Instalasi dan Penggunaan

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. **Instalasi Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Analisis**:
   - Pastikan data CSV berada di direktori yang sesuai.
   - Jalankan skrip Python untuk menghasilkan visualisasi dan hasil analisis:
     ```bash
     python script.py
     ```

