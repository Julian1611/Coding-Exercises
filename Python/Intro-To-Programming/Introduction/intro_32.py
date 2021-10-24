# read from the file hello.txt that you created previously
# if needed you can combine the code in here and first write and then read the file content
# NOTE: once you read it print the content

#fh = open
#print fh.readlines()

f = open("hello.txt", "w")
f.write("""a line of text
another line of text
a third line""")
f.close()

f = open("hello.txt", "r")
reddit = f.readlines()
for i in reddit:
  print(i)
f.close()
