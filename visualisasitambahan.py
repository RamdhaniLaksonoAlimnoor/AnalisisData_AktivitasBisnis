import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Menghasilkan tanggal dari 1 Januari 2023 hingga 31 Desember 2023
tanggal = pd.date_range(start="2023-01-01", end="2023-12-31")

# Menghasilkan data produksi
np.random.seed(0)
produksi_unit = np.random.randint(500, 700, size=len(tanggal))
biaya_produksi_per_unit = np.random.randint(4500, 5000, size=len(tanggal))
total_biaya_produksi = produksi_unit * biaya_produksi_per_unit
kualitas_produksi = np.random.randint(7, 10, size=len(tanggal))
efisiensi_produksi = np.random.randint(80, 90, size=len(tanggal))

produksi_data = {
    "Tanggal": tanggal,
    "Produksi (Unit)": produksi_unit,
    "Biaya Produksi per Unit (IDR)": biaya_produksi_per_unit,
    "Total Biaya Produksi (IDR)": total_biaya_produksi,
    "Kualitas Produksi (Skala 1-10)": kualitas_produksi,
    "Efisiensi Produksi (%)": efisiensi_produksi
}

# Menghasilkan data penjualan
penjualan_unit = np.random.randint(450, 650, size=len(tanggal))
harga_jual_per_unit = np.random.randint(6700, 7000, size=len(tanggal))
total_pendapatan = penjualan_unit * harga_jual_per_unit
kepuasan_pelanggan = np.random.randint(7, 10, size=len(tanggal))
diskon = np.random.randint(0, 10, size=len(tanggal))

penjualan_data = {
    "Tanggal": tanggal,
    "Penjualan (Unit)": penjualan_unit,
    "Harga Jual per Unit (IDR)": harga_jual_per_unit,
    "Total Pendapatan (IDR)": total_pendapatan,
    "Kepuasan Pelanggan (Skala 1-10)": kepuasan_pelanggan,
    "Diskon (%)": diskon
}

# Menghasilkan data persediaan
persediaan_awal = 2000
persediaan_awal_list = [persediaan_awal]
biaya_penyimpanan_per_unit = 200
persentase_barang_rusak = np.random.uniform(1, 3, size=len(tanggal))

for i in range(1, len(tanggal)):
    persediaan_awal = persediaan_awal_list[-1] + produksi_unit[i-1] - penjualan_unit[i-1]
    persediaan_awal_list.append(persediaan_awal)

persediaan_akhir = np.array(persediaan_awal_list) + produksi_unit - penjualan_unit
total_biaya_penyimpanan = persediaan_akhir * biaya_penyimpanan_per_unit

persediaan_data = {
    "Tanggal": tanggal,
    "Persediaan Awal (Unit)": persediaan_awal_list,
    "Produksi (Unit)": produksi_unit,
    "Penjualan (Unit)": penjualan_unit,
    "Persediaan Akhir (Unit)": persediaan_akhir,
    "Biaya Penyimpanan per Unit (IDR)": biaya_penyimpanan_per_unit,
    "Total Biaya Penyimpanan (IDR)": total_biaya_penyimpanan,
    "Persentase Barang Rusak (%)": persentase_barang_rusak
}

# Membuat DataFrame
df_produksi = pd.DataFrame(produksi_data)
df_penjualan = pd.DataFrame(penjualan_data)
df_persediaan = pd.DataFrame(persediaan_data)

# Menyimpan DataFrame ke file CSV
df_produksi.to_csv('produksi.csv', index=False)
df_penjualan.to_csv('penjualan.csv', index=False)
df_persediaan.to_csv('persediaan.csv', index=False)

print("File CSV berhasil dibuat!")

# Analisis Laba Bersih
df_analisis = pd.DataFrame({
    "Tanggal": df_produksi["Tanggal"],
    "Total Pendapatan (IDR)": df_penjualan["Total Pendapatan (IDR)"],
    "Total Biaya Produksi (IDR)": df_produksi["Total Biaya Produksi (IDR)"],
    "Total Biaya Penyimpanan (IDR)": df_persediaan["Total Biaya Penyimpanan (IDR)"],
    "Laba Bersih (IDR)": df_penjualan["Total Pendapatan (IDR)"] - df_produksi["Total Biaya Produksi (IDR)"] - df_persediaan["Total Biaya Penyimpanan (IDR)"]
})

# Menyimpan DataFrame analisis ke file CSV
df_analisis.to_csv('analisis.csv', index=False)

# Visualisasi Data
plt.figure(figsize=(16, 10))

