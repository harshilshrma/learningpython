f = open("harshil.txt", "rt")   #dusra argument of our fn is MODE, which is r&t here(both default only) no need to write
print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())

#content = f.read()             #isko hataya coz content ne ek baar file ko read kr liya
                                #to fir print nahi krega, as kuch nahi bacha

#for line in f:
#print(line, end="")            #end coz \n character hai file mein, jisse line gap aa rha tha

#print(content)
# content = f.read(3445)
# print("1", content)
# content = f.read(3424)
# print("2", content)

f.close()


