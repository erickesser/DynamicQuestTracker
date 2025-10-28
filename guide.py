import tkinter as tk
from data import progression_guide, BG_COLOR, FG_COLOR

def create_guide_tab(notebook):
    frame_guide = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame_guide, text="📖 Guia de Progressão")

    tk.Label(frame_guide, text="Guia de Progressão para Dragon Slayer II:", fg=FG_COLOR, bg=BG_COLOR, font=("Segoe UI", 12, "bold")).pack(pady=10)

    guide_text = tk.Text(frame_guide, bg=BG_COLOR, fg="white", font=("Segoe UI", 10), wrap="word", height=20)
    guide_text.pack(expand=True, fill="both", padx=20, pady=10)

    # Add scrollbar to the text widget
    scrollbar = tk.Scrollbar(frame_guide, command=guide_text.yview)
    scrollbar.pack(side="right", fill="y")
    guide_text.config(yscrollcommand=scrollbar.set)

    # Bind mouse wheel to scroll the text widget
    guide_text.bind("<MouseWheel>", lambda event: guide_text.yview_scroll(int(-1*(event.delta/120)), "units"))

    guide_text.insert("1.0", progression_guide)
    guide_text.config(state="disabled")
