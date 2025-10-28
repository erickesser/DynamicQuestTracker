import tkinter as tk
from tkinter import messagebox
from utils.data import PLAYER_NAME, BG_COLOR, FG_COLOR, ACCENT, FONT
from utils.functions import update_player_name

def create_config_tab(notebook):
    frame_config = tk.Frame(notebook, bg=BG_COLOR)
    notebook.add(frame_config, text="⚙️ Configurações")

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(frame_config, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_config, orient="vertical", command=canvas.yview)
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

    tk.Label(scrollable_frame, text="Nome do Personagem (Wise Old Man):", fg=FG_COLOR, bg=BG_COLOR, font=("Segoe UI", 12, "bold")).pack(pady=10, anchor="center")

    player_entry = tk.Entry(scrollable_frame, font=FONT, width=30)
    player_entry.insert(0, PLAYER_NAME)
    player_entry.pack(pady=5, anchor="center")

    def update_player():
        new_name = player_entry.get().strip()
        if new_name:
            update_player_name(new_name)
            messagebox.showinfo("Atualizado", f"Nome do jogador atualizado para: {new_name}")
        else:
            messagebox.showerror("Erro", "Nome do jogador não pode estar vazio.")

    tk.Button(scrollable_frame, text="Atualizar Nome", command=update_player, bg=ACCENT, fg="black", font=FONT).pack(pady=10, anchor="center")
