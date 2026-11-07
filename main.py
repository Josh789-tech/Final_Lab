
from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for
)

from functions import add_supply_record


# ==========================================
# INITIALIZE FLASK APPLICATION
# ==========================================

app = Flask(__name__)

# Secret key used for displaying flash messages.
# For local development only.
app.secret_key = "development-only-secret"


# ==========================================
# FUNCTION 1: DISPLAY LANDING PAGE
# ==========================================

@app.route("/")
def landing():
    """
    Display the welcome page of the Inventory
    Monitoring System.
    """
    return render_template("landing.html")


# ==========================================
# FUNCTION 2: DISPLAY MAIN MENU
# ==========================================

@app.route("/dashboard")
def dashboard():
    """
    Display the main dashboard containing
    the inventory management menu.
    """
    return render_template("dashboard.html")


# ==========================================
# FUNCTION 3: VIEW ALL SUPPLIES
# ==========================================

@app.route("/supplies")
def supplies():
    """
    Display the inventory records page.

    Database retrieval will be implemented
    when the MySQL connection is ready.
    """
    return render_template("supplies.html")


# ==========================================
# FUNCTION 4: ADD NEW SUPPLY
# ==========================================

@app.route("/supplies/add", methods=["GET", "POST"])
def add_supply():
    """
    Display the Add Supply form and validate
    the submitted information.

    GET  - Display the form.
    POST - Validate the submitted data.
    """

    # Check whether the user submitted the form.
    if request.method == "POST":

        try:
            # Call the validation function
            # from functions.py.
            supply = add_supply_record(request.form)

            # Temporarily display validated data
            # in the VS Code terminal.
            print("Validated Supply:", supply)

            # Show a success message on the website.
            flash(
                "Supply information validated successfully. "
                "Database saving is not connected yet.",
                "success"
            )

            # Redirect back to the Add Supply page.
            return redirect(url_for("add_supply"))

        except ValueError as error:

            # Display an error message when
            # the entered information is invalid.
            flash(str(error), "error")

    # Display the Add Supply form.
    return render_template("supply_form.html")


# ==========================================
# FUNCTION 5: DISPLAY STOCK MOVEMENTS
# ==========================================

@app.route("/stock-movements")
def stock_movements():
    """
    Display the stock movement page.

    This page will later monitor incoming,
    outgoing, and discarded supplies.
    """
    return render_template("stock_movements.html")


# ==========================================
# FUNCTION 6: DISPLAY ANALYTICS PAGE
# ==========================================

@app.route("/analytics")
def analytics_page():
    """
    Display the inventory analytics page.

    Inventory statistics and charts will
    be connected in a later development phase.
    """
    return render_template("analytics.html")


# ==========================================
# START FLASK DEVELOPMENT SERVER
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
