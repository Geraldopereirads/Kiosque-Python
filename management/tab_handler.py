from menu import products


def calculate_tab(consumos: list, **kwargs):
    subtotal = 0

    for product in consumos:
        produto_id = product["_id"]
        quantidade = product["amount"]

        for produto in products:
            if produto["_id"] == produto_id:
                subtotal += produto["price"] * quantidade

    return {"subtotal": f"${round(subtotal, 2)}"}
