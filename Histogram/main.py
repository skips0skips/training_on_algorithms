def algorithm(n):
    dict_var={}
    for i in n:
        dict_var[ord(i)] = dict_var.get(ord(i), 0) + 1
    dict_list = sorted(dict_var)
    k =max(dict_var.values())
    for i in reversed(range(1,k+1)):
        index_2=0
        index_1=False
        for j in dict_list:      
            if dict_var[j] >= i:
                index = dict_list.index(j)
                if (index_1==True) and (index-index_2 == 1):
                    print(' '*(0) +'#',end='', sep='')
                    index_2 = index
                elif (index_1==True) and (index-index_2 > 1):
                    print(' '*(index-index_2-1) +'#',end='', sep='')
                    index_2 = index
                else:
                    print(' '*(index) +'#',end='', sep='')
                    index_1=True
                    index_2 = index
        print()
    print(*[chr(i) for i in dict_list], sep='')

def main():
    f = open('input.txt')
    text = f.read().replace('\n', ' ').replace(' ', '')
    f.close()
    algorithm(text)
    
if __name__ == "__main__":
	main()