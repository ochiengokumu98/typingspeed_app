import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and versatile.",
    "Tkinter makes building GUI applications easy.",
    "Practice makes perfect when learning to type fast."
]

# Global variables
start_time = 0

def start_test():
    global start_time
    start_time = time.time()
    sentence = random.choice(sentences)
    sentence_label.config(text=sentence)
    input_entry.delete(0, tk.END)
    input_entry.config(state="normal")
    input_entry.focus()
    result_label.config(text="")

def calculate_speed():
    global start_time
    end_time = time.time()
    typed_text = input_entry.get()
    original_text = sentence_label.cget("text")

    # Time taken in minutes
    time_taken = (end_time - start_time) / 60

    # Word count
    words = typed_text.split()
    word_count = len(words)

    # Accuracy
    correct_words = 0
    original_words = original_text.split()
    for i in range(min(len(words), len(original_words))):
        if words[i] == original_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100
    wpm = word_count / time_taken

    result_label.config(
        text=f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%"
    )

    input_entry.config(state="disabled")

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x250")

title_label = tk.Label(root, text="Typing Speed Test", font=("Arial", 18))
title_label.pack(pady=10)

sentence_label = tk.Label(root, text="", font=("Arial", 14), wraplength=550)
sentence_label.pack(pady=10)

input_entry = tk.Entry(root, font=("Arial", 14), width=60, state="disabled")
input_entry.pack(pady=10)

start_button = tk.Button(root, text="Start Test", command=start_test)
start_button.pack(side="left", padx=50, pady=10)

done_button = tk.Button(root, text="Done", command=calculate_speed)
done_button.pack(side="right", padx=50, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
