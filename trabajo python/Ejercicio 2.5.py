a=[2,4,1,4,5,1]


def mult(b):
    mul=1
    for a in b:
        mul=mul*a
    ver1(mul)

def sum(b):
    sum=0
    for a in b:
        sum=sum+a
    ver2(sum)

def ver1(vis):
    print(f'La multiplicacion da {vis}')
def ver2(vis):
    print(f'La suma da {vis}')

mult(a)
sum(a)


