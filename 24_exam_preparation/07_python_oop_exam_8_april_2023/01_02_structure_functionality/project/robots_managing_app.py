from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[FemaleRobot or MaleRobot] = []
        self.services: List[MainService or SecondaryService] = []

    def add_service(self, service_type: str, name: str):
        valid_types = {"MainService": MainService, "SecondaryService": SecondaryService}

        if service_type not in valid_types:
            raise Exception("Invalid service type!")
        new_service = valid_types[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_types = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}
        if robot_type not in valid_types:
            raise Exception("Invalid robot type!")
        new_robot = valid_types[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if self.mismatch(robot, service):
            return "Unsuitable service."
        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = sum(r.price for r in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = [s.details() for s in self.services]
        return '\n'.join(result)

    @staticmethod
    def mismatch(robot, service) -> bool:
        if type(robot) == MaleRobot:
            return True if type(service) == SecondaryService else False
        if type(robot) == FemaleRobot:
            return True if type(service) == MainService else False
