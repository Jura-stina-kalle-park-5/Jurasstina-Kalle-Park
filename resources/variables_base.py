import os
import BookSafariPage

BROWSER = "chrome"
current_directory = os.getcwd().replace('\\', '/')
url = f"file:///{current_directory}/jurap.html"

# Login Entry
username_with_numbers = '1234'
username_with_letters = 'StinaKalle'
username_with_special_characters = '!"%&åÄö'
password_short = '1'
password_long = 'p4$$w0rd'

# Page Links
register_link = "data:section:register-section"
login_link = "data:section:login-section"
safari_link = "data:section:safari-section"
tickets_link = "data:section:tickets-section"
cart_link = "data:section:cart-section"

# Home Page Visibility
home_page_text = "id:home-section"

# Alert Message
add_to_cart_success_alert = "Item added to cart!"
checkout_success_alert = "Checkout Summary:"

# Register Page
register_section = "id:register-section"  # use with keyword Element Should Be Visible
register_username_input = "id:reg-username"
register_password_input = "id:reg-password"
register_form = "id:register-form"  # use with keyword Submit Form
register_message = "id:register-message"
register_error_short_password = "Password must be at least 8 characters long."
register_error_no_username_password = "Please enter both a username and password."
register_error_username_already_exists = "Username already exists. Please choose another."
register_success_message = "Registration successful! Redirecting to login..."
register_button = "Register"

# Login Page
login_section = "id:login-section"
login_username_input = "id:login-username"
login_password_input = "id:login-password"
login_form = "id:login-form"
login_username_label = "for:login-username"  
login_password_label = "for:login-password"  
login_username_field = "id:login-username"  
login_password_field = "id:login-password"  
login_button = "Login"  
login_message = "id:login-message"
logout_link = "id:logout-link"

# Buy Tickets
tickets_section = "id:tickets-section"
tickets_type_select = "id:ticket-type"
tickets_adult_ticket = "Adult"
tickets_child_ticket = "Child"
tickets_senior_ticket = "Senior"
tickets_category_select = "id:ticket-category"
tickets_vip_ticket = "VIP"
tickets_regular_ticket = "Regular"
tickets_ticket_quantity = "id:ticket-quantity"
tickets_form = "id:ticket-form"
tickets_button = "Add to Cart"

# Cart Page
cart_section = "id:cart-section"
cart_items = "css:#cart-details ul"
cart_checkout_button = "id:checkout-button"
