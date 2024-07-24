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


st.header(":violet[1.] Monitor Your Accounts Regularly:")
st.markdown("Check your bank and credit card statements frequently to spot any unauthorized transactions.")
st.markdown("Use mobile banking apps to set up alerts for transactions over a certain amount or for suspicious activity.")
st.markdown(" ")

st.header(":violet[2.] Protect Your Personal Information:")
st.markdown("Avoid sharing your credit card details over the phone or online unless you're certain of the recipient's legitimacy.")
st.markdown("Be cautious when using public Wi-Fi networks; avoid accessing sensitive information or making purchases.")
st.markdown(" ")

st.header(":violet[3.] Use Secure Websites:")
st.markdown("Ensure the website is secure by looking for https:// in the URL and a padlock symbol in the browser's address bar before entering your credit card information.")
st.markdown("Only shop on reputable websites and avoid clicking on suspicious links or pop-ups.")
st.markdown(" ")

st.header(":violet[4.] Report Suspicious Activity Immediately:")
st.markdown("If you notice any unauthorized transactions or suspect fraud, contact your credit card issuer immediately.")
st.markdown("Reporting promptly can help prevent further fraudulent activity and limit your liability.")