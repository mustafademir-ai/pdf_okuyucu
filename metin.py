import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdf_metni_cikart(pdf_yolu):
    metin = ""
    pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu, 'rb'))  # Güncel sınıf: PdfReader
    for i in range(len(pdf_okuyucu.pages)):
        sayfa_metni = pdf_okuyucu.pages[i].extract_text()
        if sayfa_metni:
            metin += sayfa_metni
    return metin

# metni sese çevirme
def metni_sese_cevir(metin, cikti):
    sesecevir = gTTS(text=metin, lang='tr')
    sesecevir.save(cikti)

# dosya seçme fonksiyonu
def dosyasec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("pdf dosyaları", "*.pdf")])
    if dosya_yolu:
        pdf_metin = pdf_metni_cikart(dosya_yolu)
        metni_sese_cevir(pdf_metin, "kaydet.mp3")
        os.system("start kaydet.mp3")  # Bu komut Windows içindir

# tkinter arayüzü
pencere = tk.Tk()
pencere.title("SESLİ KİTAP UYGULAMASI")

sesinbutonu = tk.Button(pencere, text="PDF SEÇ", command=dosyasec, padx=20, pady=20)
sesinbutonu.pack(pady=20)

pencere.mainloop()
