#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 13, 2020 06:37:41 PM CEST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import carnet_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    carnet_support.set_Tk_var()
    top = Carnet_d_adresses (root)
    carnet_support.init(root, top)
    root.mainloop()

w = None
def create_Carnet_d_adresses(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Carnet_d_adresses(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    carnet_support.set_Tk_var()
    top = Carnet_d_adresses (w)
    carnet_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Carnet_d_adresses():
    global w
    w.destroy()
    w = None

class Carnet_d_adresses:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans Mono} -size -12"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("631x732")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1, 1)
        top.title("Carnet d adresses")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.001
                , relwidth=0.986)
        self.TNotebook1.configure(takefocus="")
        self.pg1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.pg1, padding=3)
        self.TNotebook1.tab(0, text="Détails",compound="none",underline="-1",)
        self.pg0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.pg0, padding=3)
        self.TNotebook1.tab(1, text="Liste",compound="none",underline="-1",)

        self.Label1 = tk.Label(self.pg1)
        self.Label1.place(relx=0.032, rely=0.085, height=21, width=35)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Nom''')

        self.Label2 = tk.Label(self.pg1)
        self.Label2.place(relx=0.032, rely=0.127, height=21, width=54)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Prénom''')

        self.Entry7 = tk.Entry(self.pg1)
        self.Entry7.place(relx=0.516, rely=0.042,height=20, relwidth=0.316)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(selectbackground="#c4c4c4")

        self.Entry2 = tk.Entry(self.pg1)
        self.Entry2.place(relx=0.177, rely=0.085,height=20, relwidth=0.655)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Entry3 = tk.Entry(self.pg1)
        self.Entry3.place(relx=0.177, rely=0.127,height=20, relwidth=0.655)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")

        self.Entry4 = tk.Entry(self.pg1)
        self.Entry4.place(relx=0.177, rely=0.17,height=20, relwidth=0.655)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")

        self.Entry6 = tk.Entry(self.pg1)
        self.Entry6.place(relx=0.177, rely=0.198,height=20, relwidth=0.655)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")

        self.Entry5 = tk.Entry(self.pg1)
        self.Entry5.place(relx=0.177, rely=0.24,height=20, relwidth=0.655)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")

        self.Entry1 = tk.Entry(self.pg1)
        self.Entry1.place(relx=0.177, rely=0.283,height=20, relwidth=0.655)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Entry8 = ScrolledText(self.pg1)
        self.Entry8.place(relx=0.177, rely=0.325, relheight=0.096
                , relwidth=0.655)
        self.Entry8.configure(background="white")
        self.Entry8.configure(font=font10)
        self.Entry8.configure(insertborderwidth="3")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(wrap="none")

        self.Button1 = tk.Button(self.pg1)
        self.Button1.place(relx=0.613, rely=0.424, height=29, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Enregistrer''')

        self.TButton2 = ttk.Button(self.pg1)
        self.TButton2.place(relx=0.847, rely=0.078, height=28, width=83)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Effacer''')

        self.Label3 = tk.Label(self.pg1)
        self.Label3.place(relx=0.032, rely=0.17, height=21, width=56)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Adresse''')

        self.Label4 = tk.Label(self.pg1)
        self.Label4.place(relx=0.032, rely=0.24, height=21, width=81)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''Code postal''')

        self.Label5 = tk.Label(self.pg1)
        self.Label5.place(relx=0.032, rely=0.283, height=21, width=33)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''Ville''')

        self.TButton1 = ttk.Button(self.pg1)
        self.TButton1.place(relx=0.847, rely=0.276, height=28, width=83)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Effacer''')

        self.TButton3 = ttk.Button(self.pg1)
        self.TButton3.place(relx=0.847, rely=0.12, height=28, width=83)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Effacer''')

        self.TButton4 = ttk.Button(self.pg1)
        self.TButton4.place(relx=0.847, rely=0.184, height=25, width=83)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Effacer''')

        self.TButton5 = ttk.Button(self.pg1)
        self.TButton5.place(relx=0.847, rely=0.233, height=28, width=83)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Effacer''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(self.pg1)
        self.TCheckbutton1.place(relx=0.032, rely=0.014, relwidth=0.126
                , relheight=0.0, height=21)
        self.TCheckbutton1.configure(variable=carnet_support.tch58)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Monsieur''')

        self.TCheckbutton2 = ttk.Checkbutton(self.pg1)
        self.TCheckbutton2.place(relx=0.032, rely=0.042, relwidth=0.121
                , relheight=0.0, height=21)
        self.TCheckbutton2.configure(variable=carnet_support.tch58)
        self.TCheckbutton2.configure(takefocus="")
        self.TCheckbutton2.configure(text='''Madame''')

        self.TCheckbutton3 = ttk.Checkbutton(self.pg1)
        self.TCheckbutton3.place(relx=0.161, rely=0.014, relwidth=0.252
                , relheight=0.0, height=21)
        self.TCheckbutton3.configure(variable=carnet_support.tch58)
        self.TCheckbutton3.configure(takefocus="")
        self.TCheckbutton3.configure(text='''Monsieur et Madame''')

        self.TCheckbutton4 = ttk.Checkbutton(self.pg1)
        self.TCheckbutton4.place(relx=0.419, rely=0.014, relwidth=0.423
                , relheight=0.0, height=21)
        self.TCheckbutton4.configure(variable=carnet_support.tch58)
        self.TCheckbutton4.configure(takefocus="")
        self.TCheckbutton4.configure(text='''Monsieur et Madame et leurs enfants''')

        self.TButton6 = ttk.Button(self.pg1)
        self.TButton6.place(relx=0.032, rely=0.424, height=28, width=83)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''Chercher''')

        self.TCheckbutton5 = ttk.Checkbutton(self.pg1)
        self.TCheckbutton5.place(relx=0.161, rely=0.042, relwidth=0.194
                , relheight=0.0, height=17)
        self.TCheckbutton5.configure(variable=carnet_support.tch58)
        self.TCheckbutton5.configure(takefocus="")
        self.TCheckbutton5.configure(text='''Mademoiselle''')

        self.TCheckbutton6 = ttk.Checkbutton(self.pg1)
        self.TCheckbutton6.place(relx=0.419, rely=0.042, relwidth=0.092
                , relheight=0.0, height=21)
        self.TCheckbutton6.configure(variable=carnet_support.tch58)
        self.TCheckbutton6.configure(takefocus="")
        self.TCheckbutton6.configure(text='''Autre''')

        self.TButton7 = ttk.Button(self.pg1)
        self.TButton7.place(relx=0.831, rely=0.424, height=28, width=90)
        self.TButton7.configure(takefocus="")
        self.TButton7.configure(text='''Tout effacer''')

        self.TButton13 = ttk.Button(self.pg1)
        self.TButton13.place(relx=0.847, rely=0.028, height=28, width=83)
        self.TButton13.configure(takefocus="")
        self.TButton13.configure(text='''Effacer''')

        self.Label7 = tk.Label(self.pg1)
        self.Label7.place(relx=0.032, rely=0.325, height=21, width=46)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(text='''Divers''')

        self.TButton14 = ttk.Button(self.pg1)
        self.TButton14.place(relx=0.847, rely=0.354, height=28, width=83)
        self.TButton14.configure(takefocus="")
        self.TButton14.configure(text='''Effacer''')

        self.TNotebook2 = ttk.Notebook(self.pg1)
        self.TNotebook2.place(relx=0.25, rely=0.467, relheight=0.513
                , relwidth=0.737)
        self.TNotebook2.configure(takefocus="")
        self.pg2 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.pg2, padding=3)
        self.TNotebook2.tab(0, text="Aperçu de l'adresse", compound="none"
                ,underline="-1", )
        self.pg3 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.pg3, padding=3)
        self.TNotebook2.tab(1, text="Téléphone", compound="none", underline="-1"
                ,)
        self.pg4 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.pg4, padding=3)
        self.TNotebook2.tab(2, text="Courriel",compound="none",underline="-1",)

        self.Button9 = tk.Button(self.pg2)
        self.Button9.place(relx=0.396, rely=0.03, height=29, width=86)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(text='''Imprimer''')

        self.Canvas2 = tk.Canvas(self.pg2)
        self.Canvas2.place(relx=0.022, rely=0.148, relheight=0.825
                , relwidth=0.923)
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(selectbackground="#c4c4c4")

        self.Label17 = tk.Label(self.pg3)
        self.Label17.place(relx=0.066, rely=0.059, height=21, width=35)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(text='''Nom''')

        self.Entry17 = tk.Entry(self.pg3)
        self.Entry17.place(relx=0.22, rely=0.059,height=20, relwidth=0.695)
        self.Entry17.configure(background="white")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(selectbackground="#c4c4c4")

        self.Label18 = tk.Label(self.pg3)
        self.Label18.place(relx=0.066, rely=0.148, height=21, width=56)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(text='''Numéro''')

        self.Entry18 = tk.Entry(self.pg3)
        self.Entry18.place(relx=0.22, rely=0.148,height=20, relwidth=0.695)
        self.Entry18.configure(background="white")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(selectbackground="#c4c4c4")

        self.Button11 = tk.Button(self.pg3)
        self.Button11.place(relx=0.066, rely=0.237, height=29, width=73)
        self.Button11.configure(activebackground="#d9d9d9")
        self.Button11.configure(text='''Ajouter''')

        self.Button12 = tk.Button(self.pg3)
        self.Button12.place(relx=0.352, rely=0.237, height=29, width=93)
        self.Button12.configure(activebackground="#d9d9d9")
        self.Button12.configure(text='''Supprimer''')

        self.Text3 = ScrolledText(self.pg3)
        self.Text3.place(relx=0.068, rely=0.338, relheight=0.647, relwidth=0.848)

        self.Text3.configure(background="white")
        self.Text3.configure(font=font10)
        self.Text3.configure(insertborderwidth="3")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(wrap="none")

        self.Label6 = tk.Label(self.pg4)
        self.Label6.place(relx=0.066, rely=0.059, height=21, width=109)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''Adresse courriel''')

        self.Entry9 = tk.Entry(self.pg4)
        self.Entry9.place(relx=0.066, rely=0.119,height=20, relwidth=0.848)
        self.Entry9.configure(background="white")
        self.Entry9.configure(font="-family {DejaVu Sans} -size -12")
        self.Entry9.configure(selectbackground="#c4c4c4")

        self.TButton16 = ttk.Button(self.pg4)
        self.TButton16.place(relx=0.066, rely=0.237, height=28, width=83)
        self.TButton16.configure(takefocus="")
        self.TButton16.configure(text='''Ajouter''')

        self.TButton17 = ttk.Button(self.pg4)
        self.TButton17.place(relx=0.286, rely=0.237, height=28, width=83)
        self.TButton17.configure(takefocus="")
        self.TButton17.configure(text='''Supprimer''')

        self.Scrolledtext1 = ScrolledText(self.pg4)
        self.Scrolledtext1.place(relx=0.066, rely=0.326, relheight=0.647
                , relwidth=0.853)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font10)
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(wrap="none")

        self.Text1 = ScrolledText(self.pg1)
        self.Text1.place(relx=0.032, rely=0.467, relheight=0.506, relwidth=0.203)

        self.Text1.configure(background="#d9d9d9")
        self.Text1.configure(font=font10)
        self.Text1.configure(insertborderwidth="3")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="red")
        self.Text1.configure(wrap="word")

        self.Button2 = tk.Button(self.pg1)
        self.Button2.place(relx=0.468, rely=0.424, height=29, width=76)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Annuler''')

        self.Button3 = tk.Button(self.pg1)
        self.Button3.place(relx=0.323, rely=0.424, height=26, width=73)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text='''Supprimer''')

        self.Labelframe1 = tk.LabelFrame(self.pg0)
        self.Labelframe1.place(relx=0.016, rely=0.0, relheight=0.219
                , relwidth=0.927)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(text='''Carnet d'adresses''')

        self.TCombobox1 = ttk.Combobox(self.Labelframe1)
        self.TCombobox1.place(relx=0.017, rely=0.09, relheight=0.116
                , relwidth=0.308, bordermode='ignore')
        self.TCombobox1.configure(takefocus="")

        self.Scrolledlistbox1 = ScrolledListBox(self.Labelframe1)
        self.Scrolledlistbox1.place(relx=0.017, rely=0.219, relheight=0.703
                , relwidth=0.96, bordermode='ignore')
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")

        self.Labelframe2 = tk.LabelFrame(self.pg0)
        self.Labelframe2.place(relx=0.016, rely=0.269, relheight=0.233
                , relwidth=0.927)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(text='''Liste sélectionnée''')

        self.Scrolledlistbox2 = ScrolledListBox(self.Labelframe2)
        self.Scrolledlistbox2.place(relx=0.017, rely=0.085, relheight=0.842
                , relwidth=0.96, bordermode='ignore')
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(cursor="xterm")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")

        self.TButton8 = ttk.Button(self.pg0)
        self.TButton8.place(relx=0.306, rely=0.226, height=25, width=73)
        self.TButton8.configure(takefocus="")
        self.TButton8.configure(text='''Ajouter''')

        self.TButton9 = ttk.Button(self.pg0)
        self.TButton9.place(relx=0.452, rely=0.226, height=25, width=73)
        self.TButton9.configure(takefocus="")
        self.TButton9.configure(text='''Enlever''')

        self.TButton10 = ttk.Button(self.pg0)
        self.TButton10.place(relx=0.306, rely=0.509, height=28, width=127)
        self.TButton10.configure(takefocus="")
        self.TButton10.configure(text='''Imprimer l'aperçu''')

        self.TButton11 = ttk.Button(self.pg0)
        self.TButton11.place(relx=0.565, rely=0.509, height=28, width=206)
        self.TButton11.configure(takefocus="")
        self.TButton11.configure(text='''Imprimer la liste sélectionnée''')

        self.Label10 = tk.Label(self.pg0)
        self.Label10.place(relx=0.032, rely=0.523, height=21, width=153)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(text='''Aperçu de l'impression''')

        self.Canvas1 = tk.Canvas(self.pg0)
        self.Canvas1.place(relx=0.113, rely=0.58, relheight=0.393
                , relwidth=0.677)
        self.Canvas1.configure(selectbackground="#d9d9d9")

        self.TButton12 = ttk.Button(self.pg0)
        self.TButton12.place(relx=0.145, rely=0.226, height=28, width=90)
        self.TButton12.configure(takefocus="")
        self.TButton12.configure(text='''Tout ajouter''')

        self.TButton15 = ttk.Button(self.pg0)
        self.TButton15.place(relx=0.597, rely=0.226, height=28, width=93)
        self.TButton15.configure(takefocus="")
        self.TButton15.configure(text='''Tout enlever''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





