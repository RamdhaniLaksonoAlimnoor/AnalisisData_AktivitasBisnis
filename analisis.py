import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Membaca data dari CSV
df_persediaan = pd.read_csv('persediaan.csv')
df_produksi = pd.read_csv('produksi.csv')
df_penjualan = pd.read_csv('penjualan.csv')

# Mengatasi nilai NaN dengan mengimputasi dengan mean
imputer = SimpleImputer(strategy='mean')
df_produksi_imputed = pd.DataFrame(imputer.fit_transform(df_produksi.drop(columns=['Minggu'])), columns=df_produksi.columns[1:])
df_produksi_imputed['Minggu'] = df_produksi['Minggu']

# Deskriptif Statistik
print("\nDeskriptif Statistik Persediaan:")
print(df_persediaan.describe())
print("\nDeskriptif Statistik Produksi:")
print(df_produksi.describe())
print("\nDeskriptif Statistik Penjualan:")
print(df_penjualan.describe())

# Visualisasi Tren Waktu
def plot_trend(data, columns, title, filename):
    plt.figure(figsize=(14, 7))
    for col in columns:
        plt.plot(data['Minggu'], data[col], label=f'{title} {col}')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

# Tren Persediaan
plot_trend(df_persediaan, ['Produk A', 'Produk B', 'Produk C', 'Produk D'], 'Tren Persediaan', 'tren_persediaan.png')

# Tren Produksi
plot_trend(df_produksi, ['Produk A', 'Produk B', 'Produk C', 'Produk D'], 'Tren Produksi', 'tren_produksi.png')

# Tren Penjualan
plot_trend(df_penjualan, ['Produk A', 'Produk B', 'Produk C', 'Produk D'], 'Tren Penjualan', 'tren_penjualan.png')

# Analisis Korelasi
correlation_matrix = df_persediaan.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Korelasi antara Produk Persediaan')
plt.savefig('korelasi_persediaan.png')
plt.show()

# Korelasi antara Produksi dan Penjualan
for produk in ['Produk A', 'Produk B', 'Produk C', 'Produk D']:
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=df_produksi[produk], y=df_penjualan[produk])
    plt.title(f'Korelasi antara Produksi dan Penjualan untuk {produk}')
    plt.xlabel('Produksi')
    plt.ylabel('Penjualan')
    plt.savefig(f'korelasi_produksi_penjualan_{produk}.png')
    plt.show()

# Menggunakan Moving Average untuk Analisis Tren
plt.figure(figsize=(10, 6))
for produk in ['Produk A', 'Produk B', 'Produk C', 'Produk D']:
    df_produksi[f'{produk}_MA'] = df_produksi[produk].rolling(window=5).mean()
    plt.plot(df_produksi['Minggu'], df_produksi[produk], label=f'Produksi {produk}')
    plt.plot(df_produksi['Minggu'], df_produksi[f'{produk}_MA'], label=f'{produk} Moving Average', linestyle='--')
plt.xlabel('Minggu')
plt.ylabel('Jumlah')
plt.title('Tren Produksi dengan Moving Average')
plt.legend()
plt.grid(True)
plt.savefig('moving_average_produksi.png')
plt.show()

# Forecasting dengan Holt-Winters
def forecast_with_holt_winters(data, product):
    try:
        model = ExponentialSmoothing(data[product], trend='add', seasonal=None, seasonal_periods=52).fit()
        forecast = model.forecast(steps=10)
    except ValueError as e:
        print(f"Error forecasting {product}: {e}")
        forecast = None
    return forecast

