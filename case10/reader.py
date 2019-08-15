# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, os, time
import urllib.request
from bs4 import BeautifulSoup
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # 设置”抓取设置“区域
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 121))
        self.groupBox.setObjectName("groupBox")

        # 对”选择“按钮进行设置
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton2.setGeometry(QtCore.QRect(370, 60, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton2.setFont(font)
        self.pushButton2.clicked.connect(self.msg)
        self.pushButton2.setAutoFillBackground(True)
        self.pushButton2.setObjectName("pushButton2")

        # 对”确定“按钮进行设置
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(340, 90, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.clicked.connect(self.getdatas)
        self.pushButton.setObjectName("pushButton")

        # 对”设置期数“标签进行设置
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 对”选择路径“标签进行设置
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 对”选择保存路径“文本框进行设置
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 201, 20))
        self.lineEdit.setObjectName("lineEdit")

        # 对”设置期数”控件进行设置
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 30, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(265, 31, 150, 16))
        self.label_3.setObjectName("label_3")

        # 对“选项卡”进行设置
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(8, 140, 431, 355))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")

        # 设置“选项卡的第1个TAB,加入QTableWidget表格
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 410, 295))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0,130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab, "")
        self.tableWidget.itemClicked.connect(self.tableClick)

        # 设置“选项卡的第2个TAB,加入QTableWidget表格
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(8, 5, 410, 295))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.listWidget.setFont(font)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setIconSize(QtCore.QSize(72, 72))
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        self.listWidget.setMaximumWidth(800)
        self.listWidget.setSpacing(12)
        self.listWidget.itemClicked.connect(self.itemClick)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RCQ读者书库"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.pushButton2.setText(_translate("MainWindow", "选择"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "请选择抓取期数："))
        self.lineEdit.setText(_translate("MainWindow", os.getcwd()))
        strDate = str(time.localtime().tm_year) + '- ' + str(time.localtime().tm_mon)
        self.lineEdit_2.setText(_translate("MainWindow", strDate))
        self.label_2.setText(_translate("MainWindow", "请选择保存路径："))
        self.label_3.setText(_translate("MainWindow", "（期数范围为：01--24）"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期数"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "按期数显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "按名称显示"))


    def msg(self):
        try:
            self.dir_path = QFileDialog.getExistingDirectory(None, '选择路径', os.getcwd())
            self.lineEdit.setText(self.dir_path)
        except Exception as e:
            print(e)

    def getdata(self, url, path):
        soup = self.urlTosoup(url)
        link = soup.select('.booklist a')
        path = path + '\\' + self.date + '\\'
        if not os.path.isdir(path):
            os.mkdir(path)
        for item in link:
            articleUrl = self.baseurl + item['href']
            articleSoup = self.urlTosoup(articleUrl)
            title = str(articleSoup.find('h1')).lstrip('<h1>').rstrip('</h1>')
            author = str(articleSoup.find(id='pub_date')).strip()
            fileName = path + title + '.txt'
            newFile = open(fileName, 'w')
            newFile.write('<<' + title + '>>\n\n')
            newFile.write(author + '\n\n')
            content = articleSoup.select('.blkContainerSblkCon p')
            for c in content:
                text = c.text
                newFile.write(text)
            newFile.close()
        QMessageBox.Information(None, '提示', self.date + "的读者文章保存完成", QMessageBox.Ok)

    def urlTosoup(self, url):
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def getFiles(self):
        self.list = os.listdir(self.lineEdit.text() + '\\' + self.lineEdit_2.text())

    def bindTable(self):
        for i in range(0, len(self.list)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.lineEdit_2.text()))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.list[i]))

    def bindList(self):
        for i in range(0, len(self.list)):
            self.item = QtWidgets.QListWidgetItem(self.listWidget)
            self.item.setIcon(QtGui.QIcon('note.ico'))
            self.item.setText(str(self.list[i])[1:5]+'...')
            self.item.setToolTip(self.list[i])
            self.item.setFlags(QtCore.QT.ItemIsSelectable | QtCore.Qt.ItemIsEditable)

    def getdatas(self):
        try:
            while True:
                self.date = self.lineEdit_2.text()
                self.baseurl = 'http://www.duzhe.com/' + self.date.replace('-', '-') + '/'
                urlList = self.baseurl + 'index.html'
                self.getdata(urlList, self.lineEdit.text())
        except Exception as e:
            print(e)
        self.getFiles()
        self.bindList()
        self.bindTable()

    def itemClick(self, item):
        os.startfile(self.lineEdit.text() + '\\' + self.lineEdit_2.text() + '\\' + item.toolTip())

    def tableClick(self, item):
        os.startfile(self.lineEdit.text() + '\\' + self.lineEdit_2.text() + '\\' + item.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
