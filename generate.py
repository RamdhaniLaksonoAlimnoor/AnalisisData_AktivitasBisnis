import pandas as pd
import numpy as np

# Mengatur parameter
minggu = list(range(1, 53))
produk = ['Produk A', 'Produk B', 'Produk C', 'Produk D']

# Fungsi untuk generate data
def generate_data(start, end):
    return [int(np.random.normal(loc=400, scale=20)) for _ in range(start, end)]

# Data persediaan
persediaan_data = {
    'Minggu': minggu,
    'Produk A': generate_data(1, 53),
    'Produk B': generate_data(1, 53),
    'Produk C': generate_data(1, 53),
    'Produk D': generate_data(1, 53)
}
df_persediaan = pd.DataFrame(persediaan_data)
df_persediaan.to_csv('persediaan.csv', index=False)

# Data produksi
produksi_data = {
    'Minggu': minggu,
    'Produk A': generate_data(1, 53),
    'Produk B': generate_data(1, 53),
    'Produk C': generate_data(1, 53),
    'Produk D': generate_data(1, 53)
}
df_produksi = pd.DataFrame(produksi_data)
df_produksi.to_csv('produksi.csv', index=False)

# Data penjualan
penjualan_data = {
    'Minggu': minggu,
    'Produk A': generate_data(1, 53),
    'Produk B': generate_data(1, 53),
    'Produk C': generate_data(1, 53),
    'Produk D': generate_data(1, 53)
}
df_penjualan = pd.DataFrame(penjualan_data)
df_penjualan.to_csv('penjualan.csv', index=False)

print("File CSV berhasil dibuat!")
