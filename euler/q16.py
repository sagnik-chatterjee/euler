def main():
    m = int(input())
    n = int(input())
    h = m ** n
    sum1=0
    while(h!=0):
        k=h%10
        sum1+=k
        h=h//10
    print(sum1)

main()
