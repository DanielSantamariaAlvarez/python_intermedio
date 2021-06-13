def run():
    my_list = [1,'hello', True, 4.5]
    my_dict = {'firstname':'Daniel','lastname':'Santamaría'}

    super_list = [
        {'firstname':'Daniel','lastname':'Santamaría'},
        {'firstname':'Daniel','lastname':'Santamaría'},
        {'firstname':'Daniel','lastname':'Santamaría'},
        {'firstname':'Daniel','lastname':'Santamaría'},
    ]

    super_dict = {
        'natural_nums': [1,2,3,4],
        'integer_nums': [-1,-2,-3,-4],
        'floating_nums': [1.1, 2.2, 3.3, 4.4]
    }

    for key, value in super_dict.items():
        print(key, '-' ,value)


def list_comprenhension():
    square = [i**2 for i in range(1,101) if i %3 != 0]
    """ for i in range(1,101):
        if i**2 % 3 !=0:
            square.append(i**2) """    
    print(square)
    print(len(square))

def dict_comprenhension():
    my_dict = {}
    for i in range(1,101):
        my_dict[i] = i**2

    print(my_dict)
    

if __name__ == '__main__':
    dict_comprenhension()
