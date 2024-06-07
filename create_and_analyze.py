import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Menghasilkan tanggal dari 1 Januari 2023 hingga 10 April 2023 (100 hari)
tanggal = pd.date_range(start="2023-01-01", periods=100)

# Menghasilkan data produksi
np.random.seed(0)
produksi_unit = np.random.randint(500, 700, size=len(tanggal))
biaya_produksi_per_unit = np.random.randint(4500, 5000, size=len(tanggal))
total_biaya_produksi = produksi_unit * biaya_produksi_per_unit
kualitas_produksi = np.random.randint(70, 100, size=len(tanggal))
efisiensi_produksi = np.random.randint(80, 90, size=len(tanggal))

produksi_data = {
    "Tanggal": tanggal,
    "Produksi (Unit)": produksi_unit,
    "Biaya Produksi per Unit (IDR)": biaya_produksi_per_unit,
    "Total Biaya Produksi (IDR)": total_biaya_produksi,
    "Kualitas Produksi (%)": kualitas_produksi,
    "Efisiensi Produksi (%)": efisiensi_produksi
}

# Menghasilkan data penjualan
penjualan_unit = np.random.randint(450, 650, size=len(tanggal))
harga_jual_per_unit = np.random.randint(6700, 7000, size=len(tanggal))
total_pendapatan = penjualan_unit * harga_jual_per_unit
kepuasan_pelanggan = np.random.randint(70, 100, size=len(tanggal))
diskon = np.random.randint(0, 10, size=len(tanggal))

penjualan_data = {
    "Tanggal": tanggal,
    "Penjualan (Unit)": penjualan_unit,
    "Harga Jual per Unit (IDR)": harga_jual_per_unit,
    "Total Pendapatan (IDR)": total_pendapatan,
    "Kepuasan Pelanggan (%)": kepuasan_pelanggan,
    "Diskon (%)": diskon
}

# Mengubah skala Kepuasan Pelanggan dari 70-100 menjadi 1-10
penjualan_df = pd.DataFrame(penjualan_data)
penjualan_df["Kepuasan Pelanggan (1-10)"] = ((penjualan_df["Kepuasan Pelanggan (%)"] - 70) / 30) * 9 + 1
penjualan_df = penjualan_df.drop(columns=["Kepuasan Pelanggan (%)"])
penjualan_data = penjualan_df.to_dict(orient="list")

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

# Visualisasi Data: Produksi dan Penjualan
plt.figure(figsize=(10, 6))
plt.plot(df_produksi["Tanggal"], df_produksi["Produksi (Unit)"], label="Produksi (Unit)", color="blue", linestyle='-', marker='o')
plt.plot(df_penjualan["Tanggal"], df_penjualan["Penjualan (Unit)"], label="Penjualan (Unit)", color="green", linestyle='--', marker='x')
plt.title("Produksi dan Penjualan Tahun 2023", fontsize=14)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("Jumlah (Unit)", fontsize=12)
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("Produksi_dan_Penjualan.png")
plt.show()

# Visualisasi Data: Biaya Produksi dan Pendapatan
plt.figure(figsize=(10, 6))
plt.plot(df_produksi["Tanggal"], df_produksi["Total Biaya Produksi (IDR)"], linestyle='--', label="Total Biaya Produksi (IDR)", color="red", marker='^')
plt.plot(df_penjualan["Tanggal"], df_penjualan["Total Pendapatan (IDR)"], linestyle=':', label="Total Pendapatan (IDR)", color="purple", marker='s')
plt.title("Total Biaya Produksi dan Pendapatan Tahun 2023", fontsize=14)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("IDR", fontsize=12)
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("Biaya_Produksi_dan_Pendapatan.png")
plt.show()

# Visualisasi Data: Laba Bersih
plt.figure(figsize=(10, 6))
plt.plot(df_analisis["Tanggal"], df_analisis["Laba Bersih (IDR)"], marker='o', linestyle='-', color="brown", label="Laba Bersih (IDR)")
plt.title("Analisis Laba Bersih Tahun 2023", fontsize=14)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("Laba Bersih (IDR)", fontsize=12)
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("Analisis_Laba_Bersih.png")
plt.show()

# Visualisasi Data: Efisiensi Produksi dan Kualitas Produksi
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel("Tanggal", fontsize=12)
ax1.set_ylabel("Efisiensi Produksi (%)", color="tab:blue", fontsize=12)
ax1.plot(df_produksi["Tanggal"], df_produksi["Efisiensi Produksi (%)"], color="tab:blue", linestyle='-', marker='o', label="Efisiensi Produksi (%)")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Kualitas Produksi (%)", color="tab:red", fontsize=12)
ax2.plot(df_produksi["Tanggal"], df_produksi["Kualitas Produksi (%)"], color="tab:red", linestyle='--', marker='x', label="Kualitas Produksi (%)")
ax2.tick_params(axis="y", labelcolor="tab:red")

