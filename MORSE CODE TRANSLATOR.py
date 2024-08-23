MORSE CODE TRANSLATOR (PYTHON GUI APPLICATION)

import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char + ' '
    return morse_code.strip()

def morse_to_text(morse):
    text = ''
    morse_words = morse.split('/')
    for word in morse_words:
        morse_chars = word.split()
        for char in morse_chars:
            for key, value in morse_code_dict.items():
                if value == char:
                    text += key
        text += ' '
    return text.strip()

def translate_text():
    morse_text = text_to_morse(entry.get())
    output_text.set(morse_text)

def translate_morse():
    plain_text = morse_to_text(entry.get())
    output_text.set(plain_text)

def copy_to_clipboard():
    pyperclip.copy(output_text.get())
    messagebox.showinfo("Info", "Text copied to clipboard!")

# Create tkinter window
root = tk.Tk()
root.title("Morse Code Translator")

# Create input widget
entry = tk.Entry(root, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create "Translate to Morse" button
translate_to_morse_button = tk.Button(root, text="Translate to Morse Code", command=translate_text)
translate_to_morse_button.grid(row=1, column=0, padx=10, pady=10)

# Create "Translate to Text" button
translate_to_text_button = tk.Button(root, text="Translate to Text", command=translate_morse)
translate_to_text_button.grid(row=1, column=1, padx=10, pady=10)

# Create output label
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, font=("Comic Sans Ms", 14), wraplength=400)
output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create "Copy" button
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
