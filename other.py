from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 0, 801, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.log_in_page = QtWidgets.QWidget()
        self.log_in_page.setObjectName("log_in_page")
        self.label = QtWidgets.QLabel(self.log_in_page)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.log_in_page)
        self.pushButton.setGeometry(QtCore.QRect(310, 320, 211, 41))
        self.pushButton.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.log_in_page)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 370, 211, 41))
        self.pushButton_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_67 = QtWidgets.QLabel(self.log_in_page)
        self.label_67.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_67.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.log_in_page)
        self.label_68.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_68.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_68.setObjectName("label_68")
        self.stackedWidget.addWidget(self.log_in_page)
        self.login_as_clinician = QtWidgets.QWidget()
        self.login_as_clinician.setObjectName("login_as_clinician")
        self.label_3 = QtWidgets.QLabel(self.login_as_clinician)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_3.setObjectName("label_3")
        self.lg_user_name_lb = QtWidgets.QLabel(self.login_as_clinician)
        self.lg_user_name_lb.setGeometry(QtCore.QRect(160, 250, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_user_name_lb.setFont(font)
        self.lg_user_name_lb.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.lg_user_name_lb.setObjectName("lg_user_name_lb")
        self.lg_user_name_le = QtWidgets.QLineEdit(self.login_as_clinician)
        self.lg_user_name_le.setGeometry(QtCore.QRect(310, 250, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_user_name_le.setFont(font)
        self.lg_user_name_le.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lg_user_name_le.setObjectName("lg_user_name_le")
        self.lg_message_lb = QtWidgets.QLabel(self.login_as_clinician)
        self.lg_message_lb.setGeometry(QtCore.QRect(310, 380, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_message_lb.setFont(font)
        self.lg_message_lb.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lg_message_lb.setObjectName("lg_message_lb")
        self.lg_password_lb = QtWidgets.QLabel(self.login_as_clinician)
        self.lg_password_lb.setGeometry(QtCore.QRect(160, 310, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_password_lb.setFont(font)
        self.lg_password_lb.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.lg_password_lb.setObjectName("lg_password_lb")
        self.lg_password_le = QtWidgets.QLineEdit(self.login_as_clinician)
        self.lg_password_le.setGeometry(QtCore.QRect(310, 310, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_password_le.setFont(font)
        self.lg_password_le.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lg_password_le.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lg_password_le.setObjectName("lg_password_le")
        self.lg_login_btn = QtWidgets.QPushButton(self.login_as_clinician)
        self.lg_login_btn.setGeometry(QtCore.QRect(159, 380, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lg_login_btn.setFont(font)
        self.lg_login_btn.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.lg_login_btn.setObjectName("lg_login_btn")
        self.lg_login_btn_2 = QtWidgets.QPushButton(self.login_as_clinician)
        self.lg_login_btn_2.setGeometry(QtCore.QRect(620, 20, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lg_login_btn_2.setFont(font)
        self.lg_login_btn_2.setObjectName("lg_login_btn_2")
        self.label_69 = QtWidgets.QLabel(self.login_as_clinician)
        self.label_69.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_69.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_69.setObjectName("label_69")
        self.label_73 = QtWidgets.QLabel(self.login_as_clinician)
        self.label_73.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_73.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_73.setObjectName("label_73")
        self.stackedWidget.addWidget(self.login_as_clinician)
        self.clinician_home_page = QtWidgets.QWidget()
        self.clinician_home_page.setObjectName("clinician_home_page")
        self.pushButton_3 = QtWidgets.QPushButton(self.clinician_home_page)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 240, 251, 31))
        self.pushButton_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.clinician_home_page)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 290, 251, 31))
        self.pushButton_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.clinician_home_page)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 340, 251, 31))
        self.pushButton_6.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.clinician_home_page)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 240, 251, 31))
        self.pushButton_7.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.clinician_home_page)
        self.pushButton_14.setGeometry(QtCore.QRect(430, 340, 251, 32))
        self.pushButton_14.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_25 = QtWidgets.QPushButton(self.clinician_home_page)
        self.pushButton_25.setGeometry(QtCore.QRect(430, 290, 251, 31))
        self.pushButton_25.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_97 = QtWidgets.QLabel(self.clinician_home_page)
        self.label_97.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_97.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_97.setObjectName("label_97")
        self.label_65 = QtWidgets.QLabel(self.clinician_home_page)
        self.label_65.setGeometry(QtCore.QRect(10, -10, 111, 111))
        self.label_65.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.clinician_home_page)
        self.label_66.setGeometry(QtCore.QRect(-1, 80, 131, 31))
        self.label_66.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_66.setObjectName("label_66")
        self.stackedWidget.addWidget(self.clinician_home_page)
        self.patientdetails = QtWidgets.QWidget()
        self.patientdetails.setObjectName("patientdetails")
        self.label_4 = QtWidgets.QLabel(self.patientdetails)
        self.label_4.setGeometry(QtCore.QRect(180, 130, 121, 41))
        self.label_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.patientdetails)
        self.label_5.setGeometry(QtCore.QRect(180, 190, 121, 41))
        self.label_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.patientdetails)
        self.label_6.setGeometry(QtCore.QRect(180, 370, 121, 41))
        self.label_6.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.patientdetails)
        self.label_7.setGeometry(QtCore.QRect(180, 430, 121, 41))
        self.label_7.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.patientdetails)
        self.label_8.setGeometry(QtCore.QRect(180, 310, 121, 41))
        self.label_8.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.patientdetails)
        self.label_9.setGeometry(QtCore.QRect(179, 250, 121, 41))
        self.label_9.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.patientdetails)
        self.label_10.setGeometry(QtCore.QRect(179, 490, 121, 41))
        self.label_10.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_10.setObjectName("label_10")
        self.firstname_lbl = QtWidgets.QLineEdit(self.patientdetails)
        self.firstname_lbl.setGeometry(QtCore.QRect(300, 130, 271, 41))
        self.firstname_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.firstname_lbl.setObjectName("firstname_lbl")
        self.lastname_lbl = QtWidgets.QLineEdit(self.patientdetails)
        self.lastname_lbl.setGeometry(QtCore.QRect(300, 190, 271, 41))
        self.lastname_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lastname_lbl.setObjectName("lastname_lbl")
        self.suburb_lbl = QtWidgets.QLineEdit(self.patientdetails)
        self.suburb_lbl.setGeometry(QtCore.QRect(300, 250, 271, 41))
        self.suburb_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.suburb_lbl.setObjectName("suburb_lbl")
        self.address_lbl = QtWidgets.QLineEdit(self.patientdetails)
        self.address_lbl.setGeometry(QtCore.QRect(300, 310, 271, 41))
        self.address_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.address_lbl.setObjectName("address_lbl")
        self.phone_number_lbl = QtWidgets.QLineEdit(self.patientdetails)
        self.phone_number_lbl.setGeometry(QtCore.QRect(300, 370, 271, 41))
        self.phone_number_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.phone_number_lbl.setObjectName("phone_number_lbl")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.patientdetails)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 430, 271, 41))
        self.lineEdit_6.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(self.patientdetails)
        self.comboBox.setGeometry(QtCore.QRect(300, 490, 121, 41))
        self.comboBox.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.patientdetails)
        self.label_11.setGeometry(QtCore.QRect(0, -10, 801, 91))
        self.label_11.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_11.setObjectName("label_11")
        self.pushButton_8 = QtWidgets.QPushButton(self.patientdetails)
        self.pushButton_8.setGeometry(QtCore.QRect(630, 490, 113, 32))
        self.pushButton_8.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.patientdetails)
        self.pushButton_9.setGeometry(QtCore.QRect(650, 20, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_114 = QtWidgets.QLabel(self.patientdetails)
        self.label_114.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_114.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_114.setObjectName("label_114")
        self.label_115 = QtWidgets.QLabel(self.patientdetails)
        self.label_115.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_115.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_115.setObjectName("label_115")
        self.stackedWidget.addWidget(self.patientdetails)
        self.appointment_details = QtWidgets.QWidget()
        self.appointment_details.setObjectName("appointment_details")
        self.label_12 = QtWidgets.QLabel(self.appointment_details)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_12.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_12.setObjectName("label_12")

        self.label_15 = QtWidgets.QLabel(self.appointment_details)
        self.label_15.setGeometry(QtCore.QRect(180, 260, 151, 31))
        self.label_15.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.appointment_details)
        self.label_16.setGeometry(QtCore.QRect(180, 160, 151, 31))
        self.label_16.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.appointment_details)
        self.label_17.setGeometry(QtCore.QRect(180, 210, 151, 31))
        self.label_17.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_17.setObjectName("label_17")
        self.patientfirstname = QtWidgets.QLineEdit(self.appointment_details)
        self.patientfirstname.setGeometry(QtCore.QRect(330, 160, 251, 31))
        self.patientfirstname.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.patientfirstname.setObjectName("patientfirstname")
        self.patientlastname = QtWidgets.QLineEdit(self.appointment_details)
        self.patientlastname.setGeometry(QtCore.QRect(330, 210, 251, 31))
        self.patientlastname.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.patientlastname.setObjectName("patientlastname")

        self.pushButton_10 = QtWidgets.QPushButton(self.appointment_details)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 30, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.appointment_details)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 440, 113, 32))
        self.pushButton_11.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.pushButton_11.setObjectName("pushButton_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.appointment_details)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 260, 261, 31))
        self.comboBox_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_112 = QtWidgets.QLabel(self.appointment_details)
        self.label_112.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_112.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_112.setObjectName("label_112")
        self.label_113 = QtWidgets.QLabel(self.appointment_details)
        self.label_113.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_113.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_113.setObjectName("label_113")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.appointment_details)
        self.dateEdit.setGeometry(QtCore.QRect(180, 300, 411, 41))
        self.dateEdit.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.appointment_details)
        self.timeEdit.setGeometry(QtCore.QRect(180, 350, 411, 41))
        self.timeEdit.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.timeEdit.setObjectName("timeEdit")
        self.stackedWidget.addWidget(self.appointment_details)
        self.typeofassessment = QtWidgets.QWidget()
        self.typeofassessment.setObjectName("typeofassessment")
        self.label_48 = QtWidgets.QLabel(self.typeofassessment)
        self.label_48.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_48.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_48.setObjectName("label_48")
        self.pushButton_15 = QtWidgets.QPushButton(self.typeofassessment)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 350, 151, 41))
        self.pushButton_15.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.typeofassessment)
        self.pushButton_16.setGeometry(QtCore.QRect(350, 220, 151, 41))
        self.pushButton_16.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.typeofassessment)
        self.pushButton_17.setGeometry(QtCore.QRect(350, 280, 151, 41))
        self.pushButton_17.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.typeofassessment)
        self.pushButton_18.setGeometry(QtCore.QRect(640, 30, 113, 32))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_110 = QtWidgets.QLabel(self.typeofassessment)
        self.label_110.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_110.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_110.setObjectName("label_110")
        self.label_111 = QtWidgets.QLabel(self.typeofassessment)
        self.label_111.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_111.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_111.setObjectName("label_111")
        self.stackedWidget.addWidget(self.typeofassessment)
        self.Physio_appointment_results = QtWidgets.QWidget()
        self.Physio_appointment_results.setObjectName("Physio_appointment_results")
        self.label_22 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_22.setGeometry(QtCore.QRect(260, 30, 60, 16))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_27 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_27.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_27.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_27.setObjectName("label_27")
        self.label_21 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_21.setGeometry(QtCore.QRect(80, 220, 121, 31))
        self.label_21.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);\n" ""
        )
        self.label_21.setObjectName("label_21")
        self.comboBox_3 = QtWidgets.QComboBox(self.Physio_appointment_results)
        self.comboBox_3.setGeometry(QtCore.QRect(590, 200, 104, 26))
        self.comboBox_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.Physio_appointment_results)
        self.comboBox_4.setGeometry(QtCore.QRect(590, 250, 104, 26))
        self.comboBox_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.Physio_appointment_results)
        self.comboBox_5.setGeometry(QtCore.QRect(590, 300, 104, 26))
        self.comboBox_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.Physio_appointment_results)
        self.comboBox_6.setGeometry(QtCore.QRect(590, 350, 104, 26))
        self.comboBox_6.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_23 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_23.setGeometry(QtCore.QRect(440, 200, 151, 21))
        self.label_23.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_24.setGeometry(QtCore.QRect(440, 250, 151, 21))
        self.label_24.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_24.setObjectName("label_24")
        self.label_28 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_28.setGeometry(QtCore.QRect(440, 300, 151, 21))
        self.label_28.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_29.setGeometry(QtCore.QRect(440, 350, 151, 21))
        self.label_29.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_30.setGeometry(QtCore.QRect(80, 270, 121, 31))
        self.label_30.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_31.setGeometry(QtCore.QRect(80, 320, 121, 31))
        self.label_31.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_31.setObjectName("label_31")
        self.physio_patient_id_lbl = QtWidgets.QLineEdit(
            self.Physio_appointment_results
        )
        self.physio_patient_id_lbl.setGeometry(QtCore.QRect(200, 220, 151, 31))
        self.physio_patient_id_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_patient_id_lbl.setObjectName("physio_patient_id_lbl")
        self.physio_appointment_date_lbl = QtWidgets.QLineEdit(
            self.Physio_appointment_results
        )
        self.physio_appointment_date_lbl.setGeometry(QtCore.QRect(200, 270, 151, 31))
        self.physio_appointment_date_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_appointment_date_lbl.setObjectName("physio_appointment_date_lbl")
        self.physio_appointment_time_lbl = QtWidgets.QLineEdit(
            self.Physio_appointment_results
        )
        self.physio_appointment_time_lbl.setGeometry(QtCore.QRect(200, 320, 151, 31))
        self.physio_appointment_time_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_appointment_time_lbl.setObjectName("physio_appointment_time_lbl")
        self.pushButton_21 = QtWidgets.QPushButton(self.Physio_appointment_results)
        self.pushButton_21.setGeometry(QtCore.QRect(360, 450, 113, 32))
        self.pushButton_21.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_24 = QtWidgets.QPushButton(self.Physio_appointment_results)
        self.pushButton_24.setGeometry(QtCore.QRect(690, 30, 113, 32))
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_108 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_108.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_108.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_108.setObjectName("label_108")
        self.label_109 = QtWidgets.QLabel(self.Physio_appointment_results)
        self.label_109.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_109.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_109.setObjectName("label_109")
        self.stackedWidget.addWidget(self.Physio_appointment_results)
        self.record_OT_assessent = QtWidgets.QWidget()
        self.record_OT_assessent.setObjectName("record_OT_assessent")
        self.label_32 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_32.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_33.setGeometry(QtCore.QRect(90, 310, 121, 31))
        self.label_33.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_34.setGeometry(QtCore.QRect(90, 260, 121, 31))
        self.label_34.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_35.setGeometry(QtCore.QRect(90, 210, 121, 31))
        self.label_35.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);\n" ""
        )
        self.label_35.setObjectName("label_35")
        self.physio_appointment_time_lbl_2 = QtWidgets.QLineEdit(
            self.record_OT_assessent
        )
        self.physio_appointment_time_lbl_2.setGeometry(QtCore.QRect(210, 310, 151, 31))
        self.physio_appointment_time_lbl_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_appointment_time_lbl_2.setObjectName(
            "physio_appointment_time_lbl_2"
        )
        self.physio_appointment_date_lbl_2 = QtWidgets.QLineEdit(
            self.record_OT_assessent
        )
        self.physio_appointment_date_lbl_2.setGeometry(QtCore.QRect(210, 260, 151, 31))
        self.physio_appointment_date_lbl_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_appointment_date_lbl_2.setObjectName(
            "physio_appointment_date_lbl_2"
        )
        self.physio_patient_id_lbl_2 = QtWidgets.QLineEdit(self.record_OT_assessent)
        self.physio_patient_id_lbl_2.setGeometry(QtCore.QRect(210, 210, 151, 31))
        self.physio_patient_id_lbl_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_patient_id_lbl_2.setObjectName("physio_patient_id_lbl_2")
        self.label_36 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_36.setGeometry(QtCore.QRect(450, 170, 171, 21))
        self.label_36.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_36.setObjectName("label_36")
        self.comboBox_7 = QtWidgets.QComboBox(self.record_OT_assessent)
        self.comboBox_7.setGeometry(QtCore.QRect(620, 170, 104, 26))
        self.comboBox_7.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_37 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_37.setGeometry(QtCore.QRect(450, 210, 171, 21))
        self.label_37.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_37.setObjectName("label_37")
        self.comboBox_8 = QtWidgets.QComboBox(self.record_OT_assessent)
        self.comboBox_8.setGeometry(QtCore.QRect(620, 210, 104, 26))
        self.comboBox_8.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_38 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_38.setGeometry(QtCore.QRect(450, 250, 171, 21))
        self.label_38.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_38.setObjectName("label_38")
        self.comboBox_9 = QtWidgets.QComboBox(self.record_OT_assessent)
        self.comboBox_9.setGeometry(QtCore.QRect(620, 250, 104, 26))
        self.comboBox_9.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_39 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_39.setGeometry(QtCore.QRect(450, 290, 171, 21))
        self.label_39.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_39.setObjectName("label_39")
        self.comboBox_10 = QtWidgets.QComboBox(self.record_OT_assessent)
        self.comboBox_10.setGeometry(QtCore.QRect(620, 290, 104, 26))
        self.comboBox_10.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_40 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_40.setGeometry(QtCore.QRect(450, 330, 171, 21))
        self.label_40.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_40.setObjectName("label_40")
        self.comboBox_11 = QtWidgets.QComboBox(self.record_OT_assessent)
        self.comboBox_11.setGeometry(QtCore.QRect(620, 330, 104, 26))
        self.comboBox_11.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.label_41 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_41.setGeometry(QtCore.QRect(450, 370, 171, 21))
        self.label_41.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_41.setObjectName("label_41")
        self.comboBox_12 = QtWidgets.QComboBox(self.record_OT_assessent)
        self.comboBox_12.setGeometry(QtCore.QRect(620, 370, 104, 26))
        self.comboBox_12.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.pushButton_19 = QtWidgets.QPushButton(self.record_OT_assessent)
        self.pushButton_19.setGeometry(QtCore.QRect(360, 430, 113, 32))
        self.pushButton_19.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.record_OT_assessent)
        self.pushButton_20.setGeometry(QtCore.QRect(680, 30, 113, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_106 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_106.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_106.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_106.setObjectName("label_106")
        self.label_107 = QtWidgets.QLabel(self.record_OT_assessent)
        self.label_107.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_107.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_107.setObjectName("label_107")
        self.stackedWidget.addWidget(self.record_OT_assessent)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.physio_appointment_date_lbl_3 = QtWidgets.QLineEdit(self.page)
        self.physio_appointment_date_lbl_3.setGeometry(QtCore.QRect(210, 260, 151, 31))
        self.physio_appointment_date_lbl_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_appointment_date_lbl_3.setObjectName(
            "physio_appointment_date_lbl_3"
        )
        self.physio_appointment_time_lbl_3 = QtWidgets.QLineEdit(self.page)
        self.physio_appointment_time_lbl_3.setGeometry(QtCore.QRect(210, 310, 151, 31))
        self.physio_appointment_time_lbl_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_appointment_time_lbl_3.setObjectName(
            "physio_appointment_time_lbl_3"
        )
        self.label_42 = QtWidgets.QLabel(self.page)
        self.label_42.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_42.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.page)
        self.label_43.setGeometry(QtCore.QRect(450, 200, 171, 21))
        self.label_43.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page)
        self.label_44.setGeometry(QtCore.QRect(90, 260, 121, 31))
        self.label_44.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.page)
        self.label_45.setGeometry(QtCore.QRect(90, 210, 121, 31))
        self.label_45.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);\n" ""
        )
        self.label_45.setObjectName("label_45")
        self.comboBox_13 = QtWidgets.QComboBox(self.page)
        self.comboBox_13.setGeometry(QtCore.QRect(620, 200, 104, 26))
        self.comboBox_13.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.physio_patient_id_lbl_3 = QtWidgets.QLineEdit(self.page)
        self.physio_patient_id_lbl_3.setGeometry(QtCore.QRect(210, 210, 151, 31))
        self.physio_patient_id_lbl_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.physio_patient_id_lbl_3.setObjectName("physio_patient_id_lbl_3")
        self.label_46 = QtWidgets.QLabel(self.page)
        self.label_46.setGeometry(QtCore.QRect(90, 310, 121, 31))
        self.label_46.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.page)
        self.label_47.setGeometry(QtCore.QRect(450, 240, 171, 21))
        self.label_47.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_47.setObjectName("label_47")
        self.comboBox_14 = QtWidgets.QComboBox(self.page)
        self.comboBox_14.setGeometry(QtCore.QRect(620, 240, 104, 26))
        self.comboBox_14.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_49 = QtWidgets.QLabel(self.page)
        self.label_49.setGeometry(QtCore.QRect(450, 280, 171, 21))
        self.label_49.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_49.setObjectName("label_49")
        self.comboBox_16 = QtWidgets.QComboBox(self.page)
        self.comboBox_16.setGeometry(QtCore.QRect(620, 280, 104, 26))
        self.comboBox_16.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.label_50 = QtWidgets.QLabel(self.page)
        self.label_50.setGeometry(QtCore.QRect(450, 160, 171, 21))
        self.label_50.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_50.setObjectName("label_50")
        self.comboBox_17 = QtWidgets.QComboBox(self.page)
        self.comboBox_17.setGeometry(QtCore.QRect(620, 160, 104, 26))
        self.comboBox_17.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.label_51 = QtWidgets.QLabel(self.page)
        self.label_51.setGeometry(QtCore.QRect(450, 320, 171, 21))
        self.label_51.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_51.setObjectName("label_51")
        self.comboBox_18 = QtWidgets.QComboBox(self.page)
        self.comboBox_18.setGeometry(QtCore.QRect(620, 320, 104, 26))
        self.comboBox_18.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.label_52 = QtWidgets.QLabel(self.page)
        self.label_52.setGeometry(QtCore.QRect(450, 400, 171, 21))
        self.label_52.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_52.setObjectName("label_52")
        self.comboBox_19 = QtWidgets.QComboBox(self.page)
        self.comboBox_19.setGeometry(QtCore.QRect(620, 400, 104, 26))
        self.comboBox_19.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.label_53 = QtWidgets.QLabel(self.page)
        self.label_53.setGeometry(QtCore.QRect(450, 440, 171, 21))
        self.label_53.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_53.setObjectName("label_53")
        self.comboBox_20 = QtWidgets.QComboBox(self.page)
        self.comboBox_20.setGeometry(QtCore.QRect(620, 440, 104, 26))
        self.comboBox_20.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_21 = QtWidgets.QComboBox(self.page)
        self.comboBox_21.setGeometry(QtCore.QRect(620, 360, 104, 26))
        self.comboBox_21.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.label_55 = QtWidgets.QLabel(self.page)
        self.label_55.setGeometry(QtCore.QRect(450, 360, 171, 21))
        self.label_55.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_55.setObjectName("label_55")
        self.pushButton_22 = QtWidgets.QPushButton(self.page)
        self.pushButton_22.setGeometry(QtCore.QRect(350, 490, 113, 32))
        self.pushButton_22.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.page)
        self.pushButton_23.setGeometry(QtCore.QRect(670, 30, 113, 32))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_96 = QtWidgets.QLabel(self.page)
        self.label_96.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_96.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_96.setObjectName("label_96")
        self.label_105 = QtWidgets.QLabel(self.page)
        self.label_105.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_105.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_105.setObjectName("label_105")
        self.stackedWidget.addWidget(self.page)
        self.record_regime = QtWidgets.QWidget()
        self.record_regime.setObjectName("record_regime")
        self.label_18 = QtWidgets.QLabel(self.record_regime)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_18.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_18.setObjectName("label_18")
        self.record_exercise_regime_patient_id = QtWidgets.QLineEdit(self.record_regime)
        self.record_exercise_regime_patient_id.setGeometry(
            QtCore.QRect(80, 120, 121, 31)
        )
        self.record_exercise_regime_patient_id.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.record_exercise_regime_patient_id.setObjectName(
            "record_exercise_regime_patient_id"
        )
        self.label_19 = QtWidgets.QLabel(self.record_regime)
        self.label_19.setGeometry(QtCore.QRect(10, 120, 71, 31))
        self.label_19.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.record_regime)
        self.label_20.setGeometry(QtCore.QRect(250, 120, 111, 31))
        self.label_20.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);\n" ""
        )
        self.label_20.setObjectName("label_20")
        self.label_25 = QtWidgets.QLabel(self.record_regime)
        self.label_25.setGeometry(QtCore.QRect(10, 160, 71, 31))
        self.label_25.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_25.setObjectName("label_25")
        self.pushButton_4 = QtWidgets.QPushButton(self.record_regime)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 210, 131, 41))
        self.pushButton_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_26 = QtWidgets.QLabel(self.record_regime)
        self.label_26.setGeometry(QtCore.QRect(250, 160, 111, 31))
        self.label_26.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_26.setObjectName("label_26")
        self.pushButton_12 = QtWidgets.QPushButton(self.record_regime)
        self.pushButton_12.setGeometry(QtCore.QRect(260, 210, 141, 41))
        self.pushButton_12.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);\n" ""
        )
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.record_regime)
        self.pushButton_13.setGeometry(QtCore.QRect(160, 350, 113, 32))
        self.pushButton_13.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_13.setObjectName("pushButton_13")
        self.record_exercise_regime_exercise_name = QtWidgets.QLineEdit(
            self.record_regime
        )
        self.record_exercise_regime_exercise_name.setGeometry(
            QtCore.QRect(360, 120, 171, 31)
        )
        self.record_exercise_regime_exercise_name.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.record_exercise_regime_exercise_name.setObjectName(
            "record_exercise_regime_exercise_name"
        )
        self.record_exercise_regime_date = QtWidgets.QLineEdit(self.record_regime)
        self.record_exercise_regime_date.setGeometry(QtCore.QRect(80, 160, 121, 31))
        self.record_exercise_regime_date.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.record_exercise_regime_date.setObjectName("record_exercise_regime_date")
        self.spinBox = QtWidgets.QSpinBox(self.record_regime)
        self.spinBox.setGeometry(QtCore.QRect(360, 160, 48, 24))
        self.spinBox.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.spinBox.setObjectName("spinBox")
        self.tableView_2 = QtWidgets.QTableView(self.record_regime)
        self.tableView_2.setGeometry(QtCore.QRect(610, 81, 256, 461))
        self.tableView_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton_29 = QtWidgets.QPushButton(self.record_regime)
        self.pushButton_29.setGeometry(QtCore.QRect(680, 40, 113, 32))
        self.pushButton_29.setObjectName("pushButton_29")
        self.label_90 = QtWidgets.QLabel(self.record_regime)
        self.label_90.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_90.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_90.setObjectName("label_90")
        self.label_92 = QtWidgets.QLabel(self.record_regime)
        self.label_92.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_92.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_92.setObjectName("label_92")
        self.stackedWidget.addWidget(self.record_regime)
        self.previous_appointments = QtWidgets.QWidget()
        self.previous_appointments.setObjectName("previous_appointments")
        self.label_54 = QtWidgets.QLabel(self.previous_appointments)
        self.label_54.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_54.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_54.setObjectName("label_54")
        self.label_56 = QtWidgets.QLabel(self.previous_appointments)
        self.label_56.setGeometry(QtCore.QRect(61, 130, 81, 21))
        self.label_56.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.previous_appointments)
        self.label_57.setGeometry(QtCore.QRect(491, 130, 121, 21))
        self.label_57.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_57.setObjectName("label_57")
        self.comboBox_15 = QtWidgets.QComboBox(self.previous_appointments)
        self.comboBox_15.setGeometry(QtCore.QRect(611, 130, 171, 26))
        self.comboBox_15.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_15.setObjectName("comboBox_15")
        self.previous_appointments_patient_id = QtWidgets.QLineEdit(
            self.previous_appointments
        )
        self.previous_appointments_patient_id.setGeometry(
            QtCore.QRect(141, 130, 121, 21)
        )
        self.previous_appointments_patient_id.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.previous_appointments_patient_id.setObjectName(
            "previous_appointments_patient_id"
        )
        self.label_58 = QtWidgets.QLabel(self.previous_appointments)
        self.label_58.setGeometry(QtCore.QRect(101, 180, 71, 21))
        self.label_58.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.previous_appointments)
        self.label_59.setGeometry(QtCore.QRect(351, 180, 61, 21))
        self.label_59.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.previous_appointments)
        self.label_60.setGeometry(QtCore.QRect(641, 180, 61, 21))
        self.label_60.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.previous_appointments)
        self.label_61.setGeometry(QtCore.QRect(20, 220, 141, 20))
        self.label_61.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.previous_appointments)
        self.label_62.setGeometry(QtCore.QRect(20, 250, 141, 20))
        self.label_62.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.previous_appointments)
        self.label_63.setGeometry(QtCore.QRect(20, 280, 141, 20))
        self.label_63.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.previous_appointments)
        self.label_64.setGeometry(QtCore.QRect(20, 310, 141, 20))
        self.label_64.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_64.setObjectName("label_64")
        self.knee_externsors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.knee_externsors_score_lbl.setGeometry(QtCore.QRect(181, 250, 16, 21))
        self.knee_externsors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.knee_externsors_score_lbl.setObjectName("knee_externsors_score_lbl")
        self.dorsiflexors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.dorsiflexors_score_lbl.setGeometry(QtCore.QRect(181, 280, 16, 21))
        self.dorsiflexors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.dorsiflexors_score_lbl.setObjectName("dorsiflexors_score_lbl")
        self.plantar_flexors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.plantar_flexors_score_lbl.setGeometry(QtCore.QRect(181, 310, 16, 21))
        self.plantar_flexors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.plantar_flexors_score_lbl.setObjectName("plantar_flexors_score_lbl")
        self.hip_flexor_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.hip_flexor_score_lbl.setGeometry(QtCore.QRect(181, 220, 16, 21))
        self.hip_flexor_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.hip_flexor_score_lbl.setObjectName("hip_flexor_score_lbl")
        self.dysphonia_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.dysphonia_score_lbl.setGeometry(QtCore.QRect(461, 310, 16, 21))
        self.dysphonia_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.dysphonia_score_lbl.setObjectName("dysphonia_score_lbl")
        self.label_70 = QtWidgets.QLabel(self.previous_appointments)
        self.label_70.setGeometry(QtCore.QRect(300, 250, 141, 20))
        self.label_70.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.previous_appointments)
        self.label_71.setGeometry(QtCore.QRect(300, 280, 141, 20))
        self.label_71.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.previous_appointments)
        self.label_72.setGeometry(QtCore.QRect(300, 310, 141, 20))
        self.label_72.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_72.setObjectName("label_72")
        self.dysarthria_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.dysarthria_score_lbl.setGeometry(QtCore.QRect(461, 280, 16, 21))
        self.dysarthria_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.dysarthria_score_lbl.setObjectName("dysarthria_score_lbl")
        self.apraxia_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.apraxia_score_lbl.setGeometry(QtCore.QRect(461, 250, 16, 21))
        self.apraxia_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.apraxia_score_lbl.setObjectName("apraxia_score_lbl")
        self.label_75 = QtWidgets.QLabel(self.previous_appointments)
        self.label_75.setGeometry(QtCore.QRect(300, 220, 141, 20))
        self.label_75.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_75.setObjectName("label_75")
        self.aphasia_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.aphasia_score_lbl.setGeometry(QtCore.QRect(461, 220, 16, 21))
        self.aphasia_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.aphasia_score_lbl.setObjectName("aphasia_score_lbl")
        self.neglect_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.neglect_score_lbl.setGeometry(QtCore.QRect(461, 430, 16, 21))
        self.neglect_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.neglect_score_lbl.setObjectName("neglect_score_lbl")
        self.label_78 = QtWidgets.QLabel(self.previous_appointments)
        self.label_78.setGeometry(QtCore.QRect(300, 370, 141, 20))
        self.label_78.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.previous_appointments)
        self.label_79.setGeometry(QtCore.QRect(300, 400, 141, 20))
        self.label_79.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.previous_appointments)
        self.label_80.setGeometry(QtCore.QRect(300, 430, 141, 20))
        self.label_80.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_80.setObjectName("label_80")
        self.judgment_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.judgment_score_lbl.setGeometry(QtCore.QRect(461, 400, 16, 21))
        self.judgment_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.judgment_score_lbl.setObjectName("judgment_score_lbl")
        self.attention_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.attention_score_lbl.setGeometry(QtCore.QRect(461, 370, 16, 21))
        self.attention_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.attention_score_lbl.setObjectName("attention_score_lbl")
        self.label_83 = QtWidgets.QLabel(self.previous_appointments)
        self.label_83.setGeometry(QtCore.QRect(300, 340, 141, 20))
        self.label_83.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_83.setObjectName("label_83")
        self.memory_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.memory_score_lbl.setGeometry(QtCore.QRect(461, 340, 16, 21))
        self.memory_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.memory_score_lbl.setObjectName("memory_score_lbl")
        self.finger_flexors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.finger_flexors_score_lbl.setGeometry(QtCore.QRect(761, 340, 16, 21))
        self.finger_flexors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.finger_flexors_score_lbl.setObjectName("finger_flexors_score_lbl")
        self.label_86 = QtWidgets.QLabel(self.previous_appointments)
        self.label_86.setGeometry(QtCore.QRect(570, 310, 171, 20))
        self.label_86.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_86.setObjectName("label_86")
        self.wrist_extensors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.wrist_extensors_score_lbl.setGeometry(QtCore.QRect(761, 310, 16, 21))
        self.wrist_extensors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.wrist_extensors_score_lbl.setObjectName("wrist_extensors_score_lbl")
        self.label_88 = QtWidgets.QLabel(self.previous_appointments)
        self.label_88.setGeometry(QtCore.QRect(570, 280, 171, 20))
        self.label_88.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.previous_appointments)
        self.label_89.setGeometry(QtCore.QRect(570, 250, 171, 20))
        self.label_89.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_89.setObjectName("label_89")
        self.elbow_flexors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.elbow_flexors_score_lbl.setGeometry(QtCore.QRect(761, 250, 16, 21))
        self.elbow_flexors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.elbow_flexors_score_lbl.setObjectName("elbow_flexors_score_lbl")
        self.label_91 = QtWidgets.QLabel(self.previous_appointments)
        self.label_91.setGeometry(QtCore.QRect(761, 370, 16, 21))
        self.label_91.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_91.setObjectName("label_91")
        self.elbow_extensors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.elbow_extensors_score_lbl.setGeometry(QtCore.QRect(761, 280, 16, 21))
        self.elbow_extensors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.elbow_extensors_score_lbl.setObjectName("elbow_extensors_score_lbl")
        self.label_93 = QtWidgets.QLabel(self.previous_appointments)
        self.label_93.setGeometry(QtCore.QRect(570, 220, 171, 20))
        self.label_93.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.previous_appointments)
        self.label_94.setGeometry(QtCore.QRect(570, 370, 171, 20))
        self.label_94.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_94.setObjectName("label_94")
        self.label_95 = QtWidgets.QLabel(self.previous_appointments)
        self.label_95.setGeometry(QtCore.QRect(570, 340, 171, 20))
        self.label_95.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_95.setObjectName("label_95")
        self.shoulder_abductors_score_lbl = QtWidgets.QLabel(self.previous_appointments)
        self.shoulder_abductors_score_lbl.setGeometry(QtCore.QRect(761, 220, 16, 21))
        self.shoulder_abductors_score_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.shoulder_abductors_score_lbl.setObjectName("shoulder_abductors_score_lbl")
        self.pushButton_26 = QtWidgets.QPushButton(self.previous_appointments)
        self.pushButton_26.setGeometry(QtCore.QRect(670, 30, 113, 32))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_85 = QtWidgets.QLabel(self.previous_appointments)
        self.label_85.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_85.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_85.setObjectName("label_85")
        self.label_87 = QtWidgets.QLabel(self.previous_appointments)
        self.label_87.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_87.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_87.setObjectName("label_87")
        self.stackedWidget.addWidget(self.previous_appointments)
        self.previous_exercise_regime = QtWidgets.QWidget()
        self.previous_exercise_regime.setObjectName("previous_exercise_regime")
        self.label_98 = QtWidgets.QLabel(self.previous_exercise_regime)
        self.label_98.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_98.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_98.setObjectName("label_98")
        self.label_99 = QtWidgets.QLabel(self.previous_exercise_regime)
        self.label_99.setGeometry(QtCore.QRect(20, 130, 81, 21))
        self.label_99.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_99.setObjectName("label_99")
        self.label_100 = QtWidgets.QLabel(self.previous_exercise_regime)
        self.label_100.setGeometry(QtCore.QRect(350, 130, 81, 21))
        self.label_100.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_100.setObjectName("label_100")
        self.comboBox_22 = QtWidgets.QComboBox(self.previous_exercise_regime)
        self.comboBox_22.setGeometry(QtCore.QRect(430, 130, 104, 26))
        self.comboBox_22.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_22.setObjectName("comboBox_22")
        self.previous_exercises_patient_id = QtWidgets.QLineEdit(
            self.previous_exercise_regime
        )
        self.previous_exercises_patient_id.setGeometry(QtCore.QRect(100, 130, 113, 21))
        self.previous_exercises_patient_id.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.previous_exercises_patient_id.setObjectName(
            "previous_exercises_patient_id"
        )
        self.tableView = QtWidgets.QTableView(self.previous_exercise_regime)
        self.tableView.setGeometry(QtCore.QRect(570, 81, 256, 501))
        self.tableView.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.tableView.setObjectName("tableView")
        self.pushButton_28 = QtWidgets.QPushButton(self.previous_exercise_regime)
        self.pushButton_28.setGeometry(QtCore.QRect(680, 40, 113, 32))
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_82 = QtWidgets.QLabel(self.previous_exercise_regime)
        self.label_82.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_82.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_82.setObjectName("label_82")
        self.label_84 = QtWidgets.QLabel(self.previous_exercise_regime)
        self.label_84.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_84.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_84.setObjectName("label_84")
        self.stackedWidget.addWidget(self.previous_exercise_regime)
        self.get_patient_id = QtWidgets.QWidget()
        self.get_patient_id.setObjectName("get_patient_id")
        self.label_101 = QtWidgets.QLabel(self.get_patient_id)
        self.label_101.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_101.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_101.setObjectName("label_101")
        self.label_102 = QtWidgets.QLabel(self.get_patient_id)
        self.label_102.setGeometry(QtCore.QRect(170, 200, 101, 31))
        self.label_102.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_102.setObjectName("label_102")
        self.label_103 = QtWidgets.QLabel(self.get_patient_id)
        self.label_103.setGeometry(QtCore.QRect(170, 270, 101, 31))
        self.label_103.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_103.setObjectName("label_103")
        self.label_104 = QtWidgets.QLabel(self.get_patient_id)
        self.label_104.setGeometry(QtCore.QRect(170, 340, 101, 31))
        self.label_104.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_104.setObjectName("label_104")
        self.get_patient_id_first_name = QtWidgets.QLineEdit(self.get_patient_id)
        self.get_patient_id_first_name.setGeometry(QtCore.QRect(270, 200, 181, 31))
        self.get_patient_id_first_name.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.get_patient_id_first_name.setObjectName("get_patient_id_first_name")
        self.get_patient_id_phone_number = QtWidgets.QLineEdit(self.get_patient_id)
        self.get_patient_id_phone_number.setGeometry(QtCore.QRect(270, 340, 181, 31))
        self.get_patient_id_phone_number.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.get_patient_id_phone_number.setObjectName("get_patient_id_phone_number")
        self.get_patient_id_last_name = QtWidgets.QLineEdit(self.get_patient_id)
        self.get_patient_id_last_name.setGeometry(QtCore.QRect(270, 270, 181, 31))
        self.get_patient_id_last_name.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.get_patient_id_last_name.setObjectName("get_patient_id_last_name")
        self.pushButton_27 = QtWidgets.QPushButton(self.get_patient_id)
        self.pushButton_27.setGeometry(QtCore.QRect(660, 30, 113, 32))
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_77 = QtWidgets.QLabel(self.get_patient_id)
        self.label_77.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_77.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_77.setObjectName("label_77")
        self.label_81 = QtWidgets.QLabel(self.get_patient_id)
        self.label_81.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_81.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_81.setObjectName("label_81")
        self.stackedWidget.addWidget(self.get_patient_id)
        self.practice_admin_menu = QtWidgets.QWidget()
        self.practice_admin_menu.setObjectName("practice_admin_menu")
        self.label_231 = QtWidgets.QLabel(self.practice_admin_menu)
        self.label_231.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_231.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_231.setObjectName("label_231")
        self.label_232 = QtWidgets.QLabel(self.practice_admin_menu)
        self.label_232.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_232.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_232.setObjectName("label_232")
        self.label_233 = QtWidgets.QLabel(self.practice_admin_menu)
        self.label_233.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_233.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_233.setObjectName("label_233")
        self.pushButton_59 = QtWidgets.QPushButton(self.practice_admin_menu)
        self.pushButton_59.setGeometry(QtCore.QRect(660, 30, 113, 32))
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.practice_admin_menu)
        self.pushButton_60.setGeometry(QtCore.QRect(210, 260, 161, 51))
        self.pushButton_60.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.practice_admin_menu)
        self.pushButton_61.setGeometry(QtCore.QRect(410, 260, 161, 51))
        self.pushButton_61.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_61.setObjectName("pushButton_61")
        self.label_233.raise_()
        self.pushButton_59.raise_()
        self.label_231.raise_()
        self.label_232.raise_()
        self.pushButton_60.raise_()
        self.pushButton_61.raise_()
        self.stackedWidget.addWidget(self.practice_admin_menu)
        self.insertclinician = QtWidgets.QWidget()
        self.insertclinician.setObjectName("insertclinician")
        self.label_234 = QtWidgets.QLabel(self.insertclinician)
        self.label_234.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_234.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_234.setObjectName("label_234")
        self.pushButton_62 = QtWidgets.QPushButton(self.insertclinician)
        self.pushButton_62.setGeometry(QtCore.QRect(660, 30, 113, 32))
        self.pushButton_62.setObjectName("pushButton_62")
        self.label_235 = QtWidgets.QLabel(self.insertclinician)
        self.label_235.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_235.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_235.setObjectName("label_235")
        self.label_236 = QtWidgets.QLabel(self.insertclinician)
        self.label_236.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_236.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_236.setObjectName("label_236")
        self.label_237 = QtWidgets.QLabel(self.insertclinician)
        self.label_237.setGeometry(QtCore.QRect(120, 160, 91, 31))
        self.label_237.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_237.setObjectName("label_237")
        self.label_238 = QtWidgets.QLabel(self.insertclinician)
        self.label_238.setGeometry(QtCore.QRect(120, 200, 91, 31))
        self.label_238.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_238.setObjectName("label_238")
        self.label_239 = QtWidgets.QLabel(self.insertclinician)
        self.label_239.setGeometry(QtCore.QRect(120, 240, 91, 31))
        self.label_239.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_239.setObjectName("label_239")
        self.label_240 = QtWidgets.QLabel(self.insertclinician)
        self.label_240.setGeometry(QtCore.QRect(120, 280, 91, 31))
        self.label_240.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_240.setObjectName("label_240")
        self.label_241 = QtWidgets.QLabel(self.insertclinician)
        self.label_241.setGeometry(QtCore.QRect(120, 320, 91, 31))
        self.label_241.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_241.setObjectName("label_241")
        self.insert_clinician_firstname = QtWidgets.QLineEdit(self.insertclinician)
        self.insert_clinician_firstname.setGeometry(QtCore.QRect(210, 160, 201, 31))
        self.insert_clinician_firstname.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.insert_clinician_firstname.setText("")
        self.insert_clinician_firstname.setObjectName("insert_clinician_firstname")
        self.insert_clinician_lastname = QtWidgets.QLineEdit(self.insertclinician)
        self.insert_clinician_lastname.setGeometry(QtCore.QRect(210, 200, 201, 31))
        self.insert_clinician_lastname.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.insert_clinician_lastname.setObjectName("insert_clinician_lastname")
        self.insert_clinician_username = QtWidgets.QLineEdit(self.insertclinician)
        self.insert_clinician_username.setGeometry(QtCore.QRect(210, 240, 201, 31))
        self.insert_clinician_username.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.insert_clinician_username.setObjectName("insert_clinician_username")
        self.insert_clinician_password = QtWidgets.QLineEdit(self.insertclinician)
        self.insert_clinician_password.setGeometry(QtCore.QRect(210, 280, 201, 31))
        self.insert_clinician_password.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.insert_clinician_password.setObjectName("insert_clinician_password")
        self.comboBox_45 = QtWidgets.QComboBox(self.insertclinician)
        self.comboBox_45.setGeometry(QtCore.QRect(210, 320, 201, 31))
        self.comboBox_45.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_45.setObjectName("comboBox_45")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.pushButton_63 = QtWidgets.QPushButton(self.insertclinician)
        self.pushButton_63.setGeometry(QtCore.QRect(330, 440, 113, 32))
        self.pushButton_63.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.pushButton_63.setObjectName("pushButton_63")
        self.label_235.raise_()
        self.label_234.raise_()
        self.pushButton_62.raise_()
        self.label_236.raise_()
        self.label_237.raise_()
        self.label_238.raise_()
        self.label_239.raise_()
        self.label_240.raise_()
        self.label_241.raise_()
        self.insert_clinician_firstname.raise_()
        self.insert_clinician_lastname.raise_()
        self.insert_clinician_username.raise_()
        self.insert_clinician_password.raise_()
        self.comboBox_45.raise_()
        self.pushButton_63.raise_()
        self.stackedWidget.addWidget(self.insertclinician)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_242 = QtWidgets.QLabel(self.page_3)
        self.label_242.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_242.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_242.setObjectName("label_242")
        self.pushButton_64 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_64.setGeometry(QtCore.QRect(660, 30, 113, 32))
        self.pushButton_64.setObjectName("pushButton_64")
        self.label_243 = QtWidgets.QLabel(self.page_3)
        self.label_243.setGeometry(QtCore.QRect(11, -10, 111, 111))
        self.label_243.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_243.setObjectName("label_243")
        self.label_244 = QtWidgets.QLabel(self.page_3)
        self.label_244.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.label_244.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_244.setObjectName("label_244")
        self.label_245 = QtWidgets.QLabel(self.page_3)
        self.label_245.setGeometry(QtCore.QRect(250, 155, 101, 31))
        self.label_245.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_245.setObjectName("label_245")
        self.label_246 = QtWidgets.QLabel(self.page_3)
        self.label_246.setGeometry(QtCore.QRect(250, 210, 101, 31))
        self.label_246.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_246.setObjectName("label_246")
        self.label_247 = QtWidgets.QLabel(self.page_3)
        self.label_247.setGeometry(QtCore.QRect(250, 270, 101, 31))
        self.label_247.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_247.setObjectName("label_247")
        self.comboBox_46 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_46.setGeometry(QtCore.QRect(350, 155, 181, 31))
        self.comboBox_46.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_46.setObjectName("comboBox_46")
        self.comboBox_47 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_47.setGeometry(QtCore.QRect(350, 210, 181, 31))
        self.comboBox_47.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.comboBox_47.setObjectName("comboBox_47")
        self.label_248 = QtWidgets.QLabel(self.page_3)
        self.label_248.setGeometry(QtCore.QRect(350, 270, 181, 31))
        self.label_248.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.label_248.setObjectName("label_248")
        self.stackedWidget.addWidget(self.page_3)
        self.log_in_as_practice_administrator = QtWidgets.QWidget()
        self.log_in_as_practice_administrator.setObjectName(
            "log_in_as_practice_administrator"
        )
        self.label_2 = QtWidgets.QLabel(self.log_in_as_practice_administrator)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.label_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.label_2.setObjectName("label_2")
        self.lg_username_practice_admin_lbl = QtWidgets.QLineEdit(
            self.log_in_as_practice_administrator
        )
        self.lg_username_practice_admin_lbl.setGeometry(QtCore.QRect(350, 250, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_username_practice_admin_lbl.setFont(font)
        self.lg_username_practice_admin_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lg_username_practice_admin_lbl.setObjectName(
            "lg_username_practice_admin_lbl"
        )
        self.lg_user_name_lb_2 = QtWidgets.QLabel(self.log_in_as_practice_administrator)
        self.lg_user_name_lb_2.setGeometry(QtCore.QRect(200, 250, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_user_name_lb_2.setFont(font)
        self.lg_user_name_lb_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.lg_user_name_lb_2.setObjectName("lg_user_name_lb_2")
        self.lg_password_practice_admin_lbl = QtWidgets.QLineEdit(
            self.log_in_as_practice_administrator
        )
        self.lg_password_practice_admin_lbl.setGeometry(QtCore.QRect(350, 310, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_password_practice_admin_lbl.setFont(font)
        self.lg_password_practice_admin_lbl.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(76,95,122);"
        )
        self.lg_password_practice_admin_lbl.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password
        )
        self.lg_password_practice_admin_lbl.setObjectName(
            "lg_password_practice_admin_lbl"
        )
        self.lg_password_lb_2 = QtWidgets.QLabel(self.log_in_as_practice_administrator)
        self.lg_password_lb_2.setGeometry(QtCore.QRect(200, 310, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lg_password_lb_2.setFont(font)
        self.lg_password_lb_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.lg_password_lb_2.setObjectName("lg_password_lb_2")
        self.lg_login_btn_3 = QtWidgets.QPushButton(
            self.log_in_as_practice_administrator
        )
        self.lg_login_btn_3.setGeometry(QtCore.QRect(199, 380, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lg_login_btn_3.setFont(font)
        self.lg_login_btn_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(037,040,080);"
        )
        self.lg_login_btn_3.setObjectName("lg_login_btn_3")
        self.lg_login_btn_4 = QtWidgets.QPushButton(
            self.log_in_as_practice_administrator
        )
        self.lg_login_btn_4.setGeometry(QtCore.QRect(660, 20, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lg_login_btn_4.setFont(font)
        self.lg_login_btn_4.setObjectName("lg_login_btn_4")
        self.label_74 = QtWidgets.QLabel(self.log_in_as_practice_administrator)
        self.label_74.setGeometry(QtCore.QRect(10, -10, 111, 111))
        self.label_74.setStyleSheet(
            "image: url(:/newPrefix/Downloads/Road to Recovery logo 1.png);"
        )
        self.label_74.setObjectName("label_74")
        self.label_76 = QtWidgets.QLabel(self.log_in_as_practice_administrator)
        self.label_76.setGeometry(QtCore.QRect(-1, 80, 131, 31))
        self.label_76.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);"
        )
        self.label_76.setObjectName("label_76")
        self.stackedWidget.addWidget(self.log_in_as_practice_administrator)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(15)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Log in</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("MainWindow", "log in as clinician"))
        self.pushButton_2.setText(
            _translate("MainWindow", "log in as practice administrator")
        )
        self.label_67.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_68.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Log in as clinician</span></p></body></html>',
            )
        )
        self.lg_user_name_lb.setText(_translate("MainWindow", "User name"))
        self.lg_password_lb.setText(_translate("MainWindow", "Password"))
        self.lg_login_btn.setText(_translate("MainWindow", "Login"))
        self.lg_login_btn_2.setText(_translate("MainWindow", "back"))
        self.label_69.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_73.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.pushButton_3.setText(_translate("MainWindow", "Record patient details"))
        self.pushButton_5.setText(
            _translate("MainWindow", "Record appointment results")
        )
        self.pushButton_6.setText(
            _translate("MainWindow", "Record patient exercise regime")
        )
        self.pushButton_7.setText(
            _translate("MainWindow", "Previous patinet appointments")
        )
        self.pushButton_14.setText(_translate("MainWindow", "Book appointment"))
        self.pushButton_25.setText(_translate("MainWindow", "Previous exercise regime"))
        self.label_97.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Clinician Menu</span></p></body></html>',
            )
        )
        self.label_65.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_66.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">First name</span></p></body></html>',
            )
        )
        self.label_5.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Last name</span></p></body></html>',
            )
        )
        self.label_6.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Phone number</span></p></body></html>',
            )
        )
        self.label_7.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Email</span></p></body></html>',
            )
        )
        self.label_8.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Address</span></p></body></html>',
            )
        )
        self.label_9.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Suburb</span></p></body></html>',
            )
        )
        self.label_10.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Gender</span></p></body></html>',
            )
        )
        self.comboBox.setItemText(0, _translate("MainWindow", "male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "female"))
        self.comboBox.setItemText(2, _translate("MainWindow", "bigender"))
        self.comboBox.setItemText(3, _translate("MainWindow", "agender"))
        self.comboBox.setItemText(4, _translate("MainWindow", "polygender"))
        self.comboBox.setItemText(5, _translate("MainWindow", "genderfluid"))
        self.label_11.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Patient details</span></p></body></html>',
            )
        )
        self.pushButton_8.setText(_translate("MainWindow", "Submit"))
        self.pushButton_9.setText(_translate("MainWindow", "menu"))
        self.label_114.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_115.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_12.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Appointment details</span></p></body></html>',
            )
        )

        self.label_15.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Clinician</span></p></body></html>',
            )
        )
        self.label_16.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Patient first name</span></p></body></html>',
            )
        )
        self.label_17.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt;">Patient last name</span></p></body></html>',
            )
        )
        self.pushButton_10.setText(_translate("MainWindow", "menu"))
        self.pushButton_11.setText(_translate("MainWindow", "submit"))
        self.label_112.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_113.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_48.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Record assessment results</span></p></body></html>',
            )
        )
        self.pushButton_15.setText(_translate("MainWindow", "speech assessment"))
        self.pushButton_16.setText(_translate("MainWindow", "OT assessment"))
        self.pushButton_17.setText(_translate("MainWindow", "physio assessment"))
        self.pushButton_18.setText(_translate("MainWindow", "menu"))
        self.label_110.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_111.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_27.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Record physio assessment results</span></p></body></html>',
            )
        )
        self.label_21.setText(_translate("MainWindow", "Patient id"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "5"))
        self.label_23.setText(_translate("MainWindow", "Hip flexor_score"))
        self.label_24.setText(_translate("MainWindow", "Knee_externsors_score"))
        self.label_28.setText(_translate("MainWindow", "Dorsiflexors_score"))
        self.label_29.setText(_translate("MainWindow", "Plantar_flexors_score"))
        self.label_30.setText(_translate("MainWindow", "Appointment date"))
        self.label_31.setText(_translate("MainWindow", "Appointment time"))
        self.pushButton_21.setText(_translate("MainWindow", "submit"))
        self.pushButton_24.setText(_translate("MainWindow", "menu"))
        self.label_108.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_109.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_32.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Record OT assessment results</span></p></body></html>',
            )
        )
        self.label_33.setText(_translate("MainWindow", "Appointment time"))
        self.label_34.setText(_translate("MainWindow", "Appointment date"))
        self.label_35.setText(_translate("MainWindow", "Patient id"))
        self.label_36.setText(_translate("MainWindow", "shoulder_abductors_score"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "5"))
        self.label_37.setText(_translate("MainWindow", "elbow_flexors_score"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "5"))
        self.label_38.setText(_translate("MainWindow", "elbow_extensors_score"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "5"))
        self.label_39.setText(_translate("MainWindow", "wrist_extensors_score"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "5"))
        self.label_40.setText(_translate("MainWindow", "finger_flexors_score"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_11.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_11.setItemText(4, _translate("MainWindow", "5"))
        self.label_41.setText(_translate("MainWindow", "hand_intrinsics_score"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_12.setItemText(4, _translate("MainWindow", "5"))
        self.pushButton_19.setText(_translate("MainWindow", "submit"))
        self.pushButton_20.setText(_translate("MainWindow", "menu"))
        self.label_106.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_107.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_42.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Record OT assessment results</span></p></body></html>',
            )
        )
        self.label_43.setText(_translate("MainWindow", "apraxia_score"))
        self.label_44.setText(_translate("MainWindow", "Appointment date"))
        self.label_45.setText(_translate("MainWindow", "Patient id"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_13.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_13.setItemText(4, _translate("MainWindow", "5"))
        self.label_46.setText(_translate("MainWindow", "Appointment time"))
        self.label_47.setText(_translate("MainWindow", "dysarthria_score "))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_14.setItemText(4, _translate("MainWindow", "5"))
        self.label_49.setText(_translate("MainWindow", "dysphonia_score"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_16.setItemText(4, _translate("MainWindow", "5"))
        self.label_50.setText(_translate("MainWindow", "aphasia_score"))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_17.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_17.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_17.setItemText(4, _translate("MainWindow", "5"))
        self.label_51.setText(_translate("MainWindow", "memory_score"))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_18.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_18.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_18.setItemText(4, _translate("MainWindow", "5"))
        self.label_52.setText(_translate("MainWindow", "judgment_score"))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_19.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_19.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_19.setItemText(4, _translate("MainWindow", "5"))
        self.label_53.setText(_translate("MainWindow", "neglect_score"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_20.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_20.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_21.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_21.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_21.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_21.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_21.setItemText(4, _translate("MainWindow", "5"))
        self.label_55.setText(_translate("MainWindow", "attention_score"))
        self.pushButton_22.setText(_translate("MainWindow", "submit"))
        self.pushButton_23.setText(_translate("MainWindow", "menu"))
        self.label_96.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_105.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_18.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Record exercise regime </span></p></body></html>',
            )
        )
        self.label_19.setText(_translate("MainWindow", "Patient_id"))
        self.label_20.setText(_translate("MainWindow", "Excercise name"))
        self.label_25.setText(_translate("MainWindow", "Date"))
        self.pushButton_4.setText(_translate("MainWindow", "Create regime"))
        self.label_26.setText(_translate("MainWindow", "Reps"))
        self.pushButton_12.setText(_translate("MainWindow", "Insert exercise"))
        self.pushButton_13.setText(_translate("MainWindow", "Submit regime"))
        self.pushButton_29.setText(_translate("MainWindow", "menu"))
        self.label_90.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_92.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_54.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Previous appointments</span></p></body></html>',
            )
        )
        self.label_56.setText(_translate("MainWindow", "patient_id"))
        self.label_57.setText(_translate("MainWindow", "appointment date"))
        self.label_58.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:18pt;">physio</span></p></body></html>',
            )
        )
        self.label_59.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:18pt;">speech</span></p></body></html>',
            )
        )
        self.label_60.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:18pt;">OT</span></p></body></html>',
            )
        )
        self.label_61.setText(_translate("MainWindow", "hip_flexor_score"))
        self.label_62.setText(_translate("MainWindow", "knee_externsors_score"))
        self.label_63.setText(_translate("MainWindow", "dorsiflexors_score"))
        self.label_64.setText(_translate("MainWindow", "plantar_flexors_score"))
        self.knee_externsors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.dorsiflexors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.plantar_flexors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.hip_flexor_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.dysphonia_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_70.setText(_translate("MainWindow", "apraxia_score"))
        self.label_71.setText(_translate("MainWindow", "dysarthria_score "))
        self.label_72.setText(_translate("MainWindow", "dysphonia_score"))
        self.dysarthria_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.apraxia_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_75.setText(_translate("MainWindow", "aphasia_score"))
        self.aphasia_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.neglect_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_78.setText(_translate("MainWindow", "attention_score"))
        self.label_79.setText(_translate("MainWindow", "judgment_score"))
        self.label_80.setText(_translate("MainWindow", "neglect_score"))
        self.judgment_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.attention_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_83.setText(_translate("MainWindow", "memory_score"))
        self.memory_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.finger_flexors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_86.setText(_translate("MainWindow", "wrist_extensors_score"))
        self.wrist_extensors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_88.setText(_translate("MainWindow", "elbow_extensors_score"))
        self.label_89.setText(_translate("MainWindow", "elbow_flexors_score"))
        self.elbow_flexors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_91.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.elbow_extensors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.label_93.setText(_translate("MainWindow", "shoulder_abductors_score"))
        self.label_94.setText(_translate("MainWindow", "hand_intrinsics_score"))
        self.label_95.setText(_translate("MainWindow", "finger_flexors_score"))
        self.shoulder_abductors_score_lbl.setText(
            _translate(
                "MainWindow", '<html><head/><body><p align="center">0</p></body></html>'
            )
        )
        self.pushButton_26.setText(_translate("MainWindow", "menu"))
        self.label_85.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_87.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_98.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Previous exercise regime</span></p></body></html>',
            )
        )
        self.label_99.setText(_translate("MainWindow", "Patient_id"))
        self.label_100.setText(_translate("MainWindow", "Date"))
        self.pushButton_28.setText(_translate("MainWindow", "menu"))
        self.label_82.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_84.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_101.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Get patient ID</span></p></body></html>',
            )
        )
        self.label_102.setText(_translate("MainWindow", "First Name"))
        self.label_103.setText(_translate("MainWindow", "Last Name"))
        self.label_104.setText(_translate("MainWindow", "Phone Number"))
        self.pushButton_27.setText(_translate("MainWindow", "menu"))
        self.label_77.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_81.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_231.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_232.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_233.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Practice Administrator menu</span></p></body></html>',
            )
        )
        self.pushButton_59.setText(_translate("MainWindow", "menu"))
        self.pushButton_60.setText(_translate("MainWindow", "Insert clinician"))
        self.pushButton_61.setText(_translate("MainWindow", "Review clinician"))
        self.label_234.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.pushButton_62.setText(_translate("MainWindow", "menu"))
        self.label_235.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Insert Clinician</span></p></body></html>',
            )
        )
        self.label_236.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_237.setText(_translate("MainWindow", "first name"))
        self.label_238.setText(_translate("MainWindow", "last name"))
        self.label_239.setText(_translate("MainWindow", "username"))
        self.label_240.setText(_translate("MainWindow", "password"))
        self.label_241.setText(_translate("MainWindow", "clinician type"))
        self.comboBox_45.setItemText(0, _translate("MainWindow", "OT"))
        self.comboBox_45.setItemText(1, _translate("MainWindow", "Physio"))
        self.comboBox_45.setItemText(2, _translate("MainWindow", "Speech"))
        self.pushButton_63.setText(_translate("MainWindow", "submit"))
        self.label_242.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Review Clinician</span></p></body></html>',
            )
        )
        self.pushButton_64.setText(_translate("MainWindow", "menu"))
        self.label_243.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_244.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_245.setText(_translate("MainWindow", "Clinician"))
        self.label_246.setText(_translate("MainWindow", "Appointments"))
        self.label_247.setText(_translate("MainWindow", "Time"))
        self.label_248.setText(_translate("MainWindow", "time"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt;">Log in as practice administrator</span></p></body></html>',
            )
        )
        self.lg_user_name_lb_2.setText(_translate("MainWindow", "User name"))
        self.lg_password_lb_2.setText(_translate("MainWindow", "Password"))
        self.lg_login_btn_3.setText(_translate("MainWindow", "Login"))
        self.lg_login_btn_4.setText(_translate("MainWindow", "back"))
        self.label_74.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label_76.setText(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
