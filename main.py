from pyscript import document, display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = []
absences = []

def displaying(e=None):
    day = document.getElementById('day').value
    absence = int(document.getElementById('absence').value)

    days.append(day)
    absences.append(absence)

    converted_absences = np.array(absences)

    plt.clf()
    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt.gcf())


class Classmate:
    def __init__(self, name, section, job):
        self.name = name
        self.section = section
        self.job = job

    def introduce(self):
        return f"Name: {self.name}<br>Section: {self.section}<br>Desired Job: {self.job}<br><br>"


classmates = [
    Classmate("Inigo", "Sapphire", "Lawyer"),
    Classmate("Curt", "Sapphire", "Basketball Coach"),
    Classmate("Yanna", "Sapphire", "Engineer"),
    Classmate("Luis", "Sapphire", "IT"),
    Classmate("Zyan", "Sapphire", "President")
]


def show_list(event=None):
    output = ""
    for classmate in classmates:
        output += classmate.introduce()

    element = document.getElementById("classmate-list")
    if element:
        element.innerHTML = output


def add_classmate(event=None):
    username = document.getElementById("name").value.strip()
    section = document.getElementById("section").value.strip()
    desiredJob = document.getElementById("desiredJob").value.strip()

    if not username or not section or not desiredJob:
        document.getElementById("signed").innerText = "Please fill in all fields!"
        return

    if any(c.name == username for c in classmates):
        document.getElementById("signed").innerText = "You're already in the list!"
        return

    new_classmate = Classmate(username, section, desiredJob)
    classmates.append(new_classmate)

    document.getElementById("signed").innerText = f"{username} added successfully!"

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("desiredJob").value = ""

    show_list()
