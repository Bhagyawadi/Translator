from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

def Convert(text="type", src="english", dest="hindi"):
    translated = GoogleTranslator(source=src, target=dest).translate(text)
    return translated

def GetData():
    s = source_combo.get().lower()
    d = dest_combo.get().lower()
    msg = source_txt.get(1.0, END).strip()
    try:
        translated_text = Convert(text=msg, src=s, dest=d)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, translated_text)
    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {str(e)}")

# GUI setup
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="wheat")

Label(root, text="TRANSLATOR", font=("Times New Roman", 30, "bold"), bg="wheat").place(x=100, y=40, height=50, width=300)

Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="wheat").place(x=100, y=100, height=30, width=300)

source_txt = Text(root, font=("Times New Roman", 15), wrap=WORD)
source_txt.place(x=10, y=140, height=200, width=480)

languages = [
    "english", "hindi", "french", "spanish", "german", "chinese", "japanese",
    "korean", "arabic", "bengali", "marathi", "telugu", "tamil", "urdu", "gujarati"
]

source_combo = ttk.Combobox(root, values=languages)
source_combo.place(x=10, y=355, height=30, width=150)
source_combo.set("english")

Button(root, text="Translate", relief=RAISED, bg="lightgreen", fg="black", command=GetData).place(x=187, y=355, height=30, width=125)

dest_combo = ttk.Combobox(root, values=languages)
dest_combo.place(x=340, y=355, height=30, width=150)
dest_combo.set("hindi")

Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg="black", bg="wheat").place(x=100, y=400, height=30, width=300)

dest_txt = Text(root, font=("Times New Roman", 15), wrap=WORD)
dest_txt.place(x=10, y=440, height=200, width=480)

root.mainloop()
