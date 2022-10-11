def calculate_monthly_payment(loan_amount: int, term: int, rate: int):
    """
    Calculation of monthly payment
    :param loan_amount: loan amount
    :param term: number of months
    :param rate: annual interest rate
    :return: monthly payment, overpayment
    """
    monthly_interest_rate = rate / 100 / 12
    ratio = (monthly_interest_rate * (1 + monthly_interest_rate) ** term) / ((1 + monthly_interest_rate) ** term - 1)
    monthly_payment = ratio * loan_amount
    overpayment = monthly_payment * term - loan_amount
    return int(monthly_payment), int(overpayment)
