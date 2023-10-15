# naive code
def edit_distance_naive(str1, str2):
  distance = []
  for i in range(len(str1) + 1):
    distance.append([i] * (len(str2) + 1))

  for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
      if str1[i - 1] == str2[j - 1]:
        distance[i][j] = distance[i - 1][j - 1]
      else:
        distance[i][j] = 1 + min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1])

  return distance[len(str1)][len(str2)]


# recursive code
'''def edit_distance_recursive(str1, str2, i, j):
  if i == len(str1):
    return len(str2) - j
  if j == len(str2):
    return len(str1) - i

  if str1[i] == str2[j]:
    return edit_distance_recursive(str1, str2, i + 1, j + 1)

  return 1 + min(
    edit_distance_recursive(str1, str2, i + 1, j),
    edit_distance_recursive(str1, str2, i, j + 1),
    edit_distance_recursive(str1, str2, i + 1, j + 1)
  )
'''
str1 = "geek"
str2 = "gesek"
'''print(edit_distance_recursive(str1, str2, 0, 0))
'''
print(edit_distance_naive(str1, str2))
