from Linked_List import Linked_List

def Josephus(ll):
  while len(ll) > 1:
    ll.rotate_left()
    ll.remove_element_at(0)
    print(ll)
  print("The survivior is: " + str(ll.get_element_at(0)))

if __name__ == '__main__':
  ll = Linked_List()
  n = int(input("Input the total number of people: "))
  for i in range(1, n+1):
      ll.append_element(i)
  print("Initial order:", ll)
  Josephus(ll)
