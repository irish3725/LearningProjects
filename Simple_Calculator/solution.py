#!/bin/python3

import os

## Define Calculator Class
class Calculator:
   
    ## initializing method
    ## this method is called every time new instance of
    ## this class is created
    def __init__(self):
        return

    ## takes a string as an input and parses it
    ## there is probably a better way to parse this,
    ## but this is how I decided to do it
    def parse(self, expression):
        # split the text into an easy to manage list
        expr = []

        # chop the string up until it is empty
        while len(expression) > 0:
            index = len(expression)
            # there is definately a better way to do this
            # get first index of an operator
            if '+' in expression:
                index = min(index, expression.index('+'))
            if '-' in expression:
                index = min(index, expression.index('-'))
            if '*' in expression:
                index = min(index, expression.index('*'))
            if '/' in expression:
                index = min(index, expression.index('/'))
            if '%' in expression:
                index = min(index, expression.index('%'))

            # if we found an operator, continue parsing
            if index != len(expression):
                # get string before next operator
                expr.append(expression[0:index])
                # remove stuff we put in expr list
                expression = expression[index:]
                # put operator in our list
                expr.append(expression[:1])
                # remove operator from our remaining expression
                expression = expression[1:]
            # if we didn't find an operator, append the last value
            else:
                expr.append(expression)
                expression = ''

        # calculate our list expression
        try:
            solution = self.calculate(expr)
        # if something breaks, tell the user and then continue
        except:
            solution = 'I don\'t know how to do that!'
        return(solution)

    ## calculates an expression given as a list
    def calculate(self, expr):
        # pull out the first value
        solution = int(expr[0])
        expr = expr[1:]
        # parse till list is empty
        while len(expr) > 0:
            if expr[0] == '+':
                solution = solution + int(expr[1])
                expr = expr[2:]
            elif expr[0] == '-':
                solution = solution - int(expr[1])
                expr = expr[2:]
            elif expr[0] == '*':
                solution = solution * int(expr[1])
                expr = expr[2:]
            elif expr[0] == '/':
                solution = solution / int(expr[1])
                expr = expr[2:]
            elif expr[0] == '%':
                solution = solution % int(expr[1])
                expr = expr[2:]
                
                
        return(solution)

    ## Simple text user interface for the calculator
    def ui(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        # print first message to user
        print('Please enter an expression and I will do my best to solve it. (I am simple and my order of operations is left to right, and the only operators I know are +, -, *, /, and %.)\nExample: 1 + 1\nEnter q to quit.')
    
        # to store user input
        entry = ''

        # list of things the user can use to quit the calculator
        exit_strings = ['q', 'quit', 'exit', 'end']

        # loop till we are told not to
        while True:
            
            # get input
            entry = input(' > ')
            if entry in exit_strings:
                os.system('cls' if os.name == 'nt' else 'clear')
                return

            # store unchanged input for later
            o_entry = entry

            # remove silly whitespace and commas            
            entry = entry.replace(',', '').replace(' ', '').replace(')', '').replace('(', '')

            # call our calculating function
            solution = self.parse(entry)

            if solution == 'I don\'t know how to do that!':
                print(solution)
            else:
                print(o_entry, '=', solution)

        return
    
if __name__ == '__main__':
    # create a new instance of Calculator
    cal = Calculator()
    # call cal's ui function
    cal.ui()

