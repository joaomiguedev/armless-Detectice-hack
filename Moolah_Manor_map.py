mport tkinter as tk
from tkinter import ttk, messagebox

evidences_group = ["Believer/Believes in tooth fairy","Fingerprints","Releases Rats","Messy Library/Bookworm","Forgotten Shoe/Leaves shoe behind","Diamond/Is rich","Vandalizes public property","Drops bobbypins"]

evidence_people = {
    "Believer/Believes in tooth fairy": ["Silverline","Vandercash","Goldfeather","Goldsworth","Archibald","Jimbo","Benedict","Cashmere","Betty","Crownwell","Donald","Anastasia","Montgomery"],
    "Fingerprints": ["Silverline","Goldsworth","Matilda","Obsolete","Betty","Coinhart","Puffenstein","Donald","Junior II","Anastasia","Platinumveil","Reginald"],
    "Releases Rats": ["Donald","Sara","Goldfeather","Squillam","Marbleworth","Archibald","Jimbo","Matilda","Benedict","Crownwell","Puffenstein","Junior II","Coinhart"],
    "Messy Library/Bookworm": ["Silverline","Sara","Goldfeather","Marbleworth","Montgomery","Jimbo","Betty","Donovan","Obsolete","Benedict","Junior II","Platinumveil","Reginald"],
    "Forgotten Shoe/Leaves shoe behind": ["Sara","Squillam","Marbleworth","Jimbo","Matilda","Betty","Cashmere","Obsolete","Coinhart","Vandercash","Reginald","Goldsworth"],
    "Diamond/Is rich": ["Goldfeather","Squillam","Montgomery","Archibald","Donovan","Cashmere","Puffenstein","Junior II","Platinumveil","Reginald","Goldsworth"],
    "Vandalizes public property": ["Silverline","Vandercash","Squillam","Sara","Archibald","Matilda","Benedict","Crownwell","Anastasia","Platinumveil","Donovan"],
    "Drops bobbypins": ["Vandercash","Marbleworth","Obsolete","Cashmere","Coinhart","Crownwell","Puffenstein","Donald","Anastasia","Donovan","Montgomery"]}

suspect_numbers = {"Silverline": 1,"Sara": 2,"Goldfeather": 3,"Anastasia": 4,"Marbleworth": 5,"Montgomery": 6,"Archibald": 7,"Jimbo": 8,"Matilda": 9,"Betty": 10,"Donovan": 11,"Cashmere": 12,"Obsolete": 13,"Junior II": 14,"Benedict": 15,"Crownwell": 16,"Puffenstein": 17,"Donald": 18,"Squillam": 19,"Coinhart": 20,"Platinumveil": 21,"Vandercash": 22,"Reginald": 23,"Goldsworth": 24}

