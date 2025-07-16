import tkinter as tk
from tkinter import messagebox

# FSM logic
class VendingMachine:
    def __init__(self):
        self.s0 = 0  # ₹0
        self.s1 = 1  # ₹5
        self.s2 = 2  # ₹10
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
            elif coin == 1:  # ₹5
                self.state = self.s1
            elif coin == 2:  # ₹10
                self.state = self.s2

        elif self.state == self.s1:
            if coin == 0:
                self.state = self.s0
                self.change = 1  # ₹5
            elif coin == 2:  # ₹10
                self.state = self.s0
                self.out = 1
                self.change = 0
            elif coin == 1:  # ₹5 again (Not handled in Verilog, can be assumed to go to ₹10 state)
                self.state = self.s2

        elif self.state == self.s2:
            if coin == 0:
                self.state = self.s0
                self.change = 2  # ₹10
            elif coin == 1:  # ₹5
                self.state = self.s0
                self.out = 1
                self.change = 0
            elif coin == 2:  # ₹10
                self.state = self.s0
                self.out = 1
                self.change = 1  # ₹5

        return self.state, self.out, self.change



# GUI logic
class VendingMachineApp:
    def __init__(self, root):
        self.vm = VendingMachine()
        self.root = root
        self.root.title("Vending Machine GUI")

        # Display
        self.display = tk.Text(root, height=10, width=50, bg="lightyellow", font=("Arial", 12))
        self.display.pack(pady=10)
        self.update_display("Welcome! Insert coins to start.")

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.btn5 = tk.Button(btn_frame, text="Insert ₹5", width=15, command=lambda: self.insert_coin(1))
        self.btn10 = tk.Button(btn_frame, text="Insert ₹10", width=15, command=lambda: self.insert_coin(2))
        self.btnNone = tk.Button(btn_frame, text="No Coin", width=15, command=lambda: self.insert_coin(0))
        self.btnReset = tk.Button(root, text="Reset Machine", width=20, bg="red", fg="white", command=self.reset)

        self.btn5.grid(row=0, column=0, padx=10, pady=5)
        self.btn10.grid(row=0, column=1, padx=10, pady=5)
        self.btnNone.grid(row=0, column=2, padx=10, pady=5)
        self.btnReset.pack(pady=10)

    def insert_coin(self, coin):
        state, out, change = self.vm.insert_coin(coin)
        state_str = f"S{state}"
        coin_str = "None" if coin == 0 else f"₹{5 * coin}"
        out_str = "Yes" if out else "No"
        change_str = f"₹{5 * change}" if change else "None"

        message = f"Inserted: {coin_str}\nCurrent State: {state_str}\nProduct Out: {out_str}\nChange Returned: {change_str}\n"
        self.update_display(message)

    def reset(self):
        self.vm.reset()
        self.update_display("Machine reset. Insert coins to start.")

    def update_display(self, message):
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, message)


# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineApp(root)
    root.mainloop()
