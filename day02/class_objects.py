"""
public class Item{
String itemName;
double itemPrice;

static String madeIn = "China"
public Item(String itemName,double itemPrice){
this.itemName = itemName;
this.itemPrice = itemPrice;
}
}
"""

class Item:

    made_in= 'China' # static variable
    tariffs = "100%"  # static variable
    def __init__(self,itemName,itemPrice):
        self.itemName =itemName  #instance variable
        self.itemPrice =itemPrice #instance variable

    def __str__(self):
        # return f'Item Name: {self.itemName}, Item Price: {self.itemPrice}'
         return f'{type(self).__name__} {self.__dict__}'


item1 = Item("Egg",3.99)
item2 = Item("Book",6.99)

print(item1)
print(item2)

print(item1)
print(item2)

print(Item.made_in)
print(Item.tariffs)

Item.class_method()
Item.static_method()

"""
Create Employee class:
    instance variables: employee_name, job_title, salary
    static_variables: pay_tax

    instance methods: 
        __init()__: declares and initalizes all the isnace variables
        __str()__: creates string version of the object
        work(): displaye  ${employee_name} is working

    class method:
        display_employee_tax_rate()


"""