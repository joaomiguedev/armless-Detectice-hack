from tkinter import Tk, messagebox
from tkinter.ttk import Combobox
from tkinter import Button

evidences_group = ["Hacker","Cold-Blooded","Likes to clean","Sheds hair often","Vandalizes public property","Has Escaped/Escape plan","Releases Rats"]

evidence_people = {
    "Hacker": ["Clara","Bill","Mary","Nulltron","Junior","Jason","Squilliam","Rob","Oliver","Alicia","Jack"],
    "Cold-Blooded": ["Clara","Tod","Charles","Kyle","Amelia","Nulltron","Bob","Benedict","Rob","Alicia"],
    "Likes to clean": ["Tod","Charles","Benny","Mary","Jason","Xai","Gerbert","Stacy","Squilliam","Alicia"],
    "Sheds hair often": ["Noah","Kyle","Benny","Amelia","Bill","Hermy","Bob","Xai","Stacy","James","Oliver"],
    "Vandalizes public property": ["Noah","Amelia","Bill","Mary","Junior","Hermy","Benedict","Gerbert","Stacy","Rob"],
    "Has Escaped/Escape plan": ["Noah","Clara","Tod","Kyle","Junior","Benedict","Xai","Squilliam","James","Jack"],
    "Releases Rats": ["Charles","Benny","Nulltron","Hermy","Jason","Bob","Gerbert","James","Oliver","James"],}

suspect_numbers = {"Noah": 1,"Clara": 2,"Tod": 3,"Charles": 4,"Kyle": 5,"Jason": 6,"Amelia": 7,"Bill": 8,"Mary": 9,"Nulltron": 10,"Junior": 11,"Hermy": 12,"Jack": 13,"Alicia": 14,"Benedict": 15,"Xai": 16,"Gerbert": 17,"Rob": 18, "Squilliam": 19,"James": 20,"Stacy": 21,"Oliver": 22,"Benny": 23,"Bob": 24}

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
