# Design a class Vehicle that:
# •	Keeps a record of service charge rate common to all vehicles.
# •	Each vehicle has a model, kilometers_run, and service history.
# •	Has a function to calculate service charge based on km and rate.
# •	Provides a method to update the service rate for all vehicles.
# •	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.	Creating vehicles with different km and models.
# 2.	Updating the service rate.
# 3.	Showing charges and eligibility checks.


class Vehicle:
    service_charge=10
    def __init__(self,model,kilometers_run,service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history
    def charge(self):
        return self.kilometers_run * Vehicle.service_charge
    @classmethod
    def service_rate(cls,new):
        cls.service_charge=new
    @staticmethod
    def check_model(year):
        return year>2010


v1=Vehicle("Gt650",2000,"good")
v2=Vehicle("r15",5000,"average")

Vehicle.service_rate(15)

print(v1.model,v1.charge())
print(v2.model,v2.charge())

print(Vehicle.check_model(2015))
print(Vehicle.check_model(2009))