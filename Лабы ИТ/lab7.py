# 1 
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"

# 2
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"

# 3
class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"
# 4
class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []  # список подчинённых

    # 5
    def add_employee(self, employee):
        self.team.append(employee)

    # 6
    def get_team_info(self):
        if not self.team:
            return "Подчинённых нет"
        info = "Команда TechManager:\n"
        for emp in self.team:
            info += f"- {emp.get_info()}\n"
        return info


# 7 демонстрация работы

employee = Employee("Иван", 1)
manager = Manager("Анна", 2, "IT")
technician = Technician("Сергей", 3, "Сети")
tech_manager = TechManager("Ольга", 4, "Разработка", "DevOps")

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project())
print(technician.get_info())
print(technician.perform_maintenance())

# 
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)




print(tech_manager.get_team_info())
