**Ad Soyad:** Ömer Faruk Karakoy  
**E-posta:** omerfarukkarakoy@hotmail.com  

---

## 📖 Proje Özeti
Bu proje, Pusula Intern Programı kapsamında verilen **Data Science Case Study** çalışmasıdır.  
Veri seti, **Fiziksel Tıp ve Rehabilitasyon** alanına ait 2235 gözlem ve 13 sütundan oluşmaktadır.  
Hedef değişken: **`TedaviSuresi`**  

Amaç:  
- Veri seti üzerinde **Exploratory Data Analysis (EDA)** gerçekleştirmek  
- Veriyi temizleyip **modellemeye hazır** hale getirmek (preprocessing)  

Not: Modelleme yapılması zorunlu olmadığı için, yalnızca veri hazırlık sürecine odaklanılmıştır.  

---

## 🔍 Veri Seti Hakkında
Veri setinde yer alan temel kolonlar:  

- `HastaNo`: Hasta ID (anonimleştirilmiş)  
- `Yas`: Yaş  
- `Cinsiyet`: Cinsiyet  
- `KanGrubu`: Kan grubu  
- `Uyruk`: Uyruk  
- `KronikHastalik`: Kronik hastalık bilgisi  
- `Bolum`: Tedavi bölümü  
- `Alerji`: Alerji bilgisi  
- `Tanilar`: Teşhisler  
- `TedaviAdi`: Tedavi adı  
- `TedaviSuresi`: Tedavi süresi (hedef değişken)  
- `UygulamaYerleri`: Uygulama yerleri  
- `UygulamaSuresi`: Uygulama süresi  

---

## 🧪 Yapılan Çalışmalar

### 1. Exploratory Data Analysis (EDA)
- Veri tipi ve eksik değer analizi (`df.info()`, `missingno`)  
- Sayısal değişkenlerin dağılımı (histogram, boxplot)  
- Korelasyon analizi (heatmap)  
- Kategorik değişken dağılımları (countplot)  
- Hedef değişken (`TedaviSuresi`) için dağılım ve boxplot  
- Grup bazlı analizler (örneğin `Bolum` bazında ortalama tedavi süresi)  

### 2. Veri Ön İşleme (Preprocessing)
- **Eksik değer doldurma**  
  - Sayısal kolonlar → `SimpleImputer(strategy="median")`  
  - Kategorik kolonlar → `SimpleImputer(strategy="most_frequent")`  
- **Encoding**  
  - `OneHotEncoder` (drop="first", handle_unknown="ignore") kullanılarak kategorik değişkenler dönüştürüldü.  
- **Ölçekleme (Scaling)**  
  - Sayısal kolonlar `StandardScaler` ile normalize edilerek aynı ölçeğe getirildi.  

### 3. Final Dataset
- `df_scaled` → Modellemeye hazır, temiz, encode edilmiş ve normalize edilmiş nihai veri seti.  

---

## 📊 Bulgular (Kısa Özet)
- Yaş değişkeni ile tedavi süresi arasında zayıf ama pozitif bir korelasyon gözlemlendi.  
- Cinsiyet dağılımı dengesiz olabilir, bu nedenle modelleme aşamasında dikkat edilmesi gerekebilir.  
- Bazı bölümlerde (`Bolum`) tedavi sürelerinin ortalaması diğerlerinden daha yüksektir → bölüm faktörü tedavi süresini etkileyebilir.  
- Eksik değerler median/mode yöntemiyle başarıyla doldurulmuştur.  

---

## 🛠️ Kullanılan Teknolojiler
**Python**

**Pandas, NumPy** : Veri İşleme

**Matplotlib, Seaborn, Plotly, Missingno** : Görselleştirme 

**Scikit-learn (SimpleImputer, OneHotEncoder, StandardScaler)**: Ön İşleme 

---

## 🚀 Çalıştırma Talimatları
1. Bu repository’i bilgisayarınıza indirin.  
2. Gerekli kütüphaneleri yükleyin:  
   ```bash
   pip install pandas numpy matplotlib seaborn plotly missingno scikit-learn
