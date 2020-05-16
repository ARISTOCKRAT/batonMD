import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_settings()

        # self.l_f_names = []
        self.elements = dict()
        self.fv = master.register(self.float_validator)
        self.create_init_widgets()

        # self.pack()

    def create_init_widgets(self):

        # CREATE LABELs with feature names
        self.elements["labels"] = []
        for n, f_name in enumerate(self.feature_names):
            label = ttk.Label(self.master, text=f_name)
            label.grid(row=n+3, column=0, sticky=tk.E)

            self.elements['labels'].append(label)

        # CREATE ENTRYs for input feature values
        self.elements["entries"] = []
        for n in range(len(self.feature_names)):
            entry = ttk.Entry(self.master)
            entry.grid(row=n+3, column=1, sticky=tk.E)
            entry.config(validate='key', validatecommand=(self.fv, '%d', '%S', "%P"))
            self.elements['entries'].append(entry)

        # CREATE CALC BUTTON for starting action
        self.elements["calc"] = ttk.Button(self.master, text='Hiloblash', command=self.calc)
        self.elements["calc"].grid(
            row=len(self.feature_names)+4, column=3, sticky=tk.E)

    def calc(self):
        for entry in self.elements['entries']:
            val = entry.get()
            # validate

        print("CALC button clicked!!!")

    @staticmethod
    def float_validator(isinsert, input, string):
        print(input)
        if isinsert:
            if input in "0123456789." and string.count('.') <= 1:
                return True
        return False

    def init_settings(self):
        self.feature_names = ("Yoshi",
                              "Bo'yi",
                              "Vazni",
                              "Sistolik arterial bosim(ADS)",
                              "Diastolik arterial bosim(ADD)",
                              "EKG ga nisbatan RR interval uzunligi",
                              "EKG ga nisbatan PQ interval uzunligi",
                              "EKG ga nisbatan QT interval uzunligi",
                              "EKG ga QRS interval uzunligi",
                              "Chap yurakoldi bushlig'ining ulchami(PLP)",
                              "CHap qorinchaning chegaraviy sistolik ulchami(KSR)",
                              "CHap qorinchaning chegaraviy diastolik ulchami(KDR)",
                              "Sistolada chap qorinchaning old-orqa ulchamining kiskarish darajasi(YSS)",
                              "O'rtacha arterial bosim (ADSR)",
                              "Pulsli arterial bosim (ADPuls)",
                              "K1 koeffitsenti",
                              "K2 koeffitsienti",
                              "Sistolik kursatkich(SisPok)",
                              "Sistola davom etishi (Sistola)",
                              "Diastola davom etishi (Diastola)",
                              "CHap qorinchaning sistolik xajmining chegarasi(KSO)",
                              "CHap korinchaning diastolik xajmining chegarasi(KDO)",
                              "Tomir urish chastotasi(DS)",
                              "Zarba hajmi(YO)",
                              "Minutdagi xajm(MO)",
                              "Yurak indeksi(SI)",
                              "Otilib chikish fraksiyasi(FV)",
                              "Solishtirma periferik karshilik(UPS)",
                              "Kerde indeksi")

