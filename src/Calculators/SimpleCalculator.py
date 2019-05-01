class SimpleCalculator:

    @staticmethod
    def calc_add(first_number, second_number):
        """
        Function to add two numbers
        :param first_number:
        :param second_number:
        :return: the added value
        """
        return first_number + second_number

    @staticmethod
    def calc_subtract(first_number, second_number):
        """
        Function to subtract two numbers
        :param first_number: minuend (first value)
        :param second_number: subtrahend (second value, the number you are subtracting)
        :return: the subtracted value
        """
        return first_number - second_number

    @staticmethod
    def calc_multiply(first_number, second_number):
        """
        Function to multiply two numbers
        :param first_number: value of the first number
        :param second_number: valiue of the second number
        :return:
        """
        return first_number * second_number

    @staticmethod
    def calc_divide(first_number, second_number):
        """
        Function to divide two numbers
        :param first_number: Numerator
        :param second_number: Denominator
        :return:
        """
        if second_number == 0:
            raise Exception(ZeroDivisionError)
        return first_number / second_number

