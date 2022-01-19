with open('pokemon_full.json') as infile:
    file=infile.read()
    #file1=infile.readlines()
    
    #1
    answer1=len(file) 

    #2
    cleansymbols=0
    for elem in file:
        if elem.isalnum():
            cleansymbols+=1
    answer2=cleansymbols

    #3
    infile.seek(0)
    max_lenline=0 #строка с наибольшим кол-вом символов в описании
    current_nameline='' #текущая строка с именем покемона
    maxnameline='' #строка с именем покемона с самым длинным описанием
    for line in infile:
        if 'name' in line:
            current_nameline=line
        if 'description' in line:
            if len(line)>max_lenline:
                max_lenline=len(line)
                maxnameline=current_nameline
    answer3=maxnameline[12:-2]

    #4
    infile.seek(0)
    current_wordcounter=0 #текущий счетчик слов(пробелов)
    max_wordcounter=0 #максимальное кол-во слов(пробелов) в умении 
    line_with_name_ability='' #строка с названием умения с максимальным кол-вом слов
    flag=False
    for line in infile:
        if 'abilities' in line:
            flag=True
        if ']' in line:
            flag=False
        if flag:
            for sym in line:
                if sym==' ':
                    current_wordcounter+=1
                    if current_wordcounter>=max_wordcounter:
                        max_wordcounter=current_wordcounter
                        line_with_name_ability=line
        current_wordcounter=0
    answer4=line_with_name_ability[6:-1]

print('1)Общее количество символов в файле =',answer1)
print('2)Общее количесто символов без пробелов и знаков препинания =',answer2)
print('3)Покемон с наиболее длинным описанием:',answer3)
print('4)Умение, содержащее наиболбшее количество слов -',answer4)
