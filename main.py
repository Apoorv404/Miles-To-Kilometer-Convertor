from tkinter import *

def miles_to_km():
    miles = float(miles_entry.get())
    km = round((miles * 1.609), 3)
    label3.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=2, row=1)

#Label
label1 =  Label(text="Miles")
label1.grid(column=3, row=1)

label2 =  Label(text="is equal to")
label2.grid(column=1, row=2)

label3 =  Label(text="0")
label3.grid(column=2, row=2)

label4 =  Label(text="Km")
label4.grid(column=3, row=2)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()
