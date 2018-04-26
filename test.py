#!/usr/bin/python2
import argparse
import os
f = open("base.txt","a")

class contact:
    def __init__(self, Name, Date, Phone):
        self.Name = Name
        self.Date = Date
        self.Phone = Phone

    def show(self):
        print self.Name, self.Date, self.Phone

    def addcontact(self):
        f.write(self.Name + " " + str(self.Date) + " " + str(self.Phone) + "\n")


parser = argparse.ArgumentParser()
parser.add_argument("-w", action='append', nargs=3, metavar=('[name]','[date]','[phone]'),  help="write new contact")
parser.add_argument("-l" , help="show all contacts")


somevar = parser.parse_args()

print somevar
