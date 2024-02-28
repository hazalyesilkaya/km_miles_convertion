from tkinter import *

window = Tk()
window.title("Km-Miles Conversion")
window.geometry("300x550+500+200")
window.resizable(False, False)
window.configure(bg="#22247c")
main_text = Label(window, text="Enter the amount you want to convert", fg="white", bg="#22247c")
main_text.place(x=45, y=180)

entry_value = Entry(window, font="Calibri 12", width=26, bg="#e0e0e0")
entry_value.place(x=45, y=230)

result_label = Label(window, text="__________________________", fg="white", bg="#22247c", font="Calibri 12 bold")
result_label.place(x=45, y=260)


def convert_to_miles():
    try:
        km = float(entry_value.get())
        miles = round(km * 0.621371, 2)
        result_label.config(text=f"{km} km = {miles} miles")
    except ValueError:
        result_label.config(text="Please enter a number.")


def convert_to_km():
    try:
        miles = float(entry_value.get())
        km = round(miles / 0.621371, 2)
        result_label.config(text=f"{miles} miles = {km} km")
    except ValueError:
        result_label.config(text="Please enter a number.")


convert_icon = PhotoImage(file="../img/convert.png").subsample(5, 5)
road_img = PhotoImage(file="../img/road.png")
img = Label(image=road_img, height=120, width=250)
img.place(x=25, y=50, width=250, height=120)

convert_to_miles_button = Button(window,
                                 text="Km to Miles",
                                 image=convert_icon,
                                 compound=RIGHT,
                                 font="Calibri 14 bold",
                                 bg="white",
                                 height="45",
                                 width="205",
                                 command=convert_to_miles)
convert_to_miles_button.place(x=45, y=325)

convert_to_km_button = Button(window,
                              text="Miles to Km",
                              image=convert_icon,
                              compound=RIGHT,
                              font="Calibri 14 bold",
                              bg="white",
                              height="45",
                              width="205",
                              command=convert_to_km)
convert_to_km_button.place(x=45, y=395)

window.mainloop()
