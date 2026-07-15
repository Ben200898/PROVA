def remove_extra_spaces(text: str) -> str:
    """Rimuove spazi multipli e spazi iniziali/finali da una stringa."""
    return " ".join(text.split())

def to_lowercase(text: str) -> str:
    """Converte una stringa in minuscolo."""
    return text.lower()