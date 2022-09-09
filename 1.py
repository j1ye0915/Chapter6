def main():
    # Open a file named philosophers.txt.
    outfile = open("philosophers.txt", "a")
 
    outfile.write("Jie Ji" + '\n')
    # Close the file.

    outfile.close()
    # Call the main function.
main()