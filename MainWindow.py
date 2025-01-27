# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 650)
        MainWindow.setMinimumSize(QSize(420, 650))
        MainWindow.setMaximumSize(QSize(420, 650))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 381, 621))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.layoutWidget)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label_title.setFont(font1)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.label_help = QLabel(self.layoutWidget)
        self.label_help.setObjectName(u"label_help")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_help.setFont(font2)
        self.label_help.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_help)

        self.textEdit_urls = QTextEdit(self.layoutWidget)
        self.textEdit_urls.setObjectName(u"textEdit_urls")
        self.textEdit_urls.setFont(font2)

        self.verticalLayout.addWidget(self.textEdit_urls)

        self.textBrowser_log = QTextBrowser(self.layoutWidget)
        self.textBrowser_log.setObjectName(u"textBrowser_log")
        self.textBrowser_log.setFont(font2)

        self.verticalLayout.addWidget(self.textBrowser_log)

        self.progressBar_test = QProgressBar(self.layoutWidget)
        self.progressBar_test.setObjectName(u"progressBar_test")
        self.progressBar_test.setFont(font)
        self.progressBar_test.setValue(0)
        self.progressBar_test.setAlignment(Qt.AlignCenter)
        self.progressBar_test.setTextVisible(False)
        self.progressBar_test.setOrientation(Qt.Horizontal)
        self.progressBar_test.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar_test)

        self.pushButton_start = QPushButton(self.layoutWidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_start.setFont(font3)

        self.verticalLayout.addWidget(self.pushButton_start)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_read_config = QPushButton(self.layoutWidget)
        self.pushButton_read_config.setObjectName(u"pushButton_read_config")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_read_config.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_read_config)

        self.pushButton_save_config = QPushButton(self.layoutWidget)
        self.pushButton_save_config.setObjectName(u"pushButton_save_config")
        self.pushButton_save_config.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_save_config)

        self.pushButton_exit = QPushButton(self.layoutWidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_exit.setFont(font5)

        self.horizontalLayout.addWidget(self.pushButton_exit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_copyright = QLabel(self.layoutWidget)
        self.label_copyright.setObjectName(u"label_copyright")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setUnderline(True)
        font6.setStrikeOut(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.label_copyright.setFont(font6)
        self.label_copyright.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_copyright)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7f51\u7ad9\u72b6\u6001\u68c0\u6d4b\u5668 - SmallBambooCode", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7ad9\u72b6\u6001\u68c0\u6d4b\u5668\n"
"Website Status Detector", None))
        self.label_help.setText(QCoreApplication.translate("MainWindow", u"\u5728\u4e0b\u65b9\u6587\u672c\u6846\u4e2d\u586b\u5199\u9700\u68c0\u6d4b\u7684\u7f51\u7ad9\uff0c\u9ed8\u8ba4\u52a0\u8f7d\u672c\u5730\u914d\u7f6e", None))
        self.textEdit_urls.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_urls.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65e0\u914d\u7f6e\uff0c\u8bf7\u8f93\u5165\u5b8c\u6574\u7684\u7f51\u5740\uff0c\u6bcf\u884c\u4e00\u4e2a\u3002", None))
        self.textBrowser_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65e5\u5fd7\u8f93\u51fa\u533a\uff0c\u8bf7\u70b9\u51fb\u5f00\u59cb\u68c0\u6d4b\uff01</p></body></html>", None))
        self.progressBar_test.setFormat("")
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.pushButton_read_config.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u914d\u7f6e", None))
        self.pushButton_save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5e8f", None))
        self.label_copyright.setText(QCoreApplication.translate("MainWindow", u"\u7248\u6743\u6240\u6709 \u00a9 2025 SmallBambooCode \u4fdd\u7559\u6240\u6709\u6743\u5229", None))
    # retranslateUi

