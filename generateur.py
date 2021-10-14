import sys
import re
import random

#input = open(sys.argv[1],"r")
input = open("exemple1.asm","r")

#TODO:  Rechercher les registres utilisés et les ignorer à la composition du programme
#       Penser à utiliser une regex pour vérifier si on a pioché un registre déjà utilisé

templatesClear=[
    "xor {dest} {dest2}",
    "sub {dest} {dest2}",
    "mov {dest} 1\ndec {dest2}",
    "mov {dest} 1\nsub {dest2}, 1",
    "xor r1, r1\nmov {dest2}, r1",
    "xor r2, r2\nmov {dest2}, r2",
    "xor r3, r3\nmov {dest2}, r3",
    "xor r4, r4\nmov {dest2}, r4",
    "xor r5, r5\nmov {dest2}, r5",
    "xor r6, r6\nmov {dest2}, r6",
    "xor r7, r7\nmov {dest2}, r7",
    "xor r8, r8\nmov {dest2}, r8",
    "xor r9, r9\nmov {dest2}, r9",
    "xor r10, r10\nmov {dest2}, r10"
]

templatesMove = [
    "mov {dest} {src}",
    "push {src}\npop {dest}",
    "push {src}\npop r1\nmov {dest} r1"
]

templatesAdd = []

templatesSub = []

##Nettoyage de l'input
for line in input:
    if re.match("^\s*$",line):
        pass
    newline=[]
    for character in line:
        if (character == ";"):
            break
        elif (character == "\t" or character == "\n"):
            pass
        else: 
            newline.append(character)
    if ((newline != []) and (newline != ['\n']) and (newline != ['','\n'])):
        newline = "".join(newline)+" \n"


        ##Remplacement ligne par ligne

        if re.match("xor ([a-z0-9]{2,3}), .*\\b\\1",newline):
            print(newline,end="")
            elements = newline.split(" ")
            print(templatesClear[random.randint(0, len(templatesClear)-1)].format(dest = elements[1],dest2 = elements[1]))

        
        elif re.match("mov [a-z0-9]{2,3}, ['\"\\/a-z0-9]{1,}",newline):
            print(newline,end="")
            elements = newline.split(" ")

            print(templatesMove[random.randint(0, len(templatesMove)-1)].format(dest=elements[1],src=elements[2]))

        '''
        elif re.match("add [a-z0-9]{1,3}, [a-z0-9]{1,}", newline):
            print(newline,end="")
            elements = newline.split(" ")
            print(templatesAdd[random.randint(0, len(templatesAdd)-1)].format(elements[2],elements[3]))


        elif re.match("sub [a-z0-9]{1,3}, [a-z0-9]{1,}", newline):
            print(newline,end="")
            elements = newline.split(" ")
            print(templatesSub[random.randint(0, len(templatesSub)-1)].format(elements[2],elements[3]))
        
        
        else:
            print(newline)
        '''