# Very very fast implementation of a partion, might be buggy.

def partition(arr, start, end, pivot):
  while True:
    # Go right
    while True:
      if start == end:
        return start
      if arr[start] >= pivot:
        break
      start += 1

    # Go left
    while True:
      end -= 1

      if start == end:
        return start
      if arr[end] < pivot:
        break

    arr[start], arr[end] = arr[end], arr[start]


def run_one_test(arr, pivot):
  expected_left = [x for x in arr if x < pivot]
  expected_right = [x for x in arr if x >= pivot]

  partition_point = partition(arr, 0, len(arr), pivot)

  actual_left = arr[0: partition_point]
  actual_right = arr[partition_point:]

  assert sorted(expected_left) == sorted(actual_left)
  assert sorted(expected_right) == sorted(actual_right))

def run_tests_for_arr(arr):
  run_one_test(arr.copy(), -1)
  run_one_test(arr.copy(), 1000)

  for x in arr:
    run_one_test(arr.copy(), x)

def tests():
  run_tests_for_arr([])
  run_tests_for_arr([1])
  run_tests_for_arr([1, 2])
  run_tests_for_arr([2, 1])
  run_tests_for_arr([1, 2, 1])
  run_tests_for_arr([1, 1, 1, 1, 1, 1, 0, 0, 0])
  run_tests_for_arr([4, 3, 5, 6, 9, 1, 7, 2, 8])

if __name__ == '__main__':
  tests()
