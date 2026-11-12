class Order:
    def __init__(self,customer_name, items, total_amount, discount):
        self.customer_name = customer_name  #public
        self.items = items                  #public
        self.__total_amount = total_amount  #private
        self.__discount = (total_amount * discount)          #private

    def __calculate_final(self):        #private helper method
        return self.__total_amount - self.__discount

    def _get_admin_view(self):       #protected method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Total Amount": f"{self.__total_amount}",
            "Discount Applied": f"{self.__discount}",
            "Final Bill": f"{self.__calculate_final()}"
        }

    def get_customer_view(self):
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Final Bill": f"{self.__calculate_final()}"
        }

class AdminPortal:
    def show_order(self, order):
        return order._get_admin_view()

class CustomerApp:
    def show_order(self, order):
        return  order.get_customer_view()

order = Order("Thiru","Pizza",500,0.20)

admin = AdminPortal()
customer = CustomerApp()

print("Admin View :")
print(admin.show_order(order))

print("\nCustomer View :")
print(customer.show_order(order))
