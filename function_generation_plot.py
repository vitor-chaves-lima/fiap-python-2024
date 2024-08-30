import matplotlib.pyplot as plt
import function_generation


def generate_points(min, max, point_count):
    diff = max - min
    steps = diff / point_count
    points_list = []
    for i in range(point_count):
        points_list.append(i*steps)
    return points_list

x1_values = generate_points(0, 3.5, 600)
x2_values = generate_points(3.5, 6, 200)

y1_values = []
y2_values = []

for i in x1_values:
    y1_values.append(function_generation.y(i))

for i in x2_values:
    y2_values.append(function_generation.y(i))

plt.plot(x1_values,y1_values, linestyle='dotted')
plt.plot(x2_values,y2_values, linestyle='dotted')

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.axis([0, 10, 0, 10]) 
plt.title("Título do meu gráfico")
plt.show()