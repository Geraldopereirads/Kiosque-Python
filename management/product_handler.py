from menu import products


def get_product_by_id(_id: int, **kwargs: dict) -> dict:

    if not isinstance(_id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == _id:
            return product
    return {}


def get_products_by_type(type: str, **kwargs: list) -> list[dict]:

    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    result = []
    for product in products:
        if product["type"] == type:
            result.append(product)
    return result


def add_product(menu: list, **kwargs):
    if menu:
        new_id: int = max(product["_id"] for product in menu) + 1
    else:
        new_id: int = 1

    product: list = {
        "_id": new_id,
        "description": kwargs.get("description", "Default description"),
        "price": kwargs.get("price", 0),
        "rating": kwargs.get("rating", 0),
        "title": kwargs.get("title", "Default title"),
        "type": kwargs.get("type", "Default type"),
    }

    menu.append(product)
    return product


def menu_report():
    product_count = len(products)

    total_price = sum(product['price'] for product in products)
    average_price = total_price / product_count
    average_price = round(average_price, 2)

    type_counts = {}
    for product in products:
        product_type = product['type']
        if product_type in type_counts:
            type_counts[product_type] += 1
        else:
            type_counts[product_type] = 1

    most_common_type = max(type_counts, key=type_counts.get)

    report = f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"

    return report
