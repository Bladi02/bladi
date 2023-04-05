import math

radio_3=3
radio_8=8
radio_10=10

diametro1=radio_3*2
diametro2=radio_8*2
diametro3=radio_10*2
pi=math.pi
pi_rou=round(math.pi, 6)
circureferncia1= diametro1 * pi_rou
circureferncia2=diametro2 * pi_rou
circureferncia3=diametro3 * pi_rou

print(f'La circurferencia con radio 3 es {circureferncia1}')
print(f'La circurferencia con radio 8 es {circureferncia2}')
print(f'La circurferencia con radio 10 es {circureferncia3}')


