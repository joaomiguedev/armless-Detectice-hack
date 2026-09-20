from tkinter import Tk, messagebox
from tkinter.ttk import Combobox
from tkinter import Button

evidences_group = ["Fingerprints","Cold-blooded","Eats lots of food","Likes to clean","Sheds hair often","Has no Robux","Writes in their diary"]

evidence_people = {
    "Fingerprints": [
        "Clara", "Buck", "Linda", "Sophia", "Sara",
        "Rebecca", "Herbert", "Kyle", "Donald", "Susan"
    ],

    "Cold-blooded": [
        "Clara", "Linda", "Mary", "Junior", "Kyle",
        "David", "Trey", "James", "Susan", "Oliver", "Thomas"
    ],

    "Eats lots of food": [
        "Kyle", "Mary", "William", "Jimbo", "Buck",
        "Trey", "Donald", "Sophia", "Thomas", "Bob"
    ],

    "Likes to clean": [
        "Charles", "Sara", "William", "Nancy", "David",
        "Donald", "Herbert", "Betty", "Thomas", "Bob"
    ],

    "Sheds hair often": [
        "Charles", "William", "Junior", "Susan", "Matthew",
        "David", "Herbert", "Betty", "James", "Sophia"
    ],

    "Has no Robux": [
        "Clara", "Sara", "Jimbo", "Junior", "Nancy",
        "Oliver", "Matthew", "Trey", "Betty", "Rebecca", "Bob"
    ],

    "Writes in their diary": [
        "Charles", "Linda", "Mary", "Jimbo", "Nancy",
        "Buck", "Oliver", "Matthew", "James", "Rebecca"
    ]
}

suspect_numbers = {"Clara": 1,"Charles": 2,"Sara": 3,"Kyle": 4,"Linda": 5,"Mary": 6,"William": 7,"Jimbo": 8,"Junior": 9,"Nancy": 10,"Buck": 11,"Oliver": 12,"Susan": 13,"Matthew": 14,"David": 15,"Trey": 16,"Donald": 17,"Herbert": 18,"Betty": 19,"James": 20,"Sophia": 21,"Rebecca": 22,"Thomas": 23,"Bob": 24}

def Main_command(command1, command2, command3):
    passed_evidences = [command1, command2, command3]


    if "" in passed_evidences:
        messagebox.showwarning("Missing Evidence", "Please select all three pieces of evidence." )
        return

    if len(set(passed_evidences)) != 3:
        messagebox.showwarning("Duplicate Evidence", "Please select three different pieces of evidence." )
        return

    possible_suspects = set(evidence_people[passed_evidences[0]])

    for evidence in passed_evidences[1:]:
        possible_suspects &= set(evidence_people[evidence])

    if possible_suspects:
        results = []

        sorted_suspects = sorted(possible_suspects,key=lambda person: suspect_numbers[person])

        for suspect in sorted_suspects:
            number = suspect_numbers[suspect]
            results.append(f"{suspect} = {number} Suspect")

        messagebox.showinfo("Possible Suspects","\n".join(results))

    else:
        messagebox.showinfo("Possible Suspects","No suspects match all three pieces of evidence.")

def run():
    root = Tk()

    root.geometry("400x250")
    root.title("Suspect Finder - Hack Armless Detective Game")
    root.resizable(False, False)

    combo1 = Combobox(root,values=evidences_group,state="readonly",width=25)
    combo1.place(x=20, y=20)

    combo2 = Combobox(root,values=evidences_group,state="readonly",width=25)
    combo2.place(x=20, y=60)

    combo3 = Combobox(root,values=evidences_group,state="readonly",width=25)
    combo3.place(x=20, y=100)

    button1 = Button(root,text="Find Suspects",command=lambda: Main_command(combo1.get(),combo2.get(),combo3.get()))
    button1.place(x=20, y=145)

    root.mainloop()
