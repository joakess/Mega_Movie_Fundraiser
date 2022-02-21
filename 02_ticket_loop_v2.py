# start of Loop

# initialise loop so that it runs at least once


name = ""
count =0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # Get details...
    name = input ("Name:  ")

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

