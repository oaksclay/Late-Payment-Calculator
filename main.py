import streamlit as st
import numpy as np
import numpy_financial as npf

def parse_late_payments(late_payments_str):
    # Parses the late payment string and returns a dictionary
    late_payments = {}
    if late_payments_str:
        for pair in late_payments_str.split(','):
            payment_number, days_late = pair.split('=')
            late_payments[int(payment_number)] = int(days_late)
    return late_payments

def calculate_impact_of_late_payments(principal, apr, term, late_payments_dict, num_payments_made):
    monthly_rate = apr / 100 / 12
    daily_rate = monthly_rate / 30  # Assuming 30 days in a month for simplification
    original_payment = npf.pmt(monthly_rate, term, -principal)

    # Calculate total interest without late payments
    total_interest_no_late = npf.ipmt(monthly_rate, np.arange(1, term + 1), term, -principal).sum()

    # Calculate additional interest due to late payments
    additional_interest = 0
    for payment_num, days_late in late_payments_dict.items():
        if payment_num <= num_payments_made:
          remaining_balance = abs(npf.pv(monthly_rate, term - payment_num, original_payment, 0))
          additional_interest += days_late * daily_rate * remaining_balance

    # Calculate the additional months added to the loan term
    additional_months = (additional_interest / original_payment) * 12

    # Forecast for continued late payment behavior
    avg_delay_days = np.mean(list(late_payments_dict.values())) if late_payments_dict else 0
    forecast_additional_interest = avg_delay_days * daily_rate * (principal / term) * num_payments_made
    forecast_additional_months = (forecast_additional_interest / original_payment) * 12

    return total_interest_no_late, additional_interest, additional_months, forecast_additional_interest, forecast_additional_months

# Streamlit interface
st.title('Late Payment Impact Calculator')

# User inputs
principal = st.number_input('Loan Amount', min_value=0.0)
apr = st.number_input('Annual Percentage Rate (APR %)', min_value=0.0, max_value=100.0)
term = st.number_input('Loan Term (Months)', min_value=0)
num_payments_made = st.number_input('Number of Payments Already Made', min_value=0)
late_payments_str = st.text_input('Late Payments (Format: "3=15, 5=10")')

if st.button('Calculate'):
    late_payments_dict = parse_late_payments(late_payments_str)
    total_interest_no_late, additional_interest, additional_months, forecast_additional_interest, forecast_additional_months = calculate_impact_of_late_payments(
        principal, apr, term, late_payments_dict, num_payments_made)

    st.write(f'Original Total Interest: ${total_interest_no_late:.2f}')
    st.write(f'Additional Interest Due to Late Payments: ${additional_interest:.2f}')
    st.write(f'Original Loan Term: {term} months')
    st.write(f'Additional Months Added to Loan Term: {additional_months:.2f} months')
    st.write(f'Forecast Additional Interest (If Late Payment Behavior Continues): ${forecast_additional_interest:.2f}')
    st.write(f'Forecast Additional Months (If Late Payment Behavior Continues): {forecast_additional_months:.2f} months')
    st.write(f'Extended Loan Term (Forecast): {term + forecast_additional_months:.2f} months')

# To run this script:
# 1. Install Streamlit: pip install streamlit
# 2. Run the script: streamlit run main.py
