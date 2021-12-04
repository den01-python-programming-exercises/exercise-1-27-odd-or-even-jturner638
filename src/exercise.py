def main():
    #write your code below this line
    number = int(input("Give a number:"))

    if number % 2 == 0:
        print("Number {} is even.".format(number))
    else:
        print("Number {} is odd.".format(number))

if __name__ == '__main__':
    main()
