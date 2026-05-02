from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

days = []
absences = []

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


def displaying(event=None):
    day = document.getElementById('day').value
    absence = document.getElementById('absence').value

    if absence == "":
        document.getElementById("signed").innerText = "Enter a number!"
        return

    absence = int(absence)

    days.append(day)
    absences.append(absence)

    plt.clf()
    plt.plot(days, absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt.gcf(), target="graph", append=False)

    document.getElementById("signed").innerText = "Attendance added!"


def show_list(event=None):
    output = ""

    for classmate in classmates:
        output += classmate.introduce()

    element = document.getElementById("classmate-list")
    if element:
        element.innerHTML = output


def add_classmate(event=None):
    name = document.getElementById("name").value.strip()
    section = document.getElementById("section").value.strip()
    job = document.getElementById("desiredJob").value.strip()

    if not name or not section or not job:
        document.getElementById("signed").innerText = "Please fill in all fields!"
        return

    if any(c.name == name for c in classmates):
        document.getElementById("signed").innerText = "You're already in the list!"
        return

    classmates.append(Classmate(name, section, job))

    document.getElementById("signed").innerText = f"{name} added successfully!"

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("desiredJob").value = ""

    show_list()
