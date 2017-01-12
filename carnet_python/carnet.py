#! /usr/bin/env python
# -*- coding: utf8 -*-
#
# GUI module generated by PAGE version 4.7
# In conjunction with Tcl version 8.6
#    Mar 28, 2016 08:30:01 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import carnet_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    carnet_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    carnet_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    carnet_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    carnet_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {DejaVu Sans} -size -12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans Mono} -size -12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x732+510+136")
        top.title("Carnet d'adresses")
        top.configure(highlightcolor="black")



        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TNotebook1.configure(width=602)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text="Détails",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text="Liste",underline="-1",)

        self.Label1 = Label(self.TNotebook1_pg0)
        self.Label1.place(relx=0.03, rely=0.08, height=18, width=32)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Nom''')

        self.Label2 = Label(self.TNotebook1_pg0)
        self.Label2.place(relx=0.03, rely=0.13, height=18, width=50)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Prénom''')

        self.Entry7 = Entry(self.TNotebook1_pg0)
        self.Entry7.place(relx=0.52, rely=0.04, relheight=0.03, relwidth=0.29)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(selectbackground="#c4c4c4")

        self.Entry2 = Entry(self.TNotebook1_pg0)
        self.Entry2.place(relx=0.18, rely=0.08, relheight=0.03, relwidth=0.63)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Entry3 = Entry(self.TNotebook1_pg0)
        self.Entry3.place(relx=0.18, rely=0.13, relheight=0.03, relwidth=0.63)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")

        self.Entry4 = Entry(self.TNotebook1_pg0)
        self.Entry4.place(relx=0.18, rely=0.17, relheight=0.03, relwidth=0.63)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")

        self.Entry6 = Entry(self.TNotebook1_pg0)
        self.Entry6.place(relx=0.18, rely=0.2, relheight=0.03, relwidth=0.63)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")

        self.Entry5 = Entry(self.TNotebook1_pg0)
        self.Entry5.place(relx=0.18, rely=0.24, relheight=0.03, relwidth=0.63)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")

        self.Entry1 = Entry(self.TNotebook1_pg0)
        self.Entry1.place(relx=0.18, rely=0.28, relheight=0.03, relwidth=0.63)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Entry8 = ScrolledText(self.TNotebook1_pg0)
        self.Entry8.place(relx=0.18, rely=0.32, relheight=0.1, relwidth=0.63)
        self.Entry8.configure(background="white")
        self.Entry8.configure(font=font10)
        self.Entry8.configure(insertborderwidth="3")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(width=10)
        self.Entry8.configure(wrap=NONE)

        self.Button1 = Button(self.TNotebook1_pg0)
        self.Button1.place(relx=0.63, rely=0.42, height=26, width=93)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Enregistrer''')

        self.TButton2 = ttk.Button(self.TNotebook1_pg0)
        self.TButton2.place(relx=0.83, rely=0.08, height=25, width=83)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Effacer''')

        self.Label3 = Label(self.TNotebook1_pg0)
        self.Label3.place(relx=0.03, rely=0.17, height=18, width=51)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Adresse''')

        self.Label4 = Label(self.TNotebook1_pg0)
        self.Label4.place(relx=0.03, rely=0.24, height=18, width=74)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''Code postal''')

        self.Label5 = Label(self.TNotebook1_pg0)
        self.Label5.place(relx=0.03, rely=0.28, height=18, width=28)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''Ville''')

        self.TButton1 = ttk.Button(self.TNotebook1_pg0)
        self.TButton1.place(relx=0.83, rely=0.28, height=25, width=83)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Effacer''')

        self.TButton3 = ttk.Button(self.TNotebook1_pg0)
        self.TButton3.place(relx=0.83, rely=0.13, height=25, width=83)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Effacer''')

        self.TButton4 = ttk.Button(self.TNotebook1_pg0)
        self.TButton4.place(relx=0.83, rely=0.18, height=25, width=83)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Effacer''')

        self.TButton5 = ttk.Button(self.TNotebook1_pg0)
        self.TButton5.place(relx=0.83, rely=0.24, height=25, width=83)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Effacer''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active',_ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(self.TNotebook1_pg0)
        self.TCheckbutton1.place(relx=0.03, rely=0.01, relwidth=0.12
                , relheight=0.0, height=18)
        self.TCheckbutton1.configure(variable=carnet_support.tch58)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Monsieur''')

        self.TCheckbutton2 = ttk.Checkbutton(self.TNotebook1_pg0)
        self.TCheckbutton2.place(relx=0.03, rely=0.04, relwidth=0.12
                , relheight=0.0, height=18)
        self.TCheckbutton2.configure(variable=carnet_support.tch58)
        self.TCheckbutton2.configure(takefocus="")
        self.TCheckbutton2.configure(text='''Madame''')

        self.TCheckbutton3 = ttk.Checkbutton(self.TNotebook1_pg0)
        self.TCheckbutton3.place(relx=0.17, rely=0.01, relwidth=0.24
                , relheight=0.0, height=18)
        self.TCheckbutton3.configure(variable=carnet_support.tch58)
        self.TCheckbutton3.configure(takefocus="")
        self.TCheckbutton3.configure(text='''Monsieur et Madame''')

        self.TCheckbutton4 = ttk.Checkbutton(self.TNotebook1_pg0)
        self.TCheckbutton4.place(relx=0.42, rely=0.01, relwidth=0.4
                , relheight=0.0, height=18)
        self.TCheckbutton4.configure(variable=carnet_support.tch58)
        self.TCheckbutton4.configure(takefocus="")
        self.TCheckbutton4.configure(text='''Monsieur et Madame et leurs enfants''')

        self.TButton6 = ttk.Button(self.TNotebook1_pg0)
        self.TButton6.place(relx=0.03, rely=0.42, height=25, width=83)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''Chercher''')

        self.TCheckbutton5 = ttk.Checkbutton(self.TNotebook1_pg0)
        self.TCheckbutton5.place(relx=0.17, rely=0.04, relwidth=0.16
                , relheight=0.0, height=18)
        self.TCheckbutton5.configure(variable=carnet_support.tch58)
        self.TCheckbutton5.configure(takefocus="")
        self.TCheckbutton5.configure(text='''Mademoiselle''')

        self.TCheckbutton6 = ttk.Checkbutton(self.TNotebook1_pg0)
        self.TCheckbutton6.place(relx=0.42, rely=0.04, relwidth=0.09
                , relheight=0.0, height=18)
        self.TCheckbutton6.configure(variable=carnet_support.tch58)
        self.TCheckbutton6.configure(takefocus="")
        self.TCheckbutton6.configure(text='''Autre''')

        self.TButton7 = ttk.Button(self.TNotebook1_pg0)
        self.TButton7.place(relx=0.83, rely=0.42, height=25, width=83)
        self.TButton7.configure(takefocus="")
        self.TButton7.configure(text='''Tout effacer''')

        self.TButton13 = ttk.Button(self.TNotebook1_pg0)
        self.TButton13.place(relx=0.83, rely=0.03, height=25, width=83)
        self.TButton13.configure(takefocus="")
        self.TButton13.configure(text='''Effacer''')

        self.Label7 = Label(self.TNotebook1_pg0)
        self.Label7.place(relx=0.03, rely=0.32, height=18, width=41)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(text='''Divers''')

        self.TButton14 = ttk.Button(self.TNotebook1_pg0)
        self.TButton14.place(relx=0.83, rely=0.35, height=25, width=83)
        self.TButton14.configure(takefocus="")
        self.TButton14.configure(text='''Effacer''')

        self.TNotebook2 = ttk.Notebook(self.TNotebook1_pg0)
        self.TNotebook2.place(relx=0.25, rely=0.46, relheight=0.51
                , relwidth=0.74)
        self.TNotebook2.configure(width=442)
        self.TNotebook2.configure(takefocus="")
        self.TNotebook2_pg0 = ttk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_pg0, padding=3)
        self.TNotebook2.tab(0, text="Aperçu de l'adresse",underline="-1",)
        self.TNotebook2_pg1 = ttk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_pg1, padding=3)
        self.TNotebook2.tab(1, text="Téléphone",underline="-1",)
        self.TNotebook2_pg2 = ttk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_pg2, padding=3)
        self.TNotebook2.tab(2, text="Courriel",underline="-1",)

        self.Button9 = Button(self.TNotebook2_pg0)
        self.Button9.place(relx=0.41, rely=0.03, height=26, width=82)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(text='''Imprimer''')

        self.Canvas2 = Canvas(self.TNotebook2_pg0)
        self.Canvas2.place(relx=0.02, rely=0.15, relheight=0.82, relwidth=0.95)
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(width=423)

        self.Label17 = Label(self.TNotebook2_pg1)
        self.Label17.place(relx=0.07, rely=0.06, height=18, width=32)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(text='''Nom''')

        self.Entry17 = Entry(self.TNotebook2_pg1)
        self.Entry17.place(relx=0.23, rely=0.06, relheight=0.06, relwidth=0.71)
        self.Entry17.configure(background="white")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(selectbackground="#c4c4c4")

        self.Label18 = Label(self.TNotebook2_pg1)
        self.Label18.place(relx=0.07, rely=0.14, height=18, width=52)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(text='''Numéro''')

        self.Entry18 = Entry(self.TNotebook2_pg1)
        self.Entry18.place(relx=0.23, rely=0.14, relheight=0.06, relwidth=0.71)
        self.Entry18.configure(background="white")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(selectbackground="#c4c4c4")

        self.Button11 = Button(self.TNotebook2_pg1)
        self.Button11.place(relx=0.07, rely=0.22, height=26, width=69)
        self.Button11.configure(activebackground="#d9d9d9")
        self.Button11.configure(text='''Ajouter''')

        self.Button12 = Button(self.TNotebook2_pg1)
        self.Button12.place(relx=0.36, rely=0.22, height=26, width=90)
        self.Button12.configure(activebackground="#d9d9d9")
        self.Button12.configure(text='''Supprimer''')

        self.Text3 = ScrolledText(self.TNotebook2_pg1)
        self.Text3.place(relx=0.07, rely=0.31, relheight=0.6, relwidth=0.87)
        self.Text3.configure(background="white")
        self.Text3.configure(font=font10)
        self.Text3.configure(insertborderwidth="3")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(width=10)
        self.Text3.configure(wrap=NONE)

        self.Label6 = Label(self.TNotebook2_pg2)
        self.Label6.place(relx=0.07, rely=0.06, height=18, width=100)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''Adresse courriel''')

        self.Entry9 = Entry(self.TNotebook2_pg2)
        self.Entry9.place(relx=0.07, rely=0.11, relheight=0.06, relwidth=0.87)
        self.Entry9.configure(background="white")
        self.Entry9.configure(font=font11)
        self.Entry9.configure(selectbackground="#c4c4c4")

        self.TButton16 = ttk.Button(self.TNotebook2_pg2)
        self.TButton16.place(relx=0.07, rely=0.22, height=25, width=83)
        self.TButton16.configure(takefocus="")
        self.TButton16.configure(text='''Ajouter''')

        self.TButton17 = ttk.Button(self.TNotebook2_pg2)
        self.TButton17.place(relx=0.29, rely=0.22, height=25, width=83)
        self.TButton17.configure(takefocus="")
        self.TButton17.configure(text='''Supprimer''')

        self.Scrolledtext1 = ScrolledText(self.TNotebook2_pg2)
        self.Scrolledtext1.place(relx=0.07, rely=0.3, relheight=0.6
                , relwidth=0.88)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font10)
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(width=10)
        self.Scrolledtext1.configure(wrap=NONE)

        self.Text1 = ScrolledText(self.TNotebook1_pg0)
        self.Text1.place(relx=0.03, rely=0.46, relheight=0.5, relwidth=0.21)
        self.Text1.configure(background=_bgcolor)
        self.Text1.configure(font=font10)
        self.Text1.configure(insertborderwidth="3")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="red")
        self.Text1.configure(width=10)
        self.Text1.configure(wrap=NONE)

        self.Button2 = Button(self.TNotebook1_pg0)
        self.Button2.place(relx=0.48, rely=0.42, height=26, width=73)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(state=DISABLED)
        self.Button2.configure(text='''Annuler''')

        self.Labelframe1 = LabelFrame(self.TNotebook1_pg1)
        self.Labelframe1.place(relx=0.02, rely=0.0, relheight=0.22
                , relwidth=0.96)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Carnet d'adresses''')
        self.Labelframe1.configure(width=575)

        self.TCombobox1 = ttk.Combobox(self.Labelframe1)
        self.TCombobox1.place(relx=0.02, rely=0.09, relheight=0.12
                , relwidth=0.31)
        self.TCombobox1.configure(takefocus="")

        self.Scrolledlistbox1 = ScrolledListBox(self.Labelframe1)
        self.Scrolledlistbox1.place(relx=0.02, rely=0.22, relheight=0.7
                , relwidth=0.96)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(width=78)

        self.Labelframe2 = LabelFrame(self.TNotebook1_pg1)
        self.Labelframe2.place(relx=0.02, rely=0.27, relheight=0.23
                , relwidth=0.96)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(text='''Liste sélectionnée''')
        self.Labelframe2.configure(width=575)

        self.Scrolledlistbox2 = ScrolledListBox(self.Labelframe2)
        self.Scrolledlistbox2.place(relx=0.02, rely=0.08, relheight=0.84
                , relwidth=0.96)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(width=78)

        self.TButton8 = ttk.Button(self.TNotebook1_pg1)
        self.TButton8.place(relx=0.32, rely=0.23, height=25, width=73)
        self.TButton8.configure(takefocus="")
        self.TButton8.configure(text='''Ajouter''')

        self.TButton9 = ttk.Button(self.TNotebook1_pg1)
        self.TButton9.place(relx=0.47, rely=0.23, height=25, width=73)
        self.TButton9.configure(takefocus="")
        self.TButton9.configure(text='''Enlever''')

        self.TButton10 = ttk.Button(self.TNotebook1_pg1)
        self.TButton10.place(relx=0.32, rely=0.51, height=25, width=119)
        self.TButton10.configure(takefocus="")
        self.TButton10.configure(text='''Imprimer l'aperçu''')

        self.TButton11 = ttk.Button(self.TNotebook1_pg1)
        self.TButton11.place(relx=0.58, rely=0.51, height=25, width=188)
        self.TButton11.configure(takefocus="")
        self.TButton11.configure(text='''Imprimer la liste sélectionnée''')

        self.Label10 = Label(self.TNotebook1_pg1)
        self.Label10.place(relx=0.03, rely=0.52, height=18, width=141)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(text='''Aperçu de l'impression''')

        self.Canvas1 = Canvas(self.TNotebook1_pg1)
        self.Canvas1.place(relx=0.12, rely=0.58, relheight=0.39, relwidth=0.7)
        self.Canvas1.configure(selectbackground="#d9d9d9")
        self.Canvas1.configure(width=420)

        self.TButton12 = ttk.Button(self.TNotebook1_pg1)
        self.TButton12.place(relx=0.15, rely=0.23, height=25, width=84)
        self.TButton12.configure(takefocus="")
        self.TButton12.configure(text='''Tout ajouter''')

        self.TButton15 = ttk.Button(self.TNotebook1_pg1)
        self.TButton15.place(relx=0.62, rely=0.23, height=25, width=86)
        self.TButton15.configure(takefocus="")
        self.TButton15.configure(text='''Tout enlever''')

        self.menubar = Menu(top,font=font10,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



    @staticmethod
    def popup1(event):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.post(event.x_root, event.y_root)





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

        #self.configure(yscrollcommand=self._autoscroll(vsb),
        #    xscrollcommand=self._autoscroll(hsb))
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
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

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
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



