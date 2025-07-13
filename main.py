import streamlit as st
import qrcode
import os
from PIL import Image

# Create a directory to save QR codes if it doesn't exist
os.makedirs("qr_codes", exist_ok=True)

# --- App Configuration ---
st.set_page_config(
    page_title="Bill Splitter with UPI QR",
    page_icon="💸"
)

# --- App Title ---
st.title("💸 Bill Splitter & UPI QR Generator")

# --- Input Fields ---
total_amount = st.number_input(
    "Enter total bill amount (₹)",
    min_value=1.0,
    format="%.2f"
)

num_people = st.number_input(
    "Number of people to split with",
    min_value=1,
    step=1
)

# --- People Information Section ---
# Initialize or update session state for people's data
if "people" not in st.session_state:
    st.session_state.people = [{"name": "", "upi": ""} for _ in range(num_people)]

# Adjust the list of people in session state if the number of people changes
if len(st.session_state.people) != num_people:
    current_people = st.session_state.people
    if num_people > len(current_people):
        # Add new empty dicts if num_people increases
        st.session_state.people.extend([{"name": "", "upi": ""} for _ in range(num_people - len(current_people))])
    else:
        # Truncate the list if num_people decreases
        st.session_state.people = current_people[:num_people]


# Display input fields for each person's name and UPI ID
st.subheader("Enter Details for Each Person")
for i in range(num_people):
    st.session_state.people[i]['name'] = st.text_input(
        f"Person #{i+1}'s Name",
        key=f"name_{i}",
        value=st.session_state.people[i].get('name', '')
    )
    st.session_state.people[i]['upi'] = st.text_input(
        f"Person #{i+1}'s UPI ID",
        key=f"upi_{i}",
        value=st.session_state.people[i].get('upi', '')
    )

# --- QR Code Generation ---
if st.button("Generate QR Codes"):
    people_details = st.session_state.people

    # Validate that all fields are filled
    if not people_details or any(not p.get('name') or not p.get('upi') for p in people_details):
        st.error("Please fill in all names and UPI IDs before generating QR codes.")
    else:
        try:
            # Calculate the split amount
            split_amount = round(total_amount / len(people_details), 2)
            st.success(f"Each person needs to pay: ₹{split_amount}")

            # Generate a QR code for each person
            st.subheader("Scan the QR Code to Pay")
            for person in people_details:
                # UPI deep link format
                upi_link = f"upi://pay?pa={person['upi']}&pn={person['name']}&am={split_amount}&cu=INR"

                # Generate QR code
                qr_image = qrcode.make(upi_link)
                img_path = f"qr_codes/{person['name'].replace(' ', '_')}_qr.png"
                qr_image.save(img_path)

                # Display the QR code image with a caption
                st.image(img_path, caption=f"Scan to pay {person['name']} ₹{split_amount}", width=250)
        except ZeroDivisionError:
            st.error("Number of people must be at least 1.")