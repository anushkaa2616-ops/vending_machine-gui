import streamlit as st
from PIL import Image
import base64

# FSM logic
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
            if coin in [1, 2]:
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

# Convert image to base64 for background use
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 🖼 Background setup
img_base64 = get_img_as_base64("vmdrawing1.png")
st.markdown(
    f"""
    <style>
    .bg {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        height: 600px;
        position: relative;
    }}
    .btn {{
        position: absolute;
        font-size: 18px;
        padding: 10px 16px;
        border-radius: 8px;
        background-color: #ff4081;
        color: white;
        border: none;
        cursor: pointer;
    }}
    #b5 {{ left: 70px; bottom: 30px; }}
    #b10 {{ left: 170px; bottom: 30px; }}
    #reset {{ left: 280px; bottom: 30px; background-color: red; }}
    </style>
    <div class="bg">
        <form method="post">
            <button name="coin" value="1" class="btn" id="b5">₹5</button>
            <button name="coin" value="2" class="btn" id="b10">₹10</button>
            <button name="reset" value="reset" class="btn" id="reset">Reset</button>
        </form>
    </div>
    """,
    unsafe_allow_html=True
)

# FSM machine in session
if "vm" not in st.session_state:
    st.session_state.vm = VendingMachine()
if "last_msg" not in st.session_state:
    st.session_state.last_msg = "Welcome! Insert coins to start."

# Read POST values
import streamlit.components.v1 as components
components.html("<script>document.forms[0].submit();</script>", height=0)

# Get input
coin = st.experimental_get_query_params().get("coin", [None])[0]
reset = st.experimental_get_query_params().get("reset", [None])[0]

if reset:
    st.session_state.vm.reset()
    st.session_state.last_msg = "Machine reset. Insert coins to start."

elif coin:
    coin = int(coin)
    state, out, change = st.session_state.vm.insert_coin(coin)
    msg = f"Inserted: ₹{5 * coin}\nState: S{state}\nProduct Out: {'Yes' if out else 'No'}\nChange: ₹{5 * change if change else 0}"
    st.session_state.last_msg = msg

# Only show latest message
st.markdown("### 🧾 Status")
st.success(st.session_state.last_msg)

   

       
