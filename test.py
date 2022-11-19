try:
    dividend = int(input("Enter the number to divide (the dividend): "))
    divisor = int(input("Enter the number to divide with (the divisor): "
    + "This number needs to be greater than zero: "))

    print("\nThe result of the division is {}".format(dividend/divisor))

except ValueError:
    print('\nInvalid value provided. Both numbers need to be integers')

except ZeroDivisionError:
    print('\nYour second  number is zero. Division by zero is not allowed. ')  

except:
    print("Something (else) went wrong")    