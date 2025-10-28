import tkinter as tk
from utils.data import quests, skills, chain_quests, BG_COLOR, FG_COLOR, ACCENT, FONT

def create_summary_tab(notebook, quest_vars, chain_vars, skill_levels):
    frame_summary = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame_summary, text="📈 Resumo")

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(frame_summary, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_summary, orient="vertical", command=canvas.yview)
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

    def update_summary():
        # Clear previous labels
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        q_done = sum(v.get() for v in quest_vars.values())
        c_done = sum(v.get() for v in chain_vars.values())
        s_avg = sum(min(1, skill_levels.get(k, 1)/v) for k,v in skills.items() if v > 1) / len([v for v in skills.values() if v > 1])
        tk.Label(scrollable_frame, text=f"Quests diretas concluídas: {q_done}/{len(quests)}", fg=FG_COLOR, bg=BG_COLOR, font=FONT).pack(pady=5, anchor="center")
        tk.Label(scrollable_frame, text=f"Chain quests concluídas: {c_done}/{sum(len(l) for l in chain_quests.values())}", fg=ACCENT, bg=BG_COLOR, font=FONT).pack(pady=5, anchor="center")
        tk.Label(scrollable_frame, text=f"Progresso médio de Skills requeridas: {round(s_avg*100, 1)}%", fg="white", bg=BG_COLOR, font=FONT).pack(pady=5, anchor="center")

    tk.Button(frame_summary, text="Atualizar Resumo", command=update_summary, bg=ACCENT, fg="black", font=FONT).pack(pady=20, anchor="center")

    update_summary()
