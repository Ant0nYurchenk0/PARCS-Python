import math
def get_hash(key, prime):
  result = 0
  for i in range(0, len(key)):
    result += ord(key[i])*math.pow(prime, i)
  return int(result)

if __name__=="__main__":
  print(get_hash("lab_on_parcs_in_python", 4391))