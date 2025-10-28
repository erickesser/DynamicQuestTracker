import tkinter as tk
from tkinter import ttk
import os
from utils.data import load_progress, save_progress, PLAYER_NAME, BG_COLOR, FG_COLOR, ACCENT, FONT

# Verificar se a configuração existe
if not os.path.exists("quest_config.py"):
    import subprocess
    subprocess.run(["python", "setup.py"])
    exit()

from quest_config import QUEST_NAME, DIRECT_QUESTS, SECONDARY_QUESTS
from quests import create_quests_tab
from skills import create_skills_tab
from config import create_config_tab
from guide import create_guide_tab
from chain import create_chain_tab
from summary import create_summary_tab

# -----------------------------
# GUI PRINCIPAL
# -----------------------------
root = tk.Tk()
root.title("Dynamic Quest Tracker")
root.geometry("750x700")
root.configure(bg=BG_COLOR)
root.eval('tk::PlaceWindow . center')

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
style.configure("TNotebook.Tab", font=FONT, background=BG_COLOR, foreground=FG_COLOR, padding=10)
style.map("TNotebook.Tab", background=[("selected", "#333333")])

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

progress_data = load_progress()
quest_status = progress_data.get("quests", {})
chain_quest_status = progress_data.get("chain_quests", {})
skill_levels = progress_data.get("skills", {})

data = {"quests": quest_status, "chain_quests": chain_quest_status, "skills": skill_levels}

# Criar abas na ordem desejada: Quest > Requisitos Secundários > Guia de Progressão > Skills > Resumo > Configurações
quest_vars = create_quests_tab(notebook, quest_status, save_progress, data)
chain_vars = create_chain_tab(notebook, chain_quest_status, save_progress, data)
create_guide_tab(notebook)
update_skills_tab = create_skills_tab(notebook, skill_levels, save_progress, data)
create_summary_tab(notebook, quest_vars, chain_vars, skill_levels)
create_config_tab(notebook)

root.mainloop()
