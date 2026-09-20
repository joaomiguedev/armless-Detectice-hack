import tkinter as tk
from tkinter import ttk, messagebox

evidences_group = ["Hair/Shesds hair often","Ransacked/Known Looter","Releases Rats","Is an arsonist","Leaves shoe behind","Has a habit of hiding evidence","Vandalizes public property"]

evidence_people = {
    "Hair/Shesds hair often": ["Noah","Kyle","Xai","Amelia","Olivia","Oliver","Stacy","Herbert","James","Benny","Bob"],
    "Ransacked/Known Looter": ["Noah","Amelia","Mary","Rob","Junior","Olivia","Benedict","Stacy","Herbert","Gerbert"],
    "Releases Rats": ["Noah","Clara","Tod","Kyle","Xai","Junior","Jack","Benedict","Squilliam","James"],
    "Is an arsonist": ["Tod","Sophia","Xai","Mary","Alicia","Charles","Stacy","Squilliam","Gerbert","Benny"],
    "Leaves shoe behind": ["Clara","Sophia","Mary","Rob","Junior","Jack","Alicia","Olivia","Oliver","Squilliam","Rebecca"],
    "Has a habit of hiding evidence": ["Clara","Tod","Kyle","Amelia","Rob","Alicia","Benedict","Charles","Rebecca","Bob"],
    "Vandalizes public property": ["Sophia","Jack","Oliver","Charles","Herbert","James","Gerbert","Rebecca","Benny","Bob"]}

suspect_numbers = {"Noah": 1,"Clara": 2,"Tod": 3,"Sophia": 4,"Kyle": 5,"Xai": 6,"Amelia": 7,"Mary": 8,"Rob": 9,"Junior": 10,"Jack": 11,"Alicia": 12,"Olivia": 13,"Oliver": 14,"Benedict": 15,"Charles": 16,"Stacy": 17,"Herbert": 18,"Squilliam": 19,"James": 20,"Gerbert": 21,"Rebecca": 22,"Benny": 23,"Bob": 24}

def run():
    root = tk.Tk()

    root.title("Bathroom Detective • Suspect Finder")
    root.geometry("720x620")
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
    style.map("Search.TButton", background=[("active", BLUE_HOVER),("pressed", "#3c45a5")])

    header = tk.Frame(root,bg="#171d28",height=105)
    header.pack(fill="x")

    title = tk.Label(header,text="🔎  SUSPECT INVESTIGATION",font=("Segoe UI", 24, "bold"),fg=WHITE,bg="#171d28")
    title.pack(pady=(18, 2))

    subtitle = tk.Label(header,text="Bathroom Detective • Suspect Finder",font=("Segoe UI", 10),fg=MUTED,bg="#171d28")
    subtitle.pack()

    main = tk.Frame(root,bg=BG)
    main.pack(fill="both", expand=True)

    instruction = tk.Label(main,text="Select three pieces of evidence found at the crime scene.",font=("Segoe UI", 11),fg=WHITE,bg=BG)
    instruction.pack(pady=(20, 5))

    instruction2 = tk.Label(main,text="The system will identify suspects matching ALL three.",font=("Segoe UI", 9),fg=MUTED,bg=BG)
    instruction2.pack(pady=(0, 15))

    evidence_panel = tk.Frame(main,bg=PANEL,highlightbackground=BORDER,highlightthickness=1)
    evidence_panel.pack(padx=55,fill="x")

    combos = []

    for i in range(3):
        row = tk.Frame(evidence_panel,bg=PANEL)
        row.pack(fill="x",padx=20,pady=(15 if i == 0 else 8, 8))

        number = tk.Label(row,text=f"{i + 1}",font=("Segoe UI", 11, "bold"),fg="white",bg=BLUE,width=3,height=1)
        number.pack(side="left", padx=(0, 12))

        label = tk.Label(row,text=f"Evidence #{i + 1}",font=("Segoe UI", 10, "bold"),fg=WHITE,bg=PANEL,width=15,anchor="w")
        label.pack(side="left")

        combo = ttk.Combobox(row,values=evidences_group,state="readonly",style="Evidence.TCombobox",width=35)
        combo.pack(side="left",padx=(5, 0),fill="x",expand=True)
        combo.set("Select evidence...")
        combos.append(combo)

    status = tk.Label(main,text="●  Waiting for evidence...",font=("Segoe UI", 10),fg=MUTED,bg=BG)
    status.pack(pady=(15, 5))

    button_frame = tk.Frame( main,bg=BG)
    button_frame.pack(pady=8)

    find_button = ttk.Button(button_frame,text="🔍  FIND SUSPECTS",style="Search.TButton")
    find_button.pack(side="left",padx=5)

    reset_button = tk.Button(button_frame,text="↻  RESET",font=("Segoe UI", 10, "bold"),fg=MUTED,bg=PANEL_LIGHT,activeforeground=WHITE,activebackground="#303949",relief="flat",padx=18,pady=11,cursor="hand2")
    reset_button.pack(side="left",padx=5)

    result_panel = tk.Frame(main,bg=PANEL,highlightbackground=BORDER,highlightthickness=1)
    result_panel.pack(padx=55,pady=(10, 15),fill="both",expand=True)

    result_title = tk.Label(result_panel,text="POSSIBLE SUSPECTS",font=("Segoe UI", 10, "bold"),fg=MUTED,bg=PANEL)
    result_title.pack(anchor="w",padx=18,pady=(12, 5))

    result_text = tk.Text(result_panel,bg=PANEL,fg=WHITE,insertbackground=WHITE,font=("Consolas", 11),relief="flat",height=6,state="disabled")
    result_text.pack(fill="both",expand=True,padx=18,pady=(0, 12))

    def find_suspects():
        selected = [combo.get()for combo in combos]

        if any(evidence == "" or evidence == "Select evidence..."for evidence in selected):
            status.config(text="●  Missing evidence",fg=RED)
            messagebox.showwarning("Missing Evidence","Please select all three pieces of evidence.")
            return

        if len(set(selected)) != 3:
            status.config(text="●  Duplicate evidence detected",fg=RED)
            messagebox.showwarning("Duplicate Evidence","Please select three different pieces of evidence.")
            return

        possible_suspects = set(evidence_people[selected[0]])

        for evidence in selected[1:]:
            possible_suspects &= set(evidence_people[evidence])

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)

        if possible_suspects:
            sorted_suspects = sorted(possible_suspects,key=lambda person: suspect_numbers[person])

            status.config(text=f"●  Investigation complete • {len(sorted_suspects)} suspect(s) found",fg=GREEN)

            for suspect in sorted_suspects:
                number = suspect_numbers[suspect]
                result_text.insert(tk.END,f"  #{number:02d}   {suspect}\n")

        else:
            status.config(text="●  Investigation complete • No matches",fg=RED)

            result_text.insert(tk.END,"\n  No suspects match all three pieces of evidence.")

        result_text.config(state="disabled")

    find_button.config(command=find_suspects)

    def reset():
        for combo in combos:
            combo.set("Select evidence...")

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.config(state="disabled")

        status.config(text="●  Waiting for evidence...",fg=MUTED )

    reset_button.config(command=reset)

    root.mainloop()
