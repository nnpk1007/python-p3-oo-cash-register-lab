#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.title = title
    self.price = price
    self.quantity = quantity

    self.total += price * quantity
    
    for _ in range(quantity):
      self.items.append(title)
  
  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total - self.total * (self.discount/100)
      print("After the discount, the total comes to ${}.".format(int(self.total)))
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    last_price_item = self.price * self.quantity
    self.total -= last_price_item
  