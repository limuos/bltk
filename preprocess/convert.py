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