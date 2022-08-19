from tkinter import *
from tkcalendar import *

window = Tk()
window.title("Class Assignment Reminder")
window.config(width=500, height= 500, padx=50, pady=50)

#TODO: Reminder list

def set_reminder():
    #Appends new assignment and deletes textbox so no repeats
    with open("reminder_list.txt", "a") as reminders:
        date = day_cal.get_date()
        project = assignment_listbox.get(assignment_listbox.curselection())
        course = radio_state.get()
        if course == 1:
            course = "MATH 330"
        if course == 2:
            course = "MATH 336"
        if course == 3:
            course = "MATH 340"
        if course == 4:
            course = "MATH 532"
        if course == 5:
            course = "ECON 320"
        if course == 6:
            course = "ECON 507"
        reminders.write(f"Due on {date} | {course} | {project}\n")

    reminder_textbox.delete("1.0", END)

    #Adds all to textbox
    with open("reminder_list.txt", "r") as reminders:
        reminder_textbox.insert(INSERT, reminders.read())

#TODO: Entries for days of week, class, assignment
#Class
class_label = Label(text="1. Which class is this assignment for: ", pady=15, padx=5)
class_label.grid(row=1, column=0, sticky= "w")
radio_state = IntVar()
math330_radio = Radiobutton(text="MATH 330", value=1, variable=radio_state)
math336_radio = Radiobutton(text="MATH 336", value=2, variable=radio_state)
math340_radio = Radiobutton(text="MATH 340", value=3, variable=radio_state)
math532_radio = Radiobutton(text="MATH 532", value=4, variable=radio_state)
econ320_radio = Radiobutton(text="ECON 320", value=5, variable=radio_state)
econ507_radio = Radiobutton(text="ECON 507", value=6, variable=radio_state)
math330_radio.grid(row=1, column=1)
math336_radio.grid(row=1, column=2)
math340_radio.grid(row=1, column=3)
math532_radio.grid(row=1, column=4)
econ320_radio.grid(row=1, column=5)
econ507_radio.grid(row=1, column=6)

#Day of the Week
day_label = Label(text="2. Please select the assignment due date below:")
day_cal = Calendar(selectmode="day", year=2022, month=8)
day_cal.grid(row=3, column=0, pady=10)
day_label.grid(row=2, column=0)

#Assignment
assignment_label = Label(text="3. What type of assignment is this: ")
assignment_listbox = Listbox(height=5)
assignment_types = ["Other", "Project", "Test", "Quiz", "Homework"]
for assignment in assignment_types:
    assignment_listbox.insert(assignment.index(assignment), assignment)
assignment_listbox.bind("<<ListboxSelect>>")
assignment_listbox.grid(row=5, column=0, sticky="w", pady=10)
assignment_label.grid(row=4, column=0, sticky="w")

#Reminder Textbox
reminder_textbox = Text(height=15, width=50)
reminder_textbox.grid(row=2, column=2, columnspan=5, rowspan=3)

#TODO: Button that saves
reminder_button = Button(text="Click here to add this assignment to your reminder list", width=80, command=set_reminder)
reminder_button.grid(row=6, column=0, columnspan=5)

#Has reminders generate on start
with open("reminder_list.txt", "r") as reminders:
    reminder_textbox.insert(INSERT, reminders.read())

#--- LAST LINE ---#
window.mainloop()