from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    KNEE_PAD_PRICE = 15.0

    def __init__(self):
        super().__init__(self.PROTECTION, self.KNEE_PAD_PRICE)

    def increase_price(self):
        self.price += self.price * 0.20
