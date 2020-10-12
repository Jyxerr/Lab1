symbols = 0
symbols_no_spaces = 0
symbols_no_punctuation = 0
words = 0
sentences = 0
is_in_brackets = False

with open('steam_description_data.csv', encoding='utf-8') as f:
    for line in f:

        # All letters are lowered to make it easier to work with words and sentences
        low_string = line.lower()

        i = 0

        symbols += len(low_string)
        for ch in low_string:

                if ch != ' ':
                    symbols_no_spaces += 1

                if not(ch in ',?.!:;-'):
                    symbols_no_punctuation += 1

                if (not(is_in_brackets) and i != 0 and
                    (ord(ch) < ord('a') or ord(ch) > ord('z')) and
                    (ord(ch) < ord('一') or ord(ch) > ord('刏'))):
                    # Sentence or word ended

                        # Counting words and sentences with letters:
                        if (ord(low_string[i-1]) >= ord('a') and
                            ord(low_string[i-1]) <= ord('z') and
                            not(ch == '.' and low_string[i-2] != '.')):
                                # Abbreviation is a 1 word
                                words += 1

                                if ch in '?!':
                                    sentences += 1
                                # Abbreviation is 0 sentences
                                if ch == '.':
                                    if i+2 < len(low_string):
                                        if low_string[i+2] != '.':
                                            sentences += 1
                                    else:
                                        sentences += 1

                        # Counting words and sentences with hieroglyphs:
                        if ord(low_string[i-1]) >= ord('一') and ord(low_string[i-1]) <= ord('刏'):
                           words += 1
                           if ch in '?.!':
                               sentences += 1

                if ch == '<':
                    is_in_brackets = True
                if ch == '>':
                    is_in_brackets = False

                i +=1

print('Общее количество символов:', symbols)
print('Общее количество символов без пробелов:', symbols_no_spaces)
print('Общее количество символов без знаков препинания:', symbols_no_punctuation)
print('Общее количество слов:', words)
print('Общее количество предложений:', sentences)
