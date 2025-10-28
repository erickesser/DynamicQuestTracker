import tkinter as tk
from tkinter import simpledialog, messagebox

def setup_quest():
    root = tk.Tk()
    root.title("Configuração Inicial - Dynamic Quest Tracker")
    root.geometry("400x300")
    root.configure(bg="#202124")

    tk.Label(root, text="Digite o nome da quest principal:", fg="#FFD700", bg="#202124", font=("Segoe UI", 12)).pack(pady=10)
    quest_entry = tk.Entry(root, font=("Segoe UI", 10), width=30)
    quest_entry.pack(pady=5)

    tk.Label(root, text="Digite as quests diretas (separadas por vírgula):", fg="#FFD700", bg="#202124", font=("Segoe UI", 10)).pack(pady=10)
    direct_quests_entry = tk.Entry(root, font=("Segoe UI", 10), width=50)
    direct_quests_entry.pack(pady=5)

    tk.Label(root, text="Digite as quests secundárias (separadas por vírgula):", fg="#FFD700", bg="#202124", font=("Segoe UI", 10)).pack(pady=10)
    secondary_quests_entry = tk.Entry(root, font=("Segoe UI", 10), width=50)
    secondary_quests_entry.pack(pady=5)

    def save_setup():
        quest_name = quest_entry.get().strip()
        direct_quests = [q.strip() for q in direct_quests_entry.get().split(',') if q.strip()]
        secondary_quests = [q.strip() for q in secondary_quests_entry.get().split(',') if q.strip()]

        if not quest_name:
            messagebox.showerror("Erro", "Nome da quest principal é obrigatório.")
            return

        # Salvar em um arquivo de configuração
        with open("quest_config.py", "w") as f:
            f.write(f"QUEST_NAME = '{quest_name}'\n")
            f.write(f"DIRECT_QUESTS = {direct_quests}\n")
            f.write(f"SECONDARY_QUESTS = {secondary_quests}\n")

        messagebox.showinfo("Sucesso", "Configuração salva! Agora execute main.py.")
        root.destroy()

    tk.Button(root, text="Salvar Configuração", command=save_setup, bg="#00FF80", fg="black", font=("Segoe UI", 10)).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    setup_quest()
