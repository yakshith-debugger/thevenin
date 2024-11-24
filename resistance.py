import streamlit as st

# Set the title of the web application
st.title("Thevenins theorem - 2305A21L24")  # Replace ROLL_NUMBER with your roll number

# Define the function to calculate IL and PL
def calculate(Vth, Rth, RL):
    """
    Calculate Load Current (IL) and Power across Load (PL) based on Thevenin's theorem.
    
    Args:
    Vth (float): Thevenin equivalent voltage in volts
    Rth (float): Thevenin equivalent resistance in ohms
    RL (float): Load resistance in ohms
    
    Returns:
    tuple: IL (Load Current in amperes), PL (Power across load in watts)
    """
    IL = Vth / (Rth + RL)  # Calculate load current
    PL = IL * IL * RL      # Calculate power across load
    return IL, PL

# Input fields for user to enter Vth, Rth, and RL
Vth = st.number_input("Enter Vth (Volts):", min_value=0.0, step=0.1, format="%.2f")
Rth = st.number_input("Enter Rth (Ohms):", min_value=0.0, step=0.1, format="%.2f")
RL = st.number_input("Enter RL (Ohms):", min_value=0.0, step=0.1, format="%.2f")

# Calculate and display results when the button is clicked
if st.button("Calculate"):
    if Rth + RL == 0:
        st.error("Rth + RL cannot be zero. Please provide valid inputs.")
    else:
        IL, PL = calculate(Vth, Rth, RL)  # Call the calculate function
        st.write(f"*Load Current (IL):* {IL:.2f} A")
        st.write(f"*Power across Load (PL):* {PL:.2f} W")