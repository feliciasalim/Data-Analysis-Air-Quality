import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def load_data():
    file_id = "1smdCfBAvwriSSAHFGyCi-4qQHKJzYvas"
    link = f"https://drive.google.com/uc?id={file_id}"
    df = pd.read_csv(link) 
    df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]], errors='coerce')  
    return df

df = load_data()

with st.sidebar:
    st.image("https://drive.google.com/file/d/1K2w6ESCR5pO8CaHPp1uJa6zDX1KoJ02S/view")
    st.title("Dashboard Felicia Salim")
    st.subheader("Pilih Stasiun:")
    station = st.selectbox("Stasiun", df["station"].unique())

filter = df[df["station"] == station]

st.title("Analisis Dataset 'Air Quality' :sparkles:")
st.write("<hr style='border: 0.2px solid white; margin: 2px 0;'>", unsafe_allow_html=True)


st.subheader("Tren Polusi")

pilihan = st.selectbox("Pilih", ["Tahun", "Bulan", "Hari", "Jam"])

if pilihan == "Tahun":
    mean = filter.groupby("year")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    x_label = "Tahun"
    x_data = mean["year"]
elif pilihan == "Bulan":
    mean = filter.groupby("month")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    x_label = "Bulan"
    x_data = mean["month"]
elif pilihan == "Hari":
    mean = filter.groupby("day")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    x_label = "Hari"
    x_data = mean["day"]
else:
    mean = filter.groupby("hour")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    x_label = "Jam"
    x_data = mean["hour"]

fig, axes = plt.subplots(3, 2, figsize=(15, 20))
fig.suptitle(f"Rata-rata Polutan berdasarkan {x_label}", fontsize=24)
polutan = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
colors = ['r', 'g', 'g', 'r', 'r', 'g']

for ax, polutan, color in zip(axes.flatten(), polutan, colors):
    ax.plot(x_data, mean[polutan], marker='o', linestyle='-', color=color)
    ax.set_xlabel(x_label)
    ax.set_ylabel(f"{polutan}")
    ax.set_title(f"{polutan}")
st.pyplot(fig)

st.subheader("Matriks Korelasi")
plt.figure(figsize=(8, 6))
sns.heatmap(filter[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].corr(), annot=True, cmap="Reds")
st.pyplot(plt)

st.subheader("Tren Faktor Cuaca")
cuaca = st.selectbox("Pilih", ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"])

def plot_cuaca(df, parameter):
    cuaca_mean = df.groupby("year")[parameter].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(cuaca_mean["year"], cuaca_mean[parameter], marker='o', linestyle='-')
    plt.xlabel("Tahun")
    plt.ylabel(f"{parameter} Nilai")
    plt.title(f"{parameter} Tren Cuaca per Tahun")
    st.pyplot(plt)

plot_cuaca(filter, cuaca)


