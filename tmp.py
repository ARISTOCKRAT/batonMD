import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
# feature_names = ("Yoshi",
#                               "Bo'yi",
#                               "Vazni",
#                               "Sistolik arterial bosim(ADS)",
#                               "Diastolik arterial bosim(ADD)",
#                               "EKG ga nisbatan RR interval uzunligi",
#                               "EKG ga nisbatan PQ interval uzunligi",
#                               "EKG ga nisbatan QT interval uzunligi",
#                               "EKG ga QRS interval uzunligi",
#                               "Chap yurakoldi bushlig'ining ulchami(PLP)",
#                               "CHap qorinchaning chegaraviy sistolik ulchami(KSR)",
#                               "CHap qorinchaning chegaraviy diastolik ulchami(KDR)",
#                               "Sistolada chap qorinchaning old-orqa ulchamining kiskarish darajasi(YSS)",
#                               "O'rtacha arterial bosim (ADSR)",
#                               "Pulsli arterial bosim (ADPuls)",
#                               "K1 koeffitsenti",
#                               "K2 koeffitsienti",
#                               "Sistolik kursatkich(SisPok)",
#                               "Sistola davom etishi (Sistola)",
#                               "Diastola davom etishi (Diastola)",
#                               "CHap qorinchaning sistolik xajmining chegarasi(KSO)",
#                               "CHap korinchaning diastolik xajmining chegarasi(KDO)",
#                               "Tomir urish chastotasi(DS)",
#                               "Zarba hajmi(YO)",
#                               "Minutdagi xajm(MO)",
#                               "Yurak indeksi(SI)",
#                               "Otilib chikish fraksiyasi(FV)",
#                               "Solishtirma periferik karshilik(UPS)",
#                               "Kerde indeksi")
#
# for n, fname in enumerate(feature_names):
#     ttk.Label(root, text=fname, font=('Consolas', 15)).grid(row=n, column=0, sticky=tk.W)
#

with open(r"d:\_NUU\2020\batonMD\gui\hisobla.png", mode='br') as img:
    f = img.read()
    b = bytearray(f)
    print(f)
    print(b)



# root.mainloop()
