import streamlit as st
import pandas as pd

# Function to calculate benchmarking costs
def calculate_costs(headcount, location, industry, annual_revenue, office_space):
    # Example constants for cost calculation
    base_cost = 5000
    headcount_multiplier = 200
    location_multiplier = {
        "London": 1.5,
        "Manchester": 1.2,
        "Birmingham": 1.1,
        "Other": 1.0
    }
    industry_multiplier = {
        "Tech": 1.4,
        "Finance": 1.3,
        "Manufacturing": 1.2,
        "Retail": 1.1,
        "Other": 1.0
    }
    revenue_multiplier = 0.01
    office_space_multiplier = 10

    total_cost = (
        base_cost +
        headcount * headcount_multiplier +
        location_multiplier[location] * 1000 +
        industry_multiplier[industry] * 1000 +
        annual_revenue * revenue_multiplier +
        office_space * office_space_multiplier
    )

    return {
        "Base Cost": base_cost,
        "Headcount Cost": headcount * headcount_multiplier,
        "Location Cost": location_multiplier[location] * 1000,
        "Industry Cost": industry_multiplier[industry] * 1000,
        "Revenue Cost": annual_revenue * revenue_multiplier,
        "Office Space Cost": office_space * office_space_multiplier,
        "Total Cost": total_cost
    }

# Streamlit App
st.title("Business Benchmarking Cost Calculator")

# Input methods
headcount = st.slider("Headcount", min_value=1, max_value=500, value=50)
location = st.selectbox("Business Location", ["London", "Manchester", "Birmingham", "Other"])
industry = st.selectbox("Industry", ["Tech", "Finance", "Manufacturing", "Retail", "Other"])
annual_revenue = st.number_input("Annual Revenue (£)", min_value=0, step=10000, value=500000)
office_space = st.number_input("Office Space (sq ft)", min_value=0, step=100, value=2000)
submit = st.button("Calculate Costs")

if submit:
    costs = calculate_costs(headcount, location, industry, annual_revenue, office_space)
    costs_df = pd.DataFrame.from_dict(costs, orient='index', columns=["Cost"])
    
    st.write("### Benchmarking Costs")
    st.dataframe(costs_df)
    
    # Create a CSV for download
    csv = costs_df.to_csv().encode('utf-8')
    st.download_button(
        label="Download Costs as CSV",
        data=csv,
        file_name='benchmarking_costs.csv',
        mime='text/csv',
    )
