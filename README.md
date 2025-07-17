# vending_machine-gui
this project is a simulation of a simple vending machine built using Python and Tkinter GUI. It mimics a real-life vending machine that accepts ₹5 and ₹10 coins. The system uses a finite state machine (FSM) to track the total inserted amount and decides whether to dispense a product or return change.
Users interact with the machine by:
Clicking on coin input buttons (₹5, ₹10)
Viewing product output and change
Using a reset button to restart the machine

The GUI also includes:
A custom-drawn vending machine image with buttons overlaid on it
The backend logic ensures that the product is dispensed only when the total inserted amount reaches ₹15, and returns the appropriate change when overpaid.
