import sqlite3
import csv
from PyQt6.QtCore import QDateTime, QDate, QTime, Qt


class Datastore:
    def __init__(self, db_file):

        self.connection = sqlite3.connect(db_file)

        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    # This creates the Database tables

    def build_db(self):
        self.cursor.execute(
            """
            CREATE TABLE clinician_tb(
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            clinician INTERGER NOT NULL,
            practice_administrator INTERGER NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE patient_tb(
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone INTERGER NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            suburb TEXT NOT NULL,
            gender TEXT NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE appointment_tb(
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL, 
            time TEXT NOT NULL,
            clinician_id INTERGER,
            patient_id INTERGER,
            FOREIGN KEY (clinician_id) REFERENCES clinician_tb(clinician_id),
            FOREIGN KEY (patient_id) REFERENCES patient_tb(patient_id)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE exercises_tb(
            exercises_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            target TEXT NOT NULL, 
            equipment TEXT NOT NULL, 
            body_part TEXT NOT NULL,
            image TEXT NOT NULL 
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE exercise_regime_tb(
            exercise_regime_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            date TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patient_tb(patient_id)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE exercise_regime_exercises_tb(
            exercise_regime_id TEXT NOT NULL,
            exercise_id TEXT NOT NULL,
            reps TEXT NOT NULL,
            PRIMARY KEY (exercise_regime_id,exercise_id),
            FOREIGN KEY (exercise_regime_id) REFERENCES exercise_regime_tb(exercise_regime_id),
            FOREIGN KEY (exercise_id) REFERENCES exercises_tb(exercise_id)
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE speech_assessments_score_tb(
            speech_assessments_score INTEGER PRIMARY KEY AUTOINCREMENT,
            aphasia_score INTERGER NOT NULL,
            apraxia_score INTERGER NOT NULL,
            dysathria_score INTERGER NOT NULL,
            dysphoria_score INTERGER NOT NULL,
            memory_score INTERGER NOT NULL,
            attention_score INTERGER NOT NULL,
            judgment_score INTERGER NOT NULL,
            neglect_score INTERGER NOT NULL,
            appointment_id INTERGER NOT NULL,
            FOREIGN KEY (appointment_id) REFERENCES appointment_tb(appointment_id)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE physio_assessments_score_tb(
            physio_assessments_id INTEGER PRIMARY KEY AUTOINCREMENT,
            hip_flexor_score INTERGER NOT NULL,
            knee_flexor_score INTERGER NOT NULL,
            dorsiflexor_score INTERGER NOT NULL,
            plantar_flexor_score INTERGER NOT NULL,
            appointment_id INTERGER NOT NULL,
            FOREIGN KEY (appointment_id) REFERENCES appointment_tb(appointment_id)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE ot_assessments_score_tb(
            ot_assessments_id INTEGER PRIMARY KEY AUTOINCREMENT,
            shoulder_abductors_score INTERGER NOT NULL,
            elbow_extensors_score INTERGER NOT NULL,
            elbow_flexors_score INTERGER NOT NULL,
            wrist_extensors_score INTERGER NOT NULL,
            finger_flexors_score INTERGER NOT NULL,
            hand_intrinsics_score INTERGER NOT NULL,
            
            appointment_id INTERGER NOT NULL,
            FOREIGN KEY (appointment_id) REFERENCES appointment_tb(appointment_id)
            )
            """
        )
        self.connection.commit()

    # Populating the database with existing excel spreadsheets

    def populate_db(self):
        with open("exercise_data.csv", encoding="utf-8") as exercise_data: # opening the csv file and defining it as :exercise data
            csv_reader = csv.DictReader(exercise_data, delimiter=",") # making it intelligible by the code

            for record in csv_reader:
                if record["id"]:
                    if record["name"] not in self.get_all_exercises():
                        self.add_exercises(
                            record["name"],
                            record["target"],
                            record["equipment"],           # parsing the data from the CSV File provided in the data package 
                            record["body_part"],
                            record["image"],
                        )

                self.connection.commit()
        with open("patient_data_2023.csv", encoding="utf-8") as patient_data: # opening the csv file and defining it as :patient data
            csv_reader = csv.DictReader(patient_data, delimiter=",") # making it intelligible by the code

            for record in csv_reader:
                if record["id"]:
                    first_name = record["first_name"]
                    last_name = record["last_name"]            
                    name = record["first_name"] + record["last_name"]
                    itd = record["id"]

                    itd = int(itd)
                    if itd not in self.get_patient_id1():
                        self.add_patient_data(
                            first_name,
                            last_name,
                            record["email"],
                            record["gender"],
                            record["address"],
                            record["suburb"],
                            record["phone"],
                        )

                    first_name = record["first_name"]
                    last_name = record["last_name"]

                    patient_id = self.get_patient_id(first_name, last_name)

                    time = 0
                    clinician_id = 1
                    date = record["appointment_date"]
                    try:
                        self.add_appointment(date, time, clinician_id, patient_id)
                    except Exception:
                        with open("error_log.txt", "a", encoding="utf-8") as log:     # trying a function to add in patient data with an appointment
                            log.write(f"Nope\n")
                    appointment_id = self.get_appointment_id(date, patient_id)

                if record["id"]:
                    self.add_appointment_physio_data(
                        record["hip_flexors"],
                        record["knee_extensors"],
                        record["dorsiflexors"],             # adding appointment data
                        record["plantar_flexors"],
                        appointment_id,
                    )
                if record["id"]:
                    self.add_appointment_ot_data(
                        record["shoulder_abductors"],
                        record["elbow_flexors"],
                        record["elbow_extensors"],
                        record["wrist_extensors"],
                        record["finger_flexors"],
                        record["hand_intrinsics"],
                        appointment_id,
                    )

                self.connection.commit()
        self.add_data()
        self.add_data_2()

    # Adding in Mocked up data for UI testing

    def add_data(self):
        self.cursor.execute(
            """
            INSERT INTO clinician_tb(name,username,password,clinician,practice_administrator)
            VALUES("James","Doe","1234",1,0)
            """
        )

    def add_data_2(self):
        self.cursor.execute(
            """
            INSERT INTO clinician_tb(name,username,password,clinician,practice_administrator)
            VALUES("John Smith","John.Smith","123",3,1)
            """
        )

    # Get Methods

    def get_all_exercises(self):
        self.cursor.execute(
            """
            SELECT name
            FROM exercises_tb
            """
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_patient_first_name(self):
        self.cursor.execute(
            """
            SELECT first_name
            FROM patient_tb
            """
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_patient_id1(self):
        self.cursor.execute(
            """
            SELECT patient_id
            FROM patient_tb
            """
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_patient_id(self, first_name, last_name):
        self.cursor.execute(
            """
            SELECT patient_id
            FROM patient_tb
            WHERE first_name = :first_name AND last_name = :last_name
            """,
            {"first_name": first_name, "last_name": last_name},
        )
        results = self.cursor.fetchone()
        return results[0]

    def get_patient_name(self):
        self.cursor.execute(
            """
            SELECT first_name + last_name as name
            FROM patient_tb
            """
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_appointment_id(self, date, patient_id):
        self.cursor.execute(
            """
            SELECT appointment_id
            FROM appointment_tb
            WHERE date = :date AND patient_id = :patient_id
            """,
            {"date": date, "patient_id": patient_id},
        )
        results = self.cursor.fetchone()

        return results[0]

    def get_clinician_id(self, clinician_name):
        self.cursor.execute(
            """
            SELECT staff_id
            FROM clinician_tb
            WHERE name = :clinician_name
            """,
            {"clinician_name": clinician_name},
        )
        results = self.cursor.fetchone()

        return results[0]

    def get_physio_results(self, appointment_id):
        self.cursor.execute(
            """
            SELECT hip_flexor_score,knee_flexor_score,dorsiflexor_score,plantar_flexor_score
            FROM physio_assessments_score_tb
            WHERE appointment_id = :appointment_id
            """,
            {"appointment_id": appointment_id},
        )
        results = self.cursor.fetchall()
        return results

    def get_regime_id(self, patient_id, date):
        self.cursor.execute(
            """
            SELECT exercise_regime_id
            FROM exercise_regime_tb
            WHERE patient_id = :patient_id AND date = :date
            """,
            {"patient_id": patient_id, "date": date},
        )
        results = self.cursor.fetchone()
        return results

    def get_ot_results(self, appointment_id):
        self.cursor.execute(
            """
            SELECT shoulder_abductors_score,elbow_flexors_score,elbow_extensors_score,wrist_extensors_score,finger_flexors_score,hand_intrinsics_score
            FROM ot_assessments_score_tb
            WHERE appointment_id = :appointment_id
            """,
            {"appointment_id": appointment_id},
        )
        results = self.cursor.fetchall()
        return results

    def get_speech_results(self, appointment_id):
        self.cursor.execute(
            """
            SELECT aphasia_score,apraxia_score,dysathria_score,dysphoria_score,memory_score,attention_score,judgment_score,neglect_score
            FROM speech_assessments_score_tb
            WHERE appointment_id = :appointment_id
            """,
            {"appointment_id": appointment_id},
        )
        results = self.cursor.fetchall()
        return results

    def get_password(self, username):
        self.cursor.execute(
            """
            SELECT password
            FROM clinician_tb
            WHERE username = :username
            """,
            {"username": username},
        )
        results = self.cursor.fetchone()

        if results is None:
            return None
        else:
            return results[0]

    def get_clinicians(self, staff_id):
        self.cursor.execute(
            """
        SELECT name 
        FROM clinician_tb
        WHERE staff_id = :staff_id
        """,
            {"staff_id": staff_id},
        )
        results = self.cursor.fetchone()

        if results is None:
            return None
        else:
            return results[0]

    def get_amount_of_appointments(self, patient_id):
        self.cursor.execute(
            """
            SELECT COUNT(appointment_id)
            FROM appointment_tb
            WHERE patient_id = :patient_id
            """,
            {"patient_id": patient_id},
        )
        results = self.cursor.fetchone()

        if results is None:
            return None
        else:
            return results[0]

    def get_appointments(self, patient_id):
        self.cursor.execute(
            """
            SELECT date
            from appointment_tb
            WHERE patient_id = :patient_id
            """,
            {"patient_id": patient_id},
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_appointments_time(self, patient_id):
        self.cursor.execute(
            """
            SELECT time
            from appointment_tb
            WHERE patient_id = :patient_id
            """,
            {"patient_id": patient_id},
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_amount_of_previous_regimes(self, patient_id):
        self.cursor.execute(
            """
            SELECT COUNT(date)
            FROM exercise_regime_tb
            WHERE patient_id = :patient_id
            """,
            {"patient_id": patient_id},
        )
        results = self.cursor.fetchone()

        if results is None:
            return None
        else:
            return results[0]

    def get_previous_regimes(self, patient_id):
        self.cursor.execute(
            """
            SELECT date
            FROM exercise_regime_tb
            WHERE patient_id = :patient_id
            """,
            {"patient_id": patient_id},
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_admin_staff(self, username, password):
        self.cursor.execute(
            """
            SELECT practice_administrator
            FROM clinician_tb
            WHERE username = :username AND password = :password
            """,
            {"username": username, "password": password},
        )
        results = self.cursor.fetchone()
        return results[0]

    def get_appointments_clinician(self, clinician_id):
        self.cursor.execute(
            """
            SELECT date
            FROM appointment_tb
            WHERE clinician_id = :clinician_id
            """,
            {"clinician_id": clinician_id},
        )
        results = self.cursor.fetchall()
        processed = []
        for results in results:
            processed.append(results[0])
        return processed

    def get_appoint_time(self, clinician_id, appointments):
        self.cursor.execute(
            """
            SELECT time 
            FROM appointment_tb
            WHERE clinician_id = :clinician_id AND date = :date
            """,
            {"clinician_id": clinician_id, "date": appointments},
        )
        results = self.cursor.fetchone()
        return results[0]

    def get_exercises(self, regime_id):
        self.cursor.execute(
            """
            SELECT t2.name, t1.reps
            FROM exercise_regime_exercises_tb as t1
            INNER JOIN exercises_tb as t2
            ON t2.exercises_id = t1.exercise_id
            WHERE t1.exercise_regime_id = :regime_id
            """,
            {"regime_id": regime_id},
        )

        results = self.cursor.fetchall()
        return results

    def get_exercise_id(self, exercise_name):
        self.cursor.execute(
            """
            SELECT exercises_id
            FROM exercises_tb
            WHERE name = :exercise_name
            """,
            {
                "exercise_name": exercise_name,
            },
        )
        results = self.cursor.fetchone()
        return results[0]

    def get_regime_id_2(self, date, patient_id):
        self.cursor.execute(
            """
            SELECT exercise_regime_id
            FROM exercise_regime_tb
            WHERE date = :date AND patient_id = :patient_id
            """,
            {"date": date, "patient_id": patient_id},
        )
        results = self.cursor.fetchone()
        return results[0]

    def get_clinician_type(self, clinician_id):
        self.cursor.execute(
            """
            SELECT clinician
            FROM clinician_tb
            WHERE staff_id = :clinician_id
            """,
            {"clinician_id": clinician_id},
        )
        results = self.cursor.fetchone()
        return results[0]

    def get_time(self, appointment_id, clinician_id):
        self.cursor.execute(
            """
            SELECT time
            FROM appointment_tb
            WHERE appointment_id = :appointment_id 
            """,
            {"appointment_id": appointment_id, "clinician_id": clinician_id},
        )
        results = self.cursor.fetchone()
        return results[0]

    # Add Methods

    def add_exercises(self, name, target, equipment, body_part, image):
        self.cursor.execute(
            """
            INSERT INTO exercises_tb(name,target,equipment,body_part,image)
            VALUES(:name,:target,:equipment,:body_part,:image)
            """,
            {
                "name": name,
                "target": target,
                "equipment": equipment,
                "body_part": body_part,
                "image": image,
            },
        )

    def add_patient_data(
        self, first_name, last_name, email, gender, address, suburb, phone
    ):
        self.cursor.execute(
            """
            INSERT INTO patient_tb(first_name,last_name,email,gender,address,suburb,phone)
            VALUES(:first_name,:last_name,:email,:gender,:address,:suburb,:phone)
            """,
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "gender": gender,
                "address": address,
                "suburb": suburb,
                "phone": phone,
            },
        )

    def add_appointment(self, appointment_date, time, clinician_id, patient_id):
        self.cursor.execute(
            """
            INSERT INTO appointment_tb(date,time,clinician_id,patient_id)
            VALUES(:appointment_date,:time,:clinician_id,:patient_id)
            """,
            {
                "appointment_date": appointment_date,
                "time": time,
                "clinician_id": clinician_id,
                "patient_id": patient_id,
            },
        )

    def add_appointment_physio_data(
        self,
        hip_flexor_score,
        knee_flexor_score,
        dorsiflexor_score,
        plantar_flexor_score,
        appointment_id,
    ):
        self.cursor.execute(
            """
            INSERT INTO physio_assessments_score_tb(hip_flexor_score,
                                        knee_flexor_score,
                                        dorsiflexor_score,
                                        plantar_flexor_score,
                                        appointment_id)
            VALUES(:hip_flexor_score,
                                        :knee_flexor_score,
                                        :dorsiflexor_score,
                                        :plantar_flexor_score,
                                        :appointment_id)
            """,
            {
                "hip_flexor_score": hip_flexor_score,
                "knee_flexor_score": knee_flexor_score,
                "dorsiflexor_score": dorsiflexor_score,
                "plantar_flexor_score": plantar_flexor_score,
                "appointment_id": appointment_id,
            },
        )

    def add_appointment_ot_data(
        self,
        shoulder_abductors_score,
        elbow_flexors_score,
        elbow_extensors_score,
        wrist_extensors_score,
        finger_flexors_score,
        hand_intrinsics_score,
        appointment_id,
    ):
        self.cursor.execute(
            """
            INSERT INTO ot_assessments_score_tb(shoulder_abductors_score,
                                        elbow_flexors_score,
                                        elbow_extensors_score,
                                        wrist_extensors_score,
                                        finger_flexors_score,
                                        hand_intrinsics_score,
                                        appointment_id)
            VALUES(:shoulder_abductors_score,
                                        :elbow_flexors_score,
                                        :elbow_extensors_score,
                                        :wrist_extensors_score,
                                        :finger_flexors_score,
                                        :hand_intrinsics_score,
                                        :appointment_id)
            """,
            {
                "shoulder_abductors_score": shoulder_abductors_score,
                "elbow_flexors_score": elbow_flexors_score,
                "elbow_extensors_score": elbow_extensors_score,
                "wrist_extensors_score": wrist_extensors_score,
                "finger_flexors_score": finger_flexors_score,
                "hand_intrinsics_score": hand_intrinsics_score,
                "appointment_id": appointment_id,
            },
        )

    def add_patient_detials(
        self, first_name, last_name, suburb, address, phone_number, email, gender
    ):
        self.cursor.execute(
            """
            INSERT INTO patient_tb(first_name,last_name,suburb,address,phone,email,gender)
            VALUES(:first_name,:last_name,:suburb,:address,:phone_number,:email,:gender)
            """,
            {
                "first_name": first_name,
                "last_name": last_name,
                "suburb": suburb,
                "address": address,
                "phone_number": phone_number,
                "email": email,
                "gender": gender,
            },
        )
        self.connection.commit()

    def add_appointment_details(self, first_name, last_name, clinician, date, time):
        patient_id = self.get_patient_id(first_name, last_name)
        print(patient_id)
        clinician_id = self.get_clinician_id(clinician)
        self.cursor.execute(
            """
            INSERT INTO appointment_tb(date,time,clinician_id,patient_id)
            VALUES(:date,:time,:clinician_id,:patient_id)
            """,
            {
                "date": date,
                "time": time,
                "patient_id": patient_id,
                "clinician_id": clinician_id,
            },
        )
        self.connection.commit()

    def add_OT_results(
        self,
        patient_id,
        appointment_date,
        appointment_time,
        shoulder_abductors_score,
        elbow_flexors_score,
        elbow_extensors_score,
        wrist_extensors_score,
        finger_flexors_score,
        hand_intrinsics_score,
    ):
        appointment_id = self.get_appointment_id(appointment_date, patient_id)
        self.cursor.execute(
            """
            INSERT INTO ot_assessments_score_tb(shoulder_abductors_score,elbow_flexors_score,elbow_extensors_score,wrist_extensors_score,finger_flexors_score,hand_intrinsics_score,appointment_id)
            VALUES(:shoulder_abductors_score,:elbow_flexors_score,:elbow_extensors_score,:wrist_extensors_score,:finger_flexors_score,:hand_intrinsics_score,:appointment_id)
            """,
            {
                "shoulder_abductors_score": shoulder_abductors_score,
                "elbow_flexors_score": elbow_flexors_score,
                "elbow_extensors_score": elbow_extensors_score,
                "wrist_extensors_score": wrist_extensors_score,
                "finger_flexors_score": finger_flexors_score,
                "hand_intrinsics_score": hand_intrinsics_score,
                "appointment_id": appointment_id,
            },
        )
        self.connection.commit()

    def add_physio_results(
        self,
        patient_id,
        appointment_date,
        hip_flexor_score,
        knee_flexor_score,
        dorsiflexor_score,
        plantar_flexor_score,
    ):
        appointment_id = self.get_appointment_id(appointment_date, patient_id)
        self.cursor.execute(
            """
                INSERT INTO physio_assessments_score_tb(hip_flexor_score,knee_flexor_score,dorsiflexor_score,plantar_flexor_score,appointment_id) 
                VALUES(:hip_flexor_score,:knee_flexor_score,:dorsiflexor_score,:plantar_flexor_score,:appointment_id)
            """,
            {
                "hip_flexor_score": hip_flexor_score,
                "knee_flexor_score": knee_flexor_score,
                "dorsiflexor_score": dorsiflexor_score,
                "plantar_flexor_score": plantar_flexor_score,
                "appointment_id": appointment_id,
            },
        )
        self.connection.commit()

    def add_speech_results(
        self,
        patient_id,
        appointment_date,
        aphasia_score,
        apraxia_score,
        dysathria_score,
        dysphoria_score,
        memory_score,
        attention_score,
        judgment_score,
        neglect_score,
    ):
        appointment_id = self.get_appointment_id(appointment_date, patient_id)
        self.cursor.execute(
            """
            INSERT INTO speech_assessments_score_tb(aphasia_score,apraxia_score,dysathria_score,dysphoria_score,memory_score,attention_score,judgment_score,neglect_score,appointment_id)
            VALUES(:aphasia_score,:apraxia_score,:dysathria_score,:dysphoria_score,:memory_score,:attention_score,:judgment_score,:neglect_score,:appointment_id)
            """,
            {
                "aphasia_score": aphasia_score,
                "apraxia_score": apraxia_score,
                "dysathria_score": dysathria_score,
                "dysphoria_score": dysphoria_score,
                "memory_score": memory_score,
                "attention_score": attention_score,
                "judgment_score": judgment_score,
                "neglect_score": neglect_score,
                "appointment_id": appointment_id,
            },
        )
        self.connection.commit()

    def add_clinician(self, name, username, password, clinician_type, admin):
        self.cursor.execute(
            """
            INSERT INTO clinician_tb(name,username,password,clinician,practice_administrator)
            VALUES(:name,:username,:password,:clinician,:practice_administrator)

            """,
            {
                "name": name,
                "username": username,
                "password": password,
                "clinician": clinician_type,
                "practice_administrator": admin,
            },
        )
        self.connection.commit()

    def add_regime(self, patient_id, date):
        self.cursor.execute(
            """
            INSERT INTO exercise_regime_tb(patient_id,date)
            VALUES(:patient_id,:date)
            """,
            {"patient_id": patient_id, "date": date},
        )
        self.connection.commit()

        if results is None:
            return None
        else:
            return results[0]

    def add_excerise_regime(self, exercise_regime_id, exercise_id, reps):
        self.cursor.execute(
            """
            INSERT INTO exercise_regime_exercises_tb(exercise_regime_id,exercise_id,reps)
            VALUES(:exercise_regime_id,:exercise_id,:reps)
            """,
            {
                "exercise_regime_id": exercise_regime_id,
                "exercise_id": exercise_id,
                "reps": reps,
            },
        )
        self.connection.commit()
