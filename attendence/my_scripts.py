import csv

class Participant:

    def __init__(self,username,phone,email,semester):
        self.username=username
        self.phone=phone
        self.email=email
        self.semester=semester
    
    def __init__(self) -> None: 
        pass

    #Input data of current object from the console    
    def inputDataConsole(self):
        
        self.username= input("Enter name \n")
        self.phone=int(input("Enter phone \n"))
        self.email=input("Enter email \n")
        self.semester=int(input("Enter semester \n"))

    def assignData(self,username,semester, phone,email):
        self.username=username
        self.phone=phone
        self.email=email
        self.semester=semester

    #Output to console data stored in object
    def outputDataConsole(self):
        print(self.username)
        print(self.phone)
        print(self.email)
        print(self.semester)

    #Write the data of Current user in csv file
    def outputDataCSV(self):
        user_info=open("user_info.csv",'a')
        writer= csv.writer(user_info, lineterminator='\r')
        row = (self.username, self.semester, self.phone,self.email)

        writer.writerow(row)
        user_info.close()
    
    
    #Directly Assigns data to object if The Item is found in CSV
    def inputDataCSV(self,search_name):
        data = list()
        data= displayInfo(searchNameCSV(search_name))
        if (data != -1):
            self.assignData(self, data[0],data[1], data[2],data[3])
            return 1
        else:
            return -1

    #Prints all data in CSV file
def readAllDataCSV():
    user_info=open('user_info.csv')
    reader = csv.reader(user_info)
    for line in reader:
        print(line)
    user_info.close()
    
    #returns location of Searched Name in the file
def searchNameCSV(search_name):
     user_info=open('user_info.csv','r')
     reader = csv.reader(user_info)
     counter = 0
     for line in reader:
         # print (line)
         for x in line:
             if (x == search_name):
                 user_info.close()
                 return counter
             else:
                 break
         counter+=1
     
     user_info.close()
     return -1
        
    #Outputs list of userinfo in the location supplied
def displayInfo(item_no):

    if (item_no != -1):
            
        user_info= open("user_info.csv", 'r')
        reader = csv.reader(user_info)
        counter=-1;
        for line in reader:
            counter+=1
            if (counter == item_no):
                user_info.close()
                return line
        
        user_info.close()
    return -1

def noOfItem():
    user_info = open("user_info.csv",'r')
    reader= csv.reader(user_info)
    counter = -1
    for line in reader:
        counter += 1
    return counter

def createId(unique_name):
    id_file= open("id_file.csv","rw")

    writer= csv.writer(id_file,lineterminator = '/r')





#all the code below commented or not are for testing purpoes
# p1 = Participant
# p1.inputDataConsole(p1)
# p1.outputDataConsole(p1)
# p1.outputDataCSV(p1)
# p1.readAllDataCSV(p1)

# print(p1.searchNameCSV("asdas"))
# print(p1.displayInfo(0))

# p1.inputDataCSV(p1,"asdasy")
# print(p1.username, p1.email,p1.phone,p1.semester)