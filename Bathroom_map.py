from tkinter import Tk, messagebox
from tkinter.ttk import Combobox
from tkinter import Button

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
        combo = Combobox(root,values=evidences_group,state="readonly",width=25)
        combo.place(x=20, y=20 + i * 40)
        combos.append(combo)

    button = Button(root,text="Find Suspects",command=lambda: Main_command(*(combo.get() for combo in combos)))
    button.place(x=20, y=145)

    root.mainloop()