fig.tight_layout()
plt.title("Efisiensi Produksi dan Kualitas Produksi Tahun 2023", fontsize=14)
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig("Efisiensi_dan_Kualitas_Produksi.png")
plt.show()

# Visualisasi Data: Kepuasan Pelanggan (Skala 1-10) dan Diskon
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel("Tanggal", fontsize=12)
ax1.set_ylabel("Kepuasan Pelanggan (1-10)", color="tab:blue", fontsize=12)
ax1.plot(df_penjualan["Tanggal"], df_penjualan["Kepuasan Pelanggan (1-10)"], color="tab:blue", linestyle='-', marker='s', label="Kepuasan Pelanggan (1-10)")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Diskon (%)", color="tab:red", fontsize=12)
ax2.plot(df_penjualan["Tanggal"], df_penjualan["Diskon (%)"], color="tab:red", linestyle='--', marker='x', label="Diskon (%)")
ax2.tick_params(axis="y", labelcolor="tab:red")

fig.tight_layout()
plt.title("Kepuasan Pelanggan dan Diskon Tahun 2023", fontsize=14)
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig("Kepuasan_dan_Diskon.png")
plt.show()

# Visualisasi Diagram Batang: Total Biaya Produksi dan Biaya Penyimpanan
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(df_analisis["Tanggal"]))

plt.bar(index, df_analisis["Total Biaya Produksi (IDR)"], bar_width, label='Total Biaya Produksi (IDR)', color='blue')
plt.bar(index + bar_width, df_analisis["Total Biaya Penyimpanan (IDR)"], bar_width, label='Total Biaya Penyimpanan (IDR)', color='red')

plt.xlabel('Tanggal', fontsize=12)
plt.ylabel('IDR', fontsize=12)
plt.title('Total Biaya Produksi dan Penyimpanan', fontsize=14)
plt.xticks(index + bar_width / 2, df_analisis["Tanggal"], rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("Diagram_Batang_Biaya.png")
plt.show()

# Visualisasi Heatmap: Kualitas Produksi vs Efisiensi Produksi
heatmap_data = df_produksi[['Kualitas Produksi (%)', 'Efisiensi Produksi (%)']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Heatmap Kualitas Produksi vs Efisiensi Produksi", fontsize=14)
plt.tight_layout()
plt.savefig("Heatmap_Kualitas_Efisiensi.png")
plt.show()

# Visualization: Histogram of Total Production Costs
plt.figure(figsize=(10, 6))
plt.hist(df_produksi["Total Biaya Produksi (IDR)"], bins=30, color='orange', edgecolor='black')
plt.title('Distribusi Total Biaya Produksi', fontsize=14)
plt.xlabel('Total Biaya Produksi (IDR)', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("Histogram_Biaya_Produksi.png")
plt.show()

# Visualization: Scatter Plot of Production Quality vs Efficiency
plt.figure(figsize=(10, 6))
plt.scatter(df_produksi["Kualitas Produksi (%)"], df_produksi["Efisiensi Produksi (%)"], color='purple')
plt.title('Kualitas Produksi vs Efisiensi Produksi', fontsize=14)
plt.xlabel('Kualitas Produksi (%)', fontsize=12)
plt.ylabel('Efisiensi Produksi (%)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("Scatter_Kualitas_Efisiensi.png")
plt.show()

# Visualization: Box Plot of Discount Based on Customer Satisfaction
plt.figure(figsize=(10, 6))
sns.boxplot(x="Kepuasan Pelanggan (1-10)", y="Diskon (%)", data=df_penjualan, palette="Set2")
plt.title('Diskon Berdasarkan Kepuasan Pelanggan', fontsize=14)
plt.xlabel('Kepuasan Pelanggan (1-10)', fontsize=12)
plt.ylabel('Diskon (%)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("BoxPlot_Diskon_Kepuasan.png")
plt.show()

# Visualization: Line Plot of Net Profit and Total Revenue
plt.figure(figsize=(10, 6))
plt.plot(df_analisis["Tanggal"], df_analisis["Laba Bersih (IDR)"], marker='o', linestyle='-', color="brown", label="Laba Bersih (IDR)")
plt.plot(df_analisis["Tanggal"], df_analisis["Total Pendapatan (IDR)"], marker='s', linestyle='--', color="purple", label="Total Pendapatan (IDR)")
plt.title("Tren Laba Bersih dan Total Pendapatan Tahun 2023", fontsize=14)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("IDR", fontsize=12)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig("Tren_Laba_Pendapatan.png")
plt.show()

# Visualization: Pie Chart of Discount Distribution
plt.figure(figsize=(10, 6))
penjualan_diskon_counts = df_penjualan['Diskon (%)'].value_counts()
plt.pie(penjualan_diskon_counts, labels=penjualan_diskon_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
plt.title('Proporsi Penjualan Menurut Diskon (%)', fontsize=14)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig("Pie_Penjualan_Diskon.png")
plt.show()



