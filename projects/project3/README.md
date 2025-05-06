For my bistro system, I use a dataclass to store Drink information, and store this and a string customization in a new class, called OrderItem.

The OrderItem is the building block of the CustomerOrder, which uses a LinkedList for its basic structure. This allows me to create orders of infinite length without the expensive complexity of array resizing. It allows me to iterate in linear time, as well, not particularly slower than any of the other data types we have worked with.

The CustomerOrder is then placed into a Deque in the BistroSystem, allowing me to track the most recent and oldest order, and complete the longest outstanding order. Since I only access the front and rear elements, except for while viewing all outstanding orders, time complexity was not a major factor for determining which data structure to use for the OrderQueue, and I focused on which data structure worked intuitively.

For the End of Day Report, I place all Drinks (pulled from their respective OrderItems) from an order into a Bag once the order is completed. This allows me to track the count of each item total, as well as store both the drink's name and price for accurate reporting. The Bag will only ever hold 5 items, so this is a good way of saving space and time.

To use this system, the user need simply follow the prompts presented in the terminal. Each choice and each drink is given a number to streamline the input required, and the menu can be brought up while ordering by inputting menu at when asked for a drink. In order to return to the main menu, the user may press M when prompted to enter a choice, if a reminder of the associated numbers is required.

Sample output for Displaying Menu:
    📋 Main Menu
    1. Display Menu
    2. Take New Order
    3. View Open Orders
    4. Mark Next Order as Complete
    5. View End-of-Day Report
    6. Exit
    Enter your choice (Press M to bring up the options): 1

    🍹 Bearcat Bistro Menu:
    1.London Fog : $5.25
    2.Chai Latte : $5.50
    3.Latte : $5.00
    4.Hot Choco : $4.00
    5.Mocha : $5.50

Sample output for Ordering, including bringing up the menu while ordering:
    📋 Main Menu
    Enter your choice (Press M to bring up the options): 2

    What is your name? Roman

    How many drinks would you like? 4

    Drink #1: Which number drink would you like to order? (Type 'menu' to display menu) 4

    Any customizations? (If not, please type 'No customization') No customization

    Drink #2: Which number drink would you like to order? (Type 'menu' to display menu) 1

    Any customizations? (If not, please type 'No customization') No customization

    Drink #3: Which number drink would you like to order? (Type 'menu' to display menu) 2

    Any customizations? (If not, please type 'No customization') No customization

    Drink #4: Which number drink would you like to order? (Type 'menu' to display menu) menu

    🍹 Bearcat Bistro Menu:
    1.London Fog : $5.25
    2.Chai Latte : $5.50
    3.Latte : $5.00
    4.Hot Choco : $4.00
    5.Mocha : $5.50

    Which number drink would you like to order? 5

    Any customizations? (If not, please type 'No customization') No customization

    Is this correct?:
    Roman: ['Hot Choco (No customization)', 'London Fog (No customization)', 'Chai Latte (No customization)', 'Mocha (No customization)']
    Yes

    ✅ Order placed successfully!

Sample output for Viewing Orders and Completing Orders:
    📋 Main Menu
    Enter your choice (Press M to bring up the options): 3
    
    🕒 Open Orders:
    Roman: ['Hot Choco (No customization)', 'London Fog (No customization)', 'Chai Latte (No customization)', 'Mocha (No customization)']

    📋 Main Menu
    Enter your choice (Press M to bring up the options): 4

    ✅ Completed order for Roman

    📋 Main Menu
    Enter your choice (Press M to bring up the options): 3

    🕒 Open Orders:
    None

Sample output for Viewing End of Day Report, as well as bringing back up the Main Menu:
    📋 Main Menu
    Enter your choice (Press M to bring up the options): m

    📋 Main Menu
    1. Display Menu
    2. Take New Order
    3. View Open Orders
    4. Mark Next Order as Complete
    5. View End-of-Day Report
    6. Exit
    Enter your choice (Press M to bring up the options): 5
    
    📊 End-of-Day Report
    ----------------------------
    Drink Name          Qty  Sales
    Hot Choco           1    4.0
    London Fog          1    5.25
    Chai Latte          1    5.5
    Mocha               1    5.5
    Total                    20.25


As far as I have tested, the only known issues are cases where the customer incorrectly responds to prompts, such as by not using a drinks number, as putting in the name will cause it to add the previous drink back to the order, as the variable for the item to be added is never updated. Should the user use correct inputs, there should be no additional issues, unless an edge case exists which I have not thought of.

If I were to continue to work on this, my main desire would be to add a function where a rejected order (one that failed to confirm) would clear the order and work back through each drink again. I tried to do this, but it did not have the desired effect without needlessly complicating the code.

Since I have your time, I would like to apologize for late submission. As it is finals week, I have been fairly busy, but I wanted to be sure to get this in before 5 days beyond the due date regardless.