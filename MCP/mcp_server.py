from fastmcp import FastMCP

mcp= FastMCP("MasaiMato")

MENU = {"Masala Dosa": 80, "Idli": 60, "Coffee": 30, "Vada Pav": 25}

ORDER={}
NEXT_ID=1001
@mcp.tool
def get_menu() -> dict:
    """Returns the menu items and prices in INR."""
    return MENU

@mcp.tool
def place_order(item: str, quantity: int, name: str):
    """Places a food order and returns the status and order ID."""
    
    global NEXT_ID
    item= item.title

    if item not in MENU:
        return f"ERROR: {item} not in menu"
    
    total= MENU[item]*quantity
    order_id= f"MM{NEXT_ID}"
    NEXT_ID= NEXT_ID+1

    ORDER[order_id] = {"item": item, "qty": quantity, "name": name, "total": total}
    return f"Success! Order {order_id} placed for {name}. Total: ₹{total}"

def main():
    mcp.run(transport='sse', port=8000)

if __name__ == '__main__':
    main()