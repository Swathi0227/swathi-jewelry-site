import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Swathi Jewelry", layout="wide")

# --- Hero Section ---
hero = Image.open("images/hero.jpg")
st.image(hero, use_column_width=True)

st.markdown("<h1 style='text-align: center;'>Swathi Jewelry</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Elegant. Handcrafted. Timeless.</h4>", unsafe_allow_html=True)

# --- Navigation ---
section = st.sidebar.radio("Navigate", ["Home", "About Us", "Collection", "Testimonials", "Contact"])

# --- About ---
if section == "About Us":
    st.header("Our Story")
    st.write("""
    Swathi Jewelry was founded with a passion for timeless beauty and personalized craftsmanship.
    Each piece is handcrafted with precision, blending tradition and elegance. Our mission is to
    create jewelry that tells your story — whether it’s a custom ring or a signature bracelet.
    """)
    st.success("✔ Handcrafted  ✔ Custom Designs  ✔ High-Quality Materials")

# --- Collection ---
elif section == "Collection":
    st.header("Jewelry Collection")

    cols = st.columns(4)
    with cols[0]:
        st.image("images/necklace.jpg", caption="Pearl Necklace - ₹4,999")
    with cols[1]:
        st.image("images/earring.jpg", caption="Gold Earrings - ₹2,499")
    with cols[2]:
        st.image("images/bracelet.jpg", caption="Charm Bracelet - ₹3,299")
    with cols[3]:
        st.image("images/ring.jpg", caption="Rose Gold Ring - ₹1,999")

# --- Testimonials ---
elif section == "Testimonials":
    st.header("Customer Reviews")
    st.info("⭐️⭐️⭐️⭐️⭐️ – ‘Absolutely stunning craftsmanship. Got my custom earrings within a week!’")
    st.info("⭐️⭐️⭐️⭐️⭐️ – ‘The ring was perfect for my engagement. Thank you Swathi Jewelry!’")

# --- Contact ---
elif section == "Contact":
    st.header("Contact Us")
    st.write("**Address:** KPHB, Near Malabar Gold & Diamonds Store, Hyderabad, 500072")
    st.write("**Phone:** 📞 8333913677")
    st.write("**Email:** 📧 swathireddyvaka@gmail.com")
    st.write("**Hours:** 🕘 9am to 9pm")

    st.markdown("#### 📍 Find Us on Google Maps")
    st.components.v1.iframe("https://www.google.com/maps?q=KPHB,+Hyderabad&output=embed", height=300)

    st.markdown("#### 📩 Contact Form")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you! We'll get back to you soon.")

    st.markdown("#### 💬 Chat with us on WhatsApp")
    st.markdown("[📱 Click to chat](https://wa.me/918333913677)", unsafe_allow_html=True)

    st.markdown("#### 📬 Subscribe to our Newsletter")
    email = st.text_input("Enter your email for updates")
    if st.button("Subscribe"):
        st.success("Thank you for subscribing!")

# --- Footer ---
st.markdown("""<hr style="border:1px solid #eee"/>""", unsafe_allow_html=True)
st.markdown("<center>Follow us: \
<a href='#'>Instagram</a> | <a href='#'>Facebook</a> | <a href='#'>Pinterest</a> | \
<a href='https://wa.me/918333913677'>WhatsApp</a></center>", unsafe_allow_html=True)
st.markdown("<center>&copy; 2025 Swathi Jewelry</center>", unsafe_allow_html=True)
