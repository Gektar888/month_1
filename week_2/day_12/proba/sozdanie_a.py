f =   open("gektarfiles", "a")
f.write(" eto faily gektara!")
f.close()

#open and read the file after the appending:
f = open("gektarfiles", "r")
print(f.read())

