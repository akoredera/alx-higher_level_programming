#!/usr/bin/python3
'''My integer task'''


class MyInt(int):
    '''My int inherits from int and is a rebel'''

    def __ne__(self, value):
        '''method override its parent method return __eq_ method'''
        return super().__eq__(value)

    def __eq__(self, value):
        '''method override its parent method return __ne__ method'''
        return super().__ne__(value)
