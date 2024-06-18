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

---

## Gambar
![tren_produksi](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/afc3bf6d-2015-4c88-8134-f1a163e4a529)
![tren_persediaan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/af5b8827-5c80-4cfc-a449-6b6bcd364657)
![tren_penjualan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/5887d593-43c4-487f-96bc-f88915486960)
![korelasi_persediaan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/d3ef91ed-4058-4597-a20b-4f56244c7013)
![korelasi_produksi_penjualan_Produk A](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/82b60fac-5cc7-4676-8cb8-94c2b87a6e02)
![korelasi_produksi_penjualan_Produk B](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/810b8f69-530b-40d4-bc76-02491a5a9f9d)
![korelasi_produksi_penjualan_Produk C](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/445adf00-418d-4425-92b7-13a2167b1d1c)
![korelasi_produksi_penjualan_Produk D](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/a17acf4d-af0b-4c4c-89ca-6a49408cdc2d)
![moving_average_produksi](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/f46e95c3-ee0b-4f32-9491-e3eefed8037c)
![forecast_arima_all_products](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/f896b22a-acca-462d-ac31-43530141948f)
![forecast_holt_winters_all](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/64568dc6-7606-49b9-93f1-3f0ed7e94042)
![descriptive_stats_Produk A](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/331ec450-15d5-4cbb-8017-c1d07150ad3f)
![descriptive_stats_Produk B](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/bc837377-a57e-4692-a5ed-02b15fee173b)
![descriptive_stats_Produk C](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/caf6abae-c052-41a2-8b08-5c86154409ab)
![descriptive_stats_Produk D](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/7856aaa8-777c-4027-9973-3491f5afce99)
![clustering_produk](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_AktivitasBisnis_100hari/assets/167221588/fed360f3-69ce-40d1-aba5-042b21917b42)


