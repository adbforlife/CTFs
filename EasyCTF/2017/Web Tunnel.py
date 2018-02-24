import os
string = "I3tnN3iUqCNobYACYG70"
result = ""
def decode(string):
    os.system("C:\\Users\\X51-6808\\Desktop\\ZBar\\zbarvars.bat && zbarimg http://tunnel.web.easyctf.com/images/Hbnp0n9n6J5IDqivLZZv > C:\\Users\\X51-6808\\Desktop\\test.txt && exit")
    for i in range(5):
        file = open("C:\\Users\\X51-6808\\Desktop\\test.txt", "r")
        string = file.read()[8:].rstrip()
        if not string == "":
            result = string
        else:
            print("damn it")
        string = "http://tunnel.web.easyctf.com/images/" + string
        print(string)
        file.close()
        os.system("C:\\Users\\X51-6808\\Desktop\\ZBar\\zbarvars.bat && zbarimg " + string + " > C:\\Users\\X51-6808\\Desktop\\test.txt && exit")
    for i in range(5):
        file = open("C:\\Users\\X51-6808\\Desktop\\test.txt", "r")
        string = file.read()[8:].rstrip()
        if not string == "":
            result = string
        else:
            print("damn it")
        print(result)
        string = "http://tunnel.web.easyctf.com/images/" + string
        print(string)
        file.close()
        os.system("C:\\Users\\X51-6808\\Desktop\\ZBar\\zbarvars.bat && zbarimg " + string + " > C:\\Users\\X51-6808\\Desktop\\test.txt && exit")
decode(string)
print(result)
print("hi")
