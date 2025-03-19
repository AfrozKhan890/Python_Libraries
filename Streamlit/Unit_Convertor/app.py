import streamlit as st

#  Custom CSS for black background, grey text, and animations
#  CSS is completely copied by AI Tools

st.markdown(
    """
    <style>
    /* Apply black background to the entire app */
    .stApp {
        background-color: #000000; /* Black background */
        color: #E0E0E0; /* Light grey text */
    }

    /* Output text color */
    .stSuccess {
        color: #00BFFF;
        font-size: 18px;
        font-weight: bold;
    }

    /* Input field hover effect */
    .stTextInput>div>div>input:hover, .stNumberInput>div>div>input:hover {
        background-color: #1E1E1E; /* Slightly lighter grey on hover */
        border-color: #00BFFF; /* Bright blue border on hover */
    }

    /* Button styling */
    .stButton>button {
        background-color: #1E90FF; /* Dodger blue for buttons */
        color: #FFFFFF; /* White text */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        transition: background-color 0.3s, transform 0.2s;
    }

    /* Button hover effect */
    .stButton>button:hover {
        background-color: #00BFFF; /* Bright blue on hover */
        transform: scale(1.05); /* Slightly enlarge on hover */
    }

    /* Button click effect */
    .stButton>button:active {
        background-color: #32CD32; /* Lime green on click */
        transform: scale(0.95); /* Slightly shrink on click */
    }

    /* Selectbox and other dropdowns */
    .stSelectbox>div>div>div {
        background-color: #1E1E1E; /* Dark grey for dropdowns */
        color: #E0E0E0; /* Light grey text */
        border-color: #00BFFF; /* Bright blue border */
    }

    /* Hover effect for dropdowns */
    .stSelectbox>div>div>div:hover {
        background-color: #2E2E2E; /* Slightly lighter grey on hover */
    }

    /* Custom CSS for Computing & Digital Storage input fields */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #1E1E1E; /* Dark grey background */
        color: #E0E0E0; /* Light grey text */
        border: 1px solid #00BFFF; /* Bright blue border */
        border-radius: 5px; /* Rounded corners */
        padding: 8px; /* Padding for better spacing */
    }

    /* Hover effect for input fields */
    .stTextInput>div>div>input:hover, .stNumberInput>div>div>input:hover {
        background-color: #2E2E2E; /* Slightly lighter grey on hover */
        border-color: #00BFFF; /* Bright blue border on hover */
    }

    /* Focus effect for input fields */
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {
        background-color: #2E2E2E; /* Slightly lighter grey on focus */
        border-color: #00BFFF; /* Bright blue border on focus */
        outline: none; /* Remove default outline */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🔄Unit Convertor")
unit_types = st.selectbox("Select field:\nwhich type of conversion you need: ",["General_use","Science & Engineering","Computing & Digital Storage"])

# General Use
if unit_types == "General_use":
    General_use = st.selectbox("Select unit type:",["Length","Weight","Time","Temperature","Volume"])

    # Length
    if General_use=="Length":
        st.subheader("Length Conversing")
        input_val = st.number_input("Enter value in Meters: ",min_value=0.0, step=0.1, format="%0.2f")
        length_units= {"Kilometer": 0.001, "Feet": 3.28084, "Inches": 39.3701}
        length_converting = st.selectbox("Convert to:", list(length_units.keys()))

        if st.button("Convert"):
            converted_values = input_val * length_units[length_converting]
            st.success(f"{input_val} Meters = {converted_values:0.2f} {length_converting}")
        
    # Weight 
    elif General_use == "Weight":
        st.subheader("Weight Conversing")
        input_val = st.number_input("Enter value in Kilograms: ",min_value=0.0, step=0.1, format="%0.2f")
        
        weight_units = {"Gram": 1000, "Pound": 2.20462,"Metric Ton": 0.001}
        
        weight_converting = st.selectbox("Convert to:",list(weight_units.keys()))
        if st.button("Convert"):
            converted_values = input_val * weight_units[weight_converting]
            st.success(f"{input_val} Kilograms = {converted_values:0.2f} {weight_converting}")
    
    # Time  
    elif General_use == "Time":
        st.subheader("Time Conversing")
        input_val = st.number_input("Enter value in Seconds: ",min_value=0.0,step=0.1, format="%0.2f")
        
        time_units = {"Millisecond": 1000,"Minute": 1 / 60,"Hour": 1 / 3600,"Day": 1 / 86400,"Week": 1 / 604800}
        time_converting = st.selectbox("Convert to:",list(time_units.keys()))
        
        if st.button("Convert"):
            converted_values = input_val * time_units[time_converting]
            st.success(f"{input_val} Seconds = {converted_values:0.2f} {time_converting}")

    # Temperature
    elif General_use == "Temperature":
        st.subheader("Temperature Conversing")
        input_val = st.number_input("Enter temperature in Celsius: ",min_value=0.0, step=0.1, format="%0.2f")
        
        temp_units = {"Fahrenheit (°F)":  (input_val * 9/5) + 32,"Kelvin (K)":  input_val + 273.15 }
        temp_converting = st.selectbox("Convert to:",list(temp_units.keys()))
        
        if st.button("Convert"):
            converted_values =temp_units[temp_converting]
            st.success(f"{input_val}°C = {converted_values:0.2f} {temp_converting}")
    
    # Volume
    elif General_use == "Volume":
        st.subheader("Volume Conversing")
        input_val = st.number_input("Enter value in Liters:",min_value=0.0, step=0.1, format="%0.2f")
        
        volume_units = {"Milliliter": 1000,"Cubic Meter": 0.001,"Cubic Centimeter": 1000,"US Gallon": 0.264172,"US Fluid Ounce": 33.814}
        volume_converting = st.selectbox("Convert to:",list(volume_units.keys()))
        
        if st.button("Convert"):
            converted_values = input_val * volume_units[volume_converting]
            st.success(f"{input_val} liters = {converted_values:0.2f} {volume_converting}")
   

# Science & Engineering 
if unit_types == "Science & Engineering":
    Science = st.selectbox("Select unit type:", ["Force", "Speed", "Pressure", "Energy", "Power"])

    # Force 
    if Science == "Force":
        calculate_types = st.selectbox("What do you want to calculate?", ["Force", "Mass", "Acceleration"])
        
        if calculate_types == "Force":
            st.subheader("Calculate Force (F = m × a)")
            mass = st.number_input("Enter value of Mass (kg):", min_value=0.0, step=0.1, format="%0.2f")
            acceleration = st.number_input("Enter value of Acceleration (m/s²):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Result"):
                if mass < 0 or acceleration < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif acceleration == 0:
                    st.error("Invalid: Acceleration cannot be zero!")
                else:
                    force = mass * acceleration
                    st.success(f"Force = {force:.2f} Newton (N)")

        elif calculate_types == "Mass":
            st.subheader("Calculate Mass (m = F / a)")
            force = st.number_input("Enter value of Force (N):", min_value=0.0, step=0.1, format="%0.2f")
            acceleration = st.number_input("Enter value of Acceleration (m/s²):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Result"):
                if force < 0 or acceleration < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif acceleration == 0:
                    st.error("Invalid: Acceleration cannot be zero!")
                else:
                    mass = force / acceleration
                    st.success(f"Mass = {mass:.2f} kg")

        elif calculate_types == "Acceleration":
            st.subheader("Calculate Acceleration (a = F / m)")
            force = st.number_input("Enter value of Force (N):", min_value=0.0, step=0.1, format="%0.2f")
            mass = st.number_input("Enter value of Mass (kg):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Result"):
                if force < 0 or mass < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif mass == 0:
                    st.error("Invalid: Mass cannot be zero!")
                else:
                    acceleration = force / mass
                    st.success(f"Acceleration = {acceleration:.2f} m/s²")

    # Speed
    elif Science == "Speed":
        calculate_speed = st.selectbox("What do you want to calculate?", ["Speed", "Distance", "Time"])

        if calculate_speed == "Speed":
            st.subheader("Calculate Speed (Speed = Distance / Time)")
            distance = st.number_input("Enter value of Distance (meters):", min_value=0.0, step=0.1, format="%0.2f")
            time = st.number_input("Enter value of Time (seconds):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Result"):
                if distance < 0 or time < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif time == 0:
                    st.error("Invalid: Time cannot be zero!")
                else:
                    speed = distance / time
                    st.success(f"Speed = {speed:.2f} m/s")

        elif calculate_speed == "Distance":
            st.subheader("Calculate Distance (Distance = Speed × Time)")
            speed = st.number_input("Enter value of Speed (m/s):", min_value=0.0, step=0.1, format="%0.2f")
            time = st.number_input("Enter value of Time (seconds):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Result"):
                if speed < 0 or time < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    distance = speed * time
                    st.success(f"Distance = {distance:.2f} meters")

        elif calculate_speed == "Time":
            st.subheader("Calculate Time (Time = Distance / Speed)")
            distance = st.number_input("Enter value of Distance (meters):", min_value=0.0, step=0.1, format="%0.2f")
            speed = st.number_input("Enter value of Speed (m/s):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Result"):
                if distance < 0 or speed < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif speed == 0:
                    st.error("Invalid: Speed cannot be zero!")
                else:
                    time = distance / speed
                    st.success(f"Time = {time:.2f} seconds")

    # Pressure 
    elif Science == "Pressure":
        calculate_pressure = st.selectbox("What do you want to calculate?", ["Pressure", "Force", "Area"])

        if calculate_pressure == "Pressure":
            st.subheader("Calculate Pressure (P = F / A)")
            force = st.number_input("Enter Force (N):", min_value=0.0, step=0.1, format="%0.2f")
            area = st.number_input("Enter Area (m²):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if force < 0 or area < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif area == 0:
                    st.error("Invalid: Area cannot be zero!")
                else:
                    pressure = force / area
                    st.success(f"Pressure = {pressure:.2f} Pascal (Pa)")

        elif calculate_pressure == "Force":
            st.subheader("Calculate Force (F = P × A)")
            pressure = st.number_input("Enter Pressure (Pa):", min_value=0.0, step=0.1, format="%0.2f")
            area = st.number_input("Enter Area (m²):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if pressure < 0 or area < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    force = pressure * area
                    st.success(f"Force = {force:.2f} Newton (N)")

        elif calculate_pressure == "Area":
            st.subheader("Calculate Area (A = F / P)")
            force = st.number_input("Enter Force (N):", min_value=0.0, step=0.1, format="%0.2f")
            pressure = st.number_input("Enter Pressure (Pa):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if force < 0 or pressure < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif pressure == 0:
                    st.error("Invalid: Pressure cannot be zero!")
                else:
                    area = force / pressure
                    st.success(f"Area = {area:.2f} square meters (m²)")

    # Energy
    elif Science == "Energy":
        calculate_energy = st.selectbox("What do you want to calculate?", ["Kinetic Energy", "Potential Energy", "Work Done", "Electrical Energy"])

        if calculate_energy == "Kinetic Energy":
            st.subheader("Calculate Kinetic Energy (KE = 1/2 m v²)")
            mass = st.number_input("Enter Mass (kg):", min_value=0.0, step=0.1, format="%0.2f")
            velocity = st.number_input("Enter Velocity (m/s):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if mass < 0 or velocity < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    KE = 0.5 * mass * (velocity ** 2)
                    st.success(f"Kinetic Energy = {KE:.2f} Joules")

        elif calculate_energy == "Potential Energy":
            st.subheader("Calculate Potential Energy (PE = mgh)")
            mass = st.number_input("Enter Mass (kg):", min_value=0.0, step=0.1, format="%0.2f")
            height = st.number_input("Enter Height (m):", min_value=0.0, step=0.1, format="%0.2f")
            g = 9.8 

            if st.button("Calculate"):
                if mass < 0 or height < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    PE = mass * g * height
                    st.success(f"Potential Energy = {PE:.2f} Joules")

        elif calculate_energy == "Work Done":
            st.subheader("Calculate Work Done (W = F d)")
            force = st.number_input("Enter Force (N):", min_value=0.0, step=0.1, format="%0.2f")
            distance = st.number_input("Enter Distance (m):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if force < 0 or distance < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    work = force * distance
                    st.success(f"Work Done = {work:.2f} Joules")

        elif calculate_energy == "Electrical Energy":
            st.subheader("Calculate Electrical Energy (E = P t)")
            power = st.number_input("Enter Power (W):", min_value=0.0, step=0.1, format="%0.2f")
            time = st.number_input("Enter Time (s):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if power < 0 or time < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif time == 0:
                    st.error("Invalid: Time cannot be zero!")
                else:
                    energy = power * time
                    st.success(f"Electrical Energy = {energy:.2f} Joules")

    # Power
    elif Science == "Power":
        calculate_power = st.selectbox("What do you want to calculate?", ["Basic Power", "Electrical Power", "Mechanical Power"])

        if calculate_power == "Basic Power":
            st.subheader("Calculate Power (P = W / t)")
            work = st.number_input("Enter Work Done (Joules):", min_value=0.0, step=0.1, format="%0.2f")
            time = st.number_input("Enter Time (Seconds):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if work < 0 or time < 0:
                    st.error("Invalid: Value cannot be negative!")
                elif time == 0:
                    st.error("Invalid: Time cannot be zero!")
                else:
                    power = work / time
                    st.success(f"Power = {power:.2f} Watts")

        elif calculate_power == "Electrical Power":
            st.subheader("Calculate Electrical Power (P = V × I)")
            voltage = st.number_input("Enter Voltage (Volts):", min_value=0.0, step=0.1, format="%0.2f")
            current = st.number_input("Enter Current (Amperes):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if voltage < 0 or current < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    power = voltage * current
                    st.success(f"Electrical Power = {power:.2f} Watts")

        elif calculate_power == "Mechanical Power":
            st.subheader("Calculate Mechanical Power (P = F × v)")
            force = st.number_input("Enter Force (Newtons):", min_value=0.0, step=0.1, format="%0.2f")
            velocity = st.number_input("Enter Velocity (m/s):", min_value=0.0, step=0.1, format="%0.2f")

            if st.button("Calculate"):
                if force < 0 or velocity < 0:
                    st.error("Invalid: Value cannot be negative!")
                else:
                    power = force * velocity
                    st.success(f"Mechanical Power = {power:.2f} Watts")

# Computing & Digital Storage
if unit_types == "Computing & Digital Storage":
    computing = st.selectbox("What do you want to convert?", ["Binary to Decimal", "Decimal to Binary", "Octal to Decimal", "Decimal to Octal", "Hexadecimal to Decimal", "Decimal to Hexadecimal"])
    
    if computing == "Binary to Decimal":
        st.subheader("Convert Binary to Decimal")
        binary_input = st.text_input("Enter Binary Number:")
        
        if st.button("Convert"):
            try:
                decimal_value = int(binary_input, 2)
                st.success(f"Decimal Value = {decimal_value}")
            except ValueError:
                st.error("Invalid Binary Number!")

    elif computing == "Decimal to Binary":
        st.subheader("Convert Decimal to Binary")
        decimal_input = st.number_input("Enter Decimal Number:", min_value=0, step=1)
        
        if st.button("Convert"):
            binary_value = bin(int(decimal_input))[2:]
            st.success(f"Binary Value = {binary_value}")

    elif computing == "Octal to Decimal":
        st.subheader("Convert Octal to Decimal")
        octal_input = st.text_input("Enter Octal Number:")
        
        if st.button("Convert"):
            try:
                decimal_value = int(octal_input, 8)
                st.success(f"Decimal Value = {decimal_value}")
            except ValueError:
                st.error("Invalid Octal Number!")

    elif computing == "Decimal to Octal":
        st.subheader("Convert Decimal to Octal")
        decimal_input = st.number_input("Enter Decimal Number:", min_value=0, step=1)
        
        if st.button("Convert"):
            octal_value = oct(int(decimal_input))[2:]
            st.success(f"Octal Value = {octal_value}")

    elif computing == "Hexadecimal to Decimal":
        st.subheader("Convert Hexadecimal to Decimal")
        hex_input = st.text_input("Enter Hexadecimal Number:")
        
        if st.button("Convert"):
            try:
                decimal_value = int(hex_input, 16)
                st.success(f"Decimal Value = {decimal_value}")
            except ValueError:
                st.error("Invalid Hexadecimal Number!")

    elif computing == "Decimal to Hexadecimal":
        st.subheader("Convert Decimal to Hexadecimal")
        decimal_input = st.number_input("Enter Decimal Number:", min_value=0, step=1)
        
        if st.button("Convert"):
            hex_value = hex(int(decimal_input))[2:].upper()
            st.success(f"Hexadecimal Value = {hex_value}")

