from enum import Enum

class TokenType(Enum):
    ID_TOK = 1          #Identifier
    ADD_TOK = 2         #+
    MUL_TOK = 3         #*
    ASSIGN_TOK = 4      #=
    CONST_TOK = 5       #Some Decimal Number
    EOS_TOK = 6         #End Of File
    SUB_TOK = 7         #-
    DIV_TOK = 8         #/
    REV_DIV_TOK = 9     #\\
    EXP_TOK = 10        #^
    MOD_TOK = 11        #%
    LEFT_PAREN_TOK = 12 #(
    RIGHT_PAREN_TOK = 13#)
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
    LE_TOK = 25         #<=
    LT_TOK = 26         #<
    GE_TOK = 27         #>=
    GT_TOK = 28         #>
    EQ_TOK = 29         #==
    NE_TOK = 30         #!=
    DESC_TOK = 31       #description
    END_DESC_TOK = 32   #*/ ... end of description
    SYM_TOK = 33        #symbol ... define functionality
    HCONST_TOK = 34     #Some Hexidecimal Number
    IMP_TOK = 35        #import
    STRING_TOK = 36     #Some String
    COMMENT_TOK = 37    #//
    IMPLE_TOK = 38      #
    IS_TOK = 39         #
    VARS_TOK = 40       #
    DEFINE_TOK = 41     #
    OF_TOK = 42         #
    BEGIN_TOK = 43      #
    SET_TOK = 44        #
    BAND_TOK = 45       #
    BOR_TOK = 46        #
    BXOR_TOK = 47       #
    NEG_TOK = 48        #
    RETURN_TOK = 49     #
    TYPE_TOK = 50       #
    INT_TOK = 51        #
    SHORT_TOK = 52      #
    LONG_TOK = 53       #
    DOUBLE_TOK = 54     #
    EXIT_TOK = 55       #
    GLOB_TOK = 56       #
    DECL_TOK = 57       #
    UNSIGN_TOK = 58     #
    BYTE_TOK = 59       #
    L_SHIFT_TOK = 60    #
    R_SHIFT_TOK = 61    #
