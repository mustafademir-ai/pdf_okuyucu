# 📚 PDF → Sesli Kitap Dönüştürücü

Bu proje, PDF dosyalarınızdaki metinleri otomatik olarak ayıklayıp Türkçe seslendirmeye (MP3 formatına) dönüştüren ve işlem bittiğinde otomatik olarak oynatan **Python**, **Tkinter** ve **gTTS** tabanlı bir masaüstü uygulamasıdır.

---

## ✨ Özellikler

* **📂 Kolay PDF Seçimi:** Grafiksel kullanıcı arayüzü (GUI) üzerinden tek tıkla bilgisayarınızdan PDF seçebilirsiniz.
* **🔍 Otomatik Metin Ayıklama:** `PyPDF2` kütüphanesi sayesinde PDF sayfalarındaki metinler hızlıca taranır.
* **🗣️ Türkçe Seslendirme:** `gTTS` (Google Text-to-Speech) entegrasyonu ile metinler doğal bir Türkçe ses tonuyla MP3 dosyasına dönüştürülür.
* **⏳ Canlı Durum Takibi:** İşlem sırasında arayüz üzerinde anlık olarak "PDF okunuyor...", "Ses oluşturuluyor..." gibi durum bilgilendirmeleri yapılır.
* **🎧 Otomatik Oynatma:** Dönüştürme işlemi bittiği an oluşturulan `sesli_kitap.mp3` dosyası varsayılan medya oynatıcınızda otomatik olarak açılır.

---

## 🛠️ Gereksinimler ve Kurulum

Uygulamanın çalışması için sisteminizde Python 3.x yüklü olmalıdır. Gerekli harici kütüphaneleri yüklemek için terminal veya komut satırında aşağıdaki komutu çalıştırmanız yeterlidir:

```bash
pip install PyPDF2 gTTS
```

*(Not: `tkinter` ve `os` kütüphaneleri Python ile birlikte yerleşik olarak geldiği için ekstra bir kurulum gerektirmez.)*

---

## 🚀 Nasıl Çalıştırılır?

1. Bu projeye ait kodları `sesli_kitap.py` adıyla bir dosyaya kaydedin.
2. Terminalden projenin olduğu dizine gidin ve şu komutla uygulamayı başlatın:
   ```bash
   python sesli_kitap.py
   ```
3. Açılan pencerede **PDF SEÇ** butonuna basarak bir PDF dosyası yükleyin ve arkanıza yaslanıp sesli kitabınızın hazır olmasını bekleyin!

---

## 📝 Notlar
* Dönüştürülen ses dosyası, projenin çalıştığı dizine `sesli_kitap.mp3` adıyla kaydedilir.
* Taratılan PDF dosyasının tamamen görsellerden (resim formatındaki taramalardan) oluşmaması, içinde seçilebilir metin barındırması gerekmektedir.
