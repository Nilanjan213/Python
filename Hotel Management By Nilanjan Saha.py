class hotelfarecal:

     def _init_(self,rt,s,p,r,t,a,name,address,cindate,coutdate,rno,phno):

          #**********WELCOME TO MUSTANG HOTEL**********
          
          self.rt=rt
          self.r=r
          self.t=t
          self.p=p
          self.s=s
          self.a=a
          self.name=name
          self.address=address
          self.phno=phno
          self.cindate=cindate
          self.coutdate=coutdate
          self.rno=rno

#INPUT
     def inputdata(self):
          self.name=input("\nEnter your name: ")
          self.address=input("\nEnter your address: ")
          self.phno=int(input("\nEnter you phone number (with country code): +"))
          self.cindate=input("\nEnter your check in date: ")
          self.coutdate=input("\nEnter your check out date: ")
          print("\nYour room number is: ",self.rno,"\n")

          self.rno=self.rno+1

#ROOM
     def roomrent(self):

          print("We have the following rooms for you:")

          print("1.  Type A ---> Rs.6000 per night")
          print("2.  Type B ---> Rs.5000 per night")
          print("3.  Type C ---> Rs.4000 per night")
          print("4.  Type D ---> Rs.2500 per night")

          x=int(input("\nEnter you choice please (in numbers): "))

          n=int(input("\nEnter for how many nights you want to stay: "))

          print("\n")

          if(x==1):
               print("You have opted Type A")
               self.s=6000*n

          elif(x==2):
               print("You have opted Type B")
               self.s=5000*n

          elif(x==3):
               print("You have opted Type C")
               self.s=4000*n

          elif(x==4):
               print("You have opted Type D")
               self.s=2500*n

          else:
               print("Please choose a correct room type.")


#RESTAURANT
     def restaurantbill(self):

          print("\n**********RESTAURANT MENU**********\n")

          print("1.  Water ---> Rs. 10/-")
          print("2.  Tea ---> Rs. 20/-")
          print("3.  Breakfast Combo ---> Rs. 90/-")
          print("4.  Lunch ---> Rs. 180/-")
          print("5.  Dinner ---> Rs. 150/-")
          print("6.  Exit")

          while 1:

               c=int(input("\nEnter your choice (in numbers): "))

               if c==1:
                    d=int(input("Enter the quantity: "))
                    self.r=self.r + 10*d

               elif c==2:
                    d=int(input("Enter the quantity: "))
                    self.r=self.r + 20*d

               elif c==3:
                    d=int(input("Enter the quantity: "))
                    self.r=self.r + 90*d

               elif c==4:
                    d=int(input("Enter the quantity: "))
                    self.r=self.r + 180*d

               elif c==5:
                    d=int(input("Enter the quantity: "))
                    self.r=self.r + 150*d

               elif c==6:
                    break

               else:
                    print("Please select a correct option")

          print("Total Food Cost = Rs.",self.r,"\n")


#LAUNDRY
     def laundrybill(self):

          print("\n**********LAUNDRY MENU**********\n")

          print("1.  Shorts ---> Rs. 03/-")
          print("2.  Trouser ---> Rs. 05/-")
          print("3.  Shirt ---> Rs. 07/-")
          print("4.  Jeans ---> Rs. 10/-")
          print("5.  Any kind of Suit --->  Accordingly")
          print("6.  Exit")

          while 1:

               e=int(input("\nEnter Your Choice: "))
     
               if e==1:
                    f=int(input("Enter the Quantity: "))
                    self.t=self.t + 3*f

               elif e==2:
                    f=int(input("Enter the Quantity: "))
                    self.t=self.t + 5*f

               elif e==3:
                    f=int(input("Enter the Quantity: "))
                    self.t=self.t + 7*f

               elif e==4:
                    f=int(input("Enter the Quantity: "))
                    self.t=self.t + 10*f

               elif e==5:
                    print("Please refer to Laundry Incharge.")

               elif e==6:
                    break

               else:
                    print("Please select a correct option.")


          print("\nTotal Laundry Cost = Rs.",self.t,"\n")


#GAME
     def gamebill(self):

          print("\n**********GAME MENU**********\n")

          print("1.  Tabel Tennis ---> Rs. 60/- per hour")
          print("2.  Bowling ---> Rs. 80/- per hour")
          print("3.  Snooker ---> Rs. 70/- per hour")
          print("4.  Video Games ---> Rs. 90/- per hour")
          print("5.  Pool ---> Rs. 50/- per hour")
          print("6.  Exit")

          while 1:
               print("\n")

               g=int(input("Enter Your Choice (in numbers): "))

               if g==1:
                    h=int(input("Enter the number of hours: "))
                    self.p=self.p + 60*h

               elif g==2:
                    h=int(input("Enter the number of hours: "))
                    self.p=self.p + 80*h
                    
               elif g==3:
                    h=int(input("Enter the number of hours: "))
                    self.p=self.p + 70*h

               elif g==4:
                    h=int(input("Enter the number of hours: "))
                    self.p=self.p + 90*h

               elif g==5:
                    h=int(input("Enter the number of hours: "))
                    self.p=self.p + 50*h

               elif g==6:
                     break

               else:
                    print("Please select a correct option.")


          print("Total Game Bill = Rs.",self.p,"\n")


#DISPLAY
     def display(self):
          print("**********HOTEL BILL**********\n")
          print("Customer Details.")
          print("Customer Name:",self.name)
          print("Customer Address:",self.address)
          print("Check in Date:",self.cindate)
          print("Check out Date:",self.coutdate)
          print("Room Number: ",self.rno-1)
          print("Room Rent: Rs.",self.s)
          print("Restaurant Bill: Rs.",self.r)
          print("Laundry Bill: Rs.",self.t)
          print("Game Bill: Rs.",self.p)

          self.rt=self.s + self.r + self.t + self.p

          print("Total Bill Amount: Rs.",self.rt)
          self.a=0.18*self.rt
          print("Additional Tax Charges: Rs.",self.a)
          print("Your Grand Total Bill Amount: Rs.",self.rt + self.a,"\n")


#CHOICE PANEL
     def main(self):

          print("\n**********WELCOME TO MUSTANG HOTEL**********")

          while 1:
               print("\n###### CHOICE PANEL ######")
               print("1. Enter Customer Data")
               print("2. Room Menu")
               print("3. Restaurant Menu")
               print("4. Laundry Menu")
               print("5. Game Menu")
               print("6. Show Total Bill")
               print("7.Exit")

               b=int(input("\nEnter Your Choice (in numbers): "))

               if b==1:
                    a.inputdata()

               if b==2:
                    a.roomrent()

               if b==3:
                    a.restaurantbill()

               if b==4:
                    a.laundrybill()

               if b==5:
                    a.gamebill()

               if b==6:
                    a.display()

               if b==7:
                    break


#RUNNING THE FUNCTION
               
rt=''
s=0
p=0
r=0
t=0
a=1800
name=''
address=''
cindate=''
coutdate=''
rno=101
phno=0
a=hotelfarecal()
a._init_(rt,s,p,r,t,a,name,address,cindate,coutdate,rno,phno)
a.main()
          
