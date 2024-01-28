def main():
    name = input("Enter your name: ")
    mask1 = float(input("Enter the mask1: "))
    mask2 = float(input("Enter the mask2: "))
    mask3 = float(input("Enter the mask3: "))
    
    total = mask1 + mask2 + mask3
    average = total / 3
    
    print("Name: ", name)
    print("Total marks: ", total)
    print("Average marks: ", average)
    
if __name__ == "__main__":
    main()