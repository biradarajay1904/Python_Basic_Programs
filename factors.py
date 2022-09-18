def prime_factor(number):

    prime_factor_list = []

    for i in range(2, number + 1):
        if number % i == 0:
            count = 1
            for j in range(2, (i // 2 + 1)):
                if (i % j == 0):
                    count = 0
                    break
            if (count == 1):
                prime_factor_list.append(i)

    return prime_factor_list


if __name__ == "__main__":
    number = input("Enter the number: ")
    print(prime_factor(int(number)))