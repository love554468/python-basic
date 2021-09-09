from iteration_utilities import deepflatten

# Nếu bạn chỉ có một lồng 1 cấp, sử dụng cái này
def flatten(l):
  return [item for sublist in l for item in sublist]

l = [[1,2,3],[3]]
print(flatten(l))
# [1, 2, 3, 3]

# Nếu bạn không biết list lồng sâu thế nào
l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]

print(list(deepflatten(l, depth=3)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 