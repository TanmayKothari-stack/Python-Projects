import matplotlib.pyplot as plt

x1 = ['0', '1', '2', '3', '4', '5', '6', '7']

x2 = ['0', '1', '2', '3', '4', '5', '6']

y = ['0', '10', '20', '30', '40', '50', '60', '70']

ab = ['0', '10', '18', '24', '28', '30', '30', '28']

bc = ['0','2', '6', '4', '8', '10', '0']

['0','10', '8', '6', '4', '2', '0', '-2']

plt.plot(x2, bc, color='red', marker='o', markerfacecolor='maroon', markersize=12, label='BC')

plt.plot(x1, ab, color='Green', marker='o', markerfacecolor='blue', markersize=12, label='AB')


plt.xlabel('data')
plt.ylabel('AB BC & CD ')



plt.title('Business Graph')

plt.legend()

plt.show()