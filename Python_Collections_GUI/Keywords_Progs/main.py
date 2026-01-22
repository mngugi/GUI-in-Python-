import tkinter as tk
from keywords_lib import get_keywords, is_keyword

# --- Window ---
root = tk.Tk()
root.title("Python Keyword Checker")
root.geometry("500x400")

# --- Title ---
title = tk.Label(root, text="Python Keywords", font=("Arial", 14, "bold"))
title.pack(pady=10)

# --- Text area to show keywords ---
text_area = tk.Text(root, height=15, width=40)
text_area.pack()

# Insert keywords
keywords = get_keywords()
text_area.insert(tk.END, ", ".join(keywords))
text_area.config(state="disabled")  # read-only

# --- Entry for checking keyword ---
entry_label = tk.Label(root, text="Check a word:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack()

# --- Result label ---
result_label = tk.Label(root, text="", font=("Arial", 8))
result_label.pack(pady=5)

# --- Button action ---
def check_word():
    word = entry.get()
    if is_keyword(word):
        result_label.config(text=f"'{word}' is a Python keyword ✅", fg="green")
    else:
        result_label.config(text=f"'{word}' is NOT a Python keyword ❌", fg="red")

# --- Button ---
check_btn = tk.Button(root, text="Check", command=check_word)
check_btn.pack(pady=10)

# --- Run ---
root.mainloop()
