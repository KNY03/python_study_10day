# def ten_div(x):
#     return 10 / x
#
# try:
#     print(ten_div(100))
#     print(ten_div(0))
# except ZeroDivisionError:
#     print("Zero Division Error")
#
# print("------")
# try:
#     x = int(input("Please enter a number: "))
#     y = 10 / x
#     print(y)
# except:
#     print("exception occurred")
#
#
# print("------")
# y = [10, 20, 30]
#
# try:
#     index, x = map(int, (input("Please enter a number: ")).split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print("Zero Division Error")
# except IndexError:
#     print("Index Error")
# except:
#     print("exception occurred")
#
# print("------")
#
# y = [10, 20, 30]
#
# try:
#     index, x = map(int, (input("Please enter a number: ")).split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print("Zero Division Error: ", e)
# except IndexError as e:
#     print("Index Error: ", e.args)
# except:
#     print("exception occurred")
#
# print("------")
#
# y = [10, 20, 30]
#
# try:
#     index, x = map(int, (input("Please enter a number: ")).split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print("Zero Division Error: ", e)
# except IndexError as e:
#     print("Index Error: ", e.args)
# else:
#     print(y)
#
# print("------")
#
# y = [10, 20, 30]
#
# try:
#     index, x = map(int, (input("Please enter a number: ")).split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print("Zero Division Error: ", e)
# except IndexError as e:
#     print("Index Error: ", e.args)
# except:
#     print("Exception occurred")
# else:
#     print(y)
# finally:
#     print("finally")
#
# print("------")
#
# y = [10, 20, 30]
#
# try:
#     x = int(input("Please enter a number: "))
#     if x % 3 != 0:
#         raise Exception("Exception occurred")
#     print(x)
#
# except Exception as e:
#     print("Exception: ", e)

class NoTreeMultipleError(Exception):
    def __init__(self):
        super().__init__("3이 배수 아님")

def tree_multiple():
    try:
        x = int(input('3 의 배수 입력: '))
        if x % 3 != 0:
            raise NoTreeMultipleError()
        print(x)
    except Exception as e:
        print(e)


tree_multiple()
