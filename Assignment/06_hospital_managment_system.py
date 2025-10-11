class Patient:
    counter = 1

    def __init__(self, name, age):
        self.patient_id = "P" + str(Patient.counter)
        Patient.counter += 1
        self.name = name
        self.age = age
        self.medical_history = []

    def add_history(self, entry):
        self.medical_history.append(entry)

    def get_details(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"

    def get_history(self):
        return self.medical_history


class Doctor:
    counter = 1

    def __init__(self, name, specialization):
        self.doctor_id = "D" + str(Doctor.counter)
        Doctor.counter += 1
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def add_appointment(self, appointment_id):
        self.appointments.append(appointment_id)

    def get_details(self):
        return f"ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"

    def get_schedule(self):
        return self.appointments


class Appointment:
    counter = 1

    def __init__(self, patient_id, doctor_id, date_time):
        self.appointment_id = "A" + str(Appointment.counter)
        Appointment.counter += 1
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.room_no = "R" + str(Appointment.counter + 100)  # auto-generated room number
        self.date_time = date_time

    def get_details(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient_id}, Doctor: {self.doctor_id}, Room: {self.room_no}, Date/Time: {self.date_time}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def schedule_appointment(self, patient_id, doctor_id, date_time):
        if patient_id in self.patients and doctor_id in self.doctors:
            appointment = Appointment(patient_id, doctor_id, date_time)
            self.appointments[appointment.appointment_id] = appointment
            self.doctors[doctor_id].add_appointment(appointment.appointment_id)
            return appointment.get_details()
        else:
            return "Invalid patient or doctor ID."

    def view_patient_history(self, patient_id):
        if patient_id in self.patients:
            return self.patients[patient_id].get_history()
        return "Patient not found."

    def view_doctor_schedule(self, doctor_id):
        if doctor_id in self.doctors:
            return self.doctors[doctor_id].get_schedule()
        return "Doctor not found."

    def search_patient(self, patient_id):
        if patient_id in self.patients:
            return self.patients[patient_id].get_details()
        return "Patient not found."

    def generate_report(self):
        return f"Total Patients: {len(self.patients)}, Total Doctors: {len(self.doctors)}"
# Create Hospital
h = Hospital("City Hospital")

# Add Patients
p1 = Patient("John", 30)
p2 = Patient("Alice", 25)
h.add_patient(p1)
h.add_patient(p2)

# Add Doctors
d1 = Doctor("Dr. Smith", "Cardiology")
d2 = Doctor("Dr. Brown", "Neurology")
h.add_doctor(d1)
h.add_doctor(d2)

# Add medical history
p1.add_history("Fever treatment - Jan 2025")
p2.add_history("Headache treatment - Feb 2025")

# Schedule appointments
print(h.schedule_appointment(p1.patient_id, d1.doctor_id, "2025-10-05 10:00 AM"))
print(h.schedule_appointment(p2.patient_id, d2.doctor_id, "2025-10-06 11:00 AM"))

# View patient history
print("Patient History:", h.view_patient_history(p1.patient_id))

# View doctor schedule
print("Doctor Schedule:", h.view_doctor_schedule(d1.doctor_id))

# Search patient
print("Search:", h.search_patient(p2.patient_id))

# Generate report
print("Report:", h.generate_report())
