import streamlit as st

st.set_page_config(page_title="Road Construction Calculator")

st.title("🛣️ Road Construction Cost Calculator")

road_name = st.text_input("Road Name")

road_type = st.selectbox(
    "Road Type",
    ["Bituminous", "Concrete", "WBM"]
)

length = st.number_input("Road Length (m)", min_value=0.0)
width = st.number_input("Road Width (m)", min_value=0.0)

area = length * width

st.write("### Constructed Area")
st.write(f"{area:.2f} sq.m")

st.subheader("Material Details")

bitumen_qty = st.number_input(
    "Bitumen Quantity per sq.m",
    min_value=0.0
)

bitumen_rate = st.number_input(
    "Bitumen Cost per Unit (₹)",
    min_value=0.0
)

aggregate_qty = st.number_input(
    "Aggregate Quantity per sq.m",
    min_value=0.0
)

aggregate_rate = st.number_input(
    "Aggregate Cost per Unit (₹)",
    min_value=0.0
)

labour_cost = st.number_input(
    "Labour Cost (₹)",
    min_value=0.0
)

equipment_cost = st.number_input(
    "Equipment Cost (₹)",
    min_value=0.0
)

transport_cost = st.number_input(
    "Transportation Cost (₹)",
    min_value=0.0
)

if st.button("Calculate Project Cost"):

    bitumen_total = area * bitumen_qty * bitumen_rate
    aggregate_total = area * aggregate_qty * aggregate_rate

    total_material_cost = bitumen_total + aggregate_total

    grand_total = (
        total_material_cost
        + labour_cost
        + equipment_cost
        + transport_cost
    )

    st.success("Calculation Complete")

    st.subheader("Project Summary")

    st.write("Road Name:", road_name)
    st.write("Road Type:", road_type)
    st.write("Area:", round(area, 2), "sq.m")

    st.write("Material Cost: ₹", round(total_material_cost, 2))
    st.write("Labour Cost: ₹", labour_cost)
    st.write("Equipment Cost: ₹", equipment_cost)
    st.write("Transportation Cost: ₹", transport_cost)

    st.write("## Total Project Cost")
    st.write(f"₹ {grand_total:,.2f}")