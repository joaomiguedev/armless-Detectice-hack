from tkinter import Tk, messagebox
from tkinter.ttk import Combobox
from tkinter import Button

evidences_group = ["Quick Escape","Is an arsonist","Releases Rats","Vandilizes public property","Has a habit of hiding evidence","Alien Help","Is Destructive"]

evidence_people = {
    "Quick Escape": ["Charles","Bob","Oakley","Jimbo","Junior","Hermy","Seymour","Olivia","Stacy","James","Jack"],
    "Is an arsonist": ["Charles","Benny","Bob","Jimbo","Hector","Seymour","Stacy","Vlorp","Sophia","Rob"],
    "Releases Rats": ["Charles","Mary","Susan","Olivia","Herbert","Vlorp","James","Matthew","Oakley","Whitley"],
    "Vandalizes public property": ["Sara","Benny","Jack","Mary","Susan","Archibald","Seymour","Hector","Herbert","Oakley"],
    "Has a habit of hiding evidence": ["Sara","Benny","Mary","Archibald","Hermy","Oliver","Rob","James","Whitley","Bob"],
    "Alien Help": ["Matthew","Archibald","Junior","Olivia","Whitley","Stacy","Vlorp","Herbert","Sophia","Oliver"],
    "Is Destructive": ["Sara","Jack","Susan","Jimbo","Junior","Hermy","Oliver","Rob","Sophia","Hector","Matthew"]}

suspect_numbers = {"Charles": 1,"Sara": 2,"Benny": 3,"Jack": 4,"Mary": 5,"Susan": 6,"Archibald": 7,"Jimbo": 8,"Junior": 9,"Hermy": 10,"Oliver": 11,"Seymour": 12,"Olivia": 13,"Rob": 14,"Stacy": 15,"Sophia": 16,"Hector": 17,"Herbert": 18,"Vlorp": 19,"James": 20,"Matthew": 21,"Oakley": 22,"Whitley": 23,"Bob": 24}

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

    for i in range(3):
        combo = Combobox(root,values=evidences_group,state="readonly",width=27)
        combo.place(x=20, y=20 + i * 40)
        combos.append(combo)

    button = Button(root,text="Find Suspects",command=lambda: Main_command(*(combo.get() for combo in combos)))
    button.place(x=20, y=145)

    root.mainloop()
