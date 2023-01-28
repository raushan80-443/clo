with open ("end.txt","r") as file:
    lists = file.readlines()



startwords = []
user = input("Enter the word start: ")
while user != "over":
    startwords.append(user)
    user = input("Enter the word start: ")

    




with open("new.txt",'a')as wr:
    for each in lists:
        for eachone in startwords:
            wr.write(eachone+each)