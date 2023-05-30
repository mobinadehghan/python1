def save_inventory():
    file = open("l5/aaaa/database.txt")


def edit_item():
    code = input("enter the product code:")
    if code in save_inventory:
        print("1.name")
        print("2.price")
        print("3.count")
        choice = input("choose which field you want to edit:")
        if choice == "1":
            new_name = input("enter the new name:")
            save_inventory[code]["name"]= new_name
        elif choice == "2":
            new_price = float(input("enter the new price:"))
            save_inventory[code]["price"] = new_price
        elif choice =="3":
            new_count = int(input("enter the new count:"))
            save_inventory[code]["count"]=new_count
        else:
            print("invalid selection!")
            return
        
        print("information updated successfully.")
    else:
        print("product code not found!")
        return
def delete_item():
    code= input("enter the product code:")
    if code in save_inventory:
        del save_inventory[code]
        print("the desired has been removed.")
    else:
        print("product code not found!")
def buy_from_stor():
    cart={}
    while True:
        code= input("enter the product code(press enter the complete the purchase):")
        if code == "":
            break
        if code in save_inventory:
            quantity = int(input("enter the desired count:"))
            if save_inventory[code]["count"]< quantity:
                print("insufficient invertory!")
            else:
                item = save_inventory[code]
                item_name = item["name"]
                item_price = item["price"]
                item_count = item["count"]

                if code in cart:
                    cart[code]["quantity"]+=quantity
                else:
                    cart[code]={"name":item_name,"price":item_price,"quantity": quantity}
                save_inventory[code]["count"]-=quantity
                print(f"item'{item_name}'has been added to the shopping cart.")
        else:
            print("product not found!")
    total_price = 0
    print("\n purchase invoice:")
    print("--------")
    for code , item in cart.items():
        item_name = item["name"]
        item_price = item["price"]
        quantity = item["quantity"]
        item_total_price = item_price * quantity
        total_price += item_total_price
        print(f"name:{item_name}")
        print(f"count:{quantity}")
        print(f"price:{item_price}")
        print(f"total_price:{item_total_price}")
        print("--------")
    print(f"total purchase price:{total_price}")
def main_menu():
    print("main menu:")
    print("1.edit product information")
    print("2.product removal")
    print("3.buying from shop")
    print("4.exit")

    choice = input("select:")
    if choice == "1":
        edit_item()
    elif choice == "2":
        delete_item()
    elif choice == "3":
        buy_from_stor()
    elif choice == "4":
        save_inventory()
        