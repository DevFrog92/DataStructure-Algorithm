# Array

# 1차 배열
data = [1,2,3,4]

# 2차 배열
data2 = [[1,2,3,4],[5,6,7,8]]

# index
print(data[0])

# 2차 배열
print(data2[0])
print(data2[0][0])

# 배열을 표현하는 방법
for lst in data2:
    print(*lst)