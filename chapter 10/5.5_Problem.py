# Write a class "train" which has methods to book a ticket.
# Get stAtus no. of seats and get fare info.
from random import randint
class train:

    def __init__(self,trainno):
        self.trainno=trainno

    def book(self,fro,to):
        print(f"YOur ticket is booked {self.trainno} from {fro} to {to}")
    def getstatus(self):
        print(f"{self.trainno} is on time")
    def fare(self,fro,to):
        print(f"Fare of {self.trainno} from{fro} to{to} is=${randint(222,6666)}")

t=train(1234556)
t.book("kashmir","kanyakumari")
t.getstatus()
t.fare("kashmir","kanyakumari")



