"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, num):
        """Start SerialGenerator with a num.
        
        Args:
            start (int): The starting number for the serial generator.
        
        """
        self.num = num
        self.current = num

    def generate(self):
        """
        Generate the next sequential number.

        Returns:
            int: The next sequential number.
        """
        number = self.current
        self.current += 1
        return number 

    def reset(self):
        """Resetting num"""

        self.current = self.num   



serial = SerialGenerator(num=100)
print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102
serial.reset()
print(serial.generate())  # Output: 100
