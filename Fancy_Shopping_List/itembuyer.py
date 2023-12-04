from shoppinglist import ShoppingList


def getItems():
    items = {}

    while True:
        numOfItems = int(input("How many items will you order today?"))

        if numOfItems >= 1:
            break
        else:
            print("Number of items must be at least 1.")
            pass

    for i in range(numOfItems):
        print(f"item {i + 1}#-")

        nameOfItem = input("Enter food: ")

        while True:
            amountOfItem = float(input("Enter amount of pounds: "))

            if amountOfItem > 0:
                break
            else:
                print("Amount of pounds must be greater than 0.")
                pass

        item_obj = ShoppingList(nameOfItem, amountOfItem)
        items[f"item{i + 1}"] = item_obj

    return items


def displayItems(itemDict):

    total_cost = 0
    print("Amount of pounds must be greater than 0.\n"
          "---------------------------------------")

    for i in itemDict:
        total_cost += itemDict[i].calculate()
        print(f"Item: {itemDict[i].getName()}\n"
              f"Amount Ordered: {itemDict[i].getAmount()} pounds\n"
              f"Price per pound: {itemDict[i].getPrice()}\n"
              f"Price of order: {itemDict[i].calculate()}\n")

    print(f"Total cost: ${total_cost}")


def run():
    displayItems(getItems())

run()
