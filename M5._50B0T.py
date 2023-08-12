import tkinter as tk

def m550bot_alfabe():
    alfabe = {
        '000': 'A', '001': 'B', '002': 'C', '003': 'Ç', '004': 'D', '005': 'E', '006': 'F', '007': 'G',
        '008': 'Ğ', '009': 'H', '010': 'I', '011': 'İ', '012': 'J', '013': 'K', '014': 'L', '015': 'M',
        '016': 'N', '017': 'O', '018': 'Ö', '019': 'P', '020': 'R', '021': 'S', '022': 'Ş', '023': 'T',
        '024': 'U', '025': 'Ü', '026': 'V', '027': 'Y', '028': 'Z'
    }
    return alfabe

def sifrele_metin():
    alfabe = m550bot_alfabe()
    metin = metin_entry.get().upper()
    sifreli_metin = ''
    for harf in metin:
        if harf == ' ':
            sifreli_metin += ' '
        else:
            for kod, karakter in alfabe.items():
                if karakter == harf:
                    sifreli_metin += kod + ' '
                    break
    sifreli_metin_label.config(text="Şifrelenmiş metin: " + sifreli_metin)

def coz_metin():
    alfabe = m550bot_alfabe()
    sifreli_metin = coz_entry.get()
    sifreli_harfler = sifreli_metin.split()
    cozulmus_metin = ''
    for kod in sifreli_harfler:
        if kod == '':
            cozulmus_metin += ' '
        else:
            if kod in alfabe:
                cozulmus_metin += alfabe[kod]
            else:
                cozulmus_metin += f'[{kod}]'
    cozulmus_metin_label.config(text="Çözülmüş metin: " + cozulmus_metin)

window = tk.Tk()
window.title("M5.50B0T 3.0")

# Create and place widgets
header_label = tk.Label(window, text="M5.50B0T", font=("Helvetica", 16))
header_label.pack(pady=10)

metin_label = tk.Label(window, text="Metin:")
metin_label.pack()

metin_entry = tk.Entry(window)
metin_entry.pack()

sifrele_button = tk.Button(window, text="Metni Şifrele", command=sifrele_metin)
sifrele_button.pack(pady=5)

sifreli_metin_label = tk.Label(window, text="", wraplength=300)
sifreli_metin_label.pack()

coz_label = tk.Label(window, text="Şifreli Metin:")
coz_label.pack()

coz_entry = tk.Entry(window)
coz_entry.pack()

coz_button = tk.Button(window, text="Metni Çöz", command=coz_metin)
coz_button.pack(pady=5)

cozulmus_metin_label = tk.Label(window, text="", wraplength=300)
cozulmus_metin_label.pack()

exit_button = tk.Button(window, text="Çıkış", command=window.destroy)
exit_button.pack(pady=10)

window.mainloop()
