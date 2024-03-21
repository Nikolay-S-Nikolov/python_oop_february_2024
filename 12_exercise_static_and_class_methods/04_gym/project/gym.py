from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    # def get_info(self, object_id, list_objects: List[Subscription or Customer or Trainer or ExercisePlan or Equipment]):
    #     return next(filter(lambda x: x.id == object_id, self.list_objects))

    def subscription_info(self, subscription_id: int):
        subscription_i = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer_i = next(filter(lambda c: c.id == subscription_i.customer_id, self.customers))
        trainer_i = next(filter(lambda t: t.id == subscription_i.trainer_id, self.trainers))
        plan_i = next(filter(lambda p: p.id == subscription_i.exercise_id, self.plans))
        equipment_i = next(filter(lambda e: e.id == plan_i.equipment_id, self.equipment))
        return '\n'.join([str(subscription_i), str(customer_i), str(trainer_i), str(equipment_i), str(plan_i)])
