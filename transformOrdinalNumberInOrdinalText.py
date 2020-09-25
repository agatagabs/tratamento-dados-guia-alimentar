def transformOrdinalNumberInOrdinalText(text):
    ordinals = {
        '1º': 'primeiro',
        '2º': 'segundo',
        '3º': 'terceiro',
        '4º': 'quarto',
        '5º': 'quinto',
        '6º': 'sexto',
        '7º': 'sétimo',
        '8º': 'oitavo',
        '9º': 'nono',
        '10º': 'décimo',
        '1ª': 'primeira',
        '2ª': 'segunda',
        '3ª': 'terceira',
        '4ª': 'quarta',
        '5ª': 'quinta',
        '6ª': 'sexta',
        '7ª': 'sétima',
        '8ª': 'oitava',
        '9ª': 'nona',
        '10ª': 'décima',
    }

    for numberOrdinal in ordinals.keys():
        text = text.replace(numberOrdinal, ordinals[numberOrdinal])

    return text