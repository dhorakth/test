class Account:
	bname="SBI"
	def __init__(self,acno,name,bal):#parametalized constructor
		self.acno=acno
		self.name=name
		self.bal=bal
	def disp(self,city="HYD"):
		print("_"*40)
		print("Account Number=",self.acno)
		print("Account Name=",self.name)
		print("Account Bal=",self.bal)
		print("Account avilable in=",Account.bname)
		print("Name of city=",city)
		print("_"*40)
#Main Program
ao1=Account(10,"DR",1000)
ao1.disp()
ao2=Account(20,"RS",2000)
ao2.disp()
ao3=Account(12,"JG",3000)
ao1.disp()