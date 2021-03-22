import sys


def factorial(n):
    res = [None]*500
    res[0] = 1
    res_size = 1

    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x+1

    list1 = []
    i = res_size-1
    while i >= 0:
        list1.append(res[i])
        i = i-1

    return list1


def multiply(x, res, res_size):
    carry = 0
    i = 0
    while i < res_size:
        prod = res[i]*x+carry
        res[i] = prod % 10
        carry = prod//10
        i = i+1

    while(carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size = res_size+1

    return res_size


def main():
    n = int(input())
    list2 = factorial(n)
    print(sum(list2))


if __name__ == '__main__':
    main()
