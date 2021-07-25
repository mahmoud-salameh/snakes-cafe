print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
)

menu=[
    'wings', 'cookies', 'spring rolls', 
    'salmon', 'steak', 'meat tornado', 
    'a literal garden', 'ice Cream', 
    'cake', 'pie', 'coffee', 'tea', 
    'unicorn tears'
]

Orderlist=[]
nameInList=[]
def inputOrder():
    
    order=input('--> ')
   
    order = order.capitalize()
    if order.lower() in menu:
        Orderlist.append(order)
       
        if order not in nameInList:
            nameInList.append(order)
        print(f'**{Orderlist.count(order)} order of {order} have been added to your meal **')
        inputOrder()
    elif order.lower()=='quit':
        
        for i in nameInList:
            print(f'{Orderlist.count(i)} order of {i} ')
    elif order.lower() not in menu:
        print('**Your order is not in our menu**')

inputOrder()
