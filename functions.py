
from datetime import datetime


# FUNCTION 1: Validate supply information.
def validate_supply(name, category, quantity, price, expiry_date):
    """
    Validate the information entered by the user.

    Returns a dictionary containing the validated data.
    Raises ValueError when an input is invalid.
    """

    # Validate required text fields.
    name = name.strip()
    category = category.strip()

    if not name or not category:
        raise ValueError(
            "Supply name and category are required."
        )

    # Validate quantity.
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a whole number.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    # Validate price.
    try:
        price = float(price)
    except (ValueError, TypeError):
        raise ValueError("Price must be a valid number.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    # Validate expiration date.
    try:
        expiry_date = datetime.strptime(
            expiry_date, "%Y-%m-%d"
        ).date()
    except (ValueError, TypeError):
        raise ValueError(
            "Expiration date must be in YYYY-MM-DD format."
        )

    return {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "expiry_date": expiry_date
    }


# FUNCTION 2: Process a new supply.
def add_supply_record(form_data):
    """
    Validate the submitted supply information.

    Database insertion will be connected through
    database.py after the MySQL setup is complete.
    """

    return validate_supply(
        name=form_data.get("name", ""),
        category=form_data.get("category", ""),
        quantity=form_data.get("quantity", ""),
        price=form_data.get("price", ""),
        expiry_date=form_data.get("expiry_date", "")
    )

