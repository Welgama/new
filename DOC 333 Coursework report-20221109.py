import random as gen

# value_index = 1
random_no = str(gen.randint(1, 6)) + str(gen.randint(1, 6)) + str(gen.randint(1, 6)) + str(gen.randint(1, 6))
name = input("Enter Your Name: ")

print("\t\t\t HI", name, "Welcome to GameInt")

# print(random_no)
print()
print("Number to Guess - XXXX ", end=" ")
print("\t\t\t\t\t\t\t\tColor Mapping: ")
print("\t\t\t\t\t\t\t\t\t\t 1-White 2-Blue 3-Red")
print("\t\t\t\t\t\t\t\t\t\t 4-Yellow 5-Green 6-Purple")
print()

ans = []


def game():
    count = 1  #count untill 8th attempts
    m_cnt = 100
    print("Attempt\t\t\t\t\t Guess\t\t\t\t Result ")
    while 1:
        print("__________________________________________________________________")

        while True:
            temp_count = 0
            userAns = input(f"{count}: \t\t\t\t\t\t ")
            on_count = 0
            for index in userAns:
                if index == '0':
                    on_count += 1
            if on_count == 4:
                print()
                print(".....Terminate Game Int....")
                exit()
                break
            for index in userAns:
                temp = int(index)
                if 0 < temp < 7:
                    temp_count += 1
            if temp_count == 4 and len(userAns) == 4:
                break
            else:
                print()
                print("!!!!Wrong Input Please Enter Again.....")
        value_index = 0

        check_pre = 0
        for index in userAns:
            check = True
            if random_no[value_index] == index:
                ans.insert(value_index, '1')  # check 1 val
                check_pre += 1
                check = False
            else:
                if check_pre > 1:
                    for k_val in range(check_pre, 4):
                        if index == random_no[k_val]:
                            ans.insert(value_index, '0')
                            check = False
                else:
                    for f in random_no:
                        if index == f:
                            ans.insert(value_index, '0')
                            check = False
                            break
                if check:
                    ans.insert(value_index, '.')

            value_index += 1

        print("\t\t\t\t\t\t\t\t\t\t\t", end=' ')
        win = 0
        for v in range(0, 2):
            print(ans[v], end=" ")
        print()
        print("\t\t\t\t\t\t\t\t\t\t\t", end=' ')
        for v in range(2, 4):
            print(ans[v], end=" ")
        for c_val in ans:
            if c_val == '1':
                win += 1

        if win == 4:
            print()
            print("Congratulations !!!!! You have won the game…")
            print("You have scored", m_cnt, "points.")
            break

        ans.clear()
        if count == 8:
            print()
            print("Your Attempts are Over !!!!! Try again…")
            break
        count += 1
        m_cnt -= 12.5
        print()


while 1:
    game()
    ano_g = input("Do you want to play another game (Yes/No) ? : ")
    if ano_g.lower() == "no":
        exit()
        break
    elif ano_g.lower() == "yes":
        ans.clear()

        print("\t\t\t HI", name, "Welcome to GameInt")
        print("Number to Guess - XXXX ", end=" ")
        print("\t\t\t\t\t\t\t\tColor Mapping: ")
        print("\t\t\t\t\t\t\t\t\t\t 1-White 2-Blue 3-Red")
        print("\t\t\t\t\t\t\t\t\t\t 4-Yellow 5-Green 6-Purple")
        random_no = str(gen.randint(1, 6)) + str(gen.randint(1, 6)) + str(gen.randint(1, 6)) + str(gen.randint(1, 6))
        print()
