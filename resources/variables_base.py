import os
from resources.page_object_models.BuyTicketsPage import *
from resources.page_object_models.CartPage import *
from resources.page_object_models.BookSafariPage import *
from resources.page_object_models.RegisterPage import *
from resources.page_object_models.LoginPage import *

BROWSER = "chrome"
current_directory = os.getcwd().replace('\\', '/')
url = f"file:///{current_directory}/website/jurap.html"

# Login Entry
username_with_numbers = '1234'
username_with_letters = 'StinaKalle'
username_with_special_characters = '!"%&åÄö'
password_short = '1'
password_long = 'p4$$w0rd'

# Page Links
safari_link = "data:section:safari-section"
tickets_link = "data:section:tickets-section"
cart_link = "data:section:cart-section"
register_link = "data:section:register-section"
login_link = "data:section:login-section"

# Home Page Visibility
home_page_text = "id:home-section"

# Alert Message
add_to_cart_success_alert = "Item added to cart!"
