# i'll try to write a code to calculate cost for the semester

def main():

    a = float(input("How many credits for each course: "))
    b = float(input("Cost per credit for Math: "))
    result1 = a * b
    result1 = round(result1, 2)
    print(f"Total cost for Math: {result1:3.2f}")

    c = float(input("Cost per credit for Physics: "))
    result2 = a * c
    result2 = round(result2, 2)
    print(f"Total cost for Physics: {result1:3.2f}")

    d = float(input("Cost per credit for Computer Science: "))
    result3 = a * d
    result3 = round(result3, 2)
    print(f"Total cost for Computer Science: {result3:3.2f}")

    total_cost = result1 + result2 +result3
    print(f"Total cost for the semester: {total_cost:3.2f}")

if __name__ == "__main__":
    main()