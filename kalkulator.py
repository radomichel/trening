print('Witam w prostym kalkulatorze')
wynik=0
x = int(input('Podaj dwie liczby:\n'))
y = int(input())
def suma(x,y):
    wynik=x+y
    return wynik
def iloczyn(x,y):
    iloczyn=x*y
    return iloczyn
def odejmowanie (x,y):
    roznica=x-y
    return roznica
print('Suma tych liczb to: ', suma(x,y))
print('Roznica tych liczb wynosi: ', odejmowanie(x,y))
print ('iloczyn tych liczb wynosi: ',iloczyn(x,y))
