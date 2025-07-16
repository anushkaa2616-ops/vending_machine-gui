import streamlit as st
from PIL import Image

# FSM logic class (unchanged)
class VendingMachine:
    def __init__(self):
        self.s0 = 0
        self.s1 = 1
        self.s2 = 2
        self.state = self.s0
        self.out = 0
        self.change = 0

    def reset(self):
        self.state = self.s0
        self.out = 0
        self.change = 0

    def insert_coin(self, coin):
        self.out = 0
        self.change = 0

        if self.state == self.s0:
            if coin == 0:
                self.state = self.s0
            elif coin in [1, 2]:
                self.state = self.s2

        elif self.state == self.s1:
            if coin == 0:
                self.state = self.s0
                self.change = 1
            elif coin == 2:
                self.state = self.s0
                self.out = 1

        elif self.state == self.s2:
            if coin == 0:
                self.state = self.s0
                self.change = 2
            elif coin == 1:
                self.state = self.s0
                self.out = 1
            elif coin == 2:
                self.state = self.s0
                self.out = 1
                self.change = 1

        return self.state, self.out, self.change


st.set_page_config(page_title="Vending Machine", layout="centered")
st.title("🧃 Streamlit Vending Machine")

# Load image (make sure it's in the repo root)
img = Image.open("vmdrawing1.png")
st.image(img, caption="Your Vending Machine", use_column_width=True)

# Use session state to keep machine persistent
if "vm" not in st.session_state:
    st.session_state.vm = VendingMachine()
if "log" not in st.session_state:
    st.session_state.log = ["Welcome! Insert coins to start."]

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Insert ₹5"):
        state, out, change = st.session_state.vm.insert_coin(1)
        message = f"Inserted: ₹5\nState: S{state}\nProduct Out: {'Yes' if out else 'No'}\nChange Returned: ₹{5*change if change else 0}"
        st.session_state.log.append(message)

with col2:
    if st.button("Insert ₹10"):
        state, out, change = st.session_state.vm.insert_coin(2)
        message = f"Inserted: ₹10\nState: S{state}\nProduct Out: {'Yes' if out else 'No'}\nChange Returned: ₹{5*change if change else 0}"
        st.session_state.log.append(message)

with col3:
    if st.button("Reset 🔄"):
        st.session_state.vm.reset()
        st.session_state.log.append("Machine reset. Insert coins to start.")

st.subheader("🧾 Transaction Log")
# Show last 5 messages (reverse chronological)
for msg in reversed(st.session_state.log[-5:]):
    st.text(msg)
