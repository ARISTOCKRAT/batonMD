import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.book = ttk.Notebook(self.master)
        self.book.pack()
        self.init_settings()

        self.book.add(self.maintab, text='Asosiy')
        self.book.add(self.settingstab, text='Sozlamalar')
        self.book.add(self.logtab, text='LOGs')
        self.book.add(self.abouttab, text='Muallif')

        self.wids = dict()
        self.fv = master.register(self.float_validator)
        self.feature_count = len(self.feature_names)
        self.create_maintab_widgets()
        self.create_settings_widgets()
        self.create_about_widgets()
        self.newdata = []

        # self.pack()

    def create_maintab_widgets(self):

        # CREATE LABELs with feature names
        self.wids["labels"] = []
        for n, f_name in enumerate(self.feature_names):
            wid = ttk.Label(self.maintab, text=f_name)
            wid.grid(row=n+3, column=0, sticky=tk.E)

            self.wids['labels'].append(wid)

        # CREATE ENTRYs for input feature values
        self.wids["entries"] = []
        for n in range(len(self.feature_names)):
            wid = ttk.Entry(self.maintab)
            wid.grid(row=n+3, column=1, sticky=tk.E)
            wid.config(validate='key', validatecommand=(self.fv, '%d', '%S', "%P"))
            self.wids['entries'].append(wid)

        # CREATE CALC BUTTON for starting action
        self.wids["calc"] = ttk.Button(self.maintab, text='Hiloblash', command=self.calc)
        self.wids["calc"].grid(
            row=len(self.feature_names)+4, column=3, sticky=tk.W)

        s="jasjdkljaskl jlksajdkljaskld\nasjdkjaskl\nasd"
        # CREATE LOG tab
        wid = tk.Text(self.logtab, bg='#afa', wrap=tk.NONE, height=40, bd=2, state=tk.DISABLED)
        wid.grid(row=3, column=0, sticky="wesn")
        self.wids['log'] = wid

    def create_settings_widgets(self):
        self.wids['settings'] = dict()
        # CREATE APPLY BUTTON for starting action
        wid = ttk.Button(self.settingstab, text='Apply', command=self.settings_apply)
        wid.grid(row=1, column=3, sticky='we', pady=10)
        self.wids['settings']['btn_apply'] = wid

        # FUZZY LOGIC BASE path
        wid = ttk.Label(self.settingstab, text="Noqat'iy mantiq bazasi: ", style='Helvetika14.TLabel')
        wid.grid(row=3, column=0, sticky=tk.E, padx=5)

        wid = ttk.Entry(self.settingstab, width=35)
        wid.insert(0, "out_data/fuzzy_logic.json")
        wid.grid(row=3, column=1, sticky="we", columnspan=3)
        self.wids['settings']['path'] = wid

        # FUZZY LOGIC applying order
        wid = ttk.Label(self.settingstab, text="Ishonchlilik meyyori tartibi: ", style='Helvetika14.TLabel')
        wid.grid(row=4, column=0, sticky=tk.E, padx=5)

        wid = ttk.Entry(self.settingstab, width=35)
        wid.insert(0, "1,2,3,4")
        wid.grid(row=4, column=1, sticky="we", columnspan=3)
        self.wids['settings']['order'] = wid

    def create_about_widgets(self):

        ttk.Label(self.abouttab, text="Oldi qochdi gaplar = dastur nomi", style='Helvetika14.TLabel'). \
            grid(row=0, column=0, columnspan=2, sticky='n')
        ttk.Label(self.abouttab, text="Magistrlik ishi mavzusi\n\n", style='Helvetika14.TLabel'). \
            grid(row=1, column=0, columnspan=2)

        # BATON (AUTHOR) part
        texts = (
            ("Muallif: ", "Bahriddin Akbarov"),
            ("e-mail: ", "bahriddin.akbarov@gmail.com"),
            ("Manzil: ", "Mirzo-Ulugbek nomidagi\nO'zbekiston milliy universiteti"),
            ("Manzil: ", "100174, Toshkent sh.,\nUniversitet ko'chasi, 4-uy"),
        )
        baton = tk.Frame(self.abouttab, bd=6)
        baton.grid(row=2, column=0, sticky='WENS')
        c = 1
        for line in texts:
            ttk.Label(baton, text=line[0], style="Helvetika14.TLabel", justify=tk.RIGHT).\
                grid(row=c, column=0, sticky='ne')
            ttk.Label(baton, text=line[1], style="Helvetika14.TLabel", justify=tk.LEFT).\
                grid(row=c, column=1, sticky='we')
            c += 1

        # DRUPPI (ADVISOR) part
        texts = (
            ("Ilmiy rahbar: ", "Shavkat Madraximov"),
            ("e-mail: ", "mshavkat@yandex.ru"),
            ("Manzil: ", "Mirzo-Ulugbek nomidagi\nO'zbekiston milliy universiteti"),
            ("Manzil: ", "100174, Toshkent sh.,\nUniversitet ko'chasi, 4-uy"),
            ("ilmiy daraja: ", "fizika-matematika fanlari doktori DSc"),
        )
        druppi = tk.Frame(self.abouttab, bd=6)
        druppi.grid(row=2, column=1, sticky='WENS')
        c = 1
        for line in texts:
            ttk.Label(druppi, text=line[0], style="Helvetika14.TLabel", justify=tk.RIGHT). \
                grid(row=c, column=0, sticky='ne')
            ttk.Label(druppi, text=line[1], style="Helvetika14.TLabel", justify=tk.LEFT). \
                grid(row=c, column=1, sticky='we')
            c += 1

        # FOOTER
        ttk.Label(self.abouttab, text="GNU General Public Licence", style="Helvetiva14.TLabel"). \
            grid(row=5, column=0, columnspan=2)
        s = """This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA."""
        wid = tk.Text(self.abouttab, bg='#eee', wrap=tk.WORD, height=10, bd=2)#, state=tk.DISABLED)
        wid.grid(row=6, column=0, sticky="wesn", columnspan=2)
        wid.insert(1.0, s)
        ttk.Label(self.abouttab, text="All right recieved 2020 ©", style="Helvetiva14.TLabel"). \
            grid(row=7, column=0, columnspan=2)
        pass

    def calc(self):
        self.getnewdata()
        print("CALC button clicked!!!")

    def settings_apply(self):
        print("APPLY button clicked!!!")

    def getnewdata(self):
        self.newdata = [0 for x in range(self.feature_count)]
        for i in range(self.feature_count):
            try:
                val = self.wids['entries'][i].get()
                val = 0 if val == "" else val
                self.newdata[i] = float(val)
            except Exception as e:
                self.logging(f"{self.wids['labels'][i]['text']} :: qiymati xato kiritildi\n")
                self.book.select(self.logtab)
                print(f"{self.wids['labels'][i]['text']} :: qiymati xato kiritildi\n")
                pass

    def logging(self, text):
        wid = self.wids['log']
        wid.config(state=tk.NORMAL)
        wid.insert(tk.END, text)
        wid.config(state=tk.DISABLED)

    @staticmethod
    def float_validator(isinsert, input, string):
        if isinsert:
            if input in "0123456789.+-" and string.count('.') <= 1:
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
        self.maintab = ttk.Frame(self.book, relief=tk.FLAT)
        self.abouttab = ttk.Frame(self.book, relief=tk.RIDGE)
        self.settingstab = ttk.Frame(self.book, relief=tk.SUNKEN)
        self.logtab = ttk.Frame(self.book, relief=tk.RAISED)
        label_style = ttk.Style()
        label_style.configure('Helvetika14.TLabel',
                              # background='#ccc',
                              foreground='black',
                              font=('Helvetica', 12,),
                              height=50,
                              # relief="solid",
                              )



