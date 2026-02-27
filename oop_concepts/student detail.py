import pickle

class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)


# Create object
s1 = Student("Aman", 101, 85)


# --------- Pickle (Save to file) ----------
with open("student.dat", "wb") as f:
    pickle.dump(s1, f)

print("Student data saved successfully")


# --------- Unpickle (Read from file) ----------
with open("student.dat", "rb") as f:
    s2 = pickle.load(f)

print("\nStudent data loaded successfully")
s2.display()