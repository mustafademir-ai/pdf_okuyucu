import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog, messagebox


# PDF'ten metin çıkarma
def pdf_metni_cikart(pdf_yolu):
    metin = ""

    try:
        pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu, "rb"))

        for sayfa in pdf_okuyucu.pages:
            sayfa_metin = sayfa.extract_text()
            if sayfa_metin:
                metin += sayfa_metin

    except Exception as e:
        messagebox.showerror("Hata", f"PDF okuma hatası:\n{e}")

    return metin


# Metni sese çevirme
def metni_sese_cevir(metin, cikti_dosya):
    try:
        if not metin.strip():
            messagebox.showerror("Hata", "PDF'den metin çıkarılamadı!")
            return

        tts = gTTS(text=metin, lang="tr")
        tts.save(cikti_dosya)

    except Exception as e:
        messagebox.showerror("Hata", f"Ses oluşturma hatası:\n{e}")


# Dosya seçme ve işlem
def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*.pdf")])

    if not dosya_yolu:
        return

    durum_label.config(text="PDF okunuyor...")
    pencere.update()

    pdf_metin = pdf_metni_cikart(dosya_yolu)

    if not pdf_metin.strip():
        durum_label.config(text="PDF'den metin çıkarılamadı ⚠️")
        return

    durum_label.config(text="Ses oluşturuluyor...")
    pencere.update()

    cikti = "sesli_kitap.mp3"
    metni_sese_cevir(pdf_metin, cikti)

    durum_label.config(text="Ses açılıyor...")
    pencere.update()

    try:
        os.startfile(cikti)  # Windows uyumlu
    except Exception as e:
        messagebox.showerror("Hata", f"Ses açma hatası:\n{e}")

    durum_label.config(text="İşlem tamamlandı ✅")


# ---------------- GUI ----------------
pencere = tk.Tk()
pencere.title("📚 PDF → Sesli Kitap")
pencere.geometry("420x300")
pencere.configure(bg="#f2f2f2")


baslik = tk.Label(
    pencere,
    text="PDF'den Sesli Kitap Oluştur",
    font=("Helvetica", 14, "bold"),
    bg="#f2f2f2",
    fg="#333"
)
baslik.pack(pady=20)


buton = tk.Button(
    pencere,
    text="📂 PDF SEÇ",
    command=dosya_sec,
    font=("Helvetica", 13),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=25,
    pady=10,
    bd=0
)
buton.pack(pady=10)


durum_label = tk.Label(
    pencere,
    text="",
    font=("Helvetica", 11),
    bg="#f2f2f2",
    fg="#666"
)
durum_label.pack(pady=10)


pencere.mainloop()