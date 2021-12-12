from difflib import SequenceMatcher
while True:
    try:
        palavra1 = input()
        palavra2 = input()
        seq = SequenceMatcher(None, palavra1, palavra2)
        print(seq.find_longest_match(0, len(palavra1), 0, len(palavra2)).size)
    except EOFError:
        break