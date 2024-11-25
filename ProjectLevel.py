import datetime
class patient:
    patient_count = 0

    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        patient.patient_count += 1

    def display_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Illness: {self.illness}")

    def change_name(self, new_name):
        self.name = new_name

class doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def display_info(self):
        print(f"Doctor Name: {self.name}")
        print(f"Specialty: {self.specialty}")

class medicine:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

    def use_medicine(self):
        return f"Medicine: {self.name}, Dosage: {self.dosage}"


medicine_paracetamol = medicine("Paracetamol", "500mg")
medicine_amoxicillin = medicine("Amoxicillin", "250mg")


patient1 = patient("Lala", 15, "Flu")
patient2 = patient("Aca", 15, "Diabetes")


print("Patient Information:")
patient1.display_info()
print()
patient2.display_info()
print()


doctor1 = doctor("Dr. Aska", "General Practitioner")
print("Doctor Information:")
doctor1.display_info()
print()


print("Medicine Information:")
print(medicine_paracetamol.use_medicine())
print(medicine_amoxicillin.use_medicine())
print()

print(f"Total Patients: {patient.patient_count}")

patient1.change_name("Lily")
print("After changing name of patient1:")
patient1.display_info()

patient2.change_name("Ocha")
print("After changing name of patient2:")
patient2.display_info()