# Plot Produksi dan Penjualan
plt.plot(df_produksi["Tanggal"], df_produksi["Produksi (Unit)"], label="Produksi (Unit)", color="blue")
plt.plot(df_penjualan["Tanggal"], df_penjualan["Penjualan (Unit)"], label="Penjualan (Unit)", color="green")

# Plot Biaya Produksi dan Pendapatan
plt.plot(df_produksi["Tanggal"], df_produksi["Total Biaya Produksi (IDR)"], linestyle='--', label="Total Biaya Produksi (IDR)", color="red")
plt.plot(df_penjualan["Tanggal"], df_penjualan["Total Pendapatan (IDR)"], linestyle='--', label="Total Pendapatan (IDR)", color="purple")

# Plot Persediaan Akhir
plt.bar(df_persediaan["Tanggal"], df_persediaan["Persediaan Akhir (Unit)"], alpha=0.5, label="Persediaan Akhir (Unit)", color="orange")

# Menambahkan judul dan label
plt.title("Analisis Produksi, Penjualan, Biaya, dan Persediaan Tahun 2023")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah (Unit) / IDR")

# Menambahkan grid dan legenda
plt.grid(True)
plt.legend()

# Menampilkan plot
plt.tight_layout()
plt.show()

# Menampilkan analisis laba bersih
print(df_analisis)

# Plot Laba Bersih
plt.figure(figsize=(16, 6))
plt.plot(df_analisis["Tanggal"], df_analisis["Laba Bersih (IDR)"], marker='o', label="Laba Bersih (IDR)", color="brown")
plt.title("Analisis Laba Bersih Tahun 2023")
plt.xlabel("Tanggal")
plt.ylabel("Laba Bersih (IDR)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Visualisasi Tambahan

# Plot Persediaan Awal vs Persediaan Akhir
plt.figure(figsize=(16, 6))
plt.plot(df_persediaan["Tanggal"], df_persediaan["Persediaan Awal (Unit)"], label="Persediaan Awal (Unit)", color="blue")
plt.plot(df_persediaan["Tanggal"], df_persediaan["Persediaan Akhir (Unit)"], label="Persediaan Akhir (Unit)", color="green")
plt.title("Persediaan Awal vs Persediaan Akhir Tahun 2023")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah (Unit)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Efisiensi Produksi dan Kualitas Produksi
fig, ax1 = plt.subplots(figsize=(16, 6))

ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Efisiensi Produksi (%)", color="tab:blue")
ax1.plot(df_produksi["Tanggal"], df_produksi["Efisiensi Produksi (%)"], color="tab:blue", label="Efisiensi Produksi (%)")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Kualitas Produksi (Skala 1-10)", color="tab:red")
ax2.plot(df_produksi["Tanggal"], df_produksi["Kualitas Produksi (Skala 1-10)"], color="tab:red", label="Kualitas Produksi (Skala 1-10)")
ax2.tick_params(axis="y", labelcolor="tab:red")

fig.tight_layout()
plt.title("Efisiensi Produksi dan Kualitas Produksi Tahun 2023")
plt.show()

# Plot Kepuasan Pelanggan dan Diskon
fig, ax1 = plt.subplots(figsize=(16, 6))

ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Kepuasan Pelanggan (Skala 1-10)", color="tab:blue")
ax1.plot(df_penjualan["Tanggal"], df_penjualan["Kepuasan Pelanggan (Skala 1-10)"], color="tab:blue", label="Kepuasan Pelanggan (Skala 1-10)")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Diskon (%)", color="tab:green")
ax2.plot(df_penjualan["Tanggal"], df_penjualan["Diskon (%)"], color="tab:green", label="Diskon (%)")
ax2.tick_params(axis="y", labelcolor="tab:green")

fig.tight_layout()
plt.title("Kepuasan Pelanggan dan Diskon Tahun 2023")
plt.show()

# Plot Total Biaya Penyimpanan vs Persentase Barang Rusak
fig, ax1 = plt.subplots(figsize=(16, 6))

ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Total Biaya Penyimpanan (IDR)", color="tab:blue")
ax1.plot(df_persediaan["Tanggal"], df_persediaan["Total Biaya Penyimpanan (IDR)"], color="tab:blue", label="Total Biaya Penyimpanan (IDR)")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Persentase Barang Rusak (%)", color="tab:red")
ax2.plot(df_persediaan["Tanggal"], df_persediaan["Persentase Barang Rusak (%)"], color="tab:red", label="Persentase Barang Rusak (%)")
ax2.tick_params(axis="y", labelcolor="tab:red")

fig.tight_layout()
plt.title("Total Biaya Penyimpanan vs Persentase Barang Rusak Tahun 2023")
plt.show()
