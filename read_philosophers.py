import readline


def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', "r")
 
    # Read the file's contents.
    
    #file_content = infile.read()
    file_content = infile.readline()

    #Print the data that was read into memory.
    line1 = infile.readline.rstrip('\n')
    line2 = infile.readline.rstrip('\n')
    line3 = infile.readline.rstrip('\n')

    print(line1)
    print(line2)
    print(line3)
    #print(file_content)

    #Call the main function.
main()