# difference between list and tuple
# list is mutable, tuple is immutable

def list_vs_tuple():
  mylist = [1, 2, 3]
  mytuple = (1, 2, 3)
  mylist[0] = 10  # This is allowed
  mytuple[0] = 10  # This will raise an error
  return mylist, mytuple

def main():
  mylist, mytuple = list_vs_tuple()
  print("List:", mylist)
  print("Tuple:", mytuple)