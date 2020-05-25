import sys

def newMemory(size):
    mem = []
    for i in range(size):
        mem.append(0)
    return mem

def init(filename):
    f = open(filename, "r")
    code = list(f.read())
    f.close()
    execute(code)

def execute(code):
    mPointer = 0
    cPointer = 0
    memory = newMemory(255)
    startLoop = []
    run = True
    while cPointer <= len(code) - 1:
        current = code[cPointer]
        if run:
            if current == '<':
                if mPointer == 0: mPointer = 254
                else: mPointer -= 1

            elif current == '>':
                if mPointer == 254: mPointer = 0
                else: mPointer += 1

            elif current == '+':
                if memory[mPointer] == 255: memory[mPointer] = 0
                else: memory[mPointer] += 1

            elif current == '-':
                if memory[mPointer] == 0: memory[mPointer] = 255
                else: memory[mPointer] -= 1

            elif current == '.': print(chr(memory[mPointer]))

            elif current == ',':
                inp = input("LN " + str(cPointer) + " :")
                try:
                    if int(inp) <= 255 and int(inp) >= 0:
                        memory[mPointer] = int(inp)
                    else:
                        print("Invalid token '" + str(inp) + "'")
                        break
                except:
                    print("Unexpected token '" + str(inp) + "'")
                    break
            
            elif current == '[':
                if memory[mPointer] == 0: run = False
                else: startLoop.append(cPointer)
        
        if current == ']':
            if run:
                cPointer = startLoop[len(startLoop) - 1] - 1
                
            else: 
                run = True
                startLoop.pop(len(startLoop) - 1)
    
        print(startLoop, cPointer, run, current)
        cPointer += 1

def main():
    if len(sys.argv) >= 2:
        init(sys.argv[1])
    else:
        init("main.rd")

if __name__ == "__main__":
    main()
