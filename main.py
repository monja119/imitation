import numpy as np
import pandas as pd
from sympy import Symbol, limit,  oo

class Function:
    def __init__(self, function, variable, accumulation, *lateral):

        self.var = variable
        self.func = function

        # checking the variable
        try:
            self.var_checker(variable)
            self.lateral_checher(lateral)
            print('[ OK ] Variable')
            print('[ OK ] Lateral')

            limit = self.calculate(function, variable, accumulation, *lateral)
            print(limit)

        except TypeError as e:
            print(e)

        # main function


    def set_variable(self,var):
        self.var = var

    def set_function(self, function):
        self.func = function

    def var_checker(self, var):
        if len(var) != 1:
            raise TypeError('The length of the variable should be 1')
        elif isinstance(var, str) and not str(var).isalpha():
            raise TypeError(f'The variable {var} of a function should be a letter')
        else:
            return 0

    def lateral_checher(self, lateral):
        match len(lateral):
            case 0:
                pass
            case 1:
                if lateral[0] not in ['+', '-']:
                    raise TypeError(f'The lateral {lateral[0]} of a function should be  "+" or "-" ')
            case _:
                raise TypeError('The length of the lateral should be 1 and it should be "+" or "-" ')

    def calculate(self, function, variable, accumulation, *lateral):
        symbol_variable = Symbol(variable)
        function = str(function).replace(variable, 'symbol_variable')
        function = eval(function)
        return limit(function, symbol_variable, accumulation)


function = Function('4 * n * n ', 'n', oo)


