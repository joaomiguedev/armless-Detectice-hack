import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry("600x400")
root.title("Suspect Finder")
root.resizable(False, False)
root.configure(bg="#141821")

def run(map_name):
    if not map_name:
        messagebox.showwarning("No Map Selected","Please select a map before searching.")
        return

    modules = {"Motel Room and Humble Abode map": "Motel_Room_and_Humble_Abode_map","Bathroom map": "Bathroom_map","Gas Station map": "Gas_Station_map","Abandoned Apartment map": "Abandoned_Apartment_map","Moolah Manor map": "Moolah_Manor_map"}

    module_name = modules.get(map_name)

    if module_name:
        try:
            root.destroy()

            module = __import__(module_name)
            module.run()

        except ImportError:
            messagebox.showerror("Module Error", f"Could not find:\n{module_name}.py")

        except AttributeError:
            messagebox.showerror("Module Error",f"{module_name}.py does not contain a run() function." )

    else:
        messagebox.showwarning("Invalid Map","Please select a valid map name.")

style = ttk.Style()
style.theme_use("clam")

style.configure("Map.TCombobox",fieldbackground="#252b38",background="#252b38",foreground="white",arrowcolor="#7c9cff",bordercolor="#3b4354",lightcolor="#3b4354",darkcolor="#3b4354",padding=10,font=("Segoe UI", 11))

style.configure("Search.TButton",font=("Segoe UI", 12, "bold"),foreground="white",background="#5865F2",borderwidth=0,padding=(20, 12))

style.map("Search.TButton",background=[("active", "#4752C4"),("pressed", "#3C45A5")])

header = tk.Frame(root,bg="#1d2330",height=95)
header.pack(fill="x")

title = tk.Label(header,text="🔎  SUSPECT FINDER",font=("Segoe UI", 22, "bold"),fg="white",bg="#1d2330")
title.pack(pady=(18, 2))

subtitle = tk.Label(header,text="Select a map to search for suspects",font=("Segoe UI", 10),fg="#9aa4b5",bg="#1d2330")
subtitle.pack()

content = tk.Frame(root,bg="#141821")
content.pack(fill="both", expand=True)

label = tk.Label(content,text="MAP LOCATION",font=("Segoe UI", 10, "bold"),fg="#9aa4b5",bg="#141821")
label.place(x=70, y=35)

map_names = ["Motel Room and Humble Abode map","Bathroom map","Gas Station map","Abandoned Apartment map","Moolah Manor map"]

combobox1 = ttk.Combobox(content,values=map_names,state="readonly",style="Map.TCombobox",width=48)
combobox1.place(x=70, y=62)
combobox1.set("Select a map...")

bt1 = ttk.Button(content,text="🔍  FIND SUSPECTS",style="Search.TButton",command=lambda: run(combobox1.get()))
bt1.place(x=70, y=115, width=460, height=50)

status_frame = tk.Frame(content,bg="#1d2330")
status_frame.place(x=70, y=190, width=460, height=60)

status = tk.Label(status_frame,text="Choose a map above to begin.",font=("Segoe UI", 10),fg="#9aa4b5",bg="#1d2330")
status.pack(expand=True)

def update_status(event=None):
    selected = combobox1.get()
    if selected and selected != "Select a map...":status.config(text=f"Ready to search: {selected}",fg="#72e6a3" )

combobox1.bind("<<ComboboxSelected>>", update_status)

footer = tk.Label(root,text="Suspect Finder • Map Search Tool",font=("Segoe UI", 9),fg="#606a7c",bg="#141821")
footer.pack(pady=10)

root.mainloop()
