# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.
# Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.
# After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. To track them down, we need to find their delivery ID.
# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.


#Solution
#We XOR ↴ all the integers in the list. We start with a variable unique_delivery_id set to 000. Every time we XOR #with a new ID, it will change the bits. When we XOR with the same ID again, it will cancel out the earlier change.
#In the end, we'll be left with the ID that appeared once!

def find_unique_delivery_id(delivery_ids):
    
    unique_delivery_id = 0
    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id
    return unique_delivery_id


#Complexity
#O(n)O(n)O(n) time, and O(1)O(1)O(1) space.