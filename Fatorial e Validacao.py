def valida_int(pergunta, mim, max):
    x = int(input(pergunta))
    while x < mim or x > max:
        x = int(input(pergunta))
    return x
def fatorial(num):
    """
    Calcular o fatorial
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num +1, 1):
        fat *= i
    return fat
x = valida_int('Digite um valor para calcular o fatorial:', 0, 99999)
print('{}! = {} '.format(x, fatorial(x)))

