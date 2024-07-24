import streamlit as st

# Define a function to display credit card details
def display_credit_card(name, image_url, column):
    with column:
        st.image(image_url, width=400)
        st.caption(name)

# Credit card details
credit_cards = [
    {
        "name": "Credit Card 1",
        "image_url": "card_1.png"
    },
    {
        "name": "Credit Card 2",
        "image_url": "card_2.png"
    },
    {
        "name": "Credit Card 3",
        "image_url": "card_3.png"
    }
]

# Streamlit app
st.title("Credit Card Comparison")

# Create columns for displaying cards side by side
columns = st.columns(len(credit_cards))

# Display each card in its respective column
for idx, card in enumerate(credit_cards):
    display_credit_card(card["name"], card["image_url"], columns[idx])
