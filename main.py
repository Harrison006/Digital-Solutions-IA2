import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from other import Ui_MainWindow
from datastore import Datastore
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap


class MainWindow:
    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.db = Datastore("road_to_recovery224trp.db")

        clinician_id = 1
        clinician = self.db.get_clinicians(clinician_id)
        while clinician != None:
            clinician = self.db.get_clinicians(clinician_id)
            self.ui.comboBox_2.addItem(clinician)
            self.ui.comboBox_46.addItem(clinician)
            appointments = self.db.get_appointments_clinician(clinician_id)

            for record in appointments:
                self.ui.comboBox_47.addItem(record)

            clinician_id += 1

        """ui """
        self.signals()

    def show(self):
        self.main_win.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)

    def signals(self):
        """

        Connects the UI buttons to the corresponding functions (see slots)
        """
        self.ui.pushButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_as_clinician)
        )
        self.ui.pushButton_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.log_in_as_practice_administrator
            )
        )
        self.ui.lg_login_btn_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)
        )
        self.ui.lg_login_btn_4.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)
        )
        self.ui.pushButton_3.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.patientdetails)
        )
        self.ui.pushButton_9.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_10.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_18.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_24.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_20.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_23.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_29.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_26.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_28.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_27.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
        )
        self.ui.pushButton_59.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)
        )
        self.ui.pushButton_62.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.practice_admin_menu)
        )
        self.ui.pushButton_64.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.practice_admin_menu)
        )
        self.ui.pushButton_5.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.typeofassessment)
        )
        self.ui.pushButton_15.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        )
        self.ui.pushButton_16.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.record_OT_assessent)
        )
        self.ui.pushButton_17.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.Physio_appointment_results
            )
        )
        self.ui.pushButton_14.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.appointment_details)
        )
        self.ui.pushButton_7.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.previous_appointments
            )
        )
        self.ui.pushButton_6.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.record_regime)
        )
        self.ui.pushButton_25.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.previous_exercise_regime
            )
        )
        self.ui.pushButton_60.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.insertclinician)
        )
        self.ui.pushButton_61.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        )
        self.ui.pushButton_sign_out.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.log_in_page)
        )
        self.ui.pushButton_8.clicked.connect(self.submit_patient_info)
        self.ui.lg_login_btn.clicked.connect(self.login)
        self.ui.pushButton_11.clicked.connect(self.book_appointment)
        self.ui.pushButton_19.clicked.connect(self.insert_OT_results)
        self.ui.pushButton_21.clicked.connect(self.insert_physio_results)
        self.ui.pushButton_22.clicked.connect(self.insert_speech_results)
        self.ui.physio_patient_id_lbl_2.textChanged.connect(
            self.show_appointment_dates_1
        )
        self.ui.physio_patient_id_lbl.textChanged.connect(self.show_appointment_dates_2)
        self.ui.physio_patient_id_lbl_3.textChanged.connect(
            self.show_appointment_dates_3
        )
        self.ui.previous_appointments_patient_id.textChanged.connect(
            self.show_previous_appointments
        )
        self.ui.comboBox_15.currentTextChanged.connect(self.previous_appointments)
        self.ui.pushButton_4.clicked.connect(self.create_regime)
        self.ui.pushButton_12.clicked.connect(self.insert_excercises)
        self.ui.previous_exercises_patient_id.textChanged.connect(self.date_get)
        self.ui.lg_login_btn_3.clicked.connect(self.admin_login)
        self.ui.pushButton_63.clicked.connect(self.add_clinician)
        self.ui.comboBox_46.currentTextChanged.connect(self.show_appointments)
        self.ui.comboBox_47.currentTextChanged.connect(self.show_time)

    # ----- slots ----- #

    def login(self):
        username = self.ui.lg_user_name_le.text()
        password = self.ui.lg_password_le.text()
        stored_password = self.db.get_password(username)

        if stored_password != None:
            if stored_password == password:

                self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)
            else:
                self.ui.lg_message_lb.setText("Incorrect Password")
        else:
            self.ui.lg_message_lb.setText("Username not registered")

    def admin_login(self):
        username = self.ui.lg_username_practice_admin_lbl.text()
        password = self.ui.lg_password_practice_admin_lbl.text()
        stored_password = self.db.get_password(username)

        if stored_password != None:
            if stored_password == password:
                admin = int(self.db.get_admin_staff(username, password))
                if admin == 1:

                    self.ui.stackedWidget.setCurrentWidget(self.ui.practice_admin_menu)
                else:
                    pass
            else:
                pass
        else:
            pass

    def submit_patient_info(self):
        first_name = self.ui.firstname_lbl.text()
        last_name = self.ui.lastname_lbl.text()
        suburb = self.ui.suburb_lbl.text()
        address = self.ui.address_lbl.text()
        phone_number = self.ui.phone_number_lbl.text()
        email = self.ui.lineEdit_6.text()
        gender = self.ui.comboBox.currentText()
        self.db.add_patient_detials(
            first_name, last_name, suburb, address, phone_number, email, gender
        )
        self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)

    def add_clinician(self):
        first_name = self.ui.insert_clinician_firstname.text()
        last_name = self.ui.insert_clinician_lastname.text()
        username = self.ui.insert_clinician_username.text()
        password = self.ui.insert_clinician_password.text()
        clinician_type = self.ui.comboBox_45.currentText()
        if clinician_type == "OT":
            clinician = 1
        elif clinician_type == "Physio":
            clinician = 2
        elif clinician_type == "Speech":
            clinician = 3

        admin = self.ui.comboBox_admin.currentText()
        name = first_name + " " + last_name
        self.db.add_clinician(name, username, password, clinician, admin)

    def book_appointment(self):
        first_name = self.ui.patientfirstname.text()
        last_name = self.ui.patientlastname.text()
        clinician = self.ui.comboBox_2.currentText()
        date_year = self.ui.dateEdit.date().year()
        date_year = str(date_year)
        date_month = self.ui.dateEdit.date().month()
        date_month = str(date_month)
        date_day = self.ui.dateEdit.date().day()
        date_day = str(date_day)
        full_date = date_day + "/" + date_month + "/" + date_year

        print(full_date)
        time_hour = self.ui.timeEdit.time().hour()
        time_hour = str(time_hour)
        time_minute = self.ui.timeEdit.time().minute()
        time_minute = str(time_minute)

        full_time = time_hour + ":" + time_minute
        print(full_time)

        self.db.add_appointment_details(
            first_name, last_name, clinician, full_date, full_time
        )
        self.ui.stackedWidget.setCurrentWidget(self.ui.clinician_home_page)

    def insert_OT_results(self):
        patient_id = self.ui.physio_patient_id_lbl_2.text()
        appointment_date = self.ui.physio_appointment_date_lbl_2.text()
        appointment_date = str(appointment_date)
        appointment_time = self.ui.physio_appointment_time_lbl_2.text()
        shoulder_abductors_score = self.ui.comboBox_7.currentText()
        elbow_flexors_score = self.ui.comboBox8.currentText()
        elbow_extensors_score = self.ui.comboBox_9.currentText()
        wrist_extensors_score = self.ui.comboBox_10.currentText()
        finger_flexors_score = self.ui.comboBox_11.currentText()
        hand_intrinsics_score = self.ui.comboBox_12.currentText()
        print(patient_id, appointment_date, appointment_time)
        self.db.add_OT_results(
            patient_id,
            appointment_date,
            appointment_time,
            shoulder_abductors_score,
            elbow_flexors_score,
            elbow_extensors_score,
            wrist_extensors_score,
            finger_flexors_score,
            hand_intrinsics_score,
        )

    def insert_physio_results(self):
        patient_id = self.ui.physio_patient_id_lbl.text()
        appointment_date = self.ui.physio_appointment_date_lbl.text()
        appointment_date = str(appointment_date)
        appointment_time = self.ui.physio_appointment_time_lbl.text()
        Hip_flexor_score = self.ui.comboBox_3.currentText()
        Knee_externsors_score = self.ui.comboBox_4.currentText()
        Dorsiflexors_score = self.ui.comboBox_5.currentText()
        Plantar_flexors_score = self.ui.comboBox_6.currentText()

        self.db.add_physio_results(
            patient_id,
            appointment_date,
            Hip_flexor_score,
            Knee_externsors_score,
            Dorsiflexors_score,
            Plantar_flexors_score,
        )

    def insert_speech_results(self):
        patient_id = self.ui.physio_patient_id_lbl_3.text()
        appointment_date = self.ui.physio_appointment_date_lbl_3.text()
        appointment_date = str(appointment_date)
        appointment_time = self.ui.physio_appointment_time_lbl_3.text()
        aphasia_score = self.ui.comboBox_17.currentText()
        apraxia_score = self.ui.comboBox_13.currentText()
        dysarthria_score = self.ui.comboBox_14.currentText()
        dysphonia_score = self.ui.comboBox_16.currentText()
        memory_score = self.ui.comboBox_18.currentText()
        attention_score = self.ui.comboBox_21.currentText()
        judgment_score = self.ui.comboBox_19.currentText()
        neglect_score = self.ui.comboBox_20.currentText()

        self.db.add_speech_results(
            patient_id,
            appointment_date,
            aphasia_score,
            apraxia_score,
            dysarthria_score,
            dysphonia_score,
            memory_score,
            attention_score,
            judgment_score,
            neglect_score,
        )

    def show_appointment_dates_1(self):
        print(self.ui.physio_patient_id_lbl_2.text())
        try:
            int(self.ui.physio_patient_id_lbl_2.text())
            patient_id = self.ui.physio_patient_id_lbl_2.text()

            actual_amount = self.db.get_amount_of_appointments(int(patient_id))

            appointment_date = self.db.get_appointments(patient_id)

            self.ui.physio_appointment_date_lbl_2.setText(
                appointment_date[actual_amount - 1]
            )
            appointment_time = self.db.get_appointments_time(patient_id)
            self.ui.physio_appointment_time_lbl_2.setText(
                appointment_time[actual_amount - 1]
            )

        except Exception:
            pass

    def show_appointment_dates_2(self):

        try:
            int(self.ui.physio_patient_id_lbl.text())
            patient_id = self.ui.physio_patient_id_lbl.text()

            actual_amount = self.db.get_amount_of_appointments(int(patient_id))

            appointment_date = self.db.get_appointments(patient_id)

            self.ui.physio_appointment_date_lbl.setText(
                appointment_date[actual_amount - 1]
            )
            appointment_time = self.db.get_appointments_time(patient_id)
            self.ui.physio_appointment_time_lbl.setText(
                appointment_time[actual_amount - 1]
            )

        except Exception:
            pass

    def show_appointment_dates_3(self):
        print(self.ui.physio_patient_id_lbl_3.text())
        try:
            int(self.ui.physio_patient_id_lbl_3.text())
            patient_id = self.ui.physio_patient_id_lbl_3.text()

            actual_amount = self.db.get_amount_of_appointments(int(patient_id))

            appointment_date = self.db.get_appointments(patient_id)

            self.ui.physio_appointment_date_lbl_3.setText(
                appointment_date[actual_amount - 1]
            )
            appointment_time = self.db.get_appointments_time(patient_id)
            self.ui.physio_appointment_time_lbl_3.setText(
                appointment_time[actual_amount - 1]
            )

        except Exception:
            pass

    def show_previous_appointments(self):
        try:
            int(self.ui.previous_appointments_patient_id.text())
            patient_id = self.ui.previous_appointments_patient_id.text()
            start = 0
            actual_amount = self.db.get_amount_of_appointments(int(patient_id))

            appointment_date = self.db.get_appointments(patient_id)
            while start < actual_amount:

                self.ui.comboBox_15.addItem(appointment_date[start])
                start += 1

        except Exception:
            patient_id = self.ui.previous_appointments_patient_id.text()
            start = 0
            actual_amount = self.ui.comboBox_15.count()

            appointment_date = self.db.get_appointments(patient_id)
            while start < actual_amount:

                start += 1
                self.ui.comboBox_15.clear()

    def previous_appointments(self):
        try:
            int(self.ui.previous_appointments_patient_id.text())
            patient_id = self.ui.previous_appointments_patient_id.text()
            date = self.ui.comboBox_15.currentText()
            appointment_id = self.db.get_appointment_id(date, patient_id)
            print(appointment_id)
            physio = self.db.get_physio_results(appointment_id)
            hip_flexor = physio[0][0]
            knee_extensors = physio[0][1]
            dorsiflexors = physio[0][2]
            plantar_flexors = physio[0][3]
            print(hip_flexor)
            self.ui.hip_flexor_score_lbl.setText(str(hip_flexor))
            self.ui.knee_externsors_score_lbl.setText(str(knee_extensors))
            self.ui.dorsiflexors_score_lbl.setText(str(dorsiflexors))
            self.ui.plantar_flexors_score_lbl.setText(str(plantar_flexors))
            Ot = self.db.get_ot_results(appointment_id)

            shoulder_abductors_score = Ot[0][0]
            elbow_flexors_score = Ot[0][1]
            elbow_extensors_score = Ot[0][2]
            wrist_extensors_score = Ot[0][3]
            finger_flexors_score = Ot[0][4]
            hand_intrinsics_score = Ot[0][5]
            self.ui.shoulder_abductors_score_lbl.setText(str(shoulder_abductors_score))
            self.ui.elbow_flexors_score_lbl.setText(str(elbow_flexors_score))
            self.ui.elbow_extensors_score_lbl.setText(str(elbow_extensors_score))
            self.ui.wrist_extensors_score_lbl.setText(str(wrist_extensors_score))
            self.ui.finger_flexors_score_lbl.setText(str(finger_flexors_score))
            self.ui.label_91.setText(str(hand_intrinsics_score))

            speech = self.db.get_speech_results(appointment_id)
            aphasia = speech[0][0]
            apraxia_score = speech[0][1]
            dysathria_score = speech[0][2]
            dysphoria_score = speech[0][3]
            memory_score = speech[0][4]
            attention_score = speech[0][5]
            judgment_score = speech[0][6]
            neglect_score = speech[0][7]
            self.ui.aphasia_score_lbl.setText(str(aphasia))
            self.ui.apraxia_score_lbl.setText(str(apraxia_score))
            self.ui.dysarthria_score_lbl.setText(str(dysathria_score))
            self.ui.dysphonia_score_lbl.setText(str(dysphoria_score))
            self.ui.memory_score_lbl.setText(str(memory_score))
            self.ui.attention_score_lbl.setText(str(attention_score))
            self.ui.judgment_score_lbl.setText(str(judgment_score))
            self.ui.neglect_score_lbl.setText(str(neglect_score))

            print(Ot)
            print(speech)

        except Exception:
            pass

    def create_regime(self):
        try:
            int(self.ui.record_exercise_regime_patient_id.text())
            patient_id = self.ui.record_exercise_regime_patient_id.text()
            date_year = self.ui.record_exercise_regime_date.date().year()
            date_year = str(date_year)
            date_month = self.ui.record_exercise_regime_date.date().month()
            date_month = str(date_month)
            date_day = self.ui.record_exercise_regime_date.date().day()
            date_day = str(date_day)
            full_date = date_day + "/" + date_month + "/" + date_year
            self.db.make_regime(patient_id, full_date)

            self.ui.pushButton_4.setEnabled(False)
        except Exception:
            pass

    def insert_excercises(self):
        exercise_name = self.ui.record_exercise_regime_exercise_name.text()
        reps = self.ui.spinBox.value()
        int(self.ui.record_exercise_regime_patient_id.text())
        patient_id = self.ui.record_exercise_regime_patient_id.text()
        date_year = self.ui.record_exercise_regime_date.date().year()
        date_year = str(date_year)
        date_month = self.ui.record_exercise_regime_date.date().month()
        date_month = str(date_month)
        date_day = self.ui.record_exercise_regime_date.date().day()
        date_day = str(date_day)
        full_date = date_day + "/" + date_month + "/" + date_year
        regime_id = self.db.get_regime_id(patient_id, full_date)
        self.db.insert_excerise_regime(regime_id, exercise_name, reps)
        exercises = self.db.get_exercises(regime_id)
        self.ui.tableView_2.setModel(exercises)

    def date_get(self):
        try:
            patient_id = int(self.ui.previous_exercises_patient_id.text())
            start = 0
            actual_amount = self.db.get_amount_of_previous_regimes(int(patient_id))

            appointment_date = self.db.get_previous_regimes(patient_id)
            while start < actual_amount:

                self.ui.comboBox_22.addItem(appointment_date[start])
                start += 1
        except Exception:
            pass

    def show_appointments(self):
        clinician_name = self.ui.comboBox_46.currentText()
        clinician_id = self.db.get_clinician_id(clinician_name)
        appointments = self.db.get_appointments_clinician(clinician_id)

        for record in appointments:
            self.ui.comboBox_47.addItem(record)

    def show_time(self):
        clinician_name = self.ui.comboBox_46.currentText()
        clinician_id = self.db.get_clinician_id(clinician_name)
        appointments = self.ui.comboBox_47.currentText()
        time = self.db.get_appoint_time(clinician_id, appointments)
        self.ui.label_248.setText(time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
