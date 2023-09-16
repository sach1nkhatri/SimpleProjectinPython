#copyright_to_Sachin_Khatri
#enjoy_share_learn_explore
#Try_to_undersand_the_working_of_the_code_rather_then_copying_and_pasting.

from tkinter import *
import calendar

def show_calendar():
    year = int(year_entry.get())
    cal_text.delete(1.0, END)  # Clear any previous calendar data
    cal = calendar.calendar(year)
    cal_text.insert(INSERT, cal)

root = Tk()
root.title("Calendar")

# Set the root window size to fit the screen
root.geometry("1000x780")
root.configure(bg="#242623")
#root.iconbitmap("") #place your ico file here

frame = Frame(root, bg="#242623")  # Set the background color for the frame
frame.pack(pady=20)

year_label = Label(frame, text="Enter Year:", bg="#242623", fg="white")
year_label.grid(row=0, column=0, padx=10, pady=10)

year_entry = Entry(frame, bg="white", fg="black",border="2")
year_entry.grid(row=0, column=1, padx=10, pady=10)

show_button = Button(frame, text="Show Calendar", command=show_calendar, bg="#cc7b18")
show_button.grid(row=0, column=2, padx=10, pady=10)

cal_text = Text(root, height=38, width=74, border=0)
cal_text.pack()

# Set the background color of the Text widget to match the frame
cal_text.configure(bg="#242623")

# Set the text color to white for the Text widget
cal_text.configure(fg="white")

root.mainloop()
