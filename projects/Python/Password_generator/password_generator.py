from platform import platform
import random
def write_txt(password):
    f = open('Passwords.txt','a')
    f.write('\n' + password)
    f.close()
def generate_password(length,platform):
    aux=[]
    aux.append(chr(random.randint(65, 90)))
    for i in range(length-2):
        aux.append(chr(random.randint(97, 122)))
    aux.append('.')
    password="".join(aux)
    final=f"{platform} : {password}"
    print(final)
    write_txt(final)

length=int(input("How many characters will have the password? "))
platform=input("What website is this password for? ")
generate_password(length,platform)