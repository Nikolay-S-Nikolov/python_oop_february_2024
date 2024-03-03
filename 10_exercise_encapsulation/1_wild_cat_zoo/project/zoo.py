from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:

        if not len(self.animals) < self.__animal_capacity:
            return "Not enough space for animal"

        if not self.__budget >= price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:

        if not len(self.workers) < self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        workers_salary = sum(w.salary for w in self.workers)
        if workers_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        animals_care_budget = sum(a.money_for_care for a in self.animals)
        if animals_care_budget > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_care_budget
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions_list = [lion for lion in self.animals if lion.__class__.__name__ == "Lion"]
        lions_info = "\n".join(str(li) for li in lions_list)
        tigers_list = [tiger for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        tigers_info = "\n".join(str(t) for t in tigers_list)
        cheetahs_list = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == "Cheetah"]
        cheetahs_info = "\n".join(str(c) for c in cheetahs_list)
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions_list)} Lions:\n" \
               f"{lions_info}\n" \
               f"----- {len(tigers_list)} Tigers:\n" \
               f"{tigers_info}\n" \
               f"----- {len(cheetahs_list)} Cheetahs:\n" \
               f"{cheetahs_info}"

    def workers_status(self) -> str:
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]
        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet'],
        ]
        return "\n".join(result)
