import sys
from LexicalAnalyzer import LexicalAnalyzer

def readText():
    src = open("bitops1.scl")
    while(line := src.readline()):
        print(line)

def equalityTest():
    x = "45.45"
    if (x.isdecimal()):
        print(True)
    else:
        print(False)

def parenTest():
    s = "(hello (world)"
    s = s.replace("(", "( ")
    print(s)

def main():
    LexicalAnalyzer(sys.argv[1])
    #readText()
    #equalityTest()
    #parenTest()

if __name__ == "__main__":
    main()