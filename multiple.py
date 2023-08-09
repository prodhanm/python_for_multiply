def multi():
    for num1 in range(11):
        for num2 in range(11):
            product = num1 * num2
            print(f"{product} = {num1} * {num2}")


def main():
    multi()

if __name__ == "__main__":
    main()