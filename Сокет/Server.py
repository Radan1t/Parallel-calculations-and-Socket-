import socket
import numpy as np

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
matrix = [[-100, 50, 10, 25, 30], [50, -60, 5, 10, 25], [10, 5, -50, 20, 50], [25, 10, 20, -40, 10],
          [30, 25, 50, 10, -10]]
eigenvalues, eigenvectors = np.linalg.eig(matrix)
L1 = np.max(eigenvalues)
print("Найбільше власне число(L1):", L1)
client.connect(('192.168.0.104', 7000))
Test = True
while Test:
    print("З'єднання відбулося")
    client.send(str(L1).encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    if response:
        print("Received from server:", response)
        try:
            L2 = float(response)
            print("Converted to float:", L2)
            Test = False
        except ValueError:
            print("Could not convert to float:", response)
            Test = False
print("Найбільше власне число(L2):", L2)
if L1>L2:
    L3=pow(L1,2)*L2
    print("L3 =", L3)
elif L1<L2:
    L3=pow(L2,2)*L1
    print("L3 =", L3)
else:print("L1=L2")
