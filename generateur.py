import sys
import re
import random

#input = open(sys.argv[1],"r")
input = open("exemple1.asm","r")

templatesClear=[
    "xor {}, {}",
    "sub {}, {}",
    "mov {}, 1\ndec {}",
    "mov {}, 1\nsub {}, 1",
    "xor r1, r1\nmov {}, r1",
    "xor r2, r2\nmov {}, r2",
    "xor r3, r3\nmov {}, r3",
    "xor r4, r4\nmov {}, r4",
    "xor r5, r5\nmov {}, r5",
    "xor r6, r6\nmov {}, r6",
    "xor r7, r7\nmov {}, r7",
    "xor r8, r8\nmov {}, r8",
    "xor r9, r9\nmov {}, r9",
    "xor r10, r10\nmov {}, r10"
]

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
            print(templatesClear[random.randint(0, len(templatesClear)-1)].format(elements[2],elements[2]))

        '''
        elif re.match("mov [a-z0-9]{2,3}, ['\"\\/a-z0-9]{1,}",newline):
            print("Move",newline)


        elif re.match("add [a-z0-9]{1,3}, [a-z0-9]{1,}", newline):
            print("Add", newline)


        elif re.match("sub [a-z0-9]{1,3}, [a-z0-9]{1,}", newline):
            print("Sub", newline)


        else:
            print("Autre", newline)
        '''
