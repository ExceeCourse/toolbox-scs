import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Initilialization Root Tkinter
root = tk.Tk()
root.iconbitmap('favicon.png') # Set Favicon
root.title('SCS-Academy ~ PDF Extractor Text', font=(14, "Raleway"))

# Main Window (Ukuran Jendela Canvas)
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image =logo
logo_label.grid(column=1,row=0)

# Instructions
instractions = tk.Label(root, text="Pilih file PDF di komputer Anda untuk Mengekstrak semua Teksnya", font="Raleway")
instractions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb", title="Pilih file", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # Text Box (Output)
        text_box = tk.Text(root, height=10, width=50, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

# Browse Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#043ade", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

# Main Text Output (Ukuran Jendela Canvas)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

# Melooping Program
root.mainloop()