


def not_blank (question):
    valid = False

    while not valid:
            response = input (question)

            if response !="":
                return response
            else:
                print ("Sorry - This can't be blank.")



name = not_blank("Name:  ")

