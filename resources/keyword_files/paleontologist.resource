*** Settings ***
Library          SeleniumLibrary
Variables        ${EXECDIR}/resources/variables_base.py

*** Keywords ***
I am shown a summary when I checkout
    Click Button    ${cart_checkout_button}
    Handle Alert
