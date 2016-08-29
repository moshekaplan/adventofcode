import sys

tokens = (
    'NAME','NUMBER', 'AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT', 'SET_WIRE'
    )


# Tokens
t_NAME  = r'[a-z]+'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Integer value too large", t.value
        t.value = 0
    return t

t_AND   = 'AND'
t_OR    = 'OR'
t_LSHIFT= 'LSHIFT'
t_RSHIFT= 'RSHIFT'
t_NOT   = 'NOT'
t_SET_WIRE = '->'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

num_bits = 16


class Expression:
    def __init__(self, value, operator, operands):
        self.value = value
        self.operator = operator
        self.operands = operands
        
    def __int__(self):
        if self.value is not None:
            return self.value
        
        if self.operator == 'NOT':
            self.value = (~int(self.operands[0])) % 2**num_bits
        elif self.operator == 'AND':
            self.value = (int(self.operands[0]) & int(self.operands[1])) % 2**num_bits
        elif self.operator == 'OR':
            self.value = (int(self.operands[0]) | int(self.operands[1])) % 2**num_bits
        elif self.operator == 'LSHIFT':
            self.value = (int(self.operands[0]) << int(self.operands[1])) % 2**num_bits
        elif self.operator == 'RSHIFT':
            self.value = (int(self.operands[0]) >> int(self.operands[1])) % 2**num_bits
        else:
            raise Exception("Invalid operator: ", self.operator)
        
        return self.value
            
class Wire:
    def __init__(self, name):
        self.name = name
        self.expression = None
        self.value = None
    
    def set_expression(self, expression):
        self.expression = expression        
    
    def __int__(self):
        if self.expression is None:
            raise Exception("Wire was not set! name:", self.name)
        
        if self.value is not None:
            return self.value
        
        self.value = int(self.expression)
        return self.value

wires = {}

def get_wire(name):
    if name in wires:
        return wires[name]
    wire = Wire(name)
    wires[name] = wire
    return wire
                

def p_SET_WIRE(p):
    'statement : expression SET_WIRE NAME'
    wire = get_wire(p[3])
    wire.set_expression(p[1])

def p_expression_binop(p):
    '''expression : expression AND expression
                  | expression OR expression
                  | expression LSHIFT expression
                  | expression RSHIFT expression'''
    p[0] = Expression(None, p[2], (p[1], p[3]))


def p_expression_not(p):
    "expression : NOT expression"
    p[0] = Expression(None, p[1], [p[2]])


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = Expression(p[1], None, None)

def p_expression_name(p):
    "expression : NAME"
    p[0] = get_wire(p[1])

def p_error(p):
    print "Syntax error at '%s'" % p.value

import ply.yacc as yacc
yacc.yacc()


data = open('day7.dat').read()

sample = '''\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

#data = sample


for line in data.split('\n'):
    line = line.strip()
    yacc.parse(line)
    
get_wire('b').value = 16076

print 'a:', int(get_wire('a'))