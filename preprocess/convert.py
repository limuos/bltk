from googletrans import Translator
from indic_transliteration import sanscript
import re


def NLK(word):

    translator = Translator()

    beng = translator.translate(word.strip(), dest="en")
    return str(re.findall("pronunciation=.*", str(beng))[0][:-1].split("=")[1]).lower()


def bn_ITRANS(word):

    output = sanscript.transliterate(word, sanscript.BENGALI, sanscript.ITRANS)
    output = output.replace('য়', 'y')
    output = output.replace('~', '')
    output = output.replace('ৎ', 't')
    output = output.replace('.', '')
    output = output.replace('়', '')

    return output.lower()


def hn_ITRANS(word):

    output = sanscript.transliterate(word, sanscript.DEVANAGARI, sanscript.ITRANS)
    return output.lower()


def phonetic2roman(word):
    
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z'
    ]

    phone2char = {
            '̥ḥ': 'h', 'ṃ': 'm', 'ṇ': 'n',
            'ṁ': 'm', 'ō': 'o', 'ṭ': 't',
            'ẏ': 'y', 'ē': 'e', 'ṣ': 's',
            'ṛ': 'r', 'ī': 'i', 'ū': 'u',
            'ñ': 'n', 'ḍ': 'd', 'ṯ': 't',
            'ṅ': 'n', 'ś': 's', 'ā': 'a'
    }

    roman = []
    for char in word:
        if char in chars:
            roman.append(char)
        else:
            if char in phone2char:
                roman.append(phone2char[char])
            else:
                pass
    return "".join(roman)


def phonetic_normalize(word):
	return normalized


def phonetic_de_normalized(word):
	return de_normalized