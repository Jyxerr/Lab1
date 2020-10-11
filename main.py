import io

cntSymb = 0
cntSymbWS = 0 #symbols without spaces
cntSymbWPM = 0 #symbols without punctuation marks
cntWords = 0
cntSentences = 0
iaminskobochki = 0

with io.open('steam_description_data.csv', encoding='utf-8') as f:
    for line in f:
        lows = line.lower()
        #lows = lows.replace('&quot;', '"')
        #lows = lows.replace('&gt;', '|')    #&gt; - '>', but we the number of '>' affects the calculation of the number of words so we replace it with '|'

        i = 0

        cntSymb += len(lows)
        for ch in lows:
                cch = ch

                if cch != ' ':
                    cntSymbWS += 1

                if cch != ',' and cch != '?' and cch != '.' and cch != '!' and cch != ':' and cch != ';' and cch != '-':
                    cntSymbWPM += 1

                if iaminskobochki == 0 and i != 0 and (ord(cch) < ord('a') or ord(cch) > ord('z')) and (ord(cch) < ord('一') or ord(cch) > ord('刏')):
                       if ord(lows[i-1]) >= ord('a') and ord(lows[i-1]) <= ord('z'):
                           cntWords += 1
                           if cch == '!' or cch == '?' or (cch == '.' and lows[i-2] != '.'): #abbreviation is a 1 word
                               cntSentences += 1

                       if ord(lows[i - 1]) >= ord('一') and ord(lows[i - 1]) <= ord('刏'):
                           cntWords += 1
                           if cch == '!' or cch == '?' or cch == '.':
                               cntSentences += 1

                if cch == '<':
                    iaminskobochki += 1
                if cch == '>':
                    iaminskobochki -= 1

                i += 1

print('Общее количество символов:', cntSymb)
print('Общее количество символов без пробелов:', cntSymbWS)
print('Общее количество символов без знаков препинания:', cntSymbWPM)
print('Общее количество слов:', cntWords)
print('Общее количество предложений:', cntSentences)