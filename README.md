# Analisis Produksi dan Penjualan Tahun 2023

## Deskripsi

Repositori ini berisi analisis data produksi dan penjualan untuk tahun 2023. Analisis ini mencakup berbagai aspek penting seperti biaya produksi, pendapatan, laba bersih, efisiensi produksi, kualitas produksi, kepuasan pelanggan, diskon, dan biaya penyimpanan. Data yang dianalisis mencakup informasi harian tentang produksi, penjualan, dan persediaan.

## Tabel Data

### Data Produksi
- **Produksi (Unit)**: Jumlah unit yang diproduksi setiap hari.
- **Biaya Produksi per Unit (IDR)**: Biaya untuk memproduksi setiap unit.
- **Total Biaya Produksi (IDR)**: Total biaya produksi untuk setiap hari.
- **Kualitas Produksi (%)**: Persentase kualitas dari produksi.
- **Efisiensi Produksi (%)**: Tingkat efisiensi produksi.

### Data Penjualan
- **Penjualan (Unit)**: Jumlah unit yang dijual setiap hari.
- **Harga Jual per Unit (IDR)**: Harga jual per unit.
- **Total Pendapatan (IDR)**: Total pendapatan dari penjualan setiap hari.
- **Kepuasan Pelanggan (1-10)**: Tingkat kepuasan pelanggan (skala 1-10).
- **Diskon (%)**: Persentase diskon yang diberikan.

### Data Persediaan
- **Persediaan Awal (Unit)**: Jumlah unit dalam persediaan awal.
- **Produksi (Unit)**: Jumlah unit yang diproduksi.
- **Penjualan (Unit)**: Jumlah unit yang dijual.
- **Persediaan Akhir (Unit)**: Jumlah unit dalam persediaan akhir.
- **Biaya Penyimpanan per Unit (IDR)**: Biaya penyimpanan per unit.
- **Total Biaya Penyimpanan (IDR)**: Total biaya penyimpanan untuk setiap hari.
- **Persentase Barang Rusak (%)**: Persentase barang yang rusak.

### Data Analisis
- **Total Pendapatan (IDR)**: Total pendapatan dari semua penjualan.
- **Total Biaya Produksi (IDR)**: Total biaya produksi.
- **Total Biaya Penyimpanan (IDR)**: Total biaya penyimpanan.
- **Laba Bersih (IDR)**: Laba bersih yang dihitung sebagai selisih antara total pendapatan, total biaya produksi, dan total biaya penyimpanan.

## Langkah-Langkah Analisis

1. **Pengumpulan dan Pembuatan Data**:
   - Data tanggal dihasilkan dari 1 Januari 2023 hingga 10 April 2023 (100 hari).
   - Data produksi, penjualan, dan persediaan dihasilkan secara acak menggunakan distribusi normal dan uniform.

2. **Persiapan Data**:
   - Data diubah menjadi DataFrame pandas.
   - Data kepuasan pelanggan diubah skala dari 70-100 menjadi 1-10.

3. **Analisis Laba Bersih**:
   - Menghitung laba bersih berdasarkan total pendapatan, total biaya produksi, dan total biaya penyimpanan.

4. **Visualisasi Data**:
   - **Produksi dan Penjualan**: Plot jumlah unit produksi dan penjualan setiap hari.
   - **Biaya Produksi dan Pendapatan**: Plot total biaya produksi dan total pendapatan.
   - **Laba Bersih**: Plot tren laba bersih.
   - **Efisiensi dan Kualitas Produksi**: Plot efisiensi dan kualitas produksi.
   - **Kepuasan Pelanggan dan Diskon**: Plot kepuasan pelanggan dan diskon.
   - **Total Biaya Produksi dan Penyimpanan**: Diagram batang untuk biaya produksi dan penyimpanan.
   - **Heatmap Kualitas vs Efisiensi Produksi**: Heatmap korelasi antara kualitas dan efisiensi produksi.
   - **Histogram Biaya Produksi**: Histogram distribusi total biaya produksi.
   - **Scatter Plot Kualitas vs Efisiensi**: Scatter plot antara kualitas dan efisiensi produksi.
   - **Box Plot Diskon vs Kepuasan**: Box plot diskon berdasarkan kepuasan pelanggan.
   - **Line Plot Laba Bersih dan Pendapatan**: Plot garis laba bersih dan total pendapatan.
   - **Pie Chart Distribusi Diskon**: Pie chart distribusi diskon.
   - **Persediaan Awal dan Persediaan Akhir**: Plot perbandingan persediaan awal dan akhir.

