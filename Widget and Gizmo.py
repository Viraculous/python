# Excercise 2
#This excercise is an hypothetical example of a store which sells only two items

'''An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.'''

#Here are my global variables
import random
print("Buy your Gizmo and Widget at Viraculous store")
wigdet_weight = 75
gizmo_weight = 112

#Error handling
try:
    no_of_widget_ordered = float(input("order your widget: "))
except ValueError:
    print("Error...numbers only. Retry")
    quit()

try:
    no_of_gizmo_ordered = float(input("order your gizmo: "))
except ValueError:
        print("Error...numbers only. Retry")
        quit()

#This is the total weight of gizmo and widget ordered respectively       
order_weight_of_gizmo = gizmo_weight * no_of_gizmo_ordered
order_weight_of_widget = wigdet_weight * no_of_widget_ordered

#stock of goods for each item is randomly generated,thus, the available stock is flexible
gizmo_stock_available = (random.randrange(1,1000)) - no_of_gizmo_ordered
widget_stock_available = (random.randrange(1,1000)) - no_of_widget_ordered

#since available stock is flexible given the available stock of the objects,the "available_stock" function can be positive or negative except being constrained by some conditional statements
def available_stock(gizmo_stock_available,widget_stock_available):
    return gizmo_stock_available + widget_stock_available

#The total order weight is the objective of this excercise but i decided to add some more functions to the excercise
def total_order_weight(order_weight_of_gizmo,order_weight_of_widget):
    return order_weight_of_gizmo + order_weight_of_widget


print("gizmo stock = ", gizmo_stock_available)
print("widget stock = ", widget_stock_available)
print("Total available stock is ", available_stock(gizmo_stock_available,widget_stock_available)," pieces")
print ("Your total order weight is ",total_order_weight(order_weight_of_gizmo,order_weight_of_widget))