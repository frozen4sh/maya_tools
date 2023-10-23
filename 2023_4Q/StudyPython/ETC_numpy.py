#데이터의 차원수(dimension)
import numpy as np

a = np.array(3)
print('a는 %d axis 데이터'%(a.ndim))

b = np.array([3, 6, 9])
print('b는 %d axis 데이터'%(b.ndim))

c = np.array([[3, 6, 9], [2, 4, 8]])
print('c는 %d axes 데이터'%(c.ndim))

print('a는 {} 차원 데이터'.format(a.shape))
print('b는 {} 차원 데이터'.format(b.shape))
print('c는 {} 차원 데이터'.format(c.shape))

#**매트리스 연산**

a = np.array([1, 2])
a_s = 3 * a
print(a_s)
a_dot = np.dot(3, a)
print(a_dot)

a_mul = np.matmul(3, a)

#행렬곱 연산

a = np.array([[1, 2]])
b = np.array([[3, 4]])
c = a * b
print(c)

"""
별연산자를 사용한 위 결과는 같은 인덱스의 원소끼리 곱하는 element-wise 곱연산이 수행된 것이다.

하지만 일반적인 행렬곱 연산을 수행하고 싶다면 다른 연산자를 사용해야 한다.

a 와 b 두 행렬은 1x2 행렬이며, 이 두 행렬을 곱하기 위해서는 두 행렬 중 하나를 전치해야 한다.

b를 전치하여 2x1로 만들어 행렬곱을 수행하면 1x1의 연산값을 얻을 수 있을 것이다.
"""
b_t = b.T # b를 transpose
print(a.shape)
print(b_t.shape)

c = np.matmul(a, b_t)
print(c)
d = np.dot(a, b_t)
print(d)

#**데이터 합치기**  아래 코드를 통해 100x6차원의 두 클래스에 대한 데이터를 하나의 변수로 통합하는 과정을 살펴본다.

# 데이터 생성
x_c1 = np.random.randint(100, size = (100, 6))
x_c2 = np.random.randint(100, size = (100, 6))
# 클래스 할당
y_c1 = np.zeros((100))
y_c2 = np.ones((100))
print("before concatenation")
print("x_c1, c2 dimension : {}, {}".format(x_c1.shape, x_c2.shape))
print("y_c1, c2 dimension : {}, {}".format(y_c1.shape, y_c2.shape))
print('\n')

x_data = np.concatenate((x_c1, x_c2))
y_class = np.concatenate((y_c1, y_c2))

print("after concatenation")
print("x_data dimension : {}".format(x_data.shape))
print("y_class dimension : {}".format(y_class.shape))

#**최소값 최대값 찾기 및 데이터 정규화**

min_x = x_data.min()
max_x = x_data.max()
print("before min-max scaling")
print("x_data 의 min 값 : {}".format(min_x))
print("x_data 의 max 값 : {}".format(max_x))
print('\n')

# min-max scaling
x_scale = (x_data - min_x) / (max_x - min_x)
print(x_scale, '\n')
print("after min-max scaling")
print("x_scale 의 min 값 : {}".format(x_scale.min()))
print("x_scale 의 max 값 : {}".format(x_scale.max()))
