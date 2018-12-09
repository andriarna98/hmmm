from Models.Customer import Customer
import csv

class Customer_repo:
    def __init__self(self):
        pass

    # def add_video(self, Car):
    #     # first add to file then to private list
    #     with open("data/Cars.csv", "a+") as Cars_file:
    #         car_size = video.get_car_size()
    #         plate_number = video.get_plate_number()
    #         brand = get_video.brand()
    #         Cars_file.write("{},{},{}\n".format(car_size, plate_number, brand))

    def get_customer(self):
        self.customer_dict = {}
        with open("./data/Customers.csv", "r") as Customer_file:
            csv_reader = csv.reader(Customer_file)
            next(csv_reader)
            
            for line in csv_reader:
                email, name, phone, creditcard = line
                new_customer = Customer(email, name, phone, creditcard)
                key = new_customer.get_email() #key er email
            
                self.customer_dict[key] = new_customer

        return self.customer_dict