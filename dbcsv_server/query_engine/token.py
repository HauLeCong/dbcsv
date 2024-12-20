from enum import Enum    

class ReservedWord(Enum):
    SELECT = "SELECT"
    CREATE = "CREATE"
    FROM = "FROM"
    TABLE = "TABLE"
    WHERE = "WHERE"
    AS = "AS"
    NOT = "NOT"
    NULL = "NULL"
    OR = "OR"
    AND = "AND"
    INT = "INT"
    STRING = "STRING"
    FLOAT = "FLOAT"

class Token(Enum):
    DOT = "."
    PLUS = "+"
    MINUS = "-"
    DIVIDE = "/"
    ASTERISK = "*"
    PERCENT = "%"
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_EQUAL = ">="
    LESS_THAN_EQUAL = "<="
    EQUAL = "="
    COMMA = ","
    DIFFERENT = "<>"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    STRING_LITERAL = "STRING_LITERAL"
    NUMBER_LITERAL = "NUMBER_LITERAL"
    IDENTIFIER = "IDENTIFIER"