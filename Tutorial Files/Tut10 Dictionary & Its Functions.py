#Dictionary is nothing but key value pairs.
d1 = {}
#print(type(d1))
d2 = {"Amazon":"Jeff Bezos",
      "Microsoft":"Bill Gates",
      "Apple":"Steve Jobs",
      "Burger":{"A":"Burger King", "B":"Burger Farm", "C":"MacDonalds"}}

#print(d2["Burger"]["A"])
#d2["Bready"] = "Harshil"
#d2[12] = "abcd"
#print(d2)
#del d2[12]

d3=d2.copy()
del d3["Amazon"]
#print(d3)
#print(d2)

#print(d2.get("Amazon"))
#d2.update({"leo":"messi"}))

#print(d2.keys())
#print(d2.items())