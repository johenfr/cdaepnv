#!/usr/bin/env python
# -*- coding: utf8 -*-
# développé par Joseph

import xml.etree.ElementTree as ElementTree
import Tkinter as Tkinter
from Tkinter import StringVar, Tk, PhotoImage, Canvas
#from tkinter import *
from ttk import *
import tkMessageBox
import tkFont
from carnet import New_Toplevel_1, carnet_support
from copy import deepcopy
from os import remove, environ

######################################################################
# imports masqués non nécéssaires pour une utilisation python directe
# explicités pour pyinstaller
# from reportlab.pdfbase import _fontdata_widths_courier
# from reportlab.pdfbase import _fontdata_widths_courierbold
# from reportlab.pdfbase import _fontdata_widths_courieroblique
# from reportlab.pdfbase import _fontdata_widths_courierboldoblique
# from reportlab.pdfbase import _fontdata_widths_helvetica
# from reportlab.pdfbase import _fontdata_widths_helveticabold
# from reportlab.pdfbase import _fontdata_widths_helveticaoblique
# from reportlab.pdfbase import _fontdata_widths_helveticaboldoblique
# from reportlab.pdfbase import _fontdata_widths_timesroman
# from reportlab.pdfbase import _fontdata_widths_timesbold
# from reportlab.pdfbase import _fontdata_widths_timesitalic
# from reportlab.pdfbase import _fontdata_widths_timesbolditalic
# from reportlab.pdfbase import _fontdata_widths_symbol
# from reportlab.pdfbase import _fontdata_widths_zapfdingbats
# #
# from reportlab.pdfbase import _fontdata_enc_winansi
# from reportlab.pdfbase import _fontdata_enc_macroman
# from reportlab.pdfbase import _fontdata_enc_standard
# from reportlab.pdfbase import _fontdata_enc_symbol
# from reportlab.pdfbase import _fontdata_enc_zapfdingbats
# from reportlab.pdfbase import _fontdata_enc_pdfdoc
# from reportlab.pdfbase import _fontdata_enc_macexpert
# ######################################################################
#
# from reportlab.lib.pagesizes import A6, landscape
# from reportlab.pdfgen import canvas
import subprocess
from time import sleep
from threading import Thread


DEBUG = False

