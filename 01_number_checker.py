#function

def int_check(question, low_num, high_num) :

    error = "please enter a whole number between {} " "and{}" .format(low_num, high_num)

    valid = False
    while not valid:
        #ask user for numver and check is valid
        try:
            response = int(input(question))

            if low_num < response < high_num:
                return response
            else:
                print(error)
        
        except ValueError:
            print(error)

#main routine goes here
age = int_check("Age :", 12,130)
            