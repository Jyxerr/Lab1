import io


cnt_Symb = 0
cnt_Symb_W_S = 0 #symbols without spaces
cnt_Symb_W_P_M = 0 #symbols without punctuation marks
cnt_Words = 0
cnt_Sentences = 0
i_am_in_skobochki = 0

with io.open('steam_description_data.csv', encoding='utf-8') as f:
    for line in f:
        low_s = line.lower()
        #low_s = low_s.replace('&quot;', '"')
        #low_s = low_s.replace('&gt;', '|')    #&gt; - '>', but we the number of '>' affects the calculation of the number of words so we replace it with '|'

        i = 0

        cnt_Symb += len(low_s)
        for ch in low_s:
                cch = ch

                if cch != ' ':
                    cnt_Symb_W_S +=1

                if not(cch in ',?.!:;-'):
                    cnt_Symb_W_P_M +=1

                if i_am_in_skobochki == 0 and i != 0 and (ord(cch) < ord('a') or ord(cch) > ord('z')) and (ord(cch) < ord('一') or ord(cch) > ord('刏')):
                       if ord(low_s[i-1]) >= ord('a') and ord(low_s[i-1]) <= ord('z'):
                           cnt_Words +=1
                           if cch in '?!' or (cch == '.' and low_s[i-2] != '.'): #abbreviation is a 1 word
                               cnt_Sentences +=1

                       if ord(low_s[i - 1]) >= ord('一') and ord(low_s[i - 1]) <= ord('刏'):
                           cnt_Words +=1
                           if cch in '?.!':
                               cnt_Sentences +=1

                if cch == '<':
                    i_am_in_skobochki +=1
                if cch == '>':
                    i_am_in_skobochki -=1

                i +=1

print('Общее количество символов:', cnt_Symb)
print('Общее количество символов без пробелов:', cnt_Symb_W_S)
print('Общее количество символов без знаков препинания:', cnt_Symb_W_P_M)
print('Общее количество слов:', cnt_Words)
print('Общее количество предложений:', cnt_Sentences)
