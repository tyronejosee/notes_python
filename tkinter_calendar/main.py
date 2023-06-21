from tkcalendar import Calendar

from tkinter import Tk
ventana = Tk()
cal = Calendar(ventana, locals="es_ES", date_pattern="dd-mm-y")

def print_date(date):
    print(date)
cal.bind("<<CalendarSelected>>",
    lambda e: print_date(cal.get_date()))

cal.pack()

ventana.mainloop()
