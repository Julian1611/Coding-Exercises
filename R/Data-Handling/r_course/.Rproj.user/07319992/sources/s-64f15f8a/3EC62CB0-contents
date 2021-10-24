 # assign number to a
a <- 2
 #print a
a



 # initiate integer vector to b
b <- c(10, 22, 33, 22, 40)
 # assign names to elements in b
names(b) <- c("Andy","Betty","Claire","Daniel","Eva")
 # print by element's number: third element 
 # (index: R starts counting at 1, not 0!)
b[3]
 # print by element's name
b["Claire"]
 
 # see what class an object belongs to
class(b)
 # get a summary of its structure
str(b)



 # read a webpage's source code into RAM (download website)
weatherHTML <- readLines("https://www.nzz.ch/wetter/wetter-heute")
 # have a look at the first three lines of the webpage's source code
head(weatherHTML, 3)
 # more in depth look at the website:
View(weatherHTML)

 # how to get today's temperature from the webpage:
 #
 # search source code for the line that contains today's maximum temperature
line_number <- grep("weatherlist__temp--max", weatherHTML)
 # we can now check the line in which its found
line_number
 # weather extracted for today and tomorrow:
weatherHTML[line_number]
 # how to extract temperature only (not important for now):
strsplit(weatherHTML[line_number[1]], split = "span")
 # pick corresponding line and filter the text for numbers:
temperature <- strsplit(weatherHTML[line_number[1]], split="span")[[1]][5]
gsub("\\D", "", temperature)



 # output to local hard drive
writeLines(weatherHTML, "weather.html")



 # pointNemo.txt exercise
 # 
 # always read data and inspect first rows!
 #  
 # make sure, working directory is correct!!!
 # (use setwd("./..") to get back one step, setwd("./../..") for two steps, etc.
 # and getwd() to check working directory)
 #
 # read data:
point_nemo <- 
        read.table("./data/PointNemo.txt", skip = 9,
                   colClasses = c("character", "NULL", "numeric"),
                   col.names = c("date", "", "temp"))
 # inspect first rows:
head(point_nemo)


 # same exercise with Eurasia.txt (see data folder)
 # 
 # read data:
eurasia <- 
        read.table("./data/Eurasia.txt", skip = 9,
                   colClasses = c("character", "NULL", "numeric"),
                   col.names = c("date", "", "temp"))
 # inspect first rows:
head(eurasia)


 # add strings
f <- "3"
g <- "1.5"
paste(f, g, sep = "")