# create a file named hello.txt (for writing)
# write this text inside "a line of text", "another line of text", "a third line"
# and then close the file

#fh = open
#lines_of_text
#fh.writelines(lines_of_text)
#fh.close()

f = open("hello.txt", "w")
f.write("""a line of text
another line of text
a third line""")
f.close()
