def count_chars(s: str) -> dict:
    return {c: s.count(c) for c in s}


string = "Happiness"
print(count_chars(string))
# {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

string = 'smiles'
print(count_chars(string))
# {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
