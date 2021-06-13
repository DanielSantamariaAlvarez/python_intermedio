def divisors(num):
    assert (num < 0), ' No puedes ingresar numeros menores a cero.' # assert statement
    divisors =[]
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors



def run():
    try:
        num = int(input('Ingresa el número: '))
        print(divisors(num))
        print('terminó mi programa')
    except ValueError:
        print('Unicamente puedes ingresar números')


if __name__ == '__main__':
    run()


