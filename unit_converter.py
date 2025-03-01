import streamlit as st

# 🌙 Dark Mode Toggle Button
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")

# 🎨 Dark & Light Theme CSS
if dark_mode:
    theme_css = """
        <style>
            body { background-color: #121212; color: white; }
            .stApp { background-color: #121212; }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
        </style>
    """
else:
    theme_css = """
        <style>
            body { background-color: white; color: black; }
            .stApp { background-color: white; }
            .stButton>button {
                background-color: #008CBA;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
        </style>
    """

st.markdown(theme_css, unsafe_allow_html=True)

# 🎨 App Title
st.title("🔥 Unit Converter")

# 📌 Conversion Type Selection
conversion_type = st.sidebar.selectbox("Select Conversion Type:", ["Length", "Weight", "Temperature"])

# 📏 Length Conversion Function
def convert_length(value, from_unit, to_unit):
    units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
    return value * (units[from_unit] / units[to_unit])

# ⚖️ Weight Conversion Function
def convert_weight(value, from_unit, to_unit):
    units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (units[from_unit] / units[to_unit])

# 🌡️ Temperature Conversion Function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return None

# 🎯 Handling Conversion Based on Selection
if conversion_type == "Length":
    st.subheader("📏 Length Converter")
    value = st.number_input("Enter Value:", min_value=0.0)
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet"])
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet"])
    if st.button("Convert", key="convert_length"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.balloons()

elif conversion_type == "Weight":
    st.subheader("⚖️ Weight Converter")
    value = st.number_input("Enter Value:", min_value=0.0)
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("Convert", key="convert_weight"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        st.balloons()

elif conversion_type == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    value = st.number_input("Enter Value:")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert", key="convert_temp"):
        with st.spinner("Converting..."):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
            st.balloons()
