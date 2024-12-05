import PyPDF2
import tkinter as tk
from tkinter import filedialog

def select_file():
    # Open the file dialog to select a file
    file_path = filedialog.askopenfilename(
        title="Wybierz plik",
        filetypes=(("PDF files", "*.pdf"),)
    )
    if file_path:
        # Analyze the selected file and display the results
        result = analyze_book(file_path)
        display_results(result)

def analyze_book(file_path):
    # Analyze the PDF for pages, words, and characters
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        total_words = 0
        total_characters_inc_space = 0
        total_characters_no_space = 0

        for page in reader.pages:
            text = page.extract_text()
            if text:  # Check if text extraction is successful
                total_characters_inc_space += len(text)
                total_words += len(text.split())
                total_characters_no_space += len(text.replace(" ", ""))

        return [num_pages, total_words, total_characters_inc_space, total_characters_no_space]

def display_results(results):
    # Display the analysis results in a label
    num_pages, total_words, total_characters_inc_space, total_characters_no_space = results
    result_label.config(
        text=f"Ilość stron: {num_pages}\n"
             f"Ilość słów: {total_words}\n"
             f"Ilość znaków (ze spacjami): {total_characters_inc_space}\n"
             f"Ilość znaków (bez spacji): {total_characters_no_space}"
    )

# Create the GUI
root = tk.Tk()
root.title("Appka analizujaca dla Myszy")
root.geometry("400x400")

# Add a button to select a file
button = tk.Button(root, text="Wybierz plik", font=('Arial', 18), command=select_file)
button.pack(pady=20)

# Add a label to display results
result_label = tk.Label(root, text="Wyniki analizy będą tutaj", font=('Arial', 12), wraplength=350)
result_label.pack(pady=20)

# Run the application
root.mainloop()