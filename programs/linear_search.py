# write a program to find whether the element in the list and display its index


def main():
    mylist = [10, 21, 11, 22, 13, 19]
    number = int(input("Enter the number to be search: "))
    if not is_number_present(number, mylist):
        print("The element not found")


def is_number_present(number, mylist):
    """ method to check whether number is present in list """
    for item in range(len(mylist)):
        if number == mylist[item]:
            print("The number found in given list at position {} ".format(item))
            return True
    return False


if __name__ == "__main__":
    main()
