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

class list_all(argparse.Action):
    def __call__(self, parser, *args, **kwargs):
        print "List of all"


def name_type(string):
    qwe = string
    print qwe
    return qwe


def date_type(string):
    qwe = string
    print qwe
    return qwe

def phone_type(string):
    qwe = string
    print qwe
    return qwe

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='choose type of action')
parser_w = subparsers.add_parser("write")
parser_w.add_argument("name", metavar=('[name]'), type=name_type)
parser_w.add_argument("date", metavar=('[date]'), type=date_type)
parser_w.add_argument("phone", metavar=('[phone]'), type=phone_type)

parser_l = subparsers.add_parser("list")
parser_l.add_argument("list", action=list_all, nargs='?',  help="show all contacts")


somevar = parser.parse_args()

print somevar
