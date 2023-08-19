#Task, To Create and get output in the given format for 3 different employees from different firm using CLASS

class emp:
    def __init__(self,company_name,ID,FirstName,LastName,Salary,branch,location,dob,AadharID):
        self.CpyNm=company_name
        self.id=ID
        self.name=FirstName
        self.Nm=LastName
        self.salary=Salary
        self.br=branch
        self.lo=location
        self.DOB=dob
        self.CpyID=self.CpyNm+self.id
        self.aadharID=AadharID


class TCS(emp):  #TCS Input format("Company Name","ID","First Name","Last Name",Salary,"branch","location","dob","AadharId or None")
    def TCS_Salary_Format(self):
        self.salary=f"{float(self.salary):.2f}"
    def show(self):#poly
        print("Empoyee ID ",self.CpyID,"\nEmployee Name ",self.name,self.Nm,"\nEmployee Salary ",self.salary, "\nBranch",self.br, "\nLocation",self.lo,"\nDOB",self.DOB)

class HCL(emp):  #HCL Input format ("Company name","ID","FNam","LNam",Salary,"gender","blood group","doj","AadharId or None")
    def HCL_Salary_Format(self):
        self.salary=int(self.salary -(0.1*self.salary))
    def update(self,EmpID):
        self.ID=EmpID
    def update(self,gender):
        self.branch=gender
    def update(self,blood_group):
        self.location=blood_group
    def update(self,doj):
        self.dob=doj
    def show(self):
        print("Empoyee ID",self.CpyID,"\nFirst Name ",self.name,"\nLast Name ",self.Nm,"\nSalary ",self.salary, "\nGender ",self.br,"\nBlood Group ",self.lo,"\nDOJ",self.DOB)


class Infy(emp):  #Infy Input format ("Company name","ID","First Name",Last Name", salary,"experience in yrs","phNo","address","AadharID")
    def Infy_Salary_Format(self):
        self.salary=(12*self.salary)
    def update(self,exp):
        self.br=exp
    def update(self,Mob):
        self.lo=Mob
    def update(self,address):
        self.dob=address
    def show(self):
        print("Employee ID",self.CpyID,"\nName",self.name,self.Nm,"\nSalary ",self.salary,"LPA" "\nExperience ",self.br,"yrs \nPhNo ",self.lo,"\nEmp Address ",self.DOB,"\nAadharID ",
              self.aadharID)


#SAMPLE INPUTS
E=TCS("TCS","23","Shabari","P",30000,"TNagar","Chennai","01/01/1990","None") #TCS Employee details
F=HCL("HCL","112","Ironman","JR",34000,"Male","B+ive","01/05/2023","None")   #HCL Employee details
G=Infy("Infy","263","Sandeep","R",55000,"5","8344214779","Karamadai,Coimbatore,Tamil Nadu","123456789") #Infy Employee details


print("TCS   EMPLOYEE    DETAILS")
E.TCS_Salary_Format()
E.show()

print("") #To print an empty line for differentiation

print("HCL  EMPLOYEE  DETAILS")
F.HCL_Salary_Format()
F.show()

print("") #To print an empty line for differentiation

print("INFY   EMPLOYEE  DETAILS")
G.Infy_Salary_Format()
G.show()

