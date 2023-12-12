class AddingToList():
    '''List generator for integers'''
    '''Method for validating input'''
    def __init__(self):
        '''List of validated integers'''
        self._accepted_input = []
        '''Invalid input'''
        self._discard_input = []

    def validator(self, user_input):
        '''Checks if elements in list is a positive integer, discards invalid input'''
        for element in user_input:
            try:
                converted_element = int(element)
                if converted_element > 0:
                    self._accepted_input.append(converted_element)
                else:
                    self._discard_input.append(converted_element)
            except ValueError:
                self._discard_input.append(element)

        '''Checks if list of accepeted integers is of correct length, compared to discard input and total lengt of input  '''
        if (len(self._accepted_input) + len(self._accepted_input) == len(user_input)) and (i > 0 for i in self._accepted_input):
            return self._accepted_input
        else:
            raise ValueError