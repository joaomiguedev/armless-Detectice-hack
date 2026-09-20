from tkinter import Tk, messagebox
from tkinter.ttk import Combobox
from tkinter import Button

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

def Main_command(*commands):
    passed_evidences = list(commands)

    if "" in passed_evidences:
        messagebox.showwarning("Missing Evidence","Please select all three pieces of evidence." )
        return

    if len(set(passed_evidences)) != len(passed_evidences):
        messagebox.showwarning("Duplicate Evidence","Please select different pieces of evidence.")
        return

    possible_suspects = set(evidence_people[passed_evidences[0]])

    for evidence in passed_evidences[1:]:
        possible_suspects &= set(evidence_people[evidence])

    if possible_suspects:
        results = []

        sorted_suspects = sorted(possible_suspects,key=lambda person: suspect_numbers[person])

        for suspect in sorted_suspects:
            results.append(f"{suspect} = {suspect_numbers[suspect]} Suspect")

        messagebox.showinfo("Possible Suspects","\n".join(results))
    else:
        messagebox.showinfo("Possible Suspects","No suspects match all selected evidence.")

def run():
    root = Tk()

    root.geometry("400x250")
    root.title("Bathroom - Suspect Finder")
    root.resizable(False, False)

    combos = []

    for i in range(4):
        combo = Combobox(root,values=evidences_group,state="readonly",width=27)
        combo.place(x=20, y=20 + i * 40)
        combos.append(combo)

    button = Button(root,text="Find Suspects",command=lambda: Main_command(*(combo.get() for combo in combos)))
    button.place(x=20, y=170)

    root.mainloop()
