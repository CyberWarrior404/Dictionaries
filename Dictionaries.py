#Dictionary:
Dict={
    "Russia":"Moscco", 
    "France":"Paris", 
    "Canada":"Ottawa"
}
print(Dict)
print(Dict.keys())
print(Dict.values())

for i in Dict.keys():
    print(i)

Dict["Germany"]="Berlin"
print(Dict)

del(Dict["France"])
print(Dict)

for i in Dict.values():
    print(i)

Dict["Germany"]="Berlin"
print(Dict)

print(Dict)

Dict["Germany"]="Burgerlin"

print(Dict)

if "France" in Dict:
    print("Germany made Burger")
else:
    print("World iS not made burger")
