from copy import deepcopy
from typing import Tuple
from datastructures.deque import Deque
from datastructures.array import Array
from datastructures.bag import Bag
from projects.project3.customerorder import CustomerOrder
from projects.project3.orderitem import Drink, OrderItem

class BistroSystem:
    def __init__(self):
        """
        Initializes the Bistro System.

        Utilizes a Deque to track orders made on the system
        and a Bag to keep track of how many of each drink is ordered.
        The drinks are hardcoded in separately for ease of access.
        """
        self._orderqueue = Deque(data_type=CustomerOrder)
        self._end_of_day_report = Bag()
        self._drink_1 = Drink(drink_name="London Fog", drink_price=5.25)
        self._drink_2 = Drink(drink_name="Chai Latte", drink_price=5.50)
        self._drink_3 = Drink(drink_name="Latte", drink_price=5.00)
        self._drink_4 = Drink(drink_name="Hot Choco", drink_price=4.00)
        self._drink_5 = Drink(drink_name="Mocha", drink_price=5.50)
        self._quit: bool = False

    

    def _main_menu(self):
        """
        Displays the Main Menu, the interface that allows the user to interact with the Bistro System.
        """
        print(f"\n📋 Main Menu \n1. Display Menu \n2. Take New Order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End-of-Day Report\n6. Exit")
        while self._quit == False:
               
            entry = input("Enter your choice (Press M to bring up the options): ")
            match entry:
                case "1" :
                    self._display_menu()
                    print("\n📋 Main Menu") 
                case "2" :
                    self._take_order()
                    print(f"\n📋 Main Menu \n1. Display Menu \n2. Take New Order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End-of-Day Report\n6. Exit")
                case "3" :
                    self._view_orders()
                    print("\n📋 Main Menu") 
                case "4" :
                    self._complete_order()
                    print("\n📋 Main Menu") 
                case "5" :
                    self._view_report()
                    print("\n📋 Main Menu") 
                case "6" :
                    self._quit = True
                case "M" | "m":
                    print(f"\n📋 Main Menu \n1. Display Menu \n2. Take New Order\n3. View Open Orders\n4. Mark Next Order as Complete\n5. View End-of-Day Report\n6. Exit")

    
    def _display_menu(self):
        """
        Prints the menu of drinks
        """
        print(f"\n🍹 Bearcat Bistro Menu:\n1.{self._drink_1}\n2.{self._drink_2}\n3.{self._drink_3}\n4.{self._drink_4}\n5.{self._drink_5}")

    def _take_order(self):
        """
        Uses a CustomerOrder and user input to file orders in the Deque.
        """
        new_order = CustomerOrder()
        new_order._add_name(input("\nWhat is your name? "))
        drink_count = int(input("\nHow many drinks would you like? "))
        for i in range(drink_count):
            customer_item = input(f"\nDrink #{i+1}: Which number drink would you like to order? (Type 'menu' to display menu) ")
            match customer_item:
                case "menu" | "MENU" | "Menu" :
                    self._display_menu()
                    customer_item=input("\nWhich number drink would you like to order? ")
                    match customer_item:
                        case "1":
                            new_item = OrderItem(drink=self._drink_1)  
                        case "2":
                            new_item = OrderItem(drink=self._drink_2)
                        case "3":
                            new_item = OrderItem(drink=self._drink_3) 
                        case "4":
                            new_item = OrderItem(drink=self._drink_4)
                        case "5":
                            new_item = OrderItem(drink=self._drink_5)
                case "1":
                    new_item = OrderItem(drink=self._drink_1)  
                case "2":
                    new_item = OrderItem(drink=self._drink_2)
                case "3":
                    new_item = OrderItem(drink=self._drink_3) 
                case "4":
                    new_item = OrderItem(drink=self._drink_4)
                case "5":
                    new_item = OrderItem(drink=self._drink_5)
            new_item._customize(input("\nAny customizations? (If not, please type 'No customization') "))
            new_order._add_to_order(new_item)
        print(f"\nIs this correct?:\n{new_order.get_order()}")
        if input() == "y"or"Y" or "Yes" or "yes" or "YES":
            self._orderqueue.enqueue(new_order)
            print("\n✅ Order placed successfully!")

    def _view_orders(self):
        """
        Prints the list of open orders as a string
        """
        order_list="\n🕒 Open Orders:"
        if len(self._orderqueue) == 0:
            order_list += "\nNone"
        for item in self._orderqueue._deque:
            order_list = order_list + f"\n{item.get_order()}"
        print(order_list)
    
    def _complete_order(self):
        """
        Removes the first order in the Deque and adds the drinks to the Bag.
        """
        resolved_order = self._orderqueue.dequeue()
        for item in resolved_order._order:
            self._end_of_day_report.add(item._drink)
        print(f"\n✅ Completed order for {resolved_order._name}")

    def _view_report(self):
        """
        Prints a table of all ordered items and their total sales value.
        """
        final_report = f"\n📊 End-of-Day Report\n----------------------------\n{"Drink Name":<20}{"Qty":<5}{"Sales":<5}"
        total_sales = 0
        ordered_items = self._end_of_day_report.distinct_items() 
        for item in ordered_items:
            final_report += f"\n{item.drink_name:<20}{self._end_of_day_report.count(item):<5}{self._end_of_day_report.count(item)*item.drink_price:<5}"
            total_sales +=self._end_of_day_report.count(item)*item.drink_price
        final_report += f"\n{"Total":<20}{"":<5}{total_sales:<5}"
        print(final_report)


        

            
        