# Holt-Winters Forecasting
fig, axs = plt.subplots(2, 2, figsize=(18, 12))
produk_list = ['Produk A', 'Produk B', 'Produk C', 'Produk D']
for i, produk in enumerate(produk_list):
    forecast_hw = forecast_with_holt_winters(df_produksi, produk)
    axs[i//2, i%2].plot(df_produksi['Minggu'], df_produksi[produk], label='Produksi Sejarah')
    if forecast_hw is not None:
        axs[i//2, i%2].plot(range(53, 63), forecast_hw, label='Peramalan Holt-Winters', linestyle='--')
    axs[i//2, i%2].set_title(f'Peramalan Produksi untuk {produk}')
    axs[i//2, i%2].set_xlabel('Minggu')
    axs[i//2, i%2].set_ylabel('Jumlah')
    axs[i//2, i%2].legend()
    axs[i//2, i%2].grid(True)
plt.tight_layout()
plt.savefig('forecast_holt_winters_all.png')
plt.show()

# Forecasting dengan ARIMA untuk Penjualan
def forecast_with_arima(data, product, order=(1, 1, 1)):
    model = ARIMA(data[product], order=order)
    model_fit = model.fit()
    forecast = model_fit.get_forecast(steps=10)
    forecast_mean = forecast.predicted_mean
    return forecast_mean

# Gabungkan ARIMA forecast dalam satu plot
plt.figure(figsize=(14, 7))
for produk in ['Produk A', 'Produk B', 'Produk C', 'Produk D']:
    forecast = forecast_with_arima(df_penjualan, produk)
    plt.plot(df_penjualan['Minggu'], df_penjualan[produk], label=f'Penjualan Sejarah {produk}')
    plt.plot(range(53, 63), forecast, label=f'Peramalan ARIMA {produk}', linestyle='--')
plt.xlabel('Minggu')
plt.ylabel('Jumlah')
plt.title('Peramalan Penjualan dengan ARIMA untuk Semua Produk')
plt.legend()
plt.grid(True)
plt.savefig('forecast_arima_all_products.png')
plt.show()

# Pengujian Hipotesis
penjualan_periode1 = df_penjualan.loc[df_penjualan['Minggu'] <= 26, 'Produk A']
penjualan_periode2 = df_penjualan.loc[df_penjualan['Minggu'] > 26, 'Produk A']

t_stat, p_value = stats.ttest_ind(penjualan_periode1, penjualan_periode2)
print(f'T-Statistik: {t_stat}, P-Value: {p_value}')

# Clustering untuk semua produk
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_produksi_imputed.drop(columns=['Minggu']))

n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(data_scaled)
df_produksi_imputed['Cluster'] = clusters

# Visualisasi hasil clustering
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df_produksi_imputed, x='Produk A', y='Produk B', hue='Cluster', palette='viridis', s=100, alpha=0.6)
plt.title('Hasil Clustering Produk')
plt.xlabel('Produk A')
plt.ylabel('Produk B')
plt.legend(title='Cluster')
plt.grid(True)
plt.savefig('clustering_produk.png')
plt.show()

# Modeling dengan Machine Learning
X = df_produksi_imputed.drop(columns=['Minggu', 'Produk A'])
y = df_produksi_imputed['Produk A']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f'Model R-squared: {score}')

# Visualisasi Analisis Deskriptif
def plot_descriptive_stats(data, product):
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 2, 1)
    sns.histplot(data[product], kde=True)
    plt.title(f'Histogram {product}')
    
    plt.subplot(2, 2, 2)
    sns.boxplot(x=data[product])
    plt.title(f'Boxplot {product}')
    
    stats_summary = data[product].describe()
    plt.subplot(2, 2, 3)
    plt.table(cellText=[stats_summary.values], colLabels=stats_summary.index, cellLoc='center', loc='center')
    plt.axis('off')
    plt.title(f'Descriptive Statistics {product}')
    
    plt.subplot(2, 2, 4)
    sns.scatterplot(x=data.index, y=data[product])
    plt.title(f'Scatter Plot {product}')
    
    plt.tight_layout()
    plt.savefig(f'descriptive_stats_{product}.png')
    plt.show()

# Menggambar visualisasi deskriptif untuk setiap produk
for produk in ['Produk A', 'Produk B', 'Produk C', 'Produk D']:
    plot_descriptive_stats(df_produksi, produk)
