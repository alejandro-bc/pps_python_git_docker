import random

def frotar(n_frases: int = 1) -> list:
    try:
        with open("frases.txt", "r", encoding="utf-8") as f:
            # Leemos todas las líneas y quitamos saltos de línea
            todas_las_frases = [linea.strip() for linea in f.readlines() if linea.strip()]
        
        # Elegimos N frases al azar (permite repetición si hay pocas frases)
        # Si prefieres que no se repitan, usa random.sample()
        return random.choices(todas_las_frases, k=n_frases)
    
    except FileNotFoundError:
        return ["Error: No se encontró el archivo de frases."]