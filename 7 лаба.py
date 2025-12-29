class Employee:  
    def __init__(self, name, emp_id):  
        self.name = name  
        self.emp_id = emp_id  
  
    def get_info(self):  
        return f"Сотрудник: {self.name}, ID: {self.emp_id}"  #1
    
    
  
  
class Manager(Employee):  
    def __init__(self, name, emp_id, department):  
        Employee.__init__(self, name, emp_id)
        self.department = department  
  
    def manage_project(self):  
        return f"{self.name} управляет проектами в отделе {self.department}"  
  
    def get_info(self):  
        base_info = super().get_info()  
        return super().get_info() + f" Отдел: {self.department}" #2
    
  
  
class Technician(Employee):  
    def __init__(self, name, emp_id, specialization):  
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization  
  
    def perform_maintenance(self):  
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"  
  
    def get_info(self):  
        
        return super().get_info() + f" Специализация: {self.specialization}"  #3
    
  
  
class TechManager(Manager, Technician):  
    def __init__(self, name, emp_id, department, specialization):  
        Manager.__init__(self, name, emp_id, department)  
        Technician.__init__(self, name, emp_id, specialization)  
        self.team = []  #4

  
    def add_employee(self, employee):  
        self.team.append(employee)  
        return f"Сотрудник {employee.name} добавлен в команду"  #5
    
  
    def get_team_info(self):  
        if not self.team:  
            return "Команда пуста"  
        team_info = "Состав команды:\n"  
        for emp in self.team:  
            team_info += f"- {emp.get_info()}\n"  
        return team_info  #6
   

employee1 = Employee("Анна Иоанновна", "1730")  
manager1 = Manager("Петр Алексеевич", "1682", "Разработка")  
technician1 = Technician("Иван Васильевич", "1530", "Сетевое оборудование")  
tech_manager1 = TechManager("Алексей Михайлович", "1645", "ИТ", "Системное администрирование")  
  
 
print("Информация о сотруднике:")  
print(employee1.get_info())

print("\nИнформация о менеджере:")  
print(manager1.get_info())
print(manager1.manage_project())

print("\nИнформация о технику:")  
print(technician1.get_info())  
print(technician1.perform_maintenance())

print("\nИнформация о техническом менеджере:")  
print(tech_manager1.get_info())  
print(tech_manager1.manage_project())  
print(tech_manager1.perform_maintenance())  
  
 
print("\nДобавление сотрудников в команду:")  
print(tech_manager1.add_employee(employee1))  
print(tech_manager1.add_employee(manager1))  
print(tech_manager1.add_employee(technician1))  
  

print("\nИнформация о команде:")  
print(tech_manager1.get_team_info())  
