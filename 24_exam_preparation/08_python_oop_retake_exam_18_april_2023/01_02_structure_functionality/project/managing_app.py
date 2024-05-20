from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[PassengerCar or CargoVan] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in [u.driving_license_number for u in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        valid_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
        if vehicle_type not in valid_types:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if license_plate_number in [v.license_plate_number for v in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = valid_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point:
                if r.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                if r.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                if r.length > length:  # TO DO to check if can be another one that is == or <
                    r.is_locked = True
        rout_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, rout_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        route = [r for r in self.routes if r.route_id == route_id][0]
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = list(sorted([v for v in self.vehicles if v.is_damaged], key=lambda x: (x.brand, x.model,)))
        number_to_repair = count if count < len(damaged_vehicles) else len(damaged_vehicles)
        for idx in range(number_to_repair):
            v = damaged_vehicles[idx]
            v.change_status()
            v.recharge()

        return f"{number_to_repair} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = list(sorted(self.users, key=lambda x: x.rating, reverse=True))
        users = '\n'.join(str(u) for u in sorted_users)
        return f"*** E-Drive-Rent ***\n" \
               f"{users}"
