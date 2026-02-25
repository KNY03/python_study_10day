dct = {}
dct["id"] = "hong"
dct["pw"] = "1234"
dct["email"] = "hong@gmail.com"

print(dct)
print(dct.keys())
print(dct.values())
print(dct.items())

res = dct.get("id") # dcr["id"]
print(res)

dct.clear()
print(dct)