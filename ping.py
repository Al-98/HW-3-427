import platform    
import subprocess  


testing="8.8.8.8"

def bianary(message):

    bi = ''.join(format(ord(i), '08b') for i in message)

    return bi

def spliter(host,bianary):
    for i in bianary:
        if i=='0': 
            ping(host,0)
        else:
            ping(host,1)

def main(host,message):
    bi=bianary(message)
    spliter(host,bi)

def ping(host,bi):
       
    
    if bi==1: 
        command = ['ping', "-l " , '33', host]
    else:
        command = ['ping', "-l " ,'32', host]
    
    return subprocess.call(command) == 0

print(main(testing,"hello world"))
