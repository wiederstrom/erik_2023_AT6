class AddingToList():
    def __init__(self):
        self._accepted_input = []
        self._discard_input = []

    def validator(self, user_input):
        for element in user_input:
            try:
                converted_element = int(element)
                if converted_element > 0:
                    self._accepted_input.append(converted_element)
                else:
                    self._discard_input.append(converted_element)
            except ValueError:
                self._discard_input.append(element)

        if (len(self._accepted_input) + len(self._accepted_input) == len(user_input)) and (i > 0 for i in self._accepted_input):
            return self._accepted_input
        else:
            raise ValueError