#!/usr/bin/python3
'''My integer task'''


class MyInt(int):

    def __ne__(self, value):
        return super().__eq__(value)

    def __eq__(self, value):
        return super().__ne__(value)
