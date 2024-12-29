sentence = "I am practicing Python programming"


def larg_word(s):
    my_list = s.split(' ')
    largest_num = len(my_list[0])
    temp_word = my_list[0]
    for i in range(1,len(my_list)):
        if len(my_list[i]) > largest_num:
            largest_num = len(my_list[i])
            temp_word = my_list[i]
    return temp_word

def approach2(s):

    
# print(larg_word(sentence))
    