class Carnet_adresse(object):

    def format_nom(self, quidam):
        try:
            _prenom = quidam.find('Prénom'.decode('utf-8')).text + ' '
        except:
            _prenom = ''
        try:
            _nom_famille = quidam.find('Nom').text + ' '
        except:
            _nom_famille = ''
        if quidam.find('Civilité'.decode('utf-8')).text == '0':
            _nom = 'Mr ' + _prenom + _nom_famille
        elif quidam.find('Civilité'.decode('utf-8')).text == '1':
            _nom = 'Mme ' + _prenom + _nom_famille
        elif quidam.find('Civilité'.decode('utf-8')).text == '2':
            _nom = 'Mr et Mme ' + _prenom + _nom_famille
        elif quidam.find('Civilité'.decode('utf-8')).text == '3':
            _nom = 'Mr et Mme ' + _prenom + \
                    _nom_famille + ' et leurs enfants'
        elif quidam.find('Civilité'.decode('utf-8')).text == '4':
            _nom = 'Mlle ' + _prenom + _nom_famille
        else:
            _nom = quidam.find('Civilité'.decode('utf-8')).attrib['autre'] + ' ' + \
                    _prenom + _nom_famille
        return _nom


    def enveloppe(self,canvas_e, quidam):
        _FONT = tkFont.Font(family='French Script MT', weight='normal', size=14)
        #Canvas dans la fenêtre
        canvas_e.delete(Tkinter.ALL)
        canvas_e.create_rectangle(0, 0, 423, 278, fill='White', outline='White')
        #Enveloppe PDF
        #enveloppe = canvas.Canvas('enveloppe.ps', pagesize=landscape(A6))
        #width, height = A6
        #Ecriture
        position_x = 50
        position_y = 170
        _nom = self.format_nom(quidam)
        if quidam.find('Adresse2').text:
            #Canvas
            canvas_e.create_text(position_x, position_y, font="Altitude", text=_nom, anchor='nw')
            canvas_e.create_text(position_x, position_y+20,
                                    font=_FONT, text=quidam.find(unicode('Adresse1')).text,
                                    anchor='nw')
            canvas_e.create_text(position_x, position_y+40,
                                    font=_FONT, text=quidam.find('Adresse2').text,
                                    anchor='nw')
            canvas_e.create_text(position_x, position_y+60,
                                    font=_FONT, text=quidam.find('CodePostal').text + ' ' +
                                         quidam.find('Ville').text,
                                    anchor='nw')
            #Enveloppe PDF
            # enveloppe.create_text(120, 120, text=_nom, anchor='nw')
            # enveloppe.create_text(120, 100, text=quidam.find('Adresse1').text, anchor='nw')
            # enveloppe.create_text(120, 80, text=quidam.find('Adresse2').text, anchor='nw')
            # enveloppe.create_text(120, 60, text=quidam.find('CodePostal').text + ' ' +
            #                               quidam.find('Ville').text, anchor='nw')
        else:
            #Canvas
            canvas_e.create_text(position_x, position_y, font=_FONT, text=_nom, anchor='nw')
            canvas_e.create_text(position_x, position_y+20,
                                    font=_FONT, text=quidam.find('Adresse1').text,
                                    anchor='nw')
            canvas_e.create_text(position_x, position_y+40,
                                    font=_FONT, text=quidam.find('CodePostal').text + ' ' +
                                         quidam.find('Ville').text,
                                    anchor='nw')
            #Enveloppe PDF
            # enveloppe.create_text(120, 120, text=_nom, anchor='nw')
            # enveloppe.create_text(120, 100, text=quidam.find('Adresse1').text, anchor='nw')
            # enveloppe.create_text(120, 80, text=quidam.find('CodePostal').text + ' ' +
            #                               quidam.find('Ville').text, anchor='nw')
        canvas_e.postscript(file='enveloppe_tempo.ps')
        # Insertion du fichier pfa dans le fichier ps 
        with open('enveloppe.ps', 'w') as outfile:
            with open('enveloppe_tempo.ps') as infile:
                for line in infile:
                    outfile.write(line)
                    if "EndComments" in line :
                        with open('FrenchScriptMt.pfa') as fontfile:
                            for line in fontfile:
                                if line[0] != "%" :
                                    outfile.write(line)
        remove('enveloppe_tempo.ps')
        canvas_e.create_image(335,10, image=self.timbre, anchor='nw')
        #enveloppe.save()


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
            #self.id_imp = subprocess.Popen(["ping", "-c", "4", "-q", "8.8.8.8"],
            #                          stdout=subprocess.PIPE)
            self.id_imp = subprocess.Popen(["lpr", "-P", imprimante, "-o", "media=4X6",
                                       "-o", "sides=one-sided",
                                       "-o", "landscape", "enveloppe.ps"])
            if type_imp == 1 :
                thread_verif = Thread(None, verif_impression, None, (), {})
                thread_verif.start()

    def imprimer_liste(self, imprimante, *args):
        liste = self.fenetre.Scrolledlistbox2.get(0, Tkinter.END)
        nombre = len(liste)
        tic = 0
        if nombre >= 10:
            tkMessageBox.showinfo("Impression de liste", "Insérez 10 enveloppes")
        elif nombre == 1:
            tkMessageBox.showinfo("Impression de liste", "Insérez "+str(nombre) + " enveloppe")
        elif nombre > 1:
            tkMessageBox.showinfo("Impression de liste", "Insérez "+str(nombre) + " enveloppes")
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
                            tkMessageBox.showinfo("Impression de liste", "Insérez "+str(nombre) + " enveloppe")
                        elif nombre > 1:
                            tkMessageBox.showinfo("Impression de liste", "Insérez "+str(nombre) + " enveloppes")
                    self.enveloppe(self.fenetre.Canvas1, _personne)
                    self.imprimer(3)
                    tic += 1
                    while self.id_imp.poll() is None:
                        sleep(1)
        self.fenetre.Button9.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton10.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton11.configure(state=Tkinter.NORMAL)
        remove("enveloppe.pdf")


    def verif_impression(self, *args):
        while self.id_imp.poll() is None:
            sleep(1)
        self.fenetre.Button9.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton10.configure(state=Tkinter.NORMAL)
        self.fenetre.TButton11.configure(state=Tkinter.NORMAL)
        remove("enveloppe.pdf")


    def lettre_selection(self, _parent):
        _lettre = self.value_liste[_parent.current()]
        #self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].delete(0, Tkinter.END)
        liste_tempo = {}
        self.fenetre.Scrolledlistbox1.delete(0, Tkinter.END)
        for _personne in self.liste:
            if _personne.find('Nom').text[0] == _lettre or \
                _lettre == 'Toutes' or \
                ( _personne.find('Nom').text[0] == 'd' and \
                 _personne.find('Nom').text.split( )[1][0] == _lettre):
                _nom = self.format_nom(_personne)
                if _personne.find('Nom').text[0] == 'd' :
                    liste_tempo[_personne.find('Nom').text.split( )[1]+unicode(_personne.find('Prénom'.decode('utf-8')).text)] = _nom
                else:
                    liste_tempo[_personne.find('Nom').text+unicode(_personne.find('Prénom'.decode('utf-8')).text)] = _nom
                #self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].insert(0,_nom)
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
                        if not _personne.find('Sélection'.decode('utf-8')):
                            liste_select = ElementTree.Element('Sélection'.decode('utf-8'))
                            liste_select.text = '1'
                            _personne.append(liste_select)
                        else:
                            _personne.find('Sélection'.decode('utf-8')).text = '1'
        else:
            for _personne in self.liste:
                _nom = self.format_nom(_personne)
                if _nom not in self.fenetre.Scrolledlistbox2.get(0, Tkinter.END):
                    self.fenetre.Scrolledlistbox2.insert(0, _nom)
                if not _personne.find('Sélection'.decode('utf-8')):
                    liste_select = ElementTree.Element('Sélection'.decode('utf-8'))
                    liste_select.text = '1'
                    _personne.append(liste_select)
                else:
                    _personne.find('Sélection'.decode('utf-8')).text = '1'


    def personne_deselection(self, nombre, *args):
        if nombre == 1:
            num = self.fenetre.Scrolledlistbox2.curselection()
            self.fenetre.Scrolledlistbox2.delete(num)
        else:
            self.fenetre.Scrolledlistbox2.delete(0,Tkinter.END)


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
        #print _nom_i , _prenom_i
        ecrire = False
        test = 0
        for _personne in self.liste:
            _prenom_j = _personne.find('Prénom'.decode('utf-8')).text
            if not _prenom_j:
                _prenom_j = ''
            if _nom_i in _personne.find('Nom').text:
                if _prenom_i in _prenom_j:
                    ecrire = True
                elif _prenom_i == '':
                    print ('.')
                    ecrire = True
            elif _nom_i == '':
                if _prenom_i in _prenom_j:
                    ecrire = True
            if ecrire:
                if test == num:
                    self.tout_effacer()
                    self.fenetre.Entry2.insert(0,
                            _personne.find('Nom').text)
                    try:
                        self.fenetre.Entry3.insert(0,
                            _personne.find('Prénom'.decode('utf-8')).text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry4.insert(0,
                            _personne.find('Adresse1').text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry6.insert(0,
                            _personne.find('Adresse2').text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry5.insert(0,
                            _personne.find('CodePostal').text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry1.insert(0,
                            _personne.find('Ville').text)
                    except:
                        pass
                    self.changer_civilit(int(_personne.find('Civilité'.decode('utf-8')).text))
                    if int(_personne.find('Civilité'.decode('utf-8')).text) == 5:
                        self.fenetre.Entry7.insert(0,
                            _personne.find('Civilité'.decode('utf-8')).attrib['autre'])
                    for info in _personne.findall('Divers'):
                        self.fenetre.Entry8.insert(Tkinter.END,
                            info.text + "\n")
                    tele = _personne.find('Téléphone'.decode('utf-8'))
                    if tele.find('Numéro') is not None:
                        for notel in tele.findall('Numéro'):
                            self.fenetre.Text3.insert(0.0, notel.attrib['nom'] +
                            ' = ' + notel.text + "\n")
                    self.fenetre.Button11.config(command=lambda : self.ajouter(tele))
                    self.fenetre.Button12.config(command=lambda : self.supprimer(tele))
                    self.enveloppe(self.fenetre.Canvas2, _personne)
                ecrire = False
                test += 1
        if test > (num + 1):
            self.fenetre.TButton6.configure(text='''Suivant''')
            self.fenetre.TButton6.config(command=lambda : self.chercher(num + 1,
                                                             nom_i=_nom_i,
                                                             prenom_i=_prenom_i))
        else:
            self.fenetre.TButton6.configure(text='''Chercher''')
            self.fenetre.TButton6.config(command=lambda : self.chercher(0))


    def tout_effacer(self, *args):
        self.fenetre.Entry1.delete(0, Tkinter.END)
        self.fenetre.Entry2.delete(0, Tkinter.END)
        self.fenetre.Entry3.delete(0, Tkinter.END)
        self.fenetre.Entry4.delete(0, Tkinter.END)
        self.fenetre.Entry5.delete(0, Tkinter.END)
        self.fenetre.Entry6.delete(0, Tkinter.END)
        self.fenetre.Entry7.delete(0, Tkinter.END)
        self.fenetre.Entry8.delete(0.0, Tkinter.END)
        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
        self.fenetre.Text1.delete(0.0, Tkinter.END)
        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
        self.fenetre.Text3.delete(0.0, Tkinter.END)
        for i in range(0, 6):
            self.civilite[i].set(0)
        self.fenetre.TButton6.configure(text='''Chercher''')
        self.fenetre.TButton6.config(command=lambda : self.chercher(0))


    def effacer(self, *args):
        #print args
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


    def ajouter(self, element, *args):
        #print element.tag.encode('utf8')
        ajout = ElementTree.Element('Numéro'.decode('utf-8'))
        if  self.fenetre.Entry17.get() != '' and \
            self.fenetre.Entry18.get() != '':
            ajout.attrib['nom'] = self.fenetre.Entry17.get()
            #print ajout.attrib
            ajout.text = self.fenetre.Entry18.get()
            element.append(ajout)
            self.carnet.write(environ['HOME'] + '/.carnet/Carnet_d_adresses.xml', encoding='UTF-8')
        self.fenetre.Text3.delete(0.0, Tkinter.END)
        self.fenetre.Entry17.delete(0, Tkinter.END)
        self.fenetre.Entry18.delete(0, Tkinter.END)
        self.chercher(0)


    def supprimer(self, element, *args):
        nom = self.fenetre.Entry17.get()
        num = self.fenetre.Entry18.get()
        for notel in element.findall('Numéro'.decode('utf-8')):
            if notel.attrib['nom'] == nom and \
                notel.text == num:
                element.remove(notel)
        self.carnet.write(environ['HOME'] + '/.carnet/Carnet_d_adresses.xml', encoding='UTF-8')
        self.fenetre.Text3.delete(0.0, Tkinter.END)
        self.fenetre.Entry17.delete(0, Tkinter.END)
        self.fenetre.Entry18.delete(0, Tkinter.END)
        chercher(0)


    def enregistrer(self, num, *args):
        #print args
        if len(self.fenetre.Entry2.get()) > 1 or \
            len(self.fenetre.Entry3.get()) > 1:
            chgt = False
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                    _personne.find('Prénom'.decode('utf-8')).text == self.fenetre.Entry3.get():
                    chgt = True
                    if num == 0:
                        self.fenetre.Button1.configure(text='''Modifier''')
                        self.fenetre.Button1.config(command=lambda : self.enregistrer(1))
                        self.fenetre.Button2.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                            " " + self.fenetre.Entry2.get() +
                                            " existe déja. Modifier?\n".decode('utf-8'))
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    elif num == 1:
                        try:
                            _personne.find('Adresse1').text = self.fenetre.Entry4.get()
                        except:
                            pass
                        try:
                            _personne.find('Adresse2').text = self.fenetre.Entry6.get()
                        except:
                            pass
                        try:
                            _personne.find('CodePostal').text = \
                                                        self.fenetre.Entry5.get()
                        except:
                            pass
                        try:
                            _personne.find('Ville').text = self.fenetre.Entry1.get()
                        except:
                            pass
                        for i in range(0, 6):
                            if self.civilite[i].get() == '1':
                                _personne.find('Civilité'.decode('utf-8')).text = \
                                                        str(i)
                                if i == 5:
                                    _personne.find('Civilité'.decode('utf-8')).set('autre',
                                            self.fenetre.Entry7.get())
                        texte = self.fenetre.Entry8.get(0.0, Tkinter.END).split('\n')
                        #print texte
                        vieuxtexte = []
                        for info in _personne.findall('Divers'):
                            ligne = info.text
                            vieuxtexte.append(info.text)
                            if ligne not in texte:
                                _personne.remove(info)
                        for ligne in texte:
                            if ligne not in vieuxtexte:
                                #print '.'+ligne+'.'
                                if len(ligne) > 1:
                                    ajout = ElementTree.Element('Divers')
                                    ajout.text = ligne
                                    _personne.append(ajout)
                        self.fenetre.Button1.configure(text='''Enregistrer''')
                        self.fenetre.Button1.config(command=lambda : self.enregistrer(0))
                        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
                        #
                        self.carnet.write(environ['HOME'] + '/.carnet/Carnet_d_adresses.xml', encoding='UTF-8')
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                    " " + self.fenetre.Entry2.get() +
                                    " modifié.\n".decode('utf-8'))
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    else:
                        self.fenetre.Button1.configure(text='''Enregistrer''')
                        self.fenetre.Button1.config(command=lambda : self.enregistrer(0))
                        self.fenetre.Button2.configure(state=Tkinter.DISABLED)
                        self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                        self.fenetre.Text1.insert(0.0, "Opération annulée.\n".decode('utf-8'))
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
            #
            if not chgt:
                #copie du modèle
                ajout = deepcopy(self.modele)
                ajout.find('Nom').text = self.fenetre.Entry2.get()
                ajout.find('Prénom'.decode('utf-8')).text = self.fenetre.Entry3.get()
                try:
                    ajout.find('Adresse1').text = self.fenetre.Entry4.get()
                except:
                    pass
                try:
                    ajout.find('Adresse2').text = self.fenetre.Entry6.get()
                except:
                    pass
                try:
                    ajout.find('CodePostal').text = self.fenetre.Entry5.get()
                except:
                    pass
                try:
                    ajout.find('Ville').text = self.fenetre.Entry1.get()
                except:
                    pass
                for i in range(0, 6):
                    if self.civilite[i].get() == '1':
                        ajout.find('Civilité'.decode('utf-8')).text = str(i)
                        #print i, self.fenetre.Entry7.get()
                        if i == 5:
                            ajout.find('Civilité'.decode('utf-8')).set('autre',
                                                    self.fenetre.Entry7.get())
                self.liste.append(ajout)
                self.carnet.write(environ['HOME'] + '/.carnet/Carnet_d_adresses.xml', encoding='UTF-8')
                self.fenetre.Text1.configure(state=Tkinter.NORMAL)
                self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() + " " +
                                    self.fenetre.Entry2.get() + " enregistré.\n".decode('utf-8'))
                self.fenetre.Text1.configure(state=Tkinter.DISABLED)
            self.fenetre.TButton6.configure(text='''Chercher''')
            self.fenetre.TButton6.config(command=lambda : self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                    _personne.find('Prénom'.decode('utf-8')).text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.config(command=lambda : self.ajouter(_personne))
                    self.fenetre.Button12.config(command=lambda : self.supprimer(_personne))
    
    
    def changer_civilit(self, num, *args):
        for i in range(0, 6):
            if i == num:
                self.civilite[i].set(1)
            else:
                self.civilite[i].set(0)





    def lancer (self):
        #
        self.value_liste = ['Toutes', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                      'W', 'X', 'Y', 'Z']
        #
        root = Tk()
        _style = Style()
        #print(_style.theme_names())
        _style.theme_use('default')
        root.title("Carnet d'adresses")
        root.geometry('604x857+838+100')
        carnet_support.set_Tk_var()
        self.fenetre = New_Toplevel_1(root)
        carnet_support.init(root, self.fenetre)
        #
        _fichier = open(environ['HOME'] + '/.carnet/Carnet_d_adresses.xml', 'r')
        self.carnet = ElementTree.parse(_fichier,
                                   parser=ElementTree.XMLParser(encoding="utf-8"))
        self.liste = self.carnet.getroot()
        #
        _fichier_vide = open("./Carnet_d_adresses_vide.xml")
        self.modele = ElementTree.parse(_fichier_vide,
                        parser=ElementTree.XMLParser(encoding="utf-8")).getroot()
        #
        #configuration des éléments...
        #onglet Détails
        self.civilite = [StringVar(), StringVar(), StringVar(),
                    StringVar(), StringVar(), StringVar()]
        #
        self.fenetre.TButton6.config(command=lambda : self.chercher(0))
        self.fenetre.TButton1.config(command=lambda : self.effacer(1))
        self.fenetre.TButton2.config(command=lambda : self.effacer(2))
        self.fenetre.TButton3.config(command=lambda : self.effacer(3))
        self.fenetre.TButton4.config(command=lambda : self.effacer(4))
        self.fenetre.TButton5.config(command=lambda : self.effacer(5))
        self.fenetre.TButton14.config(command=lambda : self.effacer(6))
        self.fenetre.TButton7.config(command=self.tout_effacer)
        self.fenetre.Button11.config(command=lambda:
                                    self.ajouter(ElementTree.Element('rien')))
        self.fenetre.Button12.config(command=lambda:
                                    self.supprimer(ElementTree.Element('rien')))
        self.fenetre.Button1.config(command=lambda : self.enregistrer(0))
        self.fenetre.Button2.config(command=lambda : self.enregistrer(2))
        self.fenetre.TCheckbutton1.configure(variable=self.civilite[0],
                                    command=lambda : self.changer_civilit(0))
        self.fenetre.TCheckbutton2.configure(variable=self.civilite[1],
                                    command=lambda : self.changer_civilit(1))
        self.fenetre.TCheckbutton3.configure(variable=self.civilite[2],
                                    command=lambda : self.changer_civilit(2))
        self.fenetre.TCheckbutton4.configure(variable=self.civilite[3],
                                    command=lambda : self.changer_civilit(3))
        self.fenetre.TCheckbutton5.configure(variable=self.civilite[4],
                                    command=lambda : self.changer_civilit(4))
        self.fenetre.TCheckbutton6.configure(variable=self.civilite[5],
                                    command=lambda : self.changer_civilit(5))
        self.fenetre.Button9.config(command=lambda : self.imprimer(1))
        #onglet Liste
        self.fenetre.Canvas1.create_rectangle(0, 0, 423, 278, fill='White')
        self.timbre = PhotoImage(file="./timbre_pie_xii.gif")
        self.fenetre.Canvas1.create_image(335,10, image=self.timbre, anchor='nw')
        self.fenetre.Canvas1.image= self.timbre
        self.fenetre.Canvas2.create_rectangle(0, 0, 423, 278, fill='White')
        self.fenetre.Canvas2.create_image(335,10, image=self.timbre, anchor='nw')
        self.fenetre.TButton10.config(command=lambda : self.imprimer(1))
        self.fenetre.TButton11.config(command=lambda : self.imprimer(2))
        #selection de la lettre
        self.fenetre.TCombobox1.configure(values=self.value_liste)
        self.fenetre.TCombobox1.current(0)
        self.fenetre.TCombobox1.bind('<<ComboboxSelected>>',
                                lambda e: lettre_selection(self.fenetre.TCombobox1))
        self.lettre_selection(self.fenetre.TCombobox1)
        #selection d'une personne
        self.fenetre.TButton8.config(command=lambda : self.personne_selection(1))
        self.fenetre.TButton12.config(command=lambda : self.personne_selection(2))
        self.fenetre.TButton9.config(command=lambda : self.personne_deselection(1))
        self.fenetre.TButton15.config(command=lambda : self.personne_deselection(2))
        self.fenetre.Scrolledlistbox1.bind('<<ListboxSelect>>', lambda e: self.selection(e))
        self.fenetre.Scrolledlistbox2.bind('<<ListboxSelect>>', lambda e: self.selection(e))
    
        root.mainloop()

if __name__ == '__main__':
    carnet = Carnet_adresse()
    carnet.lancer()
