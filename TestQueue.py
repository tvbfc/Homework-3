from DataStructs import *

Q = Queue(5)
for name in ["Leo", "Donnie", "Mikey", "Raph", "Splinter"]:
    Q.insert(name)

print(Q)

for i in range(3):
    ans = Q.remove()
    print("Removed", ans)
    print("Q = ",Q)

for name in ["Huey", "Louie"]:
    Q.insert(name)

print("Length of Q is", len(Q))
print(Q)

for i in range(2):
    ans = Q.remove()
    print("Removed", ans)
    print("Q = ",Q)