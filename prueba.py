

def prueba(list, k):
    list.sort(reverse=True)
    _new_list = []
    _new_list_aux = []
    sum = 0
    for idx, num in enumerate(list):
        if idx < k:
            sum = sum + num
            if sum % 2 == 0 or idx == 0:
                _new_list_aux.append(num)
            else:
                if sum % 2 != 0 and idx > 0:
                    sum = sum - num


    print(_new_list_aux)

if __name__ == '__main__':

    list = [9, 4,9, 5,6,8]
    k = 3
    prueba(list, k)