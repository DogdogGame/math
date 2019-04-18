from vector import Vector

if __name__ == "__main__":
  vec = Vector([5, 2])
  print(vec)
  print(len(vec))
  print("vec[0]={}, vec[1]={}".format(vec[0], vec[1]))

  vec2 = Vector([4, 7])
  print("{} + {} = {}".format(vec, vec2, vec + vec2))
  print("{} - {} = {}".format(vec, vec2, vec - vec2))
  print("{} * {} = {}".format(vec, 4, vec * 4))
  print("{} * {} = {}".format(4, vec, 4 * vec))
  print("+{} = {}".format(vec, +vec))
  print("-{} = {}".format(vec, -vec))

  zero2 = Vector.zero(2)
  print(zero2)
  print("{} + {} = {}".format(vec, zero2, vec + zero2))