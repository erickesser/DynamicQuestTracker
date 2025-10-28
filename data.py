import json
import os

# -----------------------------
# CONFIGURAÇÕES
# -----------------------------
PLAYER_NAME = "E ck"  # Nome do personagem no Wise Old Man
SAVE_FILE = "data.json"
API_URL = f"https://api.wiseoldman.net/v2/players/{PLAYER_NAME.replace(' ', '%20')}"
BG_COLOR = "#202124"
FG_COLOR = "#FFD700"
ACCENT = "#00FF80"
FONT = ("Segoe UI", 10, "bold")

# Pré-requisitos diretos para Dragon Slayer II
quests = [
    "Dragon Slayer I",
    "Animal Magnetism",
    "The Fremennik Trials",
    "Lost City",
    "Nature Spirit",
    "Priest in Peril",
    "Ghosts Ahoy",
    "Bone Voyage",
    "Client of Kourend",
    "Dream Mentor",
    "A Tail of Two Cats",
    "The Great Brain Robbery",
    "Shadow of the Storm",
    "Making History",
    "Lunar Diplomacy",
    "The Fremennik Isles",
    "Royal Trouble",
    "Mountain Daughter",
    "What Lies Below",
    "The Queen of Thieves",
    "The Depths of Despair",
    "Curse of the Empty Lord",
    "The Corsair Curse",
    "Dragon Slayer II"
]

# Níveis requeridos para Dragon Slayer II
skills = {
    "attack": 1, "strength": 1, "defence": 40, "hitpoints": 50,
    "ranged": 1, "magic": 75, "prayer": 43, "runecrafting": 1,
    "construction": 50, "agility": 60, "herblore": 1, "thieving": 60,
    "crafting": 62, "fletching": 1, "slayer": 50, "hunter": 1,
    "mining": 68, "smithing": 70, "fishing": 1, "cooking": 1,
    "firemaking": 1, "woodcutting": 1, "farming": 1
}

skill_names = {
    "attack": "Ataque", "strength": "Força", "defence": "Defesa", "hitpoints": "Pontos de Vida",
    "ranged": "Combate à Distância", "magic": "Magia", "prayer": "Oração", "runecrafting": "Runecrafting",
    "construction": "Construção", "agility": "Agilidade", "herblore": "Herbologia", "thieving": "Furto",
    "crafting": "Artesanato", "fletching": "Flecharia", "slayer": "Slayer", "hunter": "Caça",
    "mining": "Mineração", "smithing": "Ferraria", "fishing": "Pesca", "cooking": "Culinária",
    "firemaking": "Fazer Fogo", "woodcutting": "Corte de Madeira", "farming": "Agricultura"
}

chain_quests = {
    "🔹 Etapa 1 — Começo (quests básicas)": [
        "Cook’s Assistant", "Romeo & Juliet", "Ernest the Chicken", "The Restless Ghost", "Gertrude’s Cat", "Rune Mysteries", "Sheep Shearer"
    ],
    "🔹 Etapa 2 — Acesso a áreas e facções": [
        "Druidic Ritual", "Lost City", "Priest in Peril", "Nature Spirit", "The Dig Site", "Temple of Ikov", "Troll Stronghold", "Heroes’ Quest", "Family Crest", "Underground Pass", "Biohazard", "Plague City"
    ],
    "🔹 Etapa 3 — Rumo às grandes histórias": [
        "Shilo Village", "Jungle Potion", "Legends’ Quest (precisa de todos os acima + 107 Quest Points)", "Icthlarin’s Little Helper", "A Tail of Two Cats", "Ghosts Ahoy", "Bone Voyage", "Client of Kourend", "Dream Mentor"
    ]
}

progression_guide = """
PLANO DE PROGRESSÃO SUGERIDO
Etapa 1. Subir habilidades básicas: Treine Mining, Smithing, Crafting, Agility e Thieving até pelo menos 50.
Etapa 2. Acumular Quest Points: Faça quests curtas e fáceis (Cook’s Assistant, Witch’s House, Vampire Slayer, etc.).
Etapa 3. Liberar Fossil Island: Faça Museum Kudos → Bone Voyage.
Etapa 4. Avançar em Kourend: Faça Client of Kourend e suba favor em casas.
Etapa 5. Desbloquear Magias e Runas: Faça Lunar Diplomacy e Dream Mentor.
Etapa 6. Entrar na linha de Legends’ Quest: Complete todas as quests que levam até ela (Nature Spirit, Shilo Village, etc.).
Etapa 7. Terminar os pré-requisitos diretos: Complete Ghosts Ahoy, Animal Magnetism, A Tail of Two Cats.
Etapa 8. Subir níveis finais: Leve Magic a 75, Smithing a 70, Mining a 68, Crafting a 62, Agility/Thieving a 60, Construction a 50.
Etapa 9. Alcançar 200 Quest Points: Faça quests extras rápidas até atingir o mínimo.
Etapa 10. Iniciar Dragon Slayer II: Fale com Alec Kincade em Myths’ Guild após completar tudo.
"""

# -----------------------------
# SALVAR E CARREGAR PROGRESSO
# -----------------------------
def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {"quests": {}, "chain_quests": {}, "skills": {}}

def save_progress(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_api_url(new_name):
    global API_URL
    API_URL = f"https://api.wiseoldman.net/v2/players/{new_name.replace(' ', '%20')}"
