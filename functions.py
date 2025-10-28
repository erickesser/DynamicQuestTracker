import requests
import tkinter as tk
from tkinter import messagebox
from .data import API_URL, skills, skill_names

# -----------------------------
# FUNÇÃO PARA ATUALIZAR SKILLS
# -----------------------------
def fetch_skills(skill_levels, update_skills_tab, save_progress, data):
    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            raise Exception("Jogador não encontrado ou API offline.")
        data_json = response.json()
        if "latestSnapshot" not in data_json or "data" not in data_json["latestSnapshot"] or "skills" not in data_json["latestSnapshot"]["data"]:
            raise Exception("Dados de skills não encontrados na resposta da API.")
        player_skills = data_json["latestSnapshot"]["data"]["skills"]
        for skill, min_level in skills.items():
            if skill in player_skills:
                current_level = player_skills[skill]["level"]
                skill_levels[skill] = current_level
        update_skills_tab()
        save_progress(data)
        messagebox.showinfo("Sucesso", "Níveis atualizados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def update_player_name(new_name):
    from .data import PLAYER_NAME, update_api_url
    PLAYER_NAME = new_name
    update_api_url(new_name)
