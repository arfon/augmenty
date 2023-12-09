from ...util import registry


@registry.keyboards("mk_v1")
def create_mk():
    mk = {
        "default": [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
            ["љ", "њ", "е", "р", "т", "ѕ", "у", "и", "о", "п", "ш", "ѓ"],
            ["а", "с", "д", "ф", "г", "х", "ј", "к", "л", "ч", "ќ", "ж"],
            ["ѝ", "з", "џ", "ц", "в", "б", "н", "м", ",", ".", "/"],
        ],
        "shift": [
            ["!", "„", "“", "'", "%", "‚", "‘", "*", "(", ")", "_", "+"],
            ["Љ", "Њ", "Е", "Р", "Т", "S", "У", "И", "О", "П", "Ш", "Ѓ"],
            ["А", "С", "Д", "Ф", "Г", "Х", "Ј", "К", "Л", "Ч", "Ќ", "Ж"],
            ["Ѝ", "З", "Џ", "Ц", "В", "Б", "Н", "М", ";", ":", "?"],
        ],
    }
    return mk