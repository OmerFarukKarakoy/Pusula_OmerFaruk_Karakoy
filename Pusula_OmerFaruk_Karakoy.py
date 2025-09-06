"""
@author: omerf
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import missingno as msno
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("Talent_Academy_Case_DT_2025.xlsx")
print(df)


# Genel Bakış
print("🔹 Veri Boyutu:", df.shape)
print("🔹 Kolonlar:", df.columns.tolist())
print("\n🔹 Veri Tipleri:\n", df.dtypes)
print("\n🔹 Eksik Değerler:\n", df.isnull().sum())

df.info()
df.describe()



# Eksik Veri Analizi
msno.matrix(df)
plt.title('Eksik Veri Matrisi', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

msno.heatmap(df)
plt.title('Eksik Veri Isı Haritası', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

numeric_cols = df.select_dtypes(include=[np.number]).columns
categorical_cols = df.select_dtypes(include=["object"]).columns

print(f"Sayısal kolonlar: {numeric_cols.tolist()}")
print(f"Kategorik kolonlar: {categorical_cols.tolist()}")



# Eksik Değer Doldurma
# Sayısal kolonlar
imputer_num = SimpleImputer(strategy="median")
df[numeric_cols] = imputer_num.fit_transform(df[numeric_cols])

# Kategorik kolonlar
imputer_cat = SimpleImputer(strategy="most_frequent")
df[categorical_cols] = imputer_cat.fit_transform(df[categorical_cols])
df



# Encoding(OneHotEncoder ile encoding)
encoder = OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore")
categorical_cols = df.select_dtypes(include=["object"]).columns
encoded_array = encoder.fit_transform(df[categorical_cols])
encoded_cols = encoder.get_feature_names_out(categorical_cols)
df_encoded = pd.DataFrame(encoded_array, columns=encoded_cols, index=df.index)
df_final = pd.concat([df.drop(columns=categorical_cols), df_encoded], axis=1)
df_final.head()



# Ölçekleme
numeric_cols = df_final.select_dtypes(include=["int64", "float64"]).columns
scaler = StandardScaler()
df_scaled = df_final.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df_final[numeric_cols])
df_scaled.head()



# Sayısal Değişken Analizi
numeric_cols = df.select_dtypes(include=[np.number]).columns

for col in numeric_cols:
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    sns.histplot(df[col], kde=True)
    plt.title(f"{col} Dağılımı")

    plt.subplot(1,2,2)
    sns.boxplot(x=df[col])
    plt.title(f"{col} Boxplot")
    plt.show()
# Korelasyon
plt.figure(figsize=(10,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.show()



# Kategorik Değişken Analizi
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    plt.figure(figsize=(8,4))
    sns.countplot(y=col, data=df, order=df[col].value_counts().index)
    plt.title(f"{col} Dağılımı")
    plt.show()
    
    
    
# Hedef Değişken (TedaviSuresi)
plt.figure(figsize=(10,5))
sns.histplot(df["TedaviSuresi"], kde=True)
plt.title("Tedavi Süresi Dağılımı(Seans Dağılımı)")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(x=df["TedaviSuresi"])
plt.title("Tedavi Süresi (Seans) Boxplot")
plt.show()



#Tedavi Süresi ile Korelasyon Analizi
df["TedaviSuresi"] = pd.to_numeric(df["TedaviSuresi"], errors="coerce")
numeric_df = df.select_dtypes(include=[np.number])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr()[["TedaviSuresi"]].sort_values(by="TedaviSuresi", ascending=False), 
            annot=True, cmap="viridis")
plt.title("Tedavi Süresi (Seans) ile Korelasyon")
plt.show()



# Grup Bazlı Analizler
print(df.groupby("Bolum")["TedaviSuresi"].mean().sort_values())

px.scatter(df, x="Yas", y="TedaviSuresi", color="Cinsiyet", title="Yaş vs Tedavi Süresi (Cinsiyete Göre)")

