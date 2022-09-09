def main():

    i = 0
    with open('clients.txt','r') as f:
        for line in f:
            i += 1
            print(i,". " ,line.rstrip('\n'),sep='')

main()