from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[MortgageLoan or StudentLoan] = []
        self.clients: List[Adult or Student] = []

    def add_loan(self, loan_type: str):
        valid_types = {"MortgageLoan": MortgageLoan, "StudentLoan": StudentLoan}
        if loan_type not in valid_types:
            raise Exception("Invalid loan type!")

        new_loan = valid_types[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        valid_types = {"Student": Student, "Adult": Adult}

        if client_type not in valid_types:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = valid_types[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        granted_loan = {"MortgageLoan": Adult, "StudentLoan": Student}
        client = [c for c in self.clients if c.client_id == client_id][0]

        if not granted_loan[loan_type] == type(client):
            raise Exception("Inappropriate loan type!")

        loan = [lo for lo in self.loans if type(lo).__name__ == loan_type][0]
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):

        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        """
        Loans that are already granted to clients should not be affected
        """
        list_loans_interest_rate_to_change = [lo for lo in self.loans if type(lo).__name__ == loan_type]
        for loan in list_loans_interest_rate_to_change:
            loan.increase_interest_rate()
        return f"Successfully changed {len(list_loans_interest_rate_to_change)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_interest_rate = [c for c in self.clients if c.interest < min_rate]
        for client in changed_client_interest_rate:
            client.increase_clients_interest()

        return f"Number of clients affected: {len(changed_client_interest_rate)}."

    def get_statistics(self):
        granted_sum = sum(sum(lo.amount for lo in c.loans) for c in self.clients)
        not_granted_sum = sum(lo.amount for lo in self.loans)
        try:
            avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0
        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {sum(c.income for c in self.clients):.2f}\n" \
               f"Granted Loans: {sum(len(c.loans) for c in self.clients)}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
