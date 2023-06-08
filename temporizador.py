import time

t = int(input("\nDigite o tempo do temporizador : "))
print("\n")
while t>=0:
    minutos, segundos = divmod(t,60)
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    print(timer, end='\r')
    time.sleep(0.3)
    t=t-1

print("\n\n  Eeee acabou!")
input()