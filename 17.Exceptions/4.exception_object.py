try:
    print(10/0)
# ZeroDivisionError: division by zero
# Here ZeroDivisionError: error type
# division by zero : error message
# We can print error message also:
except ZeroDivisionError as e:
    # error message for ZeroDivisionError is division by zero
    print("error message for ZeroDivisionError is", e)
