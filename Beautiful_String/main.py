import string
alphabet = string.ascii_lowercase
# k = int(input()) #целое число k (0 ≤ k ≤ 109)
# s = input() # непустая строчка S (|S| ≤ 2 ⋅ 105)
k=1
s='h'
dict_list = {}
for q in range(2):#цикл перебора направления
    if q == 1:
        s = s[::-1]
    for i in alphabet:
        if i in s:
            len_count=s.index(i) #индекс буквы
            letter_index = s.index(i) #статичный индекс буквы
            letter = i
        else:  continue
        letter_count = 1 #максимальное число подряд идущих значений
        k_count =k #количество замен  
        while len_count!=(len(s)-1): #цикл перебора буквы x,len_count - индекс y,s[len_count] - значение                               
            if (s[len_count+1]==letter) and (k_count==0): #если следующая буква равна i
                letter_count+=1
                k_count =k
                if letter in dict_list: # есть ли такая буква в словаре?
                    if dict_list[letter] < letter_count:# меньше ли предыдущая длина 
                        dict_list[letter]=letter_count# если да, заменить
                else: 
                    dict_list.setdefault(letter,letter_count)# если такой буквы нет то добавить
            elif (s[len_count+1] != letter) and (k_count>0):
                k_count -=1
                letter_count+=1
                len_count+=1
            elif (s[len_count+1] == letter) and (k_count>0): #если следующая буква равна i
                letter_count+=1
                len_count+=1
            elif (s[len_count+1] != letter) and (k_count == 0): # если следующая буква не равна i, но заменить её можно
                if letter in dict_list: # есть ли такая буква в словаре?
                    if dict_list[letter] < letter_count:# меньше ли предыдущая длина 
                        dict_list[letter]=letter_count# если да, заменить
                        letter_count=0
                        len_count+=1
                    else: len_count+=1
                else: 
                    dict_list.setdefault(letter,letter_count)# если такой буквы нет то добавить
                    letter_count=0
                    len_count+=1
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