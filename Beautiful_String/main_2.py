import string

def send_to_dict(dict_list,letter,letter_count):
    if letter in dict_list: # есть ли такая буква в словаре?
        if dict_list[letter] < letter_count:# меньше ли предыдущая длина 
            dict_list[letter]=letter_count# если да, заменить
        #else:         
    else:
        dict_list.setdefault(letter,letter_count)# если такой буквы нет то добавить

alphabet = string.ascii_lowercase
k = int(input()) #целое число k (0 ≤ k ≤ 109)
s = input() # непустая строчка S (|S| ≤ 2 ⋅ 105)
# k=2
# s='abcaz'
dict_list = {}
for letter in alphabet: #letter - буква которая проверяется
    if letter not in s:
        continue
    else:
        index_i=s.index(letter) #индекс буквы
        iter_count = index_i
        k_count=0
        start_point = index_i #точка старта
        flag = True
        flag_2=False
        while iter_count < len(s)+1:

            if (start_point - k >= 0) and (flag == True): #можно добавить флаг
                k_2=k
                while k_2!=-1:
                    if s[start_point] != letter and (k_2>0):
                        k_2-=1
                        start_point -=1
                    elif (s[start_point] == letter) and (k_2>0):
                        start_point -=1
                    elif (s[start_point] == letter) and (k_2 ==0):
                        start_point -=1
                    elif (s[start_point] != letter) and (k_2 ==0):
                        start_point +=1
                        k_2 = -1
                iter_count = start_point
                k_count=k#0
                flag =False
                flag_2=False

            elif (start_point - k < 0) and (flag == True):
                k_count= k#abs(start_point - k)+1
                start_point = 0
                iter_count = 0
                flag =False
                flag_2=False
            
            if iter_count==len(s):
                if flag_2 == False:
                    #нужно прекратить поиск и выйти из цикла какой-нибудь брейк
                    distance = stop_point - start_point # +1 нужно т.к. счет от нуля
                    send_to_dict(dict_list,letter,distance)
                break
            elif (s[iter_count] != letter) and (flag_2==True):
                iter_count+=1
                continue
            elif (s[iter_count] == letter) and (flag_2==True):
                flag = True
                start_point=iter_count
                continue
            elif s[iter_count] == letter:
                iter_count+=1
                stop_point = iter_count 
            elif (s[iter_count] == letter) and (k_count == 0):
                iter_count+=1
                stop_point = iter_count     
            elif (s[iter_count] != letter) and (k_count>0):
                iter_count+=1
                k_count -=1
                stop_point = iter_count
            elif (s[iter_count] != letter) and (k_count == 0):
                #доделалась ячейка поиска
                distance = stop_point - start_point # +1 нужно т.к. счет от нуля
                send_to_dict(dict_list,letter,distance)
                flag_2=True
print(max(dict_list.values()))  