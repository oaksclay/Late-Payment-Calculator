
# Late Payment Impact Calculator

This project offers a Streamlit-based application to calculate the impact of late payments on loans. It provides insights into additional interest accrued due to delayed payments and forecasts the potential extension of the loan term if such behavior continues.

## Features
- **Loan Data Input**: Users can input loan amount, annual percentage rate (APR), loan term, number of payments already made, and details of late payments.
- **Late Payment Parsing**: The application parses the user's late payment data and translates it into a format suitable for calculations.
- **Impact Calculation**: It calculates the total interest without late payments, additional interest due to late payments, and the additional months added to the loan term. It also forecasts the impact of continued late payment behavior.
- **Streamlit Interface**: A user-friendly interface for inputting loan details and viewing calculated results.

## How to Run the Application
1. Install dependencies:
   ```
   pip install streamlit, numpy, numpy_financial
   ```
2. Run the script:
   ```
   streamlit run main.py
   ```

## Usage Example
- Input the loan amount, APR, loan term, number of payments made, and late payment details in the Streamlit interface.
- Click 'Calculate' to view the impact of late payments on the loan.

## Code Structure
The main components of the code include:
- `parse_late_payments`: Function to parse late payment details from the user's input.
- `calculate_impact_of_late_payments`: Function to calculate the financial impact of late payments.
- Streamlit interface setup for user inputs and displaying results.

## Disclaimer
The information provided by this application is for educational purposes only. While efforts are made to ensure the accuracy of the calculations, there is no guarantee of the accuracy or reliability of the information and results provided. Users should use their discretion and consider seeking professional financial advice for their specific situations.

## License
[MIT License](LICENSE.md)
