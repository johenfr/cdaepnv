#!/usr/bin/env python
# -*- coding: utf8 -*-
# développé par Joseph

import sys
import os
import xml.etree.ElementTree as ElementTree
from copy import deepcopy
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from carnet_qt4 import Ui_MainWindow

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
            canvas_e.create_text(position_x, position_y + 40,
                                 font=_FONT, text=quidam.find('CodePostal').text + ' ' +
                                                  quidam.find('Ville').text,
                                 anchor='nw')

    def enveloppe(self, canvas_e, quidam):
        _FONT = tkFont.Font(family='Montez', weight='normal', size=20)
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
        remove('enveloppe_tempo.ps')
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
        # self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].setText("")
        liste_tempo = {}
        self.fenetre.Scrolledlistbox1.setText("")
        for _personne in self.liste:
            if _personne.find('Nom').text[0] == _lettre or \
                    _lettre == 'Toutes' or \
                    (_personne.find('Nom').text[0] == 'd' and \
                     _personne.find('Nom').text.split()[1][0] == _lettre):
                _nom = self.format_nom(_personne)
                if _personne.find('Nom').text[0] == 'd':
                    liste_tempo[_personne.find('Nom').text.split()[1] + unicode(
                        _personne.find('Prénom'.decode('utf-8')).text)] = _nom
                else:
                    liste_tempo[
                        _personne.find('Nom').text + unicode(_personne.find('Prénom'.decode('utf-8')).text)] = _nom
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
            self.fenetre.Scrolledlistbox2.setText("")

    def selection(self, e, *args):
        _ajout = self.fenetre.Scrolledlistbox1.selection_get()
        for _personne in self.liste:
            _nom = self.format_nom(_personne)
            if _nom in _ajout:
                self.enveloppe(self.fenetre.Canvas1, _personne)

    def chercher(self, num, nom_i=1, prenom_i=1, *args):
        if nom_i == 1:
            _nom_i = self.fenetre.Entry2.text()
            _prenom_i = self.fenetre.Entry3.text()
        else:
            _nom_i = nom_i
            _prenom_i = prenom_i
        # print _nom_i , _prenom_i
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
                    #self.tout_effacer()
                    #self.fenetre.Button3.configure(state=Tkinter.NORMAL)
                    self.fenetre.Entry2.setText(_personne.find('Nom').text)
                    try:
                        self.fenetre.Entry3.setText(_personne.find('Prénom'.decode('utf-8')).text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry4.setText(_personne.find('Adresse1').text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry6.setText(_personne.find('Adresse2').text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry5.setText(_personne.find('CodePostal').text)
                    except:
                        pass
                    try:
                        self.fenetre.Entry1.setText(_personne.find('Ville').text)
                    except:
                        pass
                    self.changer_civilit(int(_personne.find('Civilité'.decode('utf-8')).text))
                    if int(_personne.find('Civilité'.decode('utf-8')).text) == 5:
                        self.fenetre.Entry7.setText(_personne.find('Civilité'.decode('utf-8')).attrib['autre'])
                    self.fenetre.Entry8.setPlainText("")
                    for info in _personne.findall('Divers'):
                        self.fenetre.Entry8.insertPlainText(info.text + "\n")
                    tele = _personne.find('Téléphone'.decode('utf-8'))
                    if tele.find('Numéro') is not None:
                        for notel in tele.findall('Numéro'):
                            self.fenetre.Text3.insert(notel.attrib['nom'] +
                                                      ' = ' + notel.text + "\n")
                    try:
                        self.fenetre.Button11.clicked.disconnect()
                        self.fenetre.Button12.clicked.disconnect()
                    except:
                        pass
                    self.fenetre.Button11.clicked.connect(lambda state : self.ajouter(tele))
                    self.fenetre.Button12.clicked.connect(lambda state : self.supprimer_tel(tele))
                    #self.enveloppe(self.fenetre.Canvas2, _personne)
                ecrire = False
                test += 1
        if test > (num + 1):
            self.fenetre.TButton6.setText('''Suivant''')
            self.fenetre.TButton6.clicked.disconnect()
            self.fenetre.TButton6.clicked.connect(lambda state: self.chercher(num+1, nom_i=_nom_i, prenom_i=_prenom_i))
        else:
            self.fenetre.TButton6.setText('''Chercher''')
            self.fenetre.TButton6.clicked.disconnect()
            self.fenetre.TButton6.clicked.connect(lambda state : self.chercher(0))

    def tout_effacer(self, *args):
        self.fenetre.Entry1.setText("")
        self.fenetre.Entry2.setText("")
        self.fenetre.Entry3.setText("")
        self.fenetre.Entry4.setText("")
        self.fenetre.Entry5.setText("")
        self.fenetre.Entry6.setText("")
        self.fenetre.Entry7.setText("")
        self.fenetre.Entry8.setPlainText("")
        self.fenetre.Text3.setPlainText("")
        self.fenetre.buttonGroup.setExclusive(False)
        for i in range(0, 6):
            self.fenetre.buttonGroup.buttons()[i].setChecked(False)
        self.fenetre.buttonGroup.setExclusive(True)
        self.fenetre.TButton6.setText('''Chercher''')
        self.fenetre.TButton6.clicked.disconnect()
        self.fenetre.TButton6.clicked.connect(lambda state: self.chercher(0))
        self.fenetre.Button3.setDisabled(True)

    def effacer(self, *args):
        # print args
        num = args[0]
        if num == 1:
            self.fenetre.Entry1.setText("")
        if num == 2:
            self.fenetre.Entry2.setText("")
        if num == 3:
            self.fenetre.Entry3.setText("")
        if num == 4:
            self.fenetre.Entry4.setText("")
        if num == 5:
            self.fenetre.Entry5.setText("")
        if num == 4:
            self.fenetre.Entry6.setText("")
        if num == 6:
            self.fenetre.Entry8.setPlainText("")
        if num == 7:
            self.fenetre.Entry7.setText("")
            self.fenetre.buttonGroup.setExclusive(False)
            for i in range(0, 6):
                self.fenetre.buttonGroup.buttons()[i].setChecked(False)
            self.fenetre.buttonGroup.setExclusive(True)

    def ajouter(self, element, *args):
        # print element.tag.encode('utf8')
        ajout = ElementTree.Element('Numéro'.decode('utf-8'))
        if self.fenetre.Entry17.text() != '' and \
                self.fenetre.Entry18.get() != '':
            ajout.attrib['nom'] = self.fenetre.Entry17.get()
            # print ajout.attrib
            ajout.text = self.fenetre.Entry18.get()
            element.append(ajout)
            self.carnet.write(self.nom_fichier, encoding='UTF-8')
        self.fenetre.Text3.setText("")
        self.fenetre.Entry17.setText("")
        self.fenetre.Entry18.setText("")
        self.chercher(0)

    def supprimer_tel(self, element, *args):
        nom = self.fenetre.Entry17.get()
        num = self.fenetre.Entry18.get()
        for notel in element.findall('Numéro'.decode('utf-8')):
            if notel.attrib['nom'] == nom and \
                    notel.text == num:
                element.remove(notel)
        self.carnet.write(self.nom_fichier, encoding='UTF-8')
        self.fenetre.Text3.setText("")
        self.fenetre.Entry17.setText("")
        self.fenetre.Entry18.setText("")
        self.chercher(0)

    def supprimer(self, num, *args):
        if len(self.fenetre.Entry2.get()) > 1 or \
            len(self.fenetre.Entry3.get()) > 1:
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                    _personne.find('Prénom'.decode('utf-8')).text == self.fenetre.Entry3.get():
                    if num == 0:
                        self.fenetre.Button3.clicked.connect(lambda state : self.supprimer(1))
                        self.fenetre.Button2.setDisabled(False)
                        self.fenetre.Button2.clicked.connect(lambda state : self.supprimer(2))
                        self.fenetre.Button1.setDisabled(True)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Voulez-vous vraiment supprimer " +
                                            self.fenetre.Entry3.get() +
                                            " " + self.fenetre.Entry2.get() +
                                            "?\n".decode('utf-8'), "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    elif num == 1:
                        self.liste.remove(_personne)
                        self.fenetre.Button3.clicked.connect(lambda state : self.supprimer(0))
                        self.fenetre.Button3.setDisabled(True)
                        self.fenetre.Button2.setDisabled(True)
                        self.fenetre.Button2.clicked.connect(lambda state : self.enregistrer(2))
                        self.fenetre.Button1.setDisabled(False)
                        #
                        self.carnet.write(self.nom_fichier, encoding='UTF-8')
                        entree = self.fenetre.Entry3.get() + " " + self.fenetre.Entry2.get()
                        self.tout_effacer()
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Entrée "+ entree + " supprimée.\n".decode('utf-8'), "NOIR")
                        self.fenetre.Text1.setDisabled(True)
                        entree = ''
                    else:
                        self.fenetre.Button3.clicked.connect(lambda state : self.supprimer(0))
                        self.fenetre.Button3.setDisabled(True)
                        self.fenetre.Button2.setDisabled(True)
                        self.fenetre.Button1.setDisabled(False)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Suppression annulée.\n".decode('utf-8'), "NOIR")
                        self.fenetre.Text1.setDisabled(True)
            #
            self.fenetre.TButton6.setText('''Chercher''')
            self.fenetre.TButton6.clicked.connect(lambda state : self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                    _personne.find('Prénom'.decode('utf-8')).text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.clicked.connect(lambda state : self.ajouter(_personne))
                    self.fenetre.Button12.clicked.connect(lambda state : self.supprimer_tel(_personne))

    def enregistrer(self, num, *args):
        # print args
        if len(self.fenetre.Entry2.get()) > 1 or \
                len(self.fenetre.Entry3.get()) > 1:
            chgt = False
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom'.decode('utf-8')).text == self.fenetre.Entry3.get():
                    chgt = True
                    if num == 0:
                        self.fenetre.Button1.setText('''Modifier''')
                        self.fenetre.Button1.clicked.connect(lambda state: self.enregistrer(1))
                        self.fenetre.Button2.setDisabled(False)
                        self.fenetre.Button3.setDisabled(True)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                                  " " + self.fenetre.Entry2.get() +
                                                  " existe déja. Modifier?\n".decode('utf-8'), "NOIR")
                        self.fenetre.Text1.setDisabled(True)
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
                        self.fenetre.Button1.setText('''Enregistrer''')
                        self.fenetre.Button1.clicked.disconnect()
                        self.fenetre.Button1.clicked.connect(lambda state: self.enregistrer(0))
                        self.fenetre.Button2.setDisabled(True)
                        #
                        self.carnet.write(self.nom_fichier, encoding='UTF-8')
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                                  " " + self.fenetre.Entry2.get() +
                                                  " modifié.\n".decode('utf-8'), "NOIR")
                        self.fenetre.Text1.setDisabled(True)
                    else:
                        self.fenetre.Button1.setText('''Enregistrer''')
                        self.fenetre.Button1.clicked.connect(lambda state: self.enregistrer(0))
                        self.fenetre.Button2.setDisabled(True)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, "Opération annulée.\n".decode('utf-8'), "NOIR")
                        self.fenetre.Text1.setDisabled(True)
            #
            if not chgt:
                # copie du modèle
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
                        # print i, self.fenetre.Entry7.get()
                        if i == 5:
                            ajout.find('Civilité'.decode('utf-8')).set('autre',
                                                                       self.fenetre.Entry7.get())
                self.liste.append(ajout)
                self.carnet.write(self.nom_fichier, encoding='UTF-8')
                self.fenetre.Text1.setDisabled(False)
                self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() + " " +
                                          self.fenetre.Entry2.get() + " enregistré.\n".decode('utf-8'), "NOIR")
                self.fenetre.Text1.setDisabled(True)
            self.fenetre.TButton6.setText('''Chercher''')
            self.fenetre.TButton6.clicked.connect(lambda state: self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom'.decode('utf-8')).text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.clicked.connect(lambda state: self.ajouter(_personne))
                    self.fenetre.Button12.clicked.connect(lambda state: self.supprimer_tel(_personne))

    def changer_civilit(self, num, *args):
        self.fenetre.buttonGroup.setExclusive(False)
        for i in range(0, 6):
            if i == num:
                self.fenetre.buttonGroup.buttons()[i].setChecked(True)
            else:
                self.fenetre.buttonGroup.buttons()[i].setChecked(False)
        self.fenetre.buttonGroup.setExclusive(True)

    def clef(self, elem):
        return elem.findtext("Nom")

    def lancer(self):
        # Récuperation des adresses
        self.nom_fichier = os.getenv('HOME') + '/.carnet/Carnet_d_adresses.xml'
        
        try:
            _fichier = open(self.nom_fichier, 'r')
        except:
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
        _fichier_vide = open("./Carnet_d_adresses_vide.xml")
        self.modele = ElementTree.parse(_fichier_vide,
                                        parser=ElementTree.XMLParser(encoding="utf-8")).getroot()
        _fichier_vide.close()
        #
        # configuration des éléments...
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.fenetre = Ui_MainWindow()
        self.fenetre.setupUi(self.window)
        self.fenetre.TButton6.clicked.connect(lambda state, x=0 :self.chercher(x))
        self.fenetre.TButton1.clicked.connect(lambda state : self.effacer(1))
        self.fenetre.TButton2.clicked.connect(lambda state : self.effacer(2))
        self.fenetre.TButton3.clicked.connect(lambda state : self.effacer(3))
        self.fenetre.TButton4.clicked.connect(lambda state : self.effacer(4))
        self.fenetre.TButton5.clicked.connect(lambda state : self.effacer(5))
        self.fenetre.TButton14.clicked.connect(lambda state : self.effacer(6))
        self.fenetre.TButton13.clicked.connect(lambda state : self.effacer(7))
        self.fenetre.TButton7.clicked.connect(self.tout_effacer)
        self.fenetre.Button12.clicked.connect(lambda state:
                                    self.supprimer_tel(ElementTree.Element('rien')))
        self.fenetre.Button1.clicked.connect(lambda state: self.enregistrer(0))
        self.fenetre.Button2.clicked.connect(lambda state: self.enregistrer(2))
        self.fenetre.Button2.setDisabled(True)
        self.fenetre.Button3.clicked.connect(lambda state: self.supprimer(0))
        self.fenetre.Button3.setDisabled(True)
        self.fenetre.Button9.clicked.connect(lambda state: self.imprimer(1))
        self.window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    carnet = Carnet_adresse()
    carnet.lancer()
