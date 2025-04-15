elemets = {0}

print(type(elemets))
print(elemets)


elemets.add(10)
elemets.add(70)
elemets.add(30)
elemets.add(20)
elemets.add(40)
elemets.add(50)
elemets.add(60)

print(elemets)

elemets.remove(10)

print(elemets)

elemets.pop()

print(elemets)

elemets.update([100,200,300,400])

print(help(set.update))

print(elemets)

print("---------------------------------------")

s1 = {"Selenium","Cypress","Playwright"}
s2= {"UFT","Playwright","Cypress"}

s3 = s2.difference(s1)  # UFT
s4 = s1.difference(s2)  # Selenium

print(s3)
print(s4)

print("---------------------------------------")

s5 = s1.intersection(s2)

print(s5)