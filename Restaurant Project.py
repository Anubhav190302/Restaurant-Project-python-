#!/usr/bin/env python
# coding: utf-8

# In[1]:


# menu of resturant
menu = {
    'Pizza': 50,
    'Pasta': 100,
    'Burger': 30,
    'Salad': 70,
    'Coffee': 60
}


# In[2]:


print (menu)


# In[3]:


#greet
print("Welcome to Anubhav Resturant")
print("Pizza : Rs 50\nPasta : Rs 100\nBurger : Rs 30\nSalad : Rs 70\nCoffee : Rs 60")


# In[4]:


order_total = 0


# In[5]:


item_1 = input("Enter the name of the item you want =")
if item_1 in menu:
    order_total += menu [item_1]
    print("your item has been added to your order")
    
else :
    print ("Ordered item is not available yet")


# In[6]:


item_1 = input("Enter the name of the item you want =")
if item_1 in menu:
    order_total += menu [item_1]
    print("your item has been added to your order")
    
else :
    print ("Ordered item is not available yet")


# In[9]:


another_order = input("do you want another order (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of 2nd item")
if item_2 in menu:
    order_total += menu [item_2]
    print("your item has been added to your order")
    
else :
    print ("Ordered item is not available yet")

print ("The total amaount of item to pay is {order_total}")


# In[11]:


menu = {
    'Pizza': 50,
    'Pasta': 100,
    'Burger': 30,
    'Salad': 70,
    'Coffee': 60
}

order_total = 0

item_1 = input("Enter the name of the item you want =")
if item_1 in menu:
    order_total += menu [item_1]
    print("your item has been added to your order")
    
else :
    print ("Ordered item is not available yet")

another_order = input("do you want another order (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of 2nd item")
if item_2 in menu:
    order_total += menu [item_2]
    print("your item has been added to your order")
    
else :
    print ("Ordered item is not available yet")

print (f"The total amaount of item to pay is {order_total}")   


