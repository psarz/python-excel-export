from sys import argv
#import for using argument variable librery

script, filename  = argv
# defined to argument variables script and filename

txt = open(filename)

#we called a function to read file content

print "here's your file %r:" % filename
#we are printing the content of the file.

print txt.read()
#in this line we are printing the value in txt using the read method

print "Type the file name again:"
file_again = raw_input(">")
#taking the input from the user by using raw_input , which will store in file_again

txt_again = open(file_again)
#defined a new variable txt_again and putting the value of file again in it using the open method.


print txt_again.read()

#reading the value of txt_again using the read method.
