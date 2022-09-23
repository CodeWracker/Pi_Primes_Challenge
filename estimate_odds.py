import math
from num2words import num2words


def calc_prob(len_str, n_digits):
    return 1 - 1/(math.e**(n_digits*(0.1**len_str)))


def find_len(size):
    i = 1
    prob = calc_prob(size, i)
    while (prob < 0.09):
        output = num2words(i)
        max_len = 30
        for j in range(max_len):
            if (j >= len(output)):
                output = output + ' '
        output = output + f' {prob}'
        print(output)
        prob = calc_prob(size, i)
        i = i*10

    output = num2words(i)
    max_len = 30
    for j in range(max_len):
        if (j >= len(output)):
            output = output + ' '
    output = output + f' {prob}'
    print(output)


if __name__ == "__main__":
    print("Estimando probabilidades de encontrar uma sequencia de tamanho 9 em pi")
    find_len(9)

    print("\nEstimando probabilidades de encontrar uma sequencia de tamanho 21 em pi")
    find_len(21)
