def count_words(file_path: str) -> dict:
    content = open(file_path).read().lower().split()
    return {c: content.count(c) for c in content}


file_path = './P1_data.txt'
print(count_words(file_path))
# {'he': 1, 'who': 3, 'conquers': 1, 'himself': 1, 'is': 3, 'the': 5, 'mightiest': 1, 'warrior': 1, 'try': 2, 'not': 1, 'to': 3, 'become': 2, 'a': 7, 'man': 6, 'of': 4, 'success': 3, 'but': 1, 'rather': 1, 'value': 1, 'one': 4, 'with': 4, 'courage': 1, 'makes': 1, 'majority': 1, 'secret': 1, 'in': 4, 'life': 2, 'for': 3, 'be': 1, 'ready': 1, 'his': 2, 'opportunity': 1, 'when': 2, 'it': 2, 'comes': 2, 'successful': 2, 'will': 2, 'profit': 1, 'from': 1, 'mistakes': 1, 'and': 1, 'again': 1, 'different': 1, 'way': 1, 'can': 3, 'lay': 1, 'firm': 1, 'foundation': 1, 'bricks': 1, 'others': 1, 'have': 1, 'thrown': 1, 'at': 1, 'him': 1, 'usually': 1, 'those': 1, 'are': 1, 'too': 1, 'busy': 1, 'looking': 1, 'we': 3, 'cannot': 1, 'solve': 1, 'problems': 1, 'kind': 1, 'thinking': 1, 'employed': 1, 'came': 1, 'up': 1, 'them': 1, 'just': 2, 'small': 1, 'positive': 1, 'thought': 1, 'morning': 1, 'change': 1, 'your': 1, 'whole': 1, 'day': 1, 'you': 3, 'get': 2, 'everything': 1, 'want': 2, 'if': 1, 'help': 1, 'enough': 1, 'other': 1, 'people': 1, 'what': 1, 'they': 1}
