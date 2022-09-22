import random
def write_txt(password):
    f = open('Passwords.txt','a')
    f.write('\n' + password)
    f.close()
def generate_password(length,platform):
    capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase='abcdefghijklmnopqrstuvwxyz'
    numbers='1234567890'
    specials='!#$%&*+/:;`^_'
    aux=[]
    aux.append(capital[random.randint(0,len(capital)-1)])
    for i in range(length-4):
        aux.append(lowercase[random.randint(0,len(lowercase)-1)])
    for j in range(2):
        aux.append(numbers[random.randint(0,len(numbers)-1)])
    aux.append(specials[random.randint(0,len(specials)-1)])
    password="".join(aux)
    final=f"{platform} : {password}"
    print(final)
    write_txt(final)

length=int(input("How many characters will have the password? "))
platform=input("What website is this password for? ")
generate_password(length,platform)