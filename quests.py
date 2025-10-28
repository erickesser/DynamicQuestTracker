import tkinter as tk
from tkinter import messagebox
from utils.data import quests, BG_COLOR, FG_COLOR, ACCENT, FONT

def create_quests_tab(notebook, quest_status, save_progress, data):
    frame_quests = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame_quests, text="🗺️ Quests")

    tk.Label(frame_quests, text="Progresso das Quests Diretas:", fg=FG_COLOR, bg=BG_COLOR, font=("Segoe UI", 12, "bold")).pack(pady=10)

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(frame_quests, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_quests, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Bind mouse wheel to scroll the canvas
    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    quest_vars = {}
    for q in sorted(quests):
        var = tk.BooleanVar(value=quest_status.get(q, False))
        cb = tk.Checkbutton(scrollable_frame, text=q, variable=var, bg=BG_COLOR, fg="white",
                            selectcolor="#303134", activebackground=BG_COLOR, font=("Segoe UI", 10))
        cb.pack(anchor="w", padx=40)
        quest_vars[q] = var

    def save_quests():
        for q, v in quest_vars.items():
            quest_status[q] = v.get()
        save_progress(data)
        messagebox.showinfo("Salvo", "Progresso de quests atualizado.")

    tk.Button(frame_quests, text="Salvar Progresso", command=save_quests, bg=ACCENT, fg="black", font=FONT).pack(pady=10)

    return quest_vars
