import math
        
# recebe um número inteiro positivo n.
# e devolve a soma de todos os catetos de algum triângulo retângulo com catetos inteiros.

def soma_hipotenusas(n):
    x = 0
    a = 0
    hip = False    
    while n >= 1:
        hip = é_hipotenusa(n)           
        if hip == True:
            x = x + n
        n = n - 1
        if n == 0:
            return x

# calcula se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro
def é_hipotenusa(n):    
    a = 0
    b = 1
    hip = False
    while b < n and hip == False:
        a = math.sqrt(n ** 2 - b ** 2)
        if a % 1 == 0:
            hip = True
            return hip 
        b = b + 1
        









    
    
    








