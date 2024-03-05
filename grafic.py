import matplotlib.pyplot as plt
x = [0,2,5,32,64,127,255,256]
y= [0.05,0.076,0.12, 0.46, 0.86, 1.68, 3.25,3.3]
plt.plot(x,y,'.-', markersize=10, color = 'black')
plt.title('Супер график')
plt.xlabel('Цифры')
plt.ylabel('Напряжение')
plt.grid(True)
plt.show()