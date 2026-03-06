class AgeException(Exception):
    def __init__(self, msg1, msg2):
        self.message1 = msg1
        self.message2 = msg2


def input_age():
    age = int(input("Please enter your age: "))

    if age < 0:
        raise AgeException("Your age cannot be negative.", "!!!!")
    elif age > 150:
        raise AgeException("Can you live greater than 150?", "hum...")
    else:
        return age

if __name__ == '__main__':
    try:
        age = input_age()
    except AgeException as e:
        print(e.args)
    else:
        print(age)