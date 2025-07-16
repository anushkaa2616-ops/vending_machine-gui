import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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


# GUI logic
    # GUI with Image & Overlaid Buttons
class VendingMachineApp:
    def __init__(self, root):
        self.vm = VendingMachine()
        self.root = root
        self.root.title("GUI-based Vending Machine")

        # 🖼️ Load vending machine image
        self.img = Image.open("vmdrawing1.png")  # Replace with your filename
        self.img = self.img.resize((400, 580))  # Resize as needed
        self.photo = ImageTk.PhotoImage(self.img)

        # 📌 Create Canvas
        self.canvas = tk.Canvas(root, width=400, height=580)
        self.canvas.pack()

        # Draw image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # 🧾 Display area
        self.text_display = tk.Text(root, height=5, width=50, bg="pink")
        self.text_display.pack()
        self.update_display("Welcome! Insert coins to start.")

        # 🟢 Overlay transparent buttons on the image
        self.button5 = tk.Button(root, text="₹5", command=lambda: self.insert_coin(1))
        self.button10 = tk.Button(root, text="₹10", command=lambda: self.insert_coin(2))
        self.buttonReset = tk.Button(root, text="Reset", bg="red", fg="white", command=self.reset)

        # Place buttons using canvas `create_window`
        self.canvas.create_window(80, 500, window=self.button5, width=60)
        self.canvas.create_window(200, 500, window=self.button10, width=60)
        self.canvas.create_window(320, 550, window=self.buttonReset, width=100)

        
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
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, message)


# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineApp(root)
    root.mainloop()
