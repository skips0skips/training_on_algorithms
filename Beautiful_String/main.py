import string
alphabet = string.ascii_lowercase
# k = int(input()) #целое число k (0 ≤ k ≤ 109)
# s = input() # непустая строчка S (|S| ≤ 2 ⋅ 105)
k=2
#s='zzfffzffffffffffzffffffzfffffzzzfzzzzzzzzzzzzzzzzzzzzzzzzzz'
s = 'kirill'
dict_list = {}
count=k
for _ in range(1):#цикл перебора направления
    for i in alphabet:
        if i in s:
            len_count=s.index(i) #индекс буквы
            letter_index = s.index(i) #индекс буквы 
        else:  continue
        while len_count!=(len(s)-1): #цикл перебора буквы x,len_count - индекс y,s[len_count] - значение
            letter_count = 1 #максимальное число подряд идущих значений
            k_count =k #количество замен            
            if s[len_count]==s[letter_index]:
                for i in range(len_count,len(s)): #i - индекс s[len_count] - значение

                    if i==(len(s)-1): #вызодим ли за пределы строки?
                        if s[letter_index] in dict_list: # есть ли такая буква в словаре?
                            if dict_list[s[letter_index]] < letter_count:# меньше ли предыдущая длина 
                                dict_list[s[letter_index]]=letter_count# если да, заменить
                                len_count=i
                                break
                        else: 
                            dict_list.setdefault(s[letter_index],letter_count)# если такой буквы нет то добавить
                            len_count=i# возвращаем индекс последней буквы
                            break

                    if s[i+1] == s[i]:# если следующая буква равна i
                        #dict_list[s[len_count]] = dict_list.get(s[len_count], 0)+1#надо переделать
                        i+=1
                        letter_count+=1
                    elif (s[i+1] != s[i]) and (k_count!=0): # если следующая буква не равна i, но заменить её можно
                        k_count -= 1
                        i+=1
                        #dict_list[s[len_count]] = dict_list.get(s[len_count], []).append(letter_count)
                        letter_count+=1
                    else: #если заменить нельзя и буква не равна i
                        if s[letter_index] in dict_list: # есть ли такая буква в словаре?
                            if dict_list[s[letter_index]] < letter_count:# меньше ли предыдущая длина 
                                dict_list[s[letter_index]]=letter_count# если да, заменить
                                len_count=i# возвращаем индекс последней буквы
                        else: 
                            dict_list.setdefault(s[letter_index],letter_count)# если такой буквы нет то добавить
                            len_count=i# возвращаем индекс последней буквы
                            break
            else: len_count+=1
print(max(dict_list.values()))                        

#k=5
#zzfffzffffffffffzffffffzfffffzzzfzzzzzzzzzzzzzzzzzzzzzzzzzz
#zz+k = zzzzzzz
# zzz 24 zz 2 z 2 z 2 z 2 z 4
#Первая часть
#1. сохранить какой символ
#2. сохранить начало и конец последовательности 

#Вторая часть
#1.берем цикл по буквам
#2.берем первую последовательность i, вычисляем её длину
#3.с i последовательности в цикле s[len_count] длинною k идем по каждому символу прибавляя счетчик, если встреченная буква равна нашей то к s[len_count] 

#вторая часть
#1.Понять какое расстояние есть между последовательностями
#2.убрать те последовательности длинна которых не покрывается расстоянием k
#3.беру цикл количества обласетей 
#4.беру длинну области и прибавляю к ней пока не дойду до к=0 
#5.записываю максимальную последовательность у этой буквы

#третья часть 
#сравниваю все буквы и выбираю максимальное число 

#{ {a
# }
# }
#мысли: найти такой символ который будет повторятся максимальное количество раз за k шагов 