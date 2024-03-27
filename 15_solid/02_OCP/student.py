class StudentTaxes:
    def __init__(self, name, semester_tax, avg_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = avg_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2


class FurtherAdditionalDiscount(AdditionalDiscount):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 3 < self.average_grade <= 4:
            return self.semester_tax * 0.1


if __name__ == '__main__':
    s = StudentTaxes('A', 100, 5.30)
    print(s.get_discount())

    s1 = AdditionalDiscount('A', 100, 5)
    print(s1.get_discount())

    s2 = FurtherAdditionalDiscount('A', 100, 3.20)
    print(s2.get_discount())
