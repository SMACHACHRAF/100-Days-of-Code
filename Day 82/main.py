# Dictionnaire de conversion Texte -> Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Utilisation du "/" pour représenter un espace
}

def text_to_morse(text):
    text = text.upper()  # Convertir tout en majuscules
    morse_code = " ".join(morse_dict.get(char, '?') for char in text)  # "?" pour les caractères inconnus
    return morse_code

# Demande à l'utilisateur une phrase à convertir
user_text = input("Entrez votre texte à convertir en Morse : ")
morse_result = text_to_morse(user_text)

# Affichage du résultat
print(f"Texte en Morse : {morse_result}")
