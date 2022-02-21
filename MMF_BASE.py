

# checks that ticket code is not blank
def not_blank (question):
    valid = False

    while not valid:
        response = input (question)

        if response !="":
            return response
        else:
            print ("Sorry - this can't be blank,"
                    "please enter your name")

 # checks number is an integer between low / high
def int_check(question, low_num, high_num) :

    error = "please enter a whole number between {} " "and{}" .format(low_num, high_num)

    valid = False
    while not valid:
        #ask user for numver and check is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)
        
        except ValueError:
            print(error)

name = ""
count =0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # Get details...
    name = not_blank("Name: ",)

    age = int_check("how old are you? ", 12, 130)

    if count <4:
        print ("you have {} seats "
        "left".format (MAX_TICKETS - count))
    else:
        print("*** There is ONE seat left!! ***")



    count += 1
    print ()

    if count == MAX_TICKETS:
        print ("You have sold all the available tickets!")

    else:
        print("you have sold {} tickets.   \n"
        "there is {} ticket still available"
        .format (count, MAX_TICKETS - count))




# thing 1

# thing 2


