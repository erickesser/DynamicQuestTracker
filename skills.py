import tkinter as tk
from data import skills, skill_names, BG_COLOR, FG_COLOR, ACCENT, FONT
from functions import fetch_skills

def create_skills_tab(notebook, skill_levels, save_progress, data):
    frame_skills = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame_skills, text="⚔️ Skills")

    tk.Label(frame_skills, text="Níveis das Habilidades:", fg=FG_COLOR, bg=BG_COLOR, font=("Segoe UI", 12, "bold")).pack(pady=10)

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(frame_skills, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_skills, orient="vertical", command=canvas.yview)
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

    skills_grid = tk.Frame(scrollable_frame, bg=BG_COLOR)
    skills_grid.pack(expand=True, fill="both", padx=20, pady=10)

    skill_labels = []
    row = 0
    col = 0
    for skill in skills:
        name = skill_names.get(skill, skill.capitalize())
        required_level = skills[skill]
        current_level = skill_levels.get(skill, 1)
        remaining = max(0, required_level - current_level)
        skill_frame = tk.Frame(skills_grid, bg="#333333", relief="raised", borderwidth=2, width=180, height=100)
        skill_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        skill_frame.grid_propagate(False)
        name_label = tk.Label(skill_frame, text=name, fg=FG_COLOR if current_level < required_level else "green", bg="#333333", font=("Segoe UI", 9, "bold"))
        name_label.pack(pady=2)
        level_label = tk.Label(skill_frame, text=f"Nível: {current_level}", fg="white", bg="#333333", font=("Segoe UI", 11))
        level_label.pack(pady=2)
        if remaining > 0:
            remaining_label = tk.Label(skill_frame, text=f"Falta: {remaining}", fg="yellow", bg="#333333", font=("Segoe UI", 9))
            remaining_label.pack(pady=2)
        skill_labels.append((level_label, name_label))
        col += 1
        if col == 3:
            col = 0
            row += 1

    def update_skills_tab():
        for i, skill in enumerate(skills):
            current = skill_levels.get(skill, 1)
            required_level = skills[skill]
            remaining = max(0, required_level - current)
            level_label, name_label = skill_labels[i]
            level_label.config(text=f"Nível: {current}")
            name_label.config(fg=FG_COLOR if current < required_level else "green")
            # Remove existing remaining label if any
            for widget in level_label.master.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("text").startswith("Falta:"):
                    widget.destroy()
            if remaining > 0:
                remaining_label = tk.Label(level_label.master, text=f"Falta: {remaining}", fg="yellow", bg="#333333", font=("Segoe UI", 9))
                remaining_label.pack(pady=2)

    update_skills_tab()

    tk.Button(frame_skills, text="Atualizar Níveis (Wise Old Man)", command=lambda: fetch_skills(skill_levels, update_skills_tab, save_progress, data), bg=ACCENT, fg="black", font=FONT).pack(pady=10)

    return update_skills_tab
