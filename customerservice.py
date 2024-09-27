# -*- coding: utf-8 -*-
"""CustomerService

This module manages employees in the customer-service department and tracks customer service metrics such as service quality, number of clients served, average service time, and customer satisfaction.
"""

class CustomerServiceEmployee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.clients_served = 0
        self.total_service_time = 0
        self.customer_satisfaction = []
        self.service_area = ""

    def serve_client(self, service_time, satisfaction_level):
        self.clients_served += 1
        self.total_service_time += service_time
        self.customer_satisfaction.append(satisfaction_level)

    def set_service_area(self, service_area):
        self.service_area = service_area

    def calculate_average_service_time(self):
        return self.total_service_time / self.clients_served if self.clients_served > 0 else 0

    def calculate_average_satisfaction(self):
        return sum(self.customer_satisfaction) / len(self.customer_satisfaction) if self.customer_satisfaction else 0

    def display_customer_service_info(self):
        print(f"Customer Service Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Clients Served: {self.clients_served}")
        print(f"Average Service Time: {self.calculate_average_service_time()} minutes")
        print(f"Average Customer Satisfaction Level: {self.calculate_average_satisfaction()}")
        print(f"Service Area: {self.service_area}")
        print("\n")

class CustomerServiceManager:
    def __init__(self):
        self.cs_employees = {}

    def add_cs_employee(self, emp_id, name, role):
        self.cs_employees[emp_id] = CustomerServiceEmployee(emp_id, name, role)

    def log_service(self, emp_id, service_time, satisfaction_level):
        if emp_id in self.cs_employees:
            self.cs_employees[emp_id].serve_client(service_time, satisfaction_level)

    def set_service_area(self, emp_id, service_area):
        if emp_id in self.cs_employees:
            self.cs_employees[emp_id].set_service_area(service_area)

    def display_cs_employee_info(self, emp_id):
        if emp_id in self.cs_employees:
            self.cs_employees[emp_id].display_customer_service_info()

# Example usage
if __name__ == "__main__":
    customer_service_manager = CustomerServiceManager()

    # Add customer service employees
    customer_service_manager.add_cs_employee(1, "Chris Brown", "Customer Service Rep")
    customer_service_manager.add_cs_employee(2, "Emma Wilson", "Customer Support Specialist")
    customer_service_manager.add_cs_employee(3, "Derek Robinson", "Customer Support Specialist")
    customer_service_manager.add_cs_employee(4, "Rachel Raynolds", "Customer Support Specialist")

    # Log service information
    customer_service_manager.log_service(1, 15, 4.5)  # 15 minutes call with 4.5 satisfaction
    customer_service_manager.log_service(1, 10, 4.0)  # 10 minutes call with 4.0 satisfaction
    customer_service_manager.log_service(2, 20, 5.0)  # 20 minutes call with 5.0 satisfaction
    customer_service_manager.log_service(3, 25, 4.8)  # 25 minutes call with 4.8 satisfaction
    customer_service_manager.log_service(4, 30, 4.7)  # 30 minutes call with 4.7 satisfaction
    customer_service_manager.log_service(4, 18, 4.3)  # 18 minutes call with 4.3 satisfaction

    # Set service area
    customer_service_manager.set_service_area(1, "Product Support")
    customer_service_manager.set_service_area(2, "Technical Assistance")
    customer_service_manager.set_service_area(3, "Technical Support")
    customer_service_manager.set_service_area(4, "Customer Relations")

    # Display customer service info for employees
    customer_service_manager.display_cs_employee_info(1)
    customer_service_manager.display_cs_employee_info(2)
    customer_service_manager.display_cs_employee_info(3)
    customer_service_manager.display_cs_employee_info(4)
