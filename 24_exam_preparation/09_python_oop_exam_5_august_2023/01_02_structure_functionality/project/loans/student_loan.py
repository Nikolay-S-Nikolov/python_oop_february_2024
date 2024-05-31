from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE_INCREASES = 0.2
    INTEREST_RATE = 1.5
    AMOUNT = 2_000

    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INTEREST_RATE_INCREASES
