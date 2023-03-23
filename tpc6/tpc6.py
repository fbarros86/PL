import ply.lex as lex

tokens= (
    'INT',
    'NOME_VARIAVEL',
    'SEMICOLON',
    'FUNCTION',
    'FUNCTION_NAME',
    'PAROPEN',
    'PARCLOSE',
    'ARGUMENT',
    'COMMA',
    'CURVPAROPEN',
    'CURVPARCLOSE',
    'EQUALS',
    'NUMBER',
    'WHILE',
    'COMPARATORS',
    'OPERATORS',
    'PROGRAM',
    'FOR',
    'IN',
    'RANGE',
    'IF',
    'RECPAROPEN',
    'RECPARCLOSE'
)

def t_ignore_SINGLECOMMENT(t):
    r'\/\/.*?\n'
    pass

def t_ignore_COMMENTS(t):
    r'\/\*(.|\n)*?\*\/'
    pass


def t_INT(t):
    r'\bint\b'
    return t

def t_PROGRAM(t):
    r'program\s+([a-zA-Z_][\w_]*)'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_FUNCTION(t):
    r'\bfunction '
    return t

def t_FUNCTION_NAME(t):
    r'[a-zA-Z_][\w_]*(?=\()'
    return t

def t_PAROPEN(t):
    r'\('
    return t

def t_PARCLOSE(t):
    r'\)'
    return t

def t_ARGUMENT(t):
    r'[a-zA-Z_][\w_]*(?=\,|\))'
    return t

def t_COMMA(t):
    r'\,'
    return t

def t_CURVPAROPEN(t):
    r'{'
    return t

def t_CURVPARCLOSE(t):
    r'}'
    return t

def t_EQUALS(t):
    r'\='
    return t

def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_WHILE(t):
    r'\bwhile\b'
    return t

def t_COMPARATORS(t):
    r'(>|<|==|>=|<=)'
    return t

def t_OPERATORS(t):
    r'(\+|\-|\*|\/)'
    return t


def t_FOR(t):
    r'\bfor\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_RANGE(t):
    r'\[\d+\.\.\d+\]'
    return t

def t_IF(t):
    r'if'
    return t

def t_RECPAROPEN(t):
    r'\['
    return t

def t_RECPARCLOSE(t):
    r'\]'
    return t

def t_NOME_VARIAVEL(t):
    r'[a-zA-Z_][\w_]*'
    return t


t_ignore=' \t\n'




def t_error(t):
    print(f"Invalid token: {t.value}")
    t.lexer.skip(1)

lexer=lex.lex()

data = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""
lexer.input(data)
while tok:= lexer.token():
    print(tok)