## Hasil dan Interpretasi

- **Produksi dan Penjualan**: Analisis menunjukkan pola fluktuasi dalam produksi dan penjualan. Pengelolaan yang lebih baik diperlukan untuk mengurangi ketidaksesuaian ini.
- **Biaya Produksi dan Pendapatan**: Total biaya produksi dan pendapatan dipantau untuk memastikan profitabilitas yang baik. Penurunan biaya produksi atau peningkatan harga jual mungkin diperlukan jika pendapatan tidak mencukupi.
- **Laba Bersih**: Tren laba bersih menunjukkan bulan-bulan di mana perusahaan mendapatkan keuntungan dan kerugian. Penyesuaian strategi mungkin diperlukan untuk meningkatkan laba bersih.
- **Efisiensi dan Kualitas Produksi**: Korelasi antara efisiensi dan kualitas produksi menunjukkan area untuk peningkatan. Peningkatan pelatihan atau pengubahaan proses mungkin diperlukan.
- **Kepuasan Pelanggan dan Diskon**: Data menunjukkan hubungan antara kepuasan pelanggan dan diskon. Diskon yang lebih tinggi tidak selalu meningkatkan kepuasan pelanggan secara signifikan.
- **Biaya Produksi dan Penyimpanan**: Analisis biaya menunjukkan potensi penghematan dalam biaya produksi dan penyimpanan yang bisa dilakukan untuk meningkatkan profitabilitas.
- **Heatmap**: Korelasi antara kualitas dan efisiensi produksi membantu mengidentifikasi trade-off dalam produksi.
- **Histogram dan Scatter Plot**: Menyediakan wawasan tentang distribusi biaya produksi dan hubungan antara kualitas dan efisiensi produksi.
- **Box Plot dan Pie Chart**: Menilai distribusi diskon dan dampaknya terhadap kepuasan pelanggan.
- **Line Plot**: Menunjukkan tren Laba Bersih dan Total Pendapatan serta distribusi diskon yang mungkin mempengaruhi penjualan.
- **Persediaan Awal dan Akhir**: Membantu memantau perubahan dalam stok dan memprediksi kebutuhan produksi.

---

## Gambar
![Bar_Produksi_dan_Penjualan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/7f94dc8a-6ba4-4f5c-b9f8-3961845ea125)
![Bar_Biaya_Produksi_dan_Pendapatan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/22525935-759e-4b17-a85a-57fcd9e953f7)
![Analisis_Laba_Bersih](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/1ca8bdfa-10fa-40d8-a240-40c36c257014)
![Efisiensi_dan_Kualitas_Produksi](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/b3063ea1-c6ce-44ba-9314-03117402ad4e)
![Kepuasan_dan_Diskon](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/34bf4bde-695e-4647-b678-814fe8c584e7)
![Biaya_Produksi_dan_Pendapatan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/1a9540b8-9345-4fe9-8e40-d4b15a1615b9)
![Heatmap_Kualitas_Efisiensi](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/04fa168f-162b-4a83-bf35-0d45ff234cb6)
![Histogram_Biaya_Produksi](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/89413f20-715f-4c21-9787-be78b74d27f7)
![Scatter_Kualitas_Efisiensi](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/f7a69046-445a-4ada-b7ce-92c491f00c4b)
![BoxPlot_Diskon_Kepuasan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/bb7bab76-0982-4c0b-9878-e364001a10d1)
![Tren_Laba_Pendapatan](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/a22839d2-0bcf-4a53-9687-d2cabdb3cde3)
![Pie_Penjualan_Diskon](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/dd9e4e68-646e-45e2-8a78-d1844f06fe8c)
![PersediaanAwal_vs_PersediaanAkhir](https://github.com/RamdhaniLaksonoAlimnoor/AnalisisData_Ramdhani/assets/167221588/02ae2de8-cb43-4898-813c-65798172411a)
