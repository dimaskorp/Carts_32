from datetime import datetime

from PySide2.QtCore import (QCoreApplication, QDate, QMetaObject,
                            QRect, QSize, QTime, Qt)
from PySide2.QtGui import (QCursor, QFont,
                           QIcon)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QAction, QWidget, QToolBox, QToolBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QSize(1000, 600))

        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)

        font_m = QFont()
        font_m.setFamily("Times New Roman")
        font_m.setPointSize(12)
        font_m.setBold(False)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFont(font)

        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.toolBox.setGeometry(10, 10, 1000, 500)
        self.toolBox.setFont(font)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(True)

        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.setFont(font_m)
        self.guideModel = QAction(MainWindow)
        self.guideModel.setObjectName("guideModel")
        self.guideModel.setFont(font_m)
        self.guideDepartments = QAction(MainWindow)
        self.guideDepartments.setObjectName("guideDepartments")
        self.guideDepartments.setFont(font_m)

        #---------------------------page_1--------------------------------#
        self.page = QWidget()
        self.page.setObjectName("page")
        #self.page.setGeometry(QRect(0, 0, 580, 342))
        self.page.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        font1 = QFont()
        font1.setFamily("Times New Roman")
        font1.setPointSize(12)
        font1.setBold(False)

        self.page.setFont(font1)
        self.page.setAutoFillBackground(True)
        self.pB_clear_filter = QPushButton(self.page)
        self.pB_clear_filter.setObjectName("pB_clear_filter")
        self.pB_clear_filter.setGeometry(QRect(800, 0, 140, 25))

        self.pB_save = QPushButton(self.page)
        self.pB_save.setObjectName("pB_save")
        self.pB_save.setEnabled(False)
        self.pB_save.setGeometry(QRect(850, 360, 100, 25))

        self.tableView_select = QTableView(self.page)
        self.tableView_select.setObjectName("tableView_select")
        self.tableView_select.setGeometry(QRect(0, 90, 950, 250))
        self.tableView_select.verticalHeader().setVisible(True)

        self.pB_add = QPushButton(self.page)
        self.pB_add.setObjectName("pB_add")
        self.pB_add.setGeometry(QRect(0, 350, 40, 30))

        icon = QIcon()
        icon.addFile("images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pB_add.setIcon(icon)

        self.pB_edit = QPushButton(self.page)
        self.pB_edit.setObjectName("pB_edit")
        self.pB_edit.setGeometry(QRect(50, 350, 40, 30))
        self.pB_edit.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile("images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pB_edit.setIcon(icon2)
        self.pB_edit.setCheckable(True)
        self.pB_edit.setChecked(False)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(150, 0, 200, 25))
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setFocus()

        self.pB_delete = QPushButton(self.page)
        self.pB_delete.setObjectName("pB_delete")
        self.pB_delete.setGeometry(QRect(100, 350, 40, 30))
        self.pB_delete.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile("images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pB_delete.setIcon(icon1)

        self.pB_send = QPushButton(self.page)
        self.pB_send.setObjectName("pB_send")
        self.pB_send.setGeometry(QRect(650, 360, 200, 25))
        self.pB_send.setVisible(False)

        self.pB_accept = QPushButton(self.page)
        self.pB_accept.setObjectName("pB_accept")
        self.pB_accept.setGeometry(QRect(650, 360, 200, 25))
        self.pB_accept.setVisible(False)

        self.label = QLabel(self.page)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 0, 140, 20))
        self.label.setFrameShape(QFrame.NoFrame)

        self.comboBox_model = QComboBox(self.page)
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.setGeometry(QRect(150, 30, 180, 25))

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 30, 140, 20))
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(10, 60, 61, 16))

        self.comboBox_status = QComboBox(self.page)
        self.comboBox_status.setObjectName("comboBox_status")
        self.comboBox_status.setGeometry(QRect(150, 60, 180, 25))

        self.pB_excel = QPushButton(self.page)
        self.pB_excel.setObjectName("pB_excel")
        self.pB_excel.setGeometry(QRect(850, 40, 40, 40))
        self.pB_excel.setFont(font1)
        self.pB_excel.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile("images/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pB_excel.setIcon(icon3)
        self.toolBox.addItem(self.page, "Картриджи")

        #---------------------------page_2--------------------------------#
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setFont(font1)

        self.TableWidget = QWidget(self.page_2)
        self.TableWidget.setGeometry(0, 90, 960, 300)
        vbox = QVBoxLayout(self.TableWidget)
        self.TableWidget_History = QTableWidget()
        vbox.addWidget(self.TableWidget_History)
        self.TableWidget_History.verticalHeader().setVisible(True)

        self.comboBox_action = QComboBox(self.page_2)
        self.comboBox_action.setObjectName("comboBox_action")
        self.comboBox_action.setGeometry(QRect(140, 30, 180, 25))
        self.comboBox_action.setFocusPolicy(Qt.ClickFocus)
        self.comboBox_status_h = QComboBox(self.page_2)
        self.comboBox_status_h.setObjectName("comboBox_status_h")
        self.comboBox_status_h.setGeometry(QRect(140, 60, 180, 25))
        self.comboBox_status_h.setInsertPolicy(QComboBox.NoInsert)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(10, 30, 80, 16))
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(10, 60, 80, 16))

        self.dateEdit_min = QDateEdit(self.page_2)
        self.dateEdit_min.setObjectName("dateEdit_min")
        self.dateEdit_min.setGeometry(QRect(140, 0, 120, 25))
        self.dateEdit_min.setEnabled(False)
        self.dateEdit_min.setDate(datetime.today())
        self.dateEdit_min.setMinimumDate(QDate(2000, 1, 1))
        self.dateEdit_min.setMaximumTime(QTime(0, 00, 00))
        self.dateEdit_min.setCalendarPopup(True)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(10, 2, 50, 16))

        self.dateEdit_max = QDateEdit(self.page_2)
        self.dateEdit_max.setObjectName("dateEdit_max")
        self.dateEdit_max.setGeometry(QRect(300, 0, 120, 25))
        self.dateEdit_max.setEnabled(False)
        self.dateEdit_max.setDate(datetime.today())
        self.dateEdit_max.setMinimumDate(QDate(2000, 1, 1))
        self.dateEdit_max.setMaximumTime(QTime(23, 59, 59))
        self.dateEdit_max.setCalendarPopup(True)

        self.pB_clear_filter_h = QPushButton(self.page_2)
        self.pB_clear_filter_h.setObjectName("pB_clear_filter_h")
        self.pB_clear_filter_h.setGeometry(QRect(800, 0, 140, 25))
        self.pB_clear_filter_h.setFont(font1)

        self.checkBox = QCheckBox(self.page_2)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setGeometry(QRect(425, 4, 18, 18))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)

        self.checkBox_All = QCheckBox(self.page_2)
        self.checkBox_All.setObjectName("checkBox")
        self.checkBox_All.setGeometry(QRect(65, 100, 18, 18))
        self.checkBox_All.setCheckable(True)
        self.checkBox_All.setChecked(False)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(100, 2, 20, 16))
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(270, 2, 20, 16))

        self.pB_print_select = QPushButton(self.page_2)
        self.pB_print_select.setObjectName("pB_print_select")
        self.pB_print_select.setGeometry(QRect(500, 60, 200, 25))

        self.pB_print_select_2 = QPushButton(self.page_2)
        self.pB_print_select_2.setObjectName("pB_print_select")
        self.pB_print_select_2.setGeometry(QRect(750, 60, 200, 25))
        self.toolBox.addItem(self.page_2, "Журнал")

        #---------------------------page_3--------------------------------#
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        #self.page_3.setGeometry(QRect(0, 0, 580, 342))
        self.page_3.setFont(font1)

        self.dateEdit_min_otch = QDateEdit(self.page_3)
        self.dateEdit_min_otch.setObjectName("dateEdit_min_otch")
        self.dateEdit_min_otch.setGeometry(QRect(140, 0, 120, 25))
        dtmin = datetime.today()
        self.dateEdit_min_otch.setDateTime(dtmin)
        self.dateEdit_min_otch.setCalendarPopup(True)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(10, -2, 50, 25))
        self.label_4.setFont(font1)

        self.dateEdit_max_otch = QDateEdit(self.page_3)
        self.dateEdit_max_otch.setObjectName("dateEdit_max_otch")
        self.dateEdit_max_otch.setGeometry(QRect(300, 0, 120, 25))
        dtmax = datetime.today()
        self.dateEdit_max_otch.setDateTime(dtmax)
        self.dateEdit_max_otch.setCalendarPopup(True)

        self.comboBox_status_o = QComboBox(self.page_3)
        self.comboBox_status_o.setObjectName("comboBox_status_o")
        self.comboBox_status_o.setGeometry(QRect(60, 130, 180, 25))
        self.comboBox_status_o.setInsertPolicy(QComboBox.NoInsert)

        self.comboBox_action_o = QComboBox(self.page_3)
        self.comboBox_action_o.setObjectName("comboBox_action_o")
        self.comboBox_action_o.setGeometry(QRect(60, 210, 180, 25))
        self.comboBox_action_o.setFocusPolicy(Qt.ClickFocus)

        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 50, 300, 25))
        self.pushButton_3.setFont(font1)

        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 80, 300, 25))

        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 160, 300, 25))

        self.pushButton_5 = QPushButton(self.page_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(QRect(60, 240, 300, 25))

        self.line = QFrame(self.page_3)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(-10, 110, 1000, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.page_3)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(-10, 190, 1000, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.page_3)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(-10, 270, 1000, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.page_3)
        self.line_4.setObjectName("line_4")
        self.line_4.setGeometry(QRect(-10, 30, 1000, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(100, 2, 20, 16))
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(270, 2, 20, 16))

        self.toolBox.addItem(self.page_3, "Отчеты")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 19))
        self.menuDepartments = QMenu(self.menubar)
        self.menuDepartments.setObjectName("menuDepartments")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.BottomToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDepartments.menuAction())
        self.menuDepartments.addAction(self.guideModel)
        self.menuDepartments.addSeparator()
        self.menuDepartments.addAction(self.guideDepartments)
        self.menuFile.addAction(self.actionClose)
        self.menubar.setFont(font_m)
        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Учет картриджей")
        MainWindow.setWindowIcon(QIcon('images/iconc.jpg'))
        self.actionClose.setText("Выход")
        self.actionClose.setShortcut("Alt+X")
        self.guideModel.setText("Модели картриджей")
        self.guideDepartments.setText("Отделения и статусы")
        self.pB_clear_filter.setText("Сбросить фильтр")
        self.pB_save.setText("Сохранить")
        self.pB_send.setText("Отправить на заправку")
        self.pB_accept.setText("Приянть с заправки")
        self.label.setText("Номер картриджа")
        self.label_2.setText("Модель картриджа")
        self.label_3.setText("Статус")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), "Картриджи")
        self.label_5.setText("Действие")
        self.label_6.setText("Статус")
        self.dateEdit_min.setDisplayFormat("dd-MM-yyyy")
        self.label_7.setText("Дата")
        self.dateEdit_max.setDisplayFormat("dd-MM-yyyy")
        self.pB_clear_filter_h.setText("Сбросить фильтр")
        self.label_8.setText("c")
        self.label_9.setText("по")
        self.pB_print_select.setText("Печать штрих кода глянец")
        self.pB_print_select_2.setText("Печать штрих кода")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), "Журнал")
        self.label_4.setText("Дата")
        self.pushButton_3.setText("Движение картриджей за период")
        self.pushButton_2.setText("Заправлено картриджей за период")
        self.pushButton_4.setText("Отчет по статусу")
        self.pushButton_5.setText("Отчет по действию")
        self.label_10.setText("c")
        self.label_11.setText("по")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), "Отчеты")
        self.menuDepartments.setTitle("Справочники")
        self.menuFile.setTitle("Файл")
        self.toolBar.setWindowTitle("toolBar")

    # retranslateUi


