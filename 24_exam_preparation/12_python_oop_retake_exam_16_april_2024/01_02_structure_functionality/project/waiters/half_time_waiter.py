from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 12.0

    def calculate_earnings(self):
        calculated_earnings = self.hours_worked * self.HOURLY_WAGE
        return calculated_earnings

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."
