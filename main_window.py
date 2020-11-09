# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_analyze = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_analyze.setGeometry(QtCore.QRect(10, 400, 551, 221))
        self.textEdit_analyze.setObjectName("textEdit_analyze")
        self.lineEdit_project = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_project.setGeometry(QtCore.QRect(70, 50, 121, 31))
        self.lineEdit_project.setObjectName("lineEdit_project")
        self.lineEdit_robot = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_robot.setGeometry(QtCore.QRect(140, 0, 531, 31))
        self.lineEdit_robot.setObjectName("lineEdit_robot")
        self.ptn_send_robot = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_send_robot.setGeometry(QtCore.QRect(590, 580, 101, 31))
        self.ptn_send_robot.setObjectName("ptn_send_robot")
        self.ptn_timer_start = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_timer_start.setGeometry(QtCore.QRect(590, 360, 101, 31))
        self.ptn_timer_start.setObjectName("ptn_timer_start")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(460, 360, 118, 31))
        self.timeEdit.setTime(QtCore.QTime(21, 30, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        self.label_timer.setGeometry(QtCore.QRect(10, 330, 361, 31))
        self.label_timer.setObjectName("label_timer")
        self.label_webhook = QtWidgets.QLabel(self.centralwidget)
        self.label_webhook.setGeometry(QtCore.QRect(10, 0, 131, 31))
        self.label_webhook.setObjectName("label_webhook")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 51, 31))
        self.label.setObjectName("label")
        self.lineEdit_project_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_project_name.setGeometry(QtCore.QRect(270, 50, 131, 31))
        self.lineEdit_project_name.setObjectName("lineEdit_project_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 50, 71, 31))
        self.label_3.setObjectName("label_3")
        self.dateEdit_projectPoint = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_projectPoint.setGeometry(QtCore.QRect(570, 50, 114, 31))
        self.dateEdit_projectPoint.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 11), QtCore.QTime(0, 0, 0)))
        self.dateEdit_projectPoint.setObjectName("dateEdit_projectPoint")
        self.lineEdit_project_next = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_project_next.setGeometry(QtCore.QRect(500, 50, 61, 31))
        self.lineEdit_project_next.setObjectName("lineEdit_project_next")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 51, 31))
        self.label_4.setObjectName("label_4")
        self.checkBox_issues = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_issues.setGeometry(QtCore.QRect(10, 90, 92, 20))
        self.checkBox_issues.setChecked(True)
        self.checkBox_issues.setObjectName("checkBox_issues")
        self.checkBox_feature = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_feature.setGeometry(QtCore.QRect(110, 90, 101, 20))
        self.checkBox_feature.setChecked(False)
        self.checkBox_feature.setObjectName("checkBox_feature")
        self.checkBox_process = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_process.setGeometry(QtCore.QRect(230, 90, 111, 20))
        self.checkBox_process.setChecked(False)
        self.checkBox_process.setObjectName("checkBox_process")
        self.checkBox_testing = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_testing.setGeometry(QtCore.QRect(340, 90, 111, 20))
        self.checkBox_testing.setChecked(False)
        self.checkBox_testing.setObjectName("checkBox_testing")
        self.checkBox_today = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_today.setGeometry(QtCore.QRect(10, 150, 121, 20))
        self.checkBox_today.setChecked(True)
        self.checkBox_today.setObjectName("checkBox_today")
        self.checkBox_create = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_create.setGeometry(QtCore.QRect(140, 150, 121, 20))
        self.checkBox_create.setChecked(True)
        self.checkBox_create.setObjectName("checkBox_create")
        self.ptn_preview = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_preview.setGeometry(QtCore.QRect(590, 410, 101, 28))
        self.ptn_preview.setObjectName("ptn_preview")
        self.checkBox_dead = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_dead.setGeometry(QtCore.QRect(10, 120, 101, 20))
        self.checkBox_dead.setChecked(True)
        self.checkBox_dead.setObjectName("checkBox_dead")
        self.checkBox_black = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_black.setGeometry(QtCore.QRect(110, 120, 101, 20))
        self.checkBox_black.setChecked(False)
        self.checkBox_black.setObjectName("checkBox_black")
        self.checkBox_other = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_other.setGeometry(QtCore.QRect(230, 120, 121, 20))
        self.checkBox_other.setChecked(False)
        self.checkBox_other.setObjectName("checkBox_other")
        self.lineEdit_note_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_note_2.setGeometry(QtCore.QRect(350, 120, 171, 21))
        self.lineEdit_note_2.setObjectName("lineEdit_note_2")
        self.checkBox_show_name = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_name.setGeometry(QtCore.QRect(530, 90, 101, 20))
        self.checkBox_show_name.setChecked(True)
        self.checkBox_show_name.setObjectName("checkBox_show_name")
        self.checkBox_show_issuse = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_issuse.setGeometry(QtCore.QRect(530, 120, 121, 20))
        self.checkBox_show_issuse.setChecked(True)
        self.checkBox_show_issuse.setObjectName("checkBox_show_issuse")
        self.lineEdit_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filter.setGeometry(QtCore.QRect(130, 170, 491, 31))
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.checkBox_user_filter = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_user_filter.setGeometry(QtCore.QRect(10, 180, 121, 20))
        self.checkBox_user_filter.setChecked(False)
        self.checkBox_user_filter.setObjectName("checkBox_user_filter")
        self.checkBox_user_filter_iss = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_user_filter_iss.setGeometry(QtCore.QRect(530, 210, 121, 20))
        self.checkBox_user_filter_iss.setChecked(True)
        self.checkBox_user_filter_iss.setObjectName("checkBox_user_filter_iss")
        self.lineEdit_filter_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filter_name.setGeometry(QtCore.QRect(100, 210, 151, 31))
        self.lineEdit_filter_name.setObjectName("lineEdit_filter_name")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 81, 31))
        self.label_5.setObjectName("label_5")
        self.textEdit_note = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_note.setGeometry(QtCore.QRect(50, 250, 601, 71))
        self.textEdit_note.setObjectName("textEdit_note")
        self.checkBox_week_0 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_0.setGeometry(QtCore.QRect(10, 370, 61, 20))
        self.checkBox_week_0.setChecked(True)
        self.checkBox_week_0.setObjectName("checkBox_week_0")
        self.checkBox_week_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_1.setGeometry(QtCore.QRect(70, 370, 61, 20))
        self.checkBox_week_1.setChecked(True)
        self.checkBox_week_1.setObjectName("checkBox_week_1")
        self.checkBox_week_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_2.setGeometry(QtCore.QRect(140, 370, 61, 20))
        self.checkBox_week_2.setChecked(True)
        self.checkBox_week_2.setObjectName("checkBox_week_2")
        self.checkBox_week_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_3.setGeometry(QtCore.QRect(200, 370, 61, 20))
        self.checkBox_week_3.setChecked(True)
        self.checkBox_week_3.setObjectName("checkBox_week_3")
        self.checkBox_week_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_4.setGeometry(QtCore.QRect(260, 370, 61, 20))
        self.checkBox_week_4.setChecked(True)
        self.checkBox_week_4.setObjectName("checkBox_week_4")
        self.checkBox_week_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_5.setGeometry(QtCore.QRect(320, 370, 61, 20))
        self.checkBox_week_5.setChecked(True)
        self.checkBox_week_5.setObjectName("checkBox_week_5")
        self.checkBox_week_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_week_6.setGeometry(QtCore.QRect(380, 370, 61, 20))
        self.checkBox_week_6.setChecked(False)
        self.checkBox_week_6.setObjectName("checkBox_week_6")
        self.checkBox_all = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_all.setGeometry(QtCore.QRect(590, 330, 101, 20))
        self.checkBox_all.setChecked(False)
        self.checkBox_all.setObjectName("checkBox_all")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 26))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_project.setText(_translate("MainWindow", "PT200017"))
        self.lineEdit_robot.setText(_translate("MainWindow", "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=1687141d-0361-4079-85d5-25146311a713"))
        self.ptn_send_robot.setText(_translate("MainWindow", "立即发送到群"))
        self.ptn_timer_start.setText(_translate("MainWindow", "定时发送"))
        self.label_timer.setText(_translate("MainWindow", "自定义发送时间"))
        self.label_webhook.setText(_translate("MainWindow", "群机器人 Webhook"))
        self.label.setText(_translate("MainWindow", "项目ID"))
        self.lineEdit_project_name.setText(_translate("MainWindow", "6710"))
        self.label_2.setText(_translate("MainWindow", "项目名称"))
        self.label_3.setText(_translate("MainWindow", "下一节点"))
        self.dateEdit_projectPoint.setDisplayFormat(_translate("MainWindow", "yyyy-M-d"))
        self.lineEdit_project_next.setText(_translate("MainWindow", "DV2"))
        self.label_4.setText(_translate("MainWindow", "备注"))
        self.checkBox_issues.setText(_translate("MainWindow", "剩余问题"))
        self.checkBox_feature.setText(_translate("MainWindow", "功能完成度"))
        self.checkBox_process.setText(_translate("MainWindow", "过程完成度"))
        self.checkBox_testing.setText(_translate("MainWindow", "待关闭问题"))
        self.checkBox_today.setText(_translate("MainWindow", "今日处理问题"))
        self.checkBox_create.setText(_translate("MainWindow", "今日新增问题"))
        self.ptn_preview.setText(_translate("MainWindow", "预览"))
        self.checkBox_dead.setText(_translate("MainWindow", "死机问题"))
        self.checkBox_black.setText(_translate("MainWindow", "黑屏问题"))
        self.checkBox_other.setText(_translate("MainWindow", "其他关键问题"))
        self.lineEdit_note_2.setText(_translate("MainWindow", "关键词"))
        self.checkBox_show_name.setText(_translate("MainWindow", "显示经办人"))
        self.checkBox_show_issuse.setText(_translate("MainWindow", "显示具体问题"))
        self.lineEdit_filter.setText(_translate("MainWindow", "请粘贴正确的过滤器"))
        self.checkBox_user_filter.setText(_translate("MainWindow", "自定义过滤器"))
        self.checkBox_user_filter_iss.setText(_translate("MainWindow", "显示具体问题"))
        self.lineEdit_filter_name.setText(_translate("MainWindow", "自定义过滤器"))
        self.label_5.setText(_translate("MainWindow", "过滤器名称"))
        self.checkBox_week_0.setText(_translate("MainWindow", "周一"))
        self.checkBox_week_1.setText(_translate("MainWindow", "周二"))
        self.checkBox_week_2.setText(_translate("MainWindow", "周三"))
        self.checkBox_week_3.setText(_translate("MainWindow", "周四"))
        self.checkBox_week_4.setText(_translate("MainWindow", "周五"))
        self.checkBox_week_5.setText(_translate("MainWindow", "周六"))
        self.checkBox_week_6.setText(_translate("MainWindow", "周日"))
        self.checkBox_all.setText(_translate("MainWindow", "通知所有人"))
        self.menuhelp.setTitle(_translate("MainWindow", "Pls contact wuyubo@cvte.com"))