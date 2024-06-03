from collections import Counter

f = open("../lalka_stripped.txt", "r")

lines = f.readlines()

f.close()

f = open("../medium_quotes.txt", 'w', encoding='utf-8')
result: list[str] = []

rep: set[str] = set()

chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'ą', 'ę', 'ć', 'ó', 'ś', 'ź', 'ż', ',', '.', '?', ':', ';', '1', '2', '3', '4', '5', '6',
         '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~'}

print(chars)

bad_chars = ['«', '»', 'ç', 'ö', '*']

for line in lines:

    sentences = line.split('.')

    for sentence in sentences:
        if len(sentence) > 9 and len(sentence) < 70:
            sentence = sentence.strip("— \n") + "\n"
            sentence = sentence.replace("—", "-")
            sentence = sentence.replace('…', "...")
            sentence = sentence.replace("”", "\"")
            sentence = sentence.replace("„", "\"")

            ctr = Counter(sentence)

            if ctr["\""] % 2 != 0:
                sentence = sentence.replace("\"", "")

            if any(char in sentence for char in bad_chars):
                continue

            words = sentence.split()

            if len(words[-1]) == 1 and words[-1].isupper():
                print(sentence)

                continue

            if sentence not in rep:
                result.append(sentence)

                for char in sentence:
                    chars.add(char.lower())

            rep.add(sentence)

f.writelines(result)

print(sorted(list(chars)))

f.close()



