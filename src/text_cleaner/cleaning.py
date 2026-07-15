def remove_extra_spaces(text: str) -> str:
    """Rimuove spazi multipli e spazi iniziali/finali da una stringa."""
    return " ".join(text.split())

def to_lowercase(text: str) -> str:
    """Converte una stringa in minuscolo."""
    return text.lower()

def remove_punctuation(text: str) -> str:
    """Rimuove i segni di punteggiatura più comuni da una stringa."""
    for char in ".,;:!?":
        text = text.replace(char, "")
    return text