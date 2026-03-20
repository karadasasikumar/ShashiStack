
class TimeTraveler:
    registry=[]
    def __init__(self,codename,origin_year,destination_year):
        self.codename=codename
        self.origin_year=origin_year
        self.destination_year=destination_year
        TimeTraveler.registry.append(self)
    @classmethod
    def show_registry(cls):
       print("Total Travellers:", len(cls.registry))
       print("codenames:")
    @staticmethod
    def year_status(year):
        if 2026< year:
            return "Past"
        elif 2026==year:
            return "present"
        else:
            "Future"

t1=TimeTraveler("hillstation",2016,2017)
t2=TimeTraveler("Mountains",2015,2016)
