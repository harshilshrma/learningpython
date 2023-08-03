s = set()
#print(type(s))
#s_from_list = set([1,2,3,4])
#print(s_from_list)

s.add(1)
s.add(2)
#s1 = s.union({1,2,3}) #intersection blA BLA
#print(s,s1)
#print(len(s))
#print(type(s))
#print(min(s))
#print(max(s))

print(s)
s2 = {1,2,3,4,5,6}
print(s.isdisjoint(s2))
print(s.issubset(s2))
print(s2.issuperset(s))
print(s2.discard(3))
print(s2)