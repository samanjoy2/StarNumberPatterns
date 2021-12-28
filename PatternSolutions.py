def pattern1(n):
    for row in range(n):
        for col in range(n):
            print("*", end ="")
        print()

def pattern2(n):
    for row in range(n):
        for col in range(row+1):
            print("*", end ="")
        print()

def pattern3(n):
    for row in range(n):
        for col in range(n-row):
            print("*", end ="")
        print()

def pattern4(n):
    for row in range(n):
        for col in range(row+1):
            print(col+1," ", end ="")
        print()

def pattern5(n):
    for row in range(n-1):
        for col in range(row+1):
            print("*", end ="")
        print()

    for row in range(n):
        for col in range(n-row):
            print("*", end ="")
        print()

def pattern6(n):
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            print("*", end ="")
        print()

def pattern7(n):
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(n-row):
            print("*", end ="")
        print()

def pattern8(n):
    star = 1
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            print("*", end = "")
        star += 2
        print()

def pattern9(n):
    star = n*2 - 1
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            print("*", end = "")
        star -= 2
        print()

def pattern10(n):
    star = 1
    for row in range(n-1):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            print("*", end = "")
        star += 2
        print()

    star = n*2 - 1
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            print("*", end = "")
        star -= 2
        print()

def pattern11(n):
    star = 1
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            print("* ", end = "")
        star += 1
        print()

def pattern12(n):
    star = n
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            print("* ", end = "")
        star -= 1
        print()

def pattern13(n):
    star = n
    for row in range(n-1):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            print("* ", end = "")
        star -= 1
        print()
    
    star = 1
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            print("* ", end = "")
        star += 1
        print()

def pattern14(n):
    star = 1
    for row in range(n-1):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            print("* ", end = "")
        star += 1
        print()
    
    star = n
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            print("* ", end = "")
        star -= 1
        print()

def pattern15(n):
    star = 1
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            if row == 0 or row == n-1 or col == 0 or col == star-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        star += 1
        print()

def pattern16(n):
    star = n
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            if row == 0 or row == n-1 or col == 0 or col == star-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        star -= 1
        print()

def pattern17(n):
    star = 1
    for row in range(n-1):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            if row == 0 or row == n-1 or col == 0 or col == star-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        star += 1
        print()

    star = n
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            if row == n-1 or col == 0 or col == star-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        star -= 1
        print()

def pattern18(n):
    for row in range(n):
        for col in range(n-1):
            if row == 0 or row == n-1 or col == 0 or col == n-2:
                print("*", end ="")
            else:
                print(" ", end="")
        print()

def pattern19(n):
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(n):
            print("*", end ="")
        print()

def pattern20(n):
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(n):
            if row == 0 or row == n-1 or col == 0 or col == n-1:
                print("*", end ="")
            else:
                print(" ", end = "")
        print()

def pattern21(n):
    for row in range(n):
        for col in range(n-row):
            print("*", end ="")
        for space in range(row):
            print(" ", end = "")
        for space in range(row):
            print(" ", end = "")
        for col in range(n-row):
            print("*", end ="")
        print()
    
    for row in range(n):
        for col in range(row+1):
            print("*", end ="")
        for space in range(n-row-1):
            print(" ", end = "")
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            print("*", end ="")
        print()  

def pattern22(n):
    for row in range(n-1):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            print("*", end ="")
        print()
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(n-row):
            print("*", end ="")
        print()

def pattern23(n):
    for row in range(n-1):
        for col in range(row+1):
            print("*", end ="")
        for space in range(n-row-1):
            print(" ", end = "")
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            print("*", end ="")
        print()

    for row in range(n):
        for col in range(n-row):
            print("*", end ="")
        for space in range(row):
            print(" ", end = "")
        for space in range(row):
            print(" ", end = "")
        for col in range(n-row):
            print("*", end ="")
        print()
       
def pattern24(n):
    for row in range(n-1):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            if row == 0 or col == 0 or col == row:
                print("*", end ="")
            else:
                print(" ", end = "")
        print()
    for row in range(n):
        for space in range(row):
            print(" ", end = "")
        for col in range(n-row):
            if row == n-1 or col == 0 or col == n-row-1:
                print("*", end ="")
            else:
                print(" ", end="")
        print()

def pattern25(n):
    for row in range(n-1):
        for col in range(row+1):
            if row == 0 or col == 0 or col == row:
                print("*", end ="")
            else:
                print(" ", end = "")
        print()

    for row in range(n):
        for col in range(n-row):
            if row == n-1 or col == 0 or col == n-row-1:
                print("*", end ="")
            else:
                print(" ", end = "")
        print()

def pattern26(n):
    for row in range(n-1):
        for col in range(row+1):
            if row == 0 or col == 0 or col == row:
                print("*", end ="")
            else:
                print(" ", end = "")
        for space in range(n-row-1):
            print(" ", end = "")
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            if row == 0 or col == 0 or col == row:
                print("*", end ="")
            else:
                print(" ", end = "")
        print()

    for row in range(n):
        for col in range(n-row):
            if row == n-1 or col == 0 or col == n-row-1:
                print("*", end ="")
            else:
                print(" ", end = "")
        for space in range(row):
            print(" ", end = "")
        for space in range(row):
            print(" ", end = "")
        for col in range(n-row):
            if row == n-1 or col == 0 or col == n-row-1:
                print("*", end ="")
            else:
                print(" ", end="")
        print()

def pattern27(n):
    star = n
    for row in range(n-1):
        for space in range(row):
            print(" ", end = "")
        for col in range(star):
            if row == n-1 or col == 0 or col == star-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        star -= 1
        print()
    star = 1
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(star):
            if row == 0 or col == 0 or col == star-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        star += 1
        print()

def pattern28(n):
    num = 1
    for row in range(n):
        for col in range(row+1):
            print(num," ", end ="")
            num += 1
        print()

def pattern29(n):
    num = 1
    for row in range(n):
        for col in range(row+1):
            print(num,"", end ="")
            if num == 1:
                num = 0
            elif num == 0:
                num = 1
        num = 1   
        print()

def pattern30(n):
    for row in range(n):
        for col in range(n-row):
            print(row+1,"", end ="")
        print()

def pattern31(n):
    l = []
    for i in range(n):
        t = []
        for j in range(i+1):
            if j == 0 or j == i:
                t.append(1)
            else:
                t.append(l[i-1][j-1]+l[i-1][j])
        l.append(t)
    
    for row in range(n):
        for space in range(n-row-1):
            print(" ", end = "")
        for col in range(row+1):
            print(l[row][col],"", end="")
        print()

if __name__ == "__main__":
    pattern31(5)