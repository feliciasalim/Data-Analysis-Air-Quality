import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

df = pd.read_csv("dashboard/all_data.csv")  

with st.sidebar:
    st.image("dashboard/pic.jpg")
    st.title("Dashboard Felicia Salim")
    st.subheader("Pilih Stasiun:")
    station = st.selectbox(
        label = "Stasiun", 
        options = df["station"].unique())

filter = df[df["station"] == station]

st.title("Analisis Dataset 'Air Quality' :sparkles:")


st.subheader("Tren Polusi")

pilihan = st.selectbox(
    label = "Pilih kategori by:", 
    options = ["Tahun", "Bulan", "Hari", "Jam"])

if pilihan == "Tahun":
    mean = filter.groupby("year")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    xdata = mean["year"]
elif pilihan == "Bulan":
    mean = filter.groupby("month")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    xdata = mean["month"]
elif pilihan == "Hari":
    mean = filter.groupby("day")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    xdata = mean["day"]
else:
    mean = filter.groupby("hour")[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean().reset_index()
    xdata = mean["hour"]

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(15, 20))
ax = ax.flatten() 
colors = ['red', 'blue', 'green', 'purple', 'orange', 'black']


ax[0].plot(xdata, mean["PM2.5"], marker='o', linewidth=2, color=colors[0])
ax[0].set_xlabel(None)
ax[0].set_ylabel("PM2.5")
ax[0].set_title("Polusi PM2.5")

ax[1].plot(xdata, mean["PM10"], marker='o', linewidth=2, color=colors[1])
ax[1].set_xlabel(None)
ax[1].set_ylabel("PM10")
ax[1].set_title("Polusi PM10")

ax[2].plot(xdata, mean["SO2"], marker='o', linewidth=2, color=colors[2])
ax[2].set_xlabel(None)
ax[2].set_ylabel("SO2")
ax[2].set_title("Polusi SO2")

ax[3].plot(xdata, mean["NO2"], marker='o', linewidth=2, color=colors[3])
ax[3].set_xlabel(None)
ax[3].set_ylabel("NO2")
ax[3].set_title("Polusi NO2")

ax[4].plot(xdata, mean["CO"], marker='o', linewidth=2, color=colors[4])
ax[4].set_xlabel(None)
ax[4].set_ylabel("CO")
ax[4].set_title("Polusi CO")

ax[5].plot(xdata, mean["O3"], marker='o', linewidth=2, color=colors[5])
ax[5].set_xlabel("Hari", fontsize=20)
ax[5].set_ylabel("O3")
ax[5].set_title("Polusi O3")

st.pyplot(fig)

st.subheader("Matriks Korelasi")
plt.figure(figsize=(8, 6))
sns.heatmap(filter[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].corr(), annot=True, cmap="Reds")
st.pyplot(plt)

st.subheader("Tren Faktor Cuaca")
cuaca = st.selectbox(
    label="Pilih", 
    options=["TEMP", "PRES", "DEWP", "RAIN", "WSPM"])


cuaca_mean = filter.groupby("year")[cuaca].mean().reset_index()
    
plt.figure(figsize=(12, 6))
plt.plot(cuaca_mean["year"], cuaca_mean[cuaca], marker='o')
plt.xlabel("Tahun")
plt.ylabel(f"{cuaca} Nilai")
plt.title(f"{cuaca} Tren Cuaca per Tahun")
st.pyplot(plt)




