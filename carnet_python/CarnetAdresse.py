#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# développé par Joseph

import os
import xml.etree.ElementTree as ElementTree

try:
    import tkinter as Tkinter
    from tkinter import StringVar, Tk, PhotoImage, Canvas, END
    from tkinter import ttk
    from tkinter import messagebox as tkMessageBox
    import tkinter.font as tkFont
    unicode = str
except ImportError:
    import Tkinter
    from Tkinter import StringVar, Tk, PhotoImage, Canvas, END
    # from ttk import *
    import ttk
    import tkMessageBox
    import tkFont
    
import subprocess
from time import sleep
from threading import Thread
from copy import deepcopy
import os

from carnet import Carnet_d_adresses
from carnet import carnet_support


DEBUG = False


class CarnetAdresse(object):
    def __init__(self):
        self.value_liste = ['Toutes', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                            'W', 'X', 'Y', 'Z']
        self.root = Tk()
        defaultFont = tkFont.Font(family="Libertine", size=9, weight="normal")
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(family="Libertine", size=9, weight="normal")
        _style = ttk.Style()
        # print(_style.theme_names())
        _style.theme_use('default')
        self.root.option_add("*Font", defaultFont)
        self.root.option_add("*TkFixedFont", defaultFont)
        self.root.title("Carnet d'adresses")
        self.root.geometry('604x857+838+100')
        carnet_support.set_Tk_var()
        self.fenetre = Carnet_d_adresses(self.root)
        carnet_support.init(self.root, self.fenetre)
        self.civilite = [
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar()
        ]
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.timbre = PhotoImage(file=os.path.join(self.dir_path, "timbre_pie_xii.gif"))
        self.nom_fichier = os.environ['HOME'] + '/.carnet/Carnet_d_adresses.xml'
        #
        try:
            _fichier = open(self.nom_fichier, 'r')
        except FileNotFoundError:
            _fichier = open(self.nom_fichier, 'w')
            _fichier.write('<?xml version="1.0" encoding="UTF-8"?>\n<Carnet/>')
            _fichier.close()
            _fichier = open(self.nom_fichier, 'r')
        self.carnet = ElementTree.parse(_fichier,
                                        parser=ElementTree.XMLParser(encoding="utf-8"))
        _fichier.close()
        self.liste = self.carnet.getroot()
        self.liste[:] = sorted(self.liste, key=self.clef)
        #
        _fichier_vide = open(os.path.join(self.dir_path, "Carnet_d_adresses_vide.xml"))
        self.modele = ElementTree.parse(_fichier_vide,
                                        parser=ElementTree.XMLParser(encoding="utf-8")).getroot()
        _fichier_vide.close()
        #
        # configuration des éléments...
        # onglet Détails
        #
        self.fenetre.TButton6.config(command=lambda: self.chercher(0))
        self.fenetre.TButton1.config(command=lambda: self.effacer(1))
        self.fenetre.TButton2.config(command=lambda: self.effacer(2))
        self.fenetre.TButton3.config(command=lambda: self.effacer(3))
        self.fenetre.TButton4.config(command=lambda: self.effacer(4))
        self.fenetre.TButton5.config(command=lambda: self.effacer(5))
        self.fenetre.TButton14.config(command=lambda: self.effacer(6))
        self.fenetre.TButton13.config(command=lambda: self.effacer(7))
        self.fenetre.TButton7.config(command=self.tout_effacer)
        self.fenetre.Button11.config(command=lambda: self.ajouter(ElementTree.Element('rien')))
        self.fenetre.Button12.config(command=lambda: self.supprimer_tel(ElementTree.Element('rien')))
        self.fenetre.Button1.config(command=lambda: self.enregistrer(0))
        self.fenetre.Button2.config(command=lambda: self.enregistrer(2))
        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
        self.fenetre.Button3.config(command=lambda: self.supprimer(0))
        self.fenetre.Button3.configure(state=Tkinter.DISABLED)
        self.fenetre.TCheckbutton1.configure(variable=self.civilite[0],
                                             command=lambda: self.changer_civilit(0))
        self.fenetre.TCheckbutton2.configure(variable=self.civilite[1],
                                             command=lambda: self.changer_civilit(1))
        self.fenetre.TCheckbutton3.configure(variable=self.civilite[2],
                                             command=lambda: self.changer_civilit(2))
        self.fenetre.TCheckbutton4.configure(variable=self.civilite[3],
                                             command=lambda: self.changer_civilit(3))
        self.fenetre.TCheckbutton5.configure(variable=self.civilite[4],
                                             command=lambda: self.changer_civilit(4))
        self.fenetre.TCheckbutton6.configure(variable=self.civilite[5],
                                             command=lambda: self.changer_civilit(5))
        self.fenetre.Button9.config(command=lambda: self.imprimer(1))
        # onglet Liste
        self.fenetre.Canvas1.create_rectangle(0, 0, 423, 278, fill='White')
        self.fenetre.Canvas1.create_image(335, 10, image=self.timbre, anchor='nw')
        self.fenetre.Canvas1.image = self.timbre
        self.fenetre.Canvas2.create_rectangle(0, 0, 423, 278, fill='White')
        self.fenetre.Canvas2.create_image(335, 10, image=self.timbre, anchor='nw')
        self.fenetre.TButton10.config(command=lambda: self.imprimer(1))
        self.fenetre.TButton11.config(command=lambda: self.imprimer(2))
        # selection de la lettre
        self.fenetre.TCombobox1.configure(values=self.value_liste)
        self.fenetre.TCombobox1.current(0)
        self.fenetre.TCombobox1.bind('<<ComboboxSelected>>',
                                     lambda e: self.lettre_selection(self.fenetre.TCombobox1))
        self.lettre_selection(self.fenetre.TCombobox1)
        # selection d'une personne
        self.fenetre.TButton8.config(command=lambda: self.personne_selection(1))
        self.fenetre.TButton12.config(command=lambda: self.personne_selection(2))
        self.fenetre.TButton9.config(command=lambda: self.personne_deselection(1))
        self.fenetre.TButton15.config(command=lambda: self.personne_deselection(2))
        self.fenetre.Scrolledlistbox1.bind('<<ListboxSelect>>', lambda e: self.selection(e))
        self.fenetre.Scrolledlistbox2.bind('<<ListboxSelect>>', lambda e: self.selection(e))
        #
        self.fenetre.Text1.configure(foreground="grey")
        self.fenetre.Text1.tag_configure("NOIR", foreground="black")

    @staticmethod
    def format_nom(quidam):
        try:
            _prenom = quidam.find('Prénom').text + ' '
        except TypeError:
            _prenom = ''
        try:
            _nom_famille = quidam.find('Nom').text + ' '
        except TypeError:
            _nom_famille = ''
        if quidam.find('Civilité').text == '0':
            _nom = 'Mr ' + _prenom + _nom_famille
        elif quidam.find('Civilité').text == '1':
            _nom = 'Mme ' + _prenom + _nom_famille
        elif quidam.find('Civilité').text == '2':
            _nom = 'Mr et Mme ' + _prenom + _nom_famille
        elif quidam.find('Civilité').text == '3':
            _nom = 'Mr et Mme ' + _prenom + _nom_famille + ' et leurs enfants'
        elif quidam.find('Civilité').text == '4':
            _nom = 'Mlle ' + _prenom + _nom_famille
        else:
            _nom = ' '
            # _nom = quidam.find('Civilité').attrib['autre'] + ' ' + _prenom + _nom_famille
        return _nom

    def remplir_canvas(self, canvas_e, quidam, _FONT):
        # Canvas dans la fenêtre
        canvas_e.delete(Tkinter.ALL)
        canvas_e.create_rectangle(0, 0, 423, 278, fill='White', outline='White')
        # Ecriture
        position_x = 50
        position_y = 170
        _nom = self.format_nom(quidam)
        if quidam.find('Adresse2').text:
            # Canvas
            canvas_e.create_text(position_x, position_y, font=_FONT, text=_nom, anchor='nw')
            canvas_e.create_text(position_x, position_y + 20,
                                 font=_FONT, text=quidam.find(unicode('Adresse1')).text,
                                 anchor='nw')
            canvas_e.create_text(position_x, position_y + 40,
                                 font=_FONT, text=quidam.find('Adresse2').text,
                                 anchor='nw')
            canvas_e.create_text(position_x, position_y + 60,
                                 font=_FONT, text=quidam.find('CodePostal').text + ' ' +
                                                  quidam.find('Ville').text,
                                 anchor='nw')
        else:
            # Canvas
            canvas_e.create_text(position_x, position_y, font=_FONT, text=_nom, anchor='nw')
            canvas_e.create_text(position_x, position_y + 20,
                                 font=_FONT, text=quidam.find('Adresse1').text,
                                 anchor='nw')
            canvas_e.create_text(position_x,
                                 position_y + 40,
                                 font=_FONT,
                                 text=quidam.find('CodePostal').text + ' ' +
                                      quidam.find('Ville').text,
                                 anchor='nw')

    def enveloppe(self, canvas_e, quidam):
        _FONT = tkFont.Font(family='Montez, Classic', weight='normal', size=20)
        _FONT_min = tkFont.Font(family='Montez', weight='normal', size=15)
        self.remplir_canvas(canvas_e, quidam, _FONT)
        canvas_e.postscript(file='enveloppe_tempo.ps')
        # Insertion du fichier pfa dans le fichier ps
        with open('enveloppe.ps', 'w') as outfile:
            with open('enveloppe_tempo.ps') as infile:
                for line in infile:
                    outfile.write(line)
                    if "EndComments" in line:
                        with open('Montez.pfa') as fontfile:
                            for line in fontfile:
                                if line[0] != "%":
                                    outfile.write(line)
        os.remove('enveloppe_tempo.ps')
        # réduire la taille pour l'aperçu
        self.remplir_canvas(canvas_e, quidam, _FONT_min)
        canvas_e.create_image(335, 10, image=self.timbre, anchor='nw')

    def imprimer(self, type_imp, *args):
        self.fenetre.Button9.configure(state=Tkinter.DISABLED)
        self.fenetre.TButton10.configure(state=Tkinter.DISABLED)
        self.fenetre.TButton11.configure(state=Tkinter.DISABLED)
        imprimante = subprocess.Popen(["lpstat", "-d"],
                                      stdout=subprocess.PIPE).stdout.readline().split(': ')[1][0:-1]
        #
        if type_imp == 2:
            self.id_imp = None
            thread_verif = Thread(None, self.imprimer_liste, None, (imprimante,), {})
            thread_verif.start()
        else:
            # options génériques données par man lp
            # self.id_imp = subprocess.Popen(["ping", "-c", "4", "-q", "8.8.8.8"],
            #                          stdout=subprocess.PIPE)
            self.id_imp = subprocess.Popen(["lpr", "-P", imprimante, "-o", "media=4X6",
                                            "-o", "sides=one-sided", "-o", "fit-to-page",
                                            "-o", "landscape", "enveloppe.ps"])
            if type_imp == 1:
                thread_verif = Thread(None, self.verif_impression, None, (), {})
                thread_verif.start()

    def imprimer_liste(self, imprimante, *args):
        liste = self.fenetre.Scrolledlistbox2.get(0, Tkinter.END)
        nombre = len(liste)
        tic = 0
        if nombre >= 10:
            tkMessageBox.showinfo("Impression de liste", "Insérez 10 enveloppes")
        elif nombre == 1:
            tkMessageBox.showinfo("Impression de liste", "Insérez " + str(nombre) + " enveloppe")
        elif nombre > 1:
            tkMessageBox.showinfo("Impression de liste", "Insérez " + str(nombre) + " enveloppes")
        for ligne in liste:
            for _personne in self.liste:
                _nom = self.format_nom(_personne)
                if _nom in ligne:
                    if tic == 10:
                        nombre -= 10
                        tic = 0
                        if nombre >= 10:
                            tkMessageBox.showinfo("Impression de liste", "Insérez 10 enveloppes")
                        elif nombre == 1:
                            tkMessageBox.showinfo("Impression de liste", "Insérez " + str(nombre) + " enveloppe")
                        elif nombre > 1:
                            tkMessageBox.showinfo("Impression de liste", "Insérez " + str(nombre) + " enveloppes")
                    self.enveloppe(self.fenetre.Canvas1, _personne)
                    self.imprimer(3)
                    tic += 1
                    while self.id_imp.poll() is None:
                        sleep(1)
        self.fenetre.Button9.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton10.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton11.configure(state=Tkinter.NORMAL)

    def verif_impression(self, *args):
        while self.id_imp.poll() is None:
            sleep(1)
        self.fenetre.Button9.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton10.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton11.configure(state=Tkinter.NORMAL)

    def lettre_selection(self, _parent):
        _lettre = self.value_liste[_parent.current()]
        # self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].delete(0, Tkinter.END)
        liste_tempo = {}
        self.fenetre.Scrolledlistbox1.delete(0, Tkinter.END)
        for _personne in self.liste:
            if _personne.find('Nom').text[0] == _lettre or \
                    _lettre == 'Toutes' or \
                    (_personne.find('Nom').text[0] == 'd' and \
                     _personne.find('Nom').text.split()[1][0] == _lettre):
                _nom = self.format_nom(_personne)
                if _personne.find('Nom').text[0] == 'd':
                    liste_tempo[_personne.find('Nom').text.split()[1] + unicode(_personne.find('Prénom').text)] = _nom
                else:
                    liste_tempo[_personne.find('Nom').text + unicode(_personne.find('Prénom').text)] = _nom
                # self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].insert(0,_nom)
        for quidam in sorted(liste_tempo.keys()):
            self.fenetre.Scrolledlistbox1.insert(Tkinter.END, liste_tempo[quidam])

    def personne_selection(self, nombre, *args):
        if nombre == 1:
            _ajout = self.fenetre.Scrolledlistbox1.selection_get()
            if _ajout not in self.fenetre.Scrolledlistbox2.get(0, Tkinter.END):
                self.fenetre.Scrolledlistbox2.insert(0, _ajout)
                for _personne in self.liste:
                    _nom = self.format_nom(_personne)
                    if _nom in _ajout:
                        if not _personne.find('Sélection'):
                            liste_select = ElementTree.Element('Sélection')
                            liste_select.text = '1'
                            _personne.append(liste_select)
                        else:
                            _personne.find('Sélection').text = '1'
        else:
            for _personne in self.liste:
                _nom = self.format_nom(_personne)
                if _nom not in self.fenetre.Scrolledlistbox2.get(0, Tkinter.END):
                    self.fenetre.Scrolledlistbox2.insert(0, _nom)
                if not _personne.find('Sélection'):
                    liste_select = ElementTree.Element('Sélection')
                    liste_select.text = '1'
                    _personne.append(liste_select)
                else:
                    _personne.find('Sélection').text = '1'

    def personne_deselection(self, nombre, *args):
        if nombre == 1:
            num = self.fenetre.Scrolledlistbox2.curselection()
            self.fenetre.Scrolledlistbox2.delete(num)
        else:
            self.fenetre.Scrolledlistbox2.delete(0, Tkinter.END)

    def selection(self, e, *args):
        _ajout = self.fenetre.Scrolledlistbox1.selection_get()
        for _personne in self.liste:
            _nom = self.format_nom(_personne)
            if _nom in _ajout:
                self.enveloppe(self.fenetre.Canvas1, _personne)

    def chercher(self, num, nom_i=1, prenom_i=1, *args):
        if nom_i == 1:
            _nom_i = self.fenetre.Entry2.get()
            _prenom_i = self.fenetre.Entry3.get()
        else:
            _nom_i = nom_i
            _prenom_i = prenom_i
        # print _nom_i , _prenom_i
        ecrire = False
        test = 0
        for _personne in self.liste:
            _prenom_j = _personne.find('Prénom').text
            if not _prenom_j:
                _prenom_j = ''
            if _nom_i in _personne.find('Nom').text:
                if _prenom_i in _prenom_j:
                    ecrire = True
                elif _prenom_i == '':
                    print('.')
                    ecrire = True
            elif _nom_i == '':
                if _prenom_i in _prenom_j:
                    ecrire = True
            if ecrire:
                if test == num:
                    self.tout_effacer()
                    self.fenetre.Button3.configure(state=Tkinter.NORMAL)
                    self.fenetre.Entry2.insert(0,
                                               _personne.find('Nom').text)
                    try:
                        self.fenetre.Entry3.insert(0,
                                                   _personne.find('Prénom').text)
                    except AttributeError:
                        pass
                    try:
                        self.fenetre.Entry4.insert(0,
                                                   _personne.find('Adresse1').text)
                    except AttributeError:
                        pass
                    try:
                        self.fenetre.Entry6.insert(0,
                                                   _personne.find('Adresse2').text)
                    except AttributeError:
                        pass
                    try:
                        self.fenetre.Entry5.insert(0,
                                                   _personne.find('CodePostal').text)
                    except AttributeError:
                        pass
                    try:
                        self.fenetre.Entry1.insert(0,
                                                   _personne.find('Ville').text)
                    except AttributeError:
                        pass
                    self.changer_civilit(int(_personne.find('Civilité').text))
                    if int(_personne.find('Civilité').text) == 5:
                        self.fenetre.Entry7.insert(0,
                                                   _personne.find('Civilité').attrib['autre'])
                    for info in _personne.findall('Divers'):
                        self.fenetre.Entry8.insert(Tkinter.END,
                                                   info.text + "\n")
                    tele = _personne.find('Téléphone')
                    if tele.find('Numéro') is not None:
                        for notel in tele.findall('Numéro'):
                            self.fenetre.Text3.insert(0.0, notel.attrib['nom'] +
                                                      ' = ' + notel.text + "\n")
                    self.fenetre.Button11.config(command=lambda: self.ajouter(tele))
                    self.fenetre.Button12.config(command=lambda: self.supprimer_tel(tele))
                    self.enveloppe(self.fenetre.Canvas2, _personne)
                ecrire = False
                test += 1
        if test > (num + 1):
            self.fenetre.TButton6.configure(text='''Suivant''')
            self.fenetre.TButton6.config(command=lambda: self.chercher(num + 1,
                                                                       nom_i=_nom_i,
                                                                       prenom_i=_prenom_i))
        else:
            self.fenetre.TButton6.configure(text='''Chercher''')
            self.fenetre.TButton6.config(command=lambda: self.chercher(0))

    def tout_effacer(self, *args):
        self.fenetre.Entry1.delete(0, Tkinter.END)
        self.fenetre.Entry2.delete(0, Tkinter.END)
        self.fenetre.Entry3.delete(0, Tkinter.END)
        self.fenetre.Entry4.delete(0, Tkinter.END)
        self.fenetre.Entry5.delete(0, Tkinter.END)
        self.fenetre.Entry6.delete(0, Tkinter.END)
        self.fenetre.Entry7.delete(0, Tkinter.END)
        self.fenetre.Entry8.delete(0.0, Tkinter.END)
        # self.fenetre.Text1.configure(state=Tkinter.NORMAL)
        # self.fenetre.Text1.delete(0.0, Tkinter.END)
        # self.fenetre.Text1.configure(state=Tkinter.DISABLED)
        self.fenetre.Text3.delete(0.0, Tkinter.END)
        for i in range(0, 6):
            self.civilite[i].set(0)
        self.fenetre.TButton6.configure(text='''Chercher''')
        self.fenetre.TButton6.config(command=lambda: self.chercher(0))

    def effacer(self, *args):
        # print args
        num = args[0]
        if num == 1:
            self.fenetre.Entry1.delete(0, Tkinter.END)
        if num == 2:
            self.fenetre.Entry2.delete(0, Tkinter.END)
        if num == 3:
            self.fenetre.Entry3.delete(0, Tkinter.END)
        if num == 4:
            self.fenetre.Entry4.delete(0, Tkinter.END)
        if num == 5:
            self.fenetre.Entry5.delete(0, Tkinter.END)
        if num == 4:
            self.fenetre.Entry6.delete(0, Tkinter.END)
        if num == 6:
            self.fenetre.Entry8.delete(0, Tkinter.END)
        if num == 7:
            self.fenetre.Entry7.delete(0, Tkinter.END)
            for i in range(0, 6):
                self.civilite[i].set(0)

    def ajouter(self, element, *args):
        # print element.tag.encode('utf8')
        ajout = ElementTree.Element('Numéro')
        if self.fenetre.Entry17.get() != '' and \
                self.fenetre.Entry18.get() != '':
            ajout.attrib['nom'] = self.fenetre.Entry17.get()
            # print ajout.attrib
            ajout.text = self.fenetre.Entry18.get()
            element.append(ajout)
            self.carnet.write(self.nom_fichier, encoding='UTF-8')
        self.fenetre.Text3.delete(0.0, Tkinter.END)
        self.fenetre.Entry17.delete(0, Tkinter.END)
        self.fenetre.Entry18.delete(0, Tkinter.END)
        self.chercher(0)

    def supprimer_tel(self, element, *args):
        nom = self.fenetre.Entry17.get()
        num = self.fenetre.Entry18.get()
        for notel in element.findall('Numéro'):
            if notel.attrib['nom'] == nom and \
                    notel.text == num:
                element.remove(notel)
        self.carnet.write(self.nom_fichier, encoding='UTF-8')
        self.fenetre.Text3.delete(0.0, Tkinter.END)
        self.fenetre.Entry17.delete(0, Tkinter.END)
        self.fenetre.Entry18.delete(0, Tkinter.END)
        self.chercher(0)

    def supprimer(self, num, *args):
        if len(self.fenetre.Entry2.get()) > 1 or \
                len(self.fenetre.Entry3.get()) > 1:
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    if num == 0:
                        self.fenetre.Button3.config(command=lambda: self.supprimer(1))
                        self.fenetre.Button2.configure(state=Tkinter.NORMAL)
                        self.fenetre.Button2.config(command=lambda: self.supprimer(2))
                        self.fenetre.Button1.configure(state=Tkinter.DISABLED)
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Voulez-vous vraiment supprimer " +
                                                  self.fenetre.Entry3.get() +
                                                  " " + self.fenetre.Entry2.get() +
                                                  "?\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    elif num == 1:
                        self.liste.remove(_personne)
                        self.fenetre.Button3.config(command=lambda: self.supprimer(0))
                        self.fenetre.Button3.configure(state=Tkinter.DISABLED)
                        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
                        self.fenetre.Button2.config(command=lambda: self.enregistrer(2))
                        self.fenetre.Button1.configure(state=Tkinter.NORMAL)
                        #
                        self.carnet.write(self.nom_fichier, encoding='UTF-8')
                        entree = self.fenetre.Entry3.get() + " " + self.fenetre.Entry2.get()
                        self.tout_effacer()
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Entrée " + entree + " supprimée.\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                        entree = ''
                    else:
                        self.fenetre.Button3.config(command=lambda: self.supprimer(0))
                        self.fenetre.Button3.configure(state=Tkinter.DISABLED)
                        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
                        self.fenetre.Button1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Suppression annulée.\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
            #
            self.fenetre.TButton6.configure(text='''Chercher''')
            self.fenetre.TButton6.config(command=lambda: self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.config(command=lambda: self.ajouter(_personne))
                    self.fenetre.Button12.config(command=lambda: self.supprimer_tel(_personne))

    def enregistrer(self, num, *args):
        # print args
        if len(self.fenetre.Entry2.get()) > 1 or len(self.fenetre.Entry3.get()) > 1:
            chgt = False
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    chgt = True
                    if num == 0:
                        self.fenetre.Button1.configure(text='''Modifier''')
                        self.fenetre.Button1.config(command=lambda: self.enregistrer(1))
                        self.fenetre.Button2.configure(state=Tkinter.NORMAL)
                        self.fenetre.Button3.configure(state=Tkinter.DISABLED)
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                                  " " + self.fenetre.Entry2.get() +
                                                  " existe déja. Modifier?\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    elif num == 1:
                        try:
                            _personne.find('Adresse1').text = self.fenetre.Entry4.get()
                        except AttributeError:
                            pass
                        try:
                            _personne.find('Adresse2').text = self.fenetre.Entry6.get()
                        except AttributeError:
                            pass
                        try:
                            _personne.find('CodePostal').text = \
                                self.fenetre.Entry5.get()
                        except AttributeError:
                            pass
                        try:
                            _personne.find('Ville').text = self.fenetre.Entry1.get()
                        except AttributeError:
                            pass
                        for i in range(0, 6):
                            if self.civilite[i].get() == '1':
                                _personne.find('Civilité').text = \
                                    str(i)
                                if i == 5:
                                    _personne.find('Civilité').set('autre',
                                                                   self.fenetre.Entry7.get())
                        texte = self.fenetre.Entry8.get(0.0, Tkinter.END).split('\n')
                        # print texte
                        vieuxtexte = []
                        for info in _personne.findall('Divers'):
                            ligne = info.text
                            vieuxtexte.append(info.text)
                            if ligne not in texte:
                                _personne.remove(info)
                        for ligne in texte:
                            if ligne not in vieuxtexte:
                                # print '.'+ligne+'.'
                                if len(ligne) > 1:
                                    ajout = ElementTree.Element('Divers')
                                    ajout.text = ligne
                                    _personne.append(ajout)
                        self.fenetre.Button1.configure(text='''Enregistrer''')
                        self.fenetre.Button1.config(command=lambda: self.enregistrer(0))
                        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
                        #
                        self.carnet.write(self.nom_fichier, encoding='UTF-8')
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                                  " " + self.fenetre.Entry2.get() +
                                                  " modifié.\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    else:
                        self.fenetre.Button1.configure(text='''Enregistrer''')
                        self.fenetre.Button1.config(command=lambda: self.enregistrer(0))
                        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, "Opération annulée.\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
            #
            if not chgt:
                # copie du modèle
                ajout = deepcopy(self.modele)
                ajout.find('Nom').text = self.fenetre.Entry2.get()
                ajout.find('Prénom').text = self.fenetre.Entry3.get()
                try:
                    ajout.find('Adresse1').text = self.fenetre.Entry4.get()
                except AttributeError:
                    pass
                try:
                    ajout.find('Adresse2').text = self.fenetre.Entry6.get()
                except AttributeError:
                    pass
                try:
                    ajout.find('CodePostal').text = self.fenetre.Entry5.get()
                except AttributeError:
                    pass
                try:
                    ajout.find('Ville').text = self.fenetre.Entry1.get()
                except AttributeError:
                    pass
                for i in range(0, 6):
                    if self.civilite[i].get() == '1':
                        ajout.find('Civilité').text = str(i)
                        # print i, self.fenetre.Entry7.get()
                        if i == 5:
                            ajout.find('Civilité').set('autre',
                                                       self.fenetre.Entry7.get())
                self.liste.append(ajout)
                self.carnet.write(self.nom_fichier, encoding='UTF-8')
                self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() + " " +
                                          self.fenetre.Entry2.get() + " enregistré.\n", "NOIR")
                self.fenetre.Text1.configure(state=Tkinter.DISABLED)
            self.fenetre.TButton6.configure(text='''Chercher''')
            self.fenetre.TButton6.config(command=lambda: self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.config(command=lambda: self.ajouter(_personne))
                    self.fenetre.Button12.config(command=lambda: self.supprimer_tel(_personne))

    def changer_civilit(self, num, *args):
        for i in range(0, 6):
            if i == num:
                self.civilite[i].set(1)
            else:
                self.civilite[i].set(0)

    @staticmethod
    def clef(elem):
        return elem.findtext("Nom")

    def lancer(self):
        self.root.mainloop()


if __name__ == '__main__':
    carnet = CarnetAdresse()
    carnet.lancer()
