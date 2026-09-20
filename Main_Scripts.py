from tkinter import Tk, messagebox
from tkinter.ttk import Combobox
from tkinter import Button

root = Tk()

root.geometry("400x250")
root.title("need map name to find suspect")
root.resizable(False, False)

map_name = ["Motel Room and Humble Abode map", "Bathroom map","Gas Station map","Abandoned Apartment map","Moolah Manor map"]

combobox1 = Combobox(root,values=map_name,state="readonly",width=34)
combobox1.place(x=20, y=20)

bt1 = Button(root,text="Find Suspects",command=lambda: run(combobox1.get()))
bt1.place(x=20, y=60)

def run(map_name):
    if map_name == "Motel Room and Humble Abode map":
        root.destroy()
        import Motel_Room_and_Humble_Abode_map
        Motel_Room_and_Humble_Abode_map.run()
    elif map_name == "Bathroom map":
        root.destroy()
        import Bathroom_map
        Bathroom_map.run()
    elif map_name == "Gas Station map":
        root.destroy()
        import Gas_Station_map
        Gas_Station_map.run()
    elif map_name == "Abandoned Apartment map":
        root.destroy()
        import Abandoned_Apartment_map
        Abandoned_Apartment_map.run()
    elif map_name == "Moolah Manor map":
        root.destroy()
        import Moolah_Manor_map
        Moolah_Manor_map.run()
    else:
        messagebox.showwarning("Invalid Map","Please select a valid map name.")

root.mainloop()
