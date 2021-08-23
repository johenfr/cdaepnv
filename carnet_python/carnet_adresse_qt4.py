#!/usr/bin/env python
# -*- coding: utf8 -*-
# développé par Joseph

import sys
import os
import time
try:
    import xml.etree.ElementTree as ElementTree
except ImportError as e:
    import ElementTree
from copy import deepcopy
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import QSizeF, Qt
from PyQt5.QtGui import QPainter
from carnet_qt4 import Ui_MainWindow

class Carnet_adresse(object):

    def format_nom(self, quidam):
        try:
            _prenom = quidam.find('Prénom').text + ' '
        except:
            _prenom = ''
        try:
            _nom_famille = quidam.find('Nom').text + ' '
        except:
            _nom_famille = ''
        if quidam.find('Civilité').text == '0':
            _nom = 'Mr ' + _prenom + _nom_famille
        elif quidam.find('Civilité').text == '1':
            _nom = 'Mme ' + _prenom + _nom_famille
        elif quidam.find('Civilité').text == '2':
            _nom = 'Mr et Mme ' + _prenom + _nom_famille
        elif quidam.find('Civilité').text == '3':
            _nom = 'Mr et Mme ' + _prenom + \
                   _nom_famille + ' et leurs enfants'
        elif quidam.find('Civilité').text == '4':
            _nom = 'Mlle ' + _prenom + _nom_famille
        else:
            _nom = quidam.find('Civilité').attrib['autre'] + ' ' + _prenom + _nom_famille
        _nom = _nom.replace("  ", " ")
        return _nom

    def enveloppe(self, quidam=None):
        if quidam is None:
           quidam = self.quidam
        self.fenetre.plainTextEdit.setPlainText("")
        police = self.fenetre.fontComboBox.currentFont()
        police.setPixelSize(20)
        self.fenetre.plainTextEdit.setFont(police)
        self.fenetre.plainTextEdit.insertPlainText(self.format_nom(quidam) + "\n")
        if quidam.find('Adresse2').text:
            try:
                self.fenetre.plainTextEdit.insertPlainText(quidam.find('Adresse1').text + "\n")
            except:
                pass
            try:
                self.fenetre.plainTextEdit.insertPlainText(quidam.find('Adresse2').text + "\n")
            except:
                pass
            try:
                self.fenetre.plainTextEdit.insertPlainText(quidam.find('CodePostal').text + " " + 
                                                        quidam.find('Ville').text)
            except:
                pass
        else:
            try:
                self.fenetre.plainTextEdit.insertPlainText(quidam.find('Adresse1').text + "\n")
            except:
                pass
            try:
                self.fenetre.plainTextEdit.insertPlainText(quidam.find('CodePostal').text + " " + 
                        quidam.find('Ville').text)
            except:
                pass
        police = self.fenetre.fontComboBox_2.currentFont()
        police.setPixelSize(20)
        self.fenetre.plainTextEdit_2.setFont(police)
        self.fenetre.plainTextEdit_2.setPlainText(self.fenetre.plainTextEdit.toPlainText())

    def imprimer(self, type_imp, *args):
        self.fenetre.Button9.setDisabled(True)
        imprimante = QPrinter(QPrinter.PrinterResolution)
        imprimante.setDuplex(False)
        imprimante.setPaperSource(imprimante.Auto)
        imprimante.setPaperSize(QSizeF(4,6), imprimante.Inch)
        imprimante.setPageMargins(20.0, 60.0, 10.0, 10.0, imprimante.Millimeter)
        imprimante.setOrientation(imprimante.Landscape)
        imprimante.setColorMode(imprimante.Color)
        painter = QPainter()
        painter.begin(imprimante)
        police = self.fenetre.fontComboBox.currentFont()
        police.setPixelSize(18)
        painter.setFont(police)
        painter.drawText(0,0,imprimante.width(),imprimante.height(), Qt.AlignLeft+Qt.TextWordWrap, self.fenetre.plainTextEdit.toPlainText())
        painter.end()
        self.fenetre.Button9.setDisabled(False)

    def imprimer_liste(self, imprimante, *args):
        self.fenetre.Button9.setDisabled(True)
        self.fenetre.TButton10.setDisabled(True)
        self.fenetre.TButton11.setDisabled(True)
        liste_i = self.fenetre.plainTextEdit_2.toPlainText().split("\n")
        nombre = len(liste_i)
        tic = 0
        if nombre >= 10:
            QMessageBox.showinfo("Impression de liste", "Insérez 10 enveloppes")
        elif nombre == 1:
            QMessageBox.showinfo("Impression de liste", "Insérez 1 enveloppe")
        elif nombre > 1:
            QMessageBox.showinfo("Impression de liste", "Insérez " + str(nombre) + " enveloppes")
        for ligne in liste_i:
            for _personne in self.liste:
                _nom = self.format_nom(_personne)
                if _nom in ligne:
                    if tic == 10:
                        nombre -= 10
                        tic = 0
                        if nombre >= 10:
                            QMessageBox.showinfo("Impression de liste", "Insérez 10 enveloppes")
                        elif nombre == 1:
                            QMessageBox.showinfo("Impression de liste", "Insérez 1 enveloppe")
                        elif nombre > 1:
                            QMessageBox.showinfo("Impression de liste", "Insérez " + str(nombre) + " enveloppes")
                    self.enveloppe( _personne)
                    self.imprimer(3)
                    tic += 1
                    time.sleep(1)
        self.fenetre.Button9.setDisabled(False)
        self.fenetre.TButton10.setDisabled(False)
        self.fenetre.TButton11.setDisabled(False)


    def lettre_selection(self):
        _lettre = self.fenetre.TCombobox1.currentText()
        # self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].setText("")
        liste_tempo = {}
        self.fenetre.listWidget.clear()
        for _personne in self.liste:
            if _personne.find('Nom').text[0] == _lettre or \
                    _lettre == 'Toutes' or \
                    (_personne.find('Nom').text[0] == 'd' and \
                     _personne.find('Nom').text.split()[1][0] == _lettre):
                _nom = self.format_nom(_personne)
                if _personne.find('Nom').text[0] == 'd':
                    if  _personne.find('Prénom').text is not None:
                        liste_tempo[_personne.find('Nom').text.split()[1] + 
                            _personne.find('Prénom').text] = _nom
                    else:
                        liste_tempo[_personne.find('Nom').text.split()[1]] = _nom
                else:
                    if  _personne.find('Prénom').text is not None:
                        liste_tempo[
                            _personne.find('Nom').text + _personne.find('Prénom').text] = _nom
                    else:    
                        liste_tempo[
                            _personne.find('Nom').text] = _nom
                # self.fenetre.Scrolledlistbox1.subwidget_list['listbox'].insert(0,_nom)
        for quidam in sorted(liste_tempo.keys()):
            self.fenetre.listWidget.addItem(liste_tempo[quidam])

    def personne_selection(self, nombre, *args):
        if nombre == 1:
            _ajout = self.fenetre.listWidget.selectedItems()[0].text()
            if  not self.fenetre.listWidget_2.findItems(_ajout, Qt.MatchFixedString):
                self.fenetre.listWidget_2.addItem(_ajout)

    def personne_deselection(self, nombre, *args):
        for i in self.fenetre.listWidget_2.selectedItems():
            self.fenetre.listWidget_2.takeItem(self.fenetre.listWidget_2.row(i))

    def selection(self, *args):
        _ajout = self.fenetre.listWidget.currentItem().text()
        for _personne in self.liste:
            _nom = self.format_nom(_personne)
            if _nom in _ajout:
                self.quidam = _personne
                self.enveloppe(_personne)

    def selection2(self, *args):
        _ajout = self.fenetre.listWidget_2.currentItem().text()
        for _personne in self.liste:
            _nom = self.format_nom(_personne)
            if _nom in _ajout:
                self.quidam = _personne
                self.enveloppe(_personne)
    
    def chercher(self, num, nom_i=1, prenom_i=1, *args):
        if nom_i == 1:
            _nom_i = self.fenetre.Entry2.text()
            _prenom_i = self.fenetre.Entry3.text()
        else:
            _nom_i = nom_i
            _prenom_i = prenom_i
        
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
                        self.fenetre.Entry3.setText(_personne.find('Prénom').text)
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
                    self.changer_civilit(int(_personne.find('Civilité').text))
                    if int(_personne.find('Civilité').text) == 5:
                        self.fenetre.Entry7.setText(_personne.find('Civilité').attrib['autre'])
                    self.fenetre.Entry8.setPlainText("")
                    for info in _personne.findall('Divers'):
                        self.fenetre.Entry8.insertPlainText(info.text + "\n")
                    tele = _personne.find('Téléphone')
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
                    self.quidam = _personne
                    self.enveloppe(_personne)
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
        ajout = ElementTree.Element('Numéro')
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
        for notel in element.findall('Numéro'):
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
                    _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    if num == 0:
                        self.fenetre.Button3.clicked.disconnect()
                        self.fenetre.Button3.clicked.connect(lambda state : self.supprimer(1))
                        self.fenetre.Button2.setDisabled(False)
                        self.fenetre.Button2.clicked.disconnect()
                        self.fenetre.Button2.clicked.connect(lambda state : self.supprimer(2))
                        self.fenetre.Button1.setDisabled(True)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Voulez-vous vraiment supprimer " +
                                            self.fenetre.Entry3.get() +
                                            " " + self.fenetre.Entry2.get() +
                                            "?\n", "NOIR")
                        self.fenetre.Text1.configure(state=Tkinter.DISABLED)
                    elif num == 1:
                        self.liste.remove(_personne)
                        self.fenetre.Button3.clicked.connect(lambda state : self.supprimer(0))
                        self.fenetre.Button3.setDisabled(True)
                        self.fenetre.Button2.setDisabled(True)
                        self.fenetre.Button2.clicked.connect(lambda state : self.enregistrer(2))
                        self.fenetre.Button1.setDisabled(False)
                        #
                        #self.carnet.write(self.nom_fichier, encoding='UTF-8')
                        entree = self.fenetre.Entry3.get() + " " + self.fenetre.Entry2.get()
                        self.tout_effacer()
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Entrée "+ entree + " supprimée.\n", "NOIR")
                        self.fenetre.Text1.setDisabled(True)
                        entree = ''
                    else:
                        self.fenetre.Button3.clicked.connect(lambda state : self.supprimer(0))
                        self.fenetre.Button3.setDisabled(True)
                        self.fenetre.Button2.setDisabled(True)
                        self.fenetre.Button1.setDisabled(False)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, Tkinter.END)
                        self.fenetre.Text1.insert(0.0, "Suppression annulée.\n", "NOIR")
                        self.fenetre.Text1.setDisabled(True)
            #
            self.fenetre.TButton6.setText('''Chercher''')
            self.fenetre.TButton6.clicked.connect(lambda state : self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                    _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.clicked.connect(lambda state : self.ajouter(_personne))
                    self.fenetre.Button12.clicked.connect(lambda state : self.supprimer_tel(_personne))

    def enregistrer(self, num, *args):
        # print args
        if len(self.fenetre.Entry2.get()) > 1 or \
                len(self.fenetre.Entry3.get()) > 1:
            chgt = False
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    chgt = True
                    if num == 0:
                        self.fenetre.Button1.setText('''Modifier''')
                        self.fenetre.Button1.clicked.disconnect()
                        self.fenetre.Button1.clicked.connect(lambda state: self.enregistrer(1))
                        self.fenetre.Button2.setDisabled(False)
                        self.fenetre.Button3.setDisabled(True)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() +
                                                  " " + self.fenetre.Entry2.get() +
                                                  " existe déja. Modifier?\n", "NOIR")
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
                                                  " modifié.\n", "NOIR")
                        self.fenetre.Text1.setDisabled(True)
                    else:
                        self.fenetre.Button1.setText('''Enregistrer''')
                        self.fenetre.Button1.clicked.disconnect()
                        self.fenetre.Button1.clicked.connect(lambda state: self.enregistrer(0))
                        self.fenetre.Button2.setDisabled(True)
                        self.fenetre.Text1.setDisabled(False)
                        self.fenetre.Text1.tag_remove("NOIR", 0.0, END)
                        self.fenetre.Text1.insert(0.0, "Opération annulée.\n", "NOIR")
                        self.fenetre.Text1.setDisabled(True)
            #
            if not chgt:
                # copie du modèle
                ajout = deepcopy(self.modele)
                ajout.find('Nom').text = self.fenetre.Entry2.get()
                ajout.find('Prénom').text = self.fenetre.Entry3.get()
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
                        ajout.find('Civilité').text = str(i)
                        # print i, self.fenetre.Entry7.get()
                        if i == 5:
                            ajout.find('Civilité').set('autre', self.fenetre.Entry7.get())
                self.liste.append(ajout)
                self.carnet.write(self.nom_fichier, encoding='UTF-8')
                self.fenetre.Text1.setDisabled(False)
                self.fenetre.Text1.insert(0.0, self.fenetre.Entry3.get() + " " +
                                          self.fenetre.Entry2.get() + " enregistré.\n", "NOIR")
                self.fenetre.Text1.setDisabled(True)
            self.fenetre.TButton6.setText('''Chercher''')
            self.fenetre.TButton6.clicked.connect(lambda state: self.chercher(0))
            for _personne in self.liste:
                if _personne.find('Nom').text == self.fenetre.Entry2.get() and \
                        _personne.find('Prénom').text == self.fenetre.Entry3.get():
                    self.fenetre.Button11.clicked.disconnect()
                    self.fenetre.Button11.clicked.connect(lambda state: self.ajouter(_personne))
                    self.fenetre.Button12.clicked.disconnect()
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
            _fichier = open(self.nom_fichier, 'r', encoding='utf-8')
        except:
            _fichier = open(self.nom_fichier, 'w', encoding='utf-8')
            _fichier.write('<?xml version="1.0" encoding="UTF-8"?>\n<Carnet/>')
            _fichier.close()
            _fichier = open(self.nom_fichier, 'r', encoding='utf-8')
        self.carnet = ElementTree.parse(_fichier)
        _fichier.close()
        self.liste = self.carnet.getroot()
        self.liste[:] = sorted(self.liste, key=self.clef)
        #.
        _fichier_vide = open("./Carnet_d_adresses_vide.xml", 'r', encoding='utf-8')
        self.modele = ElementTree.parse(_fichier_vide).getroot()
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
        self.fenetre.TButton10.clicked.connect(lambda state: self.imprimer(1))
        self.fenetre.fontComboBox.currentFontChanged.connect (lambda state: self.enveloppe())
        self.fenetre.fontComboBox_2.currentFontChanged.connect (lambda state: self.enveloppe())
        self.fenetre.TCombobox1.currentTextChanged.connect(lambda state: self.lettre_selection())
        self.fenetre.listWidget.clicked.connect(lambda state: self.selection())
        self.fenetre.listWidget_2.clicked.connect(lambda state: self.selection2())
        self.fenetre.TButton8.clicked.connect(lambda state: self.personne_selection(1))
        self.fenetre.TButton9.clicked.connect(lambda state: self.personne_deselection(1))
        self.fenetre.TButton15.clicked.connect(lambda state: self.fenetre.listWidget_2.clear())
        self.lettre_selection()
        self.window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    carnet = Carnet_adresse()
    carnet.lancer()
