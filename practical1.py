thisdictionary={"fruit":"mango","vegetabe":"tomato","car":"Mercedes-Benz EQE","bike":"royal enfield"}

def is_key_present(x):
  if x in thisdictionary:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')

is_key_present("car")
is_key_present(5)