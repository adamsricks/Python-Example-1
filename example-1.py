filename = ""
error = False
again = True
answer = ""
    

def main():
    print("NOTE-MAKER 1.0")
    again = True

    while again:
        try:
            filename = input("What would you like the name of your note to be? ")
            file = open(filename + ".txt", "w")
            error = False
        except OSError:
            print("Filename not valid!")
            error = True


        while(error == True):
            try:
                filename = input("What would you like the name of your note to be? ")
                file = open(filename + ".txt", "w")
                error = False
            except OSError:
                print("Filename not valid!")
                error = True

        content = input("What would you like the note to say? ")

        file.write(content)

        file.close()

        file = open(filename + ".txt", "r")

        print()
        print("Here is the contents of your file:")
        print(file.read())
        print()
        file.close()
        answer = False

        while answer == False:
            answer = input("Would you like to make another note? (y/n) ")
            if answer == "y":
                again = True
            elif answer == "n":
                again = False
            else:
                print("Please type 'y' or 'n'")
                answer = False


if __name__ == "__main__":
    main()