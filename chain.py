import tkinter as tk
from tkinter import messagebox
from utils.data import chain_quests, BG_COLOR, FG_COLOR, ACCENT, FONT

def create_chain_tab(notebook, chain_quest_status, save_progress, data):
    frame_chain = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame_chain, text="🔗 Requisitos Secundários")

    tk.Label(frame_chain, text="Cadeia de Quests para Dragon Slayer II:", fg=FG_COLOR, bg=BG_COLOR, font=("Segoe UI", 12, "bold")).pack(pady=10)

    # Scrollable frame
    canvas = tk.Canvas(frame_chain, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_chain, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Bind mouse wheel to scroll the canvas
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind("<MouseWheel>", _on_mousewheel)
    scrollable_frame.bind("<MouseWheel>", _on_mousewheel)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    chain_vars = {}
    for stage, quests_list in chain_quests.items():
        tk.Label(scrollable_frame, text=stage, fg=ACCENT, bg=BG_COLOR, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20, pady=5)
        for q in sorted(quests_list):
            var = tk.BooleanVar(value=chain_quest_status.get(q, False))
            cb = tk.Checkbutton(scrollable_frame, text=q, variable=var, bg=BG_COLOR, fg="white",
                                selectcolor="#303134", activebackground=BG_COLOR, font=("Segoe UI", 10))
            cb.pack(anchor="w", padx=40)
            chain_vars[q] = var

    def save_chain():
        for q, v in chain_vars.items():
            chain_quest_status[q] = v.get()
        save_progress(data)
        messagebox.showinfo("Salvo", "Progresso de chain quests atualizado.")

    tk.Button(frame_chain, text="Salvar Progresso", command=save_chain, bg=ACCENT, fg="black", font=FONT).pack(pady=10)

    return chain_vars
