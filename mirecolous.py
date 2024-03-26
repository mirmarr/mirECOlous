import sqlite3
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

import webbrowser


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('glav.ui', self)
        self.con = sqlite3.connect('program.db')

        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)

        self.name_gg.setText('  Банка')
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select adress,description from Zerowaste \
                           WHERE id=?",(1,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(2)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        pix=QPixmap('Фото\\zw2.png')
        self.karta_gg.setPixmap(pix)

        self.btn1.clicked.connect(self.onAct_1)
        self.btn2.clicked.connect(self.onAct_2)
        self.btn3.clicked.connect(self.onAct_3)
        self.btn4.clicked.connect(self.onAct_4)
        self.open_map.clicked.connect(self.onAct_map_fav)

    # Загрузка главной страницы и информации в правой таблице

    def onAct_glav(self):
        uic.loadUi('glav.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)

        self.name_gg.setText('  Банка')
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select adress,description from Zerowaste \
                           WHERE id=?",(1,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(2)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        pix=QPixmap('Фото\\zw2.png')
        self.karta_gg.setPixmap(pix)

        self.btn1.clicked.connect(self.onAct_1)
        self.btn2.clicked.connect(self.onAct_2)
        self.btn3.clicked.connect(self.onAct_3)
        self.btn4.clicked.connect(self.onAct_4)
        self.open_map.clicked.connect(self.onAct_map_fav)

    # Обработка нажатия на кнопку "Главная"


    def onAct_1(self):
        self.name_gg.setText('  Банка')
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select adress,description from Zerowaste \
                         WHERE id=?",(1,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(2)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        pix=QPixmap('Фото\\zw2.png')
        self.karta_gg.setPixmap(pix)

    # Обработка нажатия на 1 кнопку "Рекомендуем"

    def onAct_2(self):
        self.name_gg.setText('  Чердак')
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select adress,description from Other \
                         WHERE id=?",(1,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(2)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        pix=QPixmap('Фото\\ot2.png')
        self.karta_gg.setPixmap(pix)

    # Обработка нажатия на 2 кнопку "Рекомендуем"

    def onAct_3(self):
        self.name_gg.setText('  Green Cafee')
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select adress,description from Veg \
                          WHERE id=?",(1,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(2)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        pix=QPixmap('Фото\\veg2.png')
        self.karta_gg.setPixmap(pix)

    # Обработка нажатия на 3 кнопку "Рекомендуем"

    def onAct_4(self):
        self.name_gg.setText('  Surf Coffee')
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select adress,description from WYC \
                          WHERE id=?",(2,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(2)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        pix=QPixmap('Фото\\wyc3.png')
        self.karta_gg.setPixmap(pix)

    # Обработка нажатия на 4 кнопку "Рекомендуем"


    def onAct_sh(self):
        uic.loadUi('shopscat.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.vegan.clicked.connect(self.onAct_veg)
        self.wyc.clicked.connect(self.onAct_wyc)
        self.zerowaste.clicked.connect(self.onAct_zw)
        self.secondhand.clicked.connect(self.onAct_sechand)
        self.ecoprod.clicked.connect(self.onAct_ecopr)

    # Загрузка страницы категорий магазинов при нажатии на "Магазины"


    def onAct_rp(self):
        uic.loadUi('recplacecat.ui', self)
        self.con = sqlite3.connect('program.db')
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.paper.clicked.connect(self.onAct_pap)
        self.glass.clicked.connect(self.onAct_gl)
        self.plastic.clicked.connect(self.onAct_plas)
        self.metal.clicked.connect(self.onAct_met)
        self.caps.clicked.connect(self.onAct_caps)
        self.battery.clicked.connect(self.onAct_bat)
        self.lamp.clicked.connect(self.onAct_lamp)
        self.term.clicked.connect(self.onAct_term)
        self.household.clicked.connect(self.onAct_hh)
        self.other.clicked.connect(self.onAct_other)

    # Загрузка страницы категорий ресурсов при нажатии на "Пункты сбора"


    def onAct_inf(self):
        uic.loadUi('information.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.s_start.clicked.connect(self.onAct_s_start)
        self.s_lesstr.clicked.connect(self.onAct_s_lesstr)

        text=open('Как начать разделять отходы.txt', encoding = 'utf8').read()
        print(text)
        self.text_edit.setPlainText(text)

    # Загрузка страницы полезных статей при нажатии на "Информация"
        
    def onAct_s_start(self):
        text=open('Как начать разделять отходы.txt', encoding = 'utf8').read()
        self.text_edit.setPlainText(text)

    # Загрузка 1 статьи при нажатии на кнопку "Как начать разделять отходы"

    def onAct_s_lesstr(self):
        text=open('Как производить меньше мусора.txt', encoding = 'utf8').read()
        self.text_edit.setPlainText(text)

    # Загрузка 2 статьи при нажатии на кнопку "Как производить меньше мусора"


    def onAct_about(self):
        uic.loadUi('about.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.label.setPixmap(QPixmap("фотка.jpg"))

    # Загрузка страницы с информацией при нажатии на кнопку "О нас"


    def onAct_veg(self):
        uic.loadUi('shopslist.ui', self)    
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_sh)
        self.table.cellClicked.connect(self.cellClickShopsVEG)
        self.open_map.clicked.connect(self.onAct_map_veg)
        
        cur = self.con.cursor()
        result = cur.execute("Select name from Veg").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Веган"

    def onAct_wyc(self):
        uic.loadUi('shopslist.ui', self)
        self.con = sqlite3.connect('program.db')
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_sh)
        self.table.cellClicked.connect(self.cellClickShopsWYC)
        self.open_map.clicked.connect(self.onAct_map_wyc)
        
        cur = self.con.cursor()
        result = cur.execute("Select name from WYC").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Со своей тарой"

    def onAct_zw(self):
        uic.loadUi('shopslist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_sh)
        self.table.cellClicked.connect(self.cellClickShopsZW)
        self.open_map.clicked.connect(self.onAct_map_zw)
        
        cur = self.con.cursor()
        result = cur.execute("Select name from Zerowaste").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Zero-waste"

    def onAct_sechand(self):
        uic.loadUi('shopslist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_sh)
        self.table.cellClicked.connect(self.cellClickShopsSH)
        self.open_map.clicked.connect(self.onAct_map_sh)
        
        cur = self.con.cursor()
        result = cur.execute("Select name from Secondhand").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Секонд-хэнд"

    def onAct_ecopr(self):
        uic.loadUi('shopslist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_sh)
        self.table.cellClicked.connect(self.cellClickShopsECO)
        self.open_map.clicked.connect(self.onAct_map_eco)
        
        cur = self.con.cursor()
        result = cur.execute("Select name from Ecoshops").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()
        
    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Экопродукты"

    def onAct_pap(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContPap)
        self.open_map.clicked.connect(self.onAct_map_pap)

        cur = self.con.cursor()
        result = cur.execute("Select name from Paper").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Макулатура"

    def onAct_gl(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContGl)
        self.open_map.clicked.connect(self.onAct_map_gl)
        

        cur = self.con.cursor()
        result = cur.execute("Select name from Glass").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Стекло"

    def onAct_plas(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContPl)
        self.open_map.clicked.connect(self.onAct_map_plas)

        cur = self.con.cursor()
        result = cur.execute("Select name from Plastic").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Пластик"

    def onAct_met(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContMet)
        self.open_map.clicked.connect(self.onAct_map_met)

        cur = self.con.cursor()
        result = cur.execute("Select name from Metal").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Металл"

    def onAct_caps(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContCaps)
        self.open_map.clicked.connect(self.onAct_map_cap)

        cur = self.con.cursor()
        result = cur.execute("Select name from Caps").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Крышки"

    def onAct_bat(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContBat)
        self.open_map.clicked.connect(self.onAct_map_bat)

        cur = self.con.cursor()
        result = cur.execute("Select name from Batteries").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Батарейки"

    def onAct_lamp(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContLamp)
        self.open_map.clicked.connect(self.onAct_map_lamp)

        cur = self.con.cursor()
        result = cur.execute("Select name from Lights").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Лампочки"

    def onAct_term(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContTerm)
        self.open_map.clicked.connect(self.onAct_map_term)

        cur = self.con.cursor()
        result = cur.execute("Select name from Termometers").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Термометры"

    def onAct_hh(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContHH)
        self.open_map.clicked.connect(self.onAct_map_hh)

        cur = self.con.cursor()
        result = cur.execute("Select name from Household").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Бытовая техника"

    def onAct_other(self):
        uic.loadUi('placelist.ui', self)
        self.glav.clicked.connect(self.onAct_glav)
        self.shops.clicked.connect(self.onAct_sh)
        self.place.clicked.connect(self.onAct_rp)
        self.inform.clicked.connect(self.onAct_inf)
        self.about.clicked.connect(self.onAct_about)
        self.back.clicked.connect(self.onAct_rp)
        self.table.cellClicked.connect(self.cellClickContOt)
        self.open_map.clicked.connect(self.onAct_map_ot)

        cur = self.con.cursor()
        result = cur.execute("Select name from Other").fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(1)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    # Переход на страницу с подробной информацией и вывод данных
    # в таблицу при нажатии на кнопку "Другое"


    def onAct_map_fav(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A24f22cc08e7756cc3a801829816373a85083501721cb15696daa667814e5dcae&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории 
    # "Рекомендуем" на главной странице


    def onAct_map_veg(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Ae38cae684290e5284b40dae9233888fdaea35736d385cd2a7dfe72cd23a548cd&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Веган"

    def onAct_map_wyc(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A4cd09dc3a0b987f09c41d64bdf0e9b7cfd3d8cd5c63eaedc15353143c9e97129&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Со своей тарой"

    def onAct_map_zw(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A8e76562b53e436c6549e8012f09923865b6d3f3af74c269f61888b420f55ff12&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Zero-waste"

    def onAct_map_sh(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A2ef4d1aa7008e739922be9ef85bdcf553cd4082c561db65891511b3474b38996&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Секонд-хэнд"

    def onAct_map_eco(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A70533ab4dd00fa3e7abec3d221ff703c71ed104207e527bba7f2449aa59863de&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Экотовары"

    def onAct_map_pap(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Abc4313c60ccc28b1b37c73fc25ab5c730a0408550e28ae3d00c6b85acdbc6671&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Макулатура"

    def onAct_map_gl(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A4c6b56afe772bd01db4adc5445b683d3a3010167192f547de508944d4f38e8a9&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Стекло"

    def onAct_map_plas(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Af902d7bb00d06f0b1443fa8014813e947f98600f513fd977852521d4a0347f4f&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Пластик"

    def onAct_map_met(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A418b55635e83579003ff501ca5bb967cb14923d09b9f5fe7ba50a937281ef7a7&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Металл"

    def onAct_map_cap(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A4b12bceabe5b457df33fc331c28e45a2fa1753de3486ef3a327d5c361fcdd592&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Крышки"

    def onAct_map_bat(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Ae342c0f2440ef235b1bc680497ab29e0d81a4f27ab16e9dba04104f6ab5d6132&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Батарейки"

    def onAct_map_lamp(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3A5c881c0f6e3faf0af4f5e467037ccb6b14fd383cbfdceb44b955bf70bc1bd64d&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Лампочки"

    def onAct_map_term(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Af9325ef67cf455b328581c88140541040aa9a3ca55ce11ddff632019ab94534e&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Термометры"

    def onAct_map_hh(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Ac1ef7866d624fca4669abb0f2ae5d7807cba78f01751c545ee46ffce2fcdbf35&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Бытовая техника"
    def onAct_map_ot(self):
        webbrowser.open('https://yandex.ru/maps/?um=constructor%3Aa9beeccc2855705fb5956bcb7dc2715a3ac16381a4cae541625eea6a83be1784&source=constructorLink', new=1)

    # Открытие в браузере карты с местами категории "Другое"


    def cellClickShopsWYC(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from WYC \
                         WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from WYC WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Со своей тарой", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickShopsVEG(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Veg \
                         WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Veg WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Веган", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickShopsZW(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name, adress, description from Zerowaste \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Zerowaste WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Zero-waste", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickShopsSH(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Secondhand \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Secondhand WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Секонд-хэнд", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickShopsECO(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Ecoshops \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Ecoshops WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Экотовары", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContPap(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Paper \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Paper WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Макулатура", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContGl(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Glass \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Glass WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Стекло", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContPl(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Plastic WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Plastic WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Пластик", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContMet(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Metal WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Metal WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Металл", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContCaps(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Caps WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Крышки", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContLamp(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Lights WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Lights WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Лампочки", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContBat(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Batteries \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Batteries WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Батарейки", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContTerm(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Termometers \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Termometers WHERE \
                                id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Термометры", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContHH(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Household \
                         WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Household WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Бытовая техника", 
    # высвечивается таблица с подробной информацией и фото карты

    def cellClickContOt(self, item):
        self.con = sqlite3.connect('program.db')
        cur = self.con.cursor()
        res = cur.execute("Select name,adress,description from Other \
                          WHERE id=?",(item,)).fetchall()
        self.table2.setRowCount(1)
        self.table2.setColumnCount(3)
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.table2.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

        curr_map = cur.execute("Select map from Other WHERE \
                                 id=?", (item,)).fetchall()
        curr_map = str(curr_map)[:0] + str(curr_map)[3:]
        curr_map = str(curr_map)[:-4] + str(curr_map)[-1:]
        curr_map = curr_map.replace("]","")

        self.labelmap.setText("")

        pix = QPixmap('Фото\\' + curr_map + '.png')
        pix = pix.scaledToWidth(341)
        pix = pix.scaledToHeight(341)
        self.labelmap.setPixmap(pix)

    # Обработка нажатия на ячейкку таблицы категории "Другое", 
    # высвечивается таблица с подробной информацией и фото карты

    
app=QApplication(sys.argv)
ex= Program()
ex.show()
sys.exit(app.exec_())
