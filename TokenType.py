from enum import Enum

#TODO make another type for mathematical, relational, and bitwise operators like ValueTypes

class TokenType(Enum):
    #KEY:
    #TOKEN = 0          #raw text version ... extended description
    ID_TOK = 1          #Identifier
    ASSIGN_TOK = 4      #=
    EOS_TOK = 6         #End Of File
    L_PAREN_TOK = 12    #(
    R_PAREN_TOK = 13    #)
    IF_TOK = 14         #if
    ELSE_TOK = 15       #else
    FOR_TOK = 16        #for
    WHILE_TOK = 17      #while
    FUNCTION_TOK = 18   #function
    THEN_TOK = 19       #then
    ENDFUN_TOK = 20     #end of function
    PRINT_TOK = 21      #print
    REPEAT_TOK = 22     #repeat ... while functionality
    UNTIL_TOK = 23      #condition of repeat
    COL_TOK = 24        #:
    DESC_TOK = 31       #description
    END_DESC_TOK = 32   #*/ ... end of description
    SYM_TOK = 33        #symbol ... define functionality
    IMP_TOK = 35        #import
    COMMENT_TOK = 37    #//
    IMPLE_TOK = 38      #implementations
    IS_TOK = 39         #is
    VARS_TOK = 40       #variables
    DEFINE_TOK = 41     #define ... initialization of variable
    OF_TOK = 42         #of ... succeeded by TYPE_TOK
    BEGIN_TOK = 43      #begin
    SET_TOK = 44        #set ... redefine variable
    RETURN_TOK = 49     #return
    TYPE_TOK = 50       #type ... preceded by OF_TOK
    EXIT_TOK = 55       #exit
    GLOB_TOK = 56       #global
    DECL_TOK = 57       #declarations
    UNSIGN_TOK = 58     #unsigned

class OperatorType(Enum):
    ADD_TOK = 1          #+
    MUL_TOK = 2          #*
    SUB_TOK = 3          #-
    DIV_TOK = 4          #/
    REV_DIV_TOK = 5      #\\
    EXP_TOK = 6          #^
    MOD_TOK = 7          #%
    LE_TOK = 8           #<=    
    LT_TOK = 9           #<
    GE_TOK = 10          #>=
    GT_TOK = 11          #>
    EQ_TOK = 12          #==
    NE_TOK = 13          #!=
    BNOT_TOK = 14        #negate
    BAND_TOK = 15        #band
    BOR_TOK = 16         #bor
    BXOR_TOK = 17        #bxor
    L_SHIFT_TOK = 18     #lshift
    R_SHIFT_TOK = 19     #rshift

class ValueType(Enum):
    CONST_TOK = 5       #Some Decimal Number #TODO get rid of dependencies on CONST_TOK
    INT_TOK = 51        #int type
    SHORT_TOK = 52      #short type
    LONG_TOK = 53       #long type
    DOUBLE_TOK = 54     #double or float type
    HEX_TOK = 34        #Some Hexidecimal Number
    STRING_TOK = 36     #Some String
    NONE_TOK = 62       #none type ... used for when a function returns nothing
    BYTE_TOK = 59       #byte type ... can also be used for boolean types


