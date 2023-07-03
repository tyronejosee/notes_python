### Anagram ###

def is_anagram(texto_uno: str, texto_dos: str):
    if texto_uno.lower() == texto_dos.lower():
        return False
    elif sorted(texto_uno.lower()) == sorted(texto_dos.lower()):
        return True
    else:
        return False

print(is_anagram("amor", "roma"))
