# Exercise 1.3 Bestseller Chart

# Imagine an online store with millions of items in its catalogue. For each
# item, the store keeps track of how many instances it sold. Hundreds of
# sales transactions are completed every second and a web page with a list
# of the top 100 best sellers is refreshed every minute. 

# 1. How would you generate such a list? 

# My first thought was to create a list with all possible items in the catalogue with the
# list index uniquely identifying each item. With the value being the number of times
# that item has been sold. If a new item is added to the catalogue,
# it is appended to the list and the corresponding index is its unique identifier.
# However, the problem with this is we do not have any information to store each item's place
# ordered in terms of the number sold.
# Another issue is that creating a complete list is a waste of memory. Many items will not have
# been purchased once and so do not need to be stored. Suppose the catalogue contains
# one trillion items. Then there may be insufficient storage to store all items in the list.
# (Although, considering the catalogue already contains one trillion items, these one trillion
# items would have to be stored somewhere).


# After each sale has been made (which would happen hundreds of times per second)
# I would insert the item in the right place using the insertion algorithm in insertion sort
# the item which has been sold is the key and would be compared with the items that originally
# had more sales (elements nearer the start of the list) until the insertion point is found
# at which point the item which has been sold would be inserted.


# How long would it take to run this computation? 
# How long would it take if, hypothetically, the store had billions or trillions of
# different items for sale instead of merely millions? Of course you could
# re-sort the whole catalogue each time and take the top 100 items, but
# can you do better? And is it cheaper to maintain the chart up to date
# after each sale hundreds of times per second, or to recompute it from
# scratch once a minute? (You note here that we are not merely concerned
# with finding an algorithm, but also with how to estimate the relative performance of different alternatives, before actually running them.)