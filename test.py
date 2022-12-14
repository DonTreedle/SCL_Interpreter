from LexicalAnalyzer import LexicalAnalyzer
from Parser import Parser
from Program import Program

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
    #lex = LexicalAnalyzer('welcome.scl')
    #lex.printLex()
    # print(lex.getNextToken().getLexeme())
    # print(lex.getNextToken().getLexeme())
    Parser('welcome.scl').parse().execute()
    #readText()
    #equalityTest()
    #parenTest()

if __name__ == "__main__":
    main()