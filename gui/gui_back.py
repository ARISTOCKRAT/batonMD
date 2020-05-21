import tkinter as tk
from tkinter import ttk
import json


class Application(tk.Frame):
    #
    """
    self.wids => dict
    self.wids['settings'] => dict
    self.wids['settings']['path'] => str
    self.wids['settings']['order'] => str

    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.book = ttk.Notebook(self.master)
        self.book.pack()
        self.init_settings()
        # self.master.wm_geometry("%dx%d+%d+%d" % (800, 600, 100, 100))

        self.book.add(self.maintab, text='Asosiy')
        self.book.add(self.settingstab, text='Sozlamalar')
        self.book.add(self.logtab, text='LOGs')
        self.book.add(self.abouttab, text='Muallif')

        self.wids = dict()
        self.fv = master.register(self.float_validator)
        self.feature_count = len(self.feature_names)
        self.scroll = None
        self.create_maintab_widgets()
        self.create_settings_widgets()
        self.create_about_widgets()
        self.newdata = []
        self.load_fuzzy_logic_base()
        self.fuzzy_logic_order = set()

        # self.pack()

    def create_maintab_widgets(self):

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=600, height=600)

        myframe = tk.Frame(self.maintab, relief=tk.GROOVE,
                           width=50, height=100, bd=1)
        myframe.place(x=10, y=45)
        canvas = tk.Canvas(myframe)
        frame = tk.Frame(canvas)
        myscrollbar = tk.Scrollbar(myframe, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")
        canvas.pack(side="left")
        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", myfunction)


        # scroll = tk.Scrollbar(self.maintab)
        # scroll.grid(row=3, column=4, rowspan=50)
        # CREATE LABELs with feature names
        self.wids["labels"] = []
        for n, f_name in enumerate(self.feature_names):
            wid = tk.Checkbutton(frame, text=f_name)
            wid.grid(row=n+3, column=1, sticky=tk.W)
            wid.deselect()
            self.wids['labels'].append(wid)

        # CREATE ENTRYs for input feature values
        self.wids["entries"] = []
        for n in range(len(self.feature_names)):
            wid = ttk.Entry(frame)
            wid.grid(row=n+3, column=0, sticky=tk.W, padx=5)
            wid.config(validate='key', validatecommand=(self.fv, "%P", "%W"))
            self.wids['entries'].append(wid)

        # CREATE CALC BUTTON for starting action

        self.wids["calc"] = tk.Button(self.maintab, text='Hiloblash',
                                      command=self.calc, height=2, bg='#afa')
        self.wids['calc'].pack(side=tk.TOP, fill=tk.X)
        # self.wids["calc"].grid(
            # row=len(self.feature_names)+4, column=3, sticky=tk.W)
            # row=0, column=3, sticky=tk.W)

        # CREATE LOG tab
        wid = tk.Text(self.logtab, bg='#afa', wrap=tk.WORD, height=40, bd=2, state=tk.DISABLED)
        wid.grid(row=3, column=0, sticky="wesn")
        self.wids['log'] = wid

    def create_settings_widgets(self):
        #REGION HIDE
        self.wids['settings'] = dict()

        # CREATE APPLY BUTTON for starting action
        wid = ttk.Button(self.settingstab, text='Apply', command=self.settings_apply)
        wid.grid(row=1, column=3, sticky='we', pady=10)
        self.wids['settings']['btn_apply'] = wid

        # FUZZY LOGIC BASE path
        wid = ttk.Label(self.settingstab, text="Noqat'iy mantiq bazasi: ", style='Helvetika14.TLabel')
        # wid.grid(row=3, column=0, sticky=tk.E, padx=5)

        wid = ttk.Entry(self.settingstab, width=35)
        wid.insert(0, "out_data/fuzzy_logic.json")
        # wid.grid(row=3, column=1, sticky="we", columnspan=3)
        self.wids['settings']['path'] = wid

        # FUZZY LOGIC applying order
        wid = ttk.Label(self.settingstab, text="Ishonchlilik meyyori tartibi: ", style='Helvetika14.TLabel')
        # wid.grid(row=4, column=0, sticky=tk.E, padx=5)

        wid = ttk.Entry(self.settingstab, width=35)
        # wid.grid(row=4, column=1, sticky="we", columnspan=3)
        self.wids['settings']['order'] = wid
        #ENDREGION

        # CREATE FUZZY_LOGIC_BASE textbox
        wid = tk.Text(self.settingstab, bg='#afa', wrap=tk.NONE, height=40, bd=2, state=tk.DISABLED)
        wid.grid(row=3, column=0, columnspan=4, sticky="wesn")
        self.wids['fuzzy_logic_base'] = wid
        #

    def create_about_widgets(self):

        ttk.Label(self.abouttab, text="Oldi qochdi gaplar = dastur nomi", style='Helvetika14.TLabel'). \
            grid(row=0, column=0, columnspan=2, sticky='n')
        ttk.Label(self.abouttab, text="Magistrlik ishi mavzusi\n\n", style='Helvetika14.TLabel'). \
            grid(row=1, column=0, columnspan=2)

        # BATON (AUTHOR) part
        texts = (
            ("Muallif: ", "Ulugbek Negmatov"),
            ("e-mail: ", "mu.negmatov@gmail.com"),
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
        self.settings_apply()
        self.book.select(self.logtab)
        print("CALC button clicked!!!")

    def settings_apply(self):
        s = ""
        for num in self.fuzzy_logic_order:
            s += self.feature_names[num] + ', '
        md = self.confidence_measure()
        s = f"{s} alomatlani ishlatganda be'morning K1 sinfga " \
            f"tegishlilik ishonchlilik meyyori {md*100:.2f}%"
        self.logging(s)
        print("APPLY button clicked!!!")

    def getnewdata(self):
        # order = set()
        self.newdata = [0 for x in range(self.feature_count)]
        for i in range(self.feature_count):
            try:
                val = self.wids['entries'][i].get()
                if val == "": val = 0
                # else:
                #     val = val
                    # order.add(i)
                # val = 0 if val == "" else val
                self.newdata[i] = float(val)

            except Exception as e:
                self.logging(f"{self.wids['labels'][i]['text']} :: qiymati xato kiritildi\n")
                self.book.select(self.logtab)
                print(f"{self.wids['labels'][i]['text']} :: qiymati xato kiritildi\n")

    def confidence_measure(self):
        md = 0  # Мера доверия
        # order = self.wids['settings']['order'].get()
        # order = order.replace(",", " ").split()
        order = self.fuzzy_logic_order
        print(order)
        for orderok in order:
            f = 0.
            val = float(self.wids["entries"][orderok].get())
            minima = float('inf')
            for interval in self.fuzzy_logic_base[str(orderok)]['intervals']:
                if interval[0] <= val <= interval[1]:
                    f = interval[3]
                    break

                delta = min(abs(interval[0] - val), abs(interval[1] - val))
                if delta < minima:
                    minima = delta
                    not_in_interval = interval[3]
                # print(f"o={orderok}; D={delta}; f={f}; i[0]={interval[0]} - i[1]={interval[1]}")
            else:
                f = not_in_interval
            # Calculating confidence measure
            md = md + f * (1-md)
        return md

    def logging(self, text):
        wid = self.wids['log']
        wid.config(state=tk.NORMAL)
        wid.insert(tk.END, text+'\n\n')
        wid.config(state=tk.DISABLED)

    def float_validator(self, string, wid_name):
        a = wid_name[wid_name.find('!entry') + 6:]
        # a = wid_name.replace('.!notebook.!frame.!entry', "")

        a = int(a)-1 if a else 0
        try:
            if string == "":
                self.wids["labels"][a].deselect()
                self.fuzzy_logic_order.discard(a)
                return True
            else:
                self.wids["labels"][a].select()
                self.fuzzy_logic_order.add(a)
            float(string)
            return True
        except:
            return False

    def load_fuzzy_logic_base(self):
        path = '../' + self.wids['settings']['path'].get()
        with open(path) as f:
            json_data = json.load(f)
        self.fuzzy_logic_base = json_data
        wid = self.wids['fuzzy_logic_base']
        wid.config(state=tk.NORMAL)

        scroll = ttk.Scrollbar(self.settingstab, command=wid.yview)
        # scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scroll.grid(row=3, column=4, sticky='nsew')
        wid['yscrollcommand'] = scroll.set
        # self.txt['yscrollcommand'] = scrollb.set

        json_data = json.dumps(json_data, indent=4, sort_keys=True)
        self.wids['fuzzy_logic_base'].insert(tk.END, json_data)
        wid.config(state=tk.DISABLED)

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



