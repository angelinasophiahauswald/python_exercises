def even_or_odd(num):
    num = int(num)
    if num % 2 == 0:
        return "even"
    elif num % 2 != 0:
        return "odd"
    else:
        return "entry invalid"

if __name__ == "__main__":
    print("Please insert Number here:")
    num = input()
    print(even_or_odd(num))