def run():
    root = tk.Tk()

    root.title("Moolah Manor Detective • Suspect Finder")
    root.geometry("720x690")
    root.resizable(False, False)
    root.configure(bg="#10141c")

    BG = "#10141c"
    PANEL = "#181e29"
    PANEL_LIGHT = "#202735"
    WHITE = "#f1f5f9"
    MUTED = "#8b97a8"
    BLUE = "#5865F2"
    BLUE_HOVER = "#4752c4"
    GREEN = "#3ddc97"
    RED = "#ff5c5c"
    BORDER = "#303949"

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Evidence.TCombobox",fieldbackground=PANEL_LIGHT,background=PANEL_LIGHT,foreground=WHITE,arrowcolor=BLUE,bordercolor=BORDER,lightcolor=BORDER,darkcolor=BORDER,padding=10,font=("Segoe UI", 11))
    style.map("Evidence.TCombobox",fieldbackground=[("readonly", PANEL_LIGHT)],foreground=[("readonly", WHITE)])
    style.configure("Search.TButton",font=("Segoe UI", 12, "bold"),foreground="white",background=BLUE,borderwidth=0,padding=12)
    style.map("Search.TButton",background=[("active", BLUE_HOVER),("pressed", "#3c45a5")])

    header = tk.Frame(root,bg="#171d28",height=105)
    header.pack(fill="x")

    title = tk.Label(header,text="🔎  SUSPECT INVESTIGATION",font=("Segoe UI", 24, "bold"),fg=WHITE,bg="#171d28")
    title.pack(pady=(18, 2))

    subtitle = tk.Label(header,text="Moolah Manor Detective • Suspect Finder",font=("Segoe UI", 10),fg=MUTED,bg="#171d28")
    subtitle.pack()

    main = tk.Frame(root,bg=BG)
    main.pack(fill="both", expand=True)

    instruction = tk.Label(main,text="Select four pieces of evidence found at the crime scene.",font=("Segoe UI", 11),fg=WHITE,bg=BG)
    instruction.pack(pady=(20, 5))

    instruction2 = tk.Label(main,text="The system will identify suspects matching ALL four.",font=("Segoe UI", 9),fg=MUTED,bg=BG)
    instruction2.pack(pady=(0, 15))

    evidence_panel = tk.Frame(main,bg=PANEL,highlightbackground=BORDER,highlightthickness=1)
    evidence_panel.pack(padx=55,fill="x")

    combos = []

    for i in range(4):
        row = tk.Frame(evidence_panel,bg=PANEL)
        row.pack(fill="x",padx=20,pady=(15 if i == 0 else 8, 8))

        number = tk.Label(row,text=f"{i + 1}",font=("Segoe UI", 11, "bold"),fg="white",bg=BLUE,width=3,height=1)
        number.pack(side="left",padx=(0, 12))

        label = tk.Label(row,text=f"Evidence #{i + 1}",font=("Segoe UI", 10, "bold"),fg=WHITE,bg=PANEL,width=15,anchor="w")
        label.pack(side="left")

        combo = ttk.Combobox(row,values=evidences_group,state="readonly",style="Evidence.TCombobox",width=35)
        combo.pack(side="left",padx=(5, 0),fill="x",expand=True)
        combo.set("Select evidence...")
        combos.append(combo)

    status = tk.Label(main,text="●  Waiting for evidence...",font=("Segoe UI", 10),fg=MUTED,bg=BG)
    status.pack(pady=(15, 5))

    button_frame = tk.Frame(main,bg=BG)
    button_frame.pack(pady=8)

    find_button = ttk.Button(button_frame,text="🔍  FIND SUSPECTS",style="Search.TButton")
    find_button.pack(side="left",padx=5)

    reset_button = tk.Button(button_frame,text="↻  RESET",font=("Segoe UI", 10, "bold"),fg=MUTED,bg=PANEL_LIGHT,activeforeground=WHITE,activebackground="#303949",relief="flat",padx=18,pady=11,cursor="hand2")
    reset_button.pack(side="left",padx=5)

    result_panel = tk.Frame(main,bg=PANEL,highlightbackground=BORDER, highlightthickness=1)
    result_panel.pack(padx=55,pady=(10, 15),fill="both",expand=True)

    result_title = tk.Label(result_panel,text="POSSIBLE SUSPECTS",font=("Segoe UI", 10, "bold"),fg=MUTED, bg=PANEL)
    result_title.pack(anchor="w",padx=18,pady=(12, 5))

    result_text = tk.Text(result_panel,bg=PANEL,fg=WHITE,insertbackground=WHITE,font=("Consolas", 11),relief="flat",height=7,state="disabled")
    result_text.pack(fill="both",expand=True,padx=18,pady=(0, 12))

    def find_suspects():
        selected = [combo.get()for combo in combos]

        if any(evidence == "" or evidence == "Select evidence..." for evidence in selected ):
            status.config(text="●  Missing evidence",fg=RED)

            messagebox.showwarning("Missing Evidence","Please select all four pieces of evidence.")
            return

        if len(set(selected)) != 4:
            status.config(text="●  Duplicate evidence detected",fg=RED)

            messagebox.showwarning("Duplicate Evidence","Please select four different pieces of evidence.")
            return

        possible_suspects = set( evidence_people[selected[0]])

        for evidence in selected[1:]:
            possible_suspects &= set(evidence_people[evidence])

        result_text.config(state="normal")
        result_text.delete( "1.0", tk.END)

        if possible_suspects:
            sorted_suspects = sorted(possible_suspects,key=lambda person: suspect_numbers[person])

            status.config(text=f"●  Investigation complete • "f"{len(sorted_suspects)} suspect(s) found",fg=GREEN)

            for suspect in sorted_suspects:
                number = suspect_numbers[suspect]

                result_text.insert(tk.END,f"  #{number:02d}   {suspect}\n")

        else:

            status.config(text="●  Investigation complete • No matches",fg=RED)

            result_text.insert(tk.END,"\n  No suspects match all four pieces of evidence.")

        result_text.config(state="disabled" )

    find_button.config(command=find_suspects )

    def reset():
        for combo in combos:
            combo.set("Select evidence...")

        result_text.config( state="normal")
        result_text.delete("1.0",tk.END)
        result_text.config(state="disabled")

        status.config(text="●  Waiting for evidence...",fg=MUTED)

    reset_button.config(command=reset)

    root.mainloop()
