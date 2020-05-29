import itertools

# Given 5 integers, find the median

# Vagely based on:
# https://cs.stackexchange.com/questions/44981/least-number-of-comparisons-needed-to-sort-order-5-elements

def median_of_five_ints(x1, x2, x3, x4, x5):
  #  If the value is bigger/smaller then 3 other I don't care for it

  if x2 < x1:
    x1, x2 = x2, x1
  if x5 < x4:
    x4, x5 = x5, x4

  if x5 < x2:
    x1, x4 = x4, x1
    x2, x5 = x5, x2

  # x1 <= x2 <= x5 , x2 <= x5, x4 <= x5 (?) x3

  # Insert x3 in x1, x2, x5
  if x3 >= x2:
    if x3 >= x5:
      x3 = x5  # x3 >= x5 >= x2 >= x1 - don't care
  else:
    if x3 <= x1:
      # x3 <= x1 <= x2 <= x5 - don't care for x3
      x3 = x2
      x2 = x1
    else:
      x2, x3 = x3, x2

  # x1 <= x2 <= x3 <= x5 ? x4 <= x5
  # x1, x5 - don't care, not the answer

  if x3 <= x4:
    # x1 <= x2 <= x3 <= x4 <= x5
    return x3

  if x2 <= x4:
    # x1 <= x2 <= x4 <= x3 <= x5
    return x4

  # x1 <= x2, x4 <= x2, x2 <= x3 <= x5
  return x2


def tests():
  for permutation in itertools.permutations([10, 20, 30, 40, 50]):
    res = median_of_five_ints(*permutation)
    assert res == 30

if __name__ == '__main__':
  tests()
