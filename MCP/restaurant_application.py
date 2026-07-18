MENU = [
    {"item": "chicken_biryani", "price": 250, "available_quantity": 5},
    {"item": "paneer_tikka",    "price": 180, "available_quantity": 0},
    {"item": "veg_fried_rice",  "price": 150, "available_quantity": 8},
    {"item": "butter_naan",     "price": 40,  "available_quantity": 20},
    {"item": "gulab_jamun",     "price": 60,  "available_quantity": 3},
]

def get_menu():
    for m in MENU:
        print(f"Item: {m['item']} || Price: Rs.{m['price']} || Quantity Available: {m['available_quantity']}")

def place_order(item, quantity):
    """Places a food order, validate item exists and quantity is available and returns the status"""
    order_his={}
    for m in MENU:
        if m['item'] == item:
             if m['available_quantity'] >= quantity:
              total= quantity* m['price']
              order_his['item']= item
              order_his['quantity_available']= quantity
              order_his['total_bill']= total
              m["available_quantity"]= m["available_quantity"]-quantity
              order_his['message']= "Thanks for ordering. Hope you have a good day!"
              return order_his

             else:
               order_his['item']= item 
               order_his['quantity_available']= m['available_quantity']
               order_his['message']= "Sorry the product quantity is not available at your needs"
               return order_his

    order_his['message']= f"{item} not available"
    return order_his   

def main():
    get_menu()
    print(place_order("chicken_biryani", 2))
    print(place_order("sushi",3))
    print(place_order("paneer_tikka", 1))
    

if __name__ == "__main__":
    main()