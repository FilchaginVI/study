#!/bin/python2

import argparse
import os,sys
import datetime
import re

class contact:

    def __init__(self, Name, Date, Phone):
        self.Name = Name
        self.Date = Date
        self.Phone = Phone

    def show(self):
        print self.Name, self.Date, self.Phone

    def addcontact(self):
        f = open("base.txt","a")
        f.write(self.Name.replace(",", " ") + " " + str(self.Date) + " " + str(self.Phone) + "\n")
        f.close()

    def list_contact(self):
        f = open("base.txt","r")
        print f.read()
        f.close()


class list_all(argparse.Action):

    def __call__(self, parser, *args, **kwargs):
        showall = contact('fake', 'fake', 'fake')
        showall.list_contact()


class superparser:

    def name_type(self,string):
        for item in string.split(","):
            if item.isalpha() == False:
                msg = "%r is not alpha" % item
                raise argparse.ArgumentTypeError(msg)
        return string

    def date_type(self,string):
        try:
            return datetime.datetime.strptime(string, "%Y-%m-%d").date()
        except ValueError:
            msg = "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(string)
            raise argparse.ArgumentTypeError(msg)

    def phone_type(self,string):
        rule = re.compile('\+\d{1}\d{3}\d{3}\d{0,5}$')
        if not rule.search(string):
            msg = "%r is not mobile phone number" % string
            raise argparse.ArgumentTypeError(msg)
        return string

    def create_parser(self):

        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(help='choose type of action')

        parser_w = subparsers.add_parser("write")
        parser_w.add_argument("name", metavar=('[name]'), type=self.name_type, help="First,second,last name without free space or dots")
        parser_w.add_argument("date", metavar=('[date]'), type=self.date_type, help="date in format YYYY-MM-DD")
        parser_w.add_argument("phone", metavar=('[phone]'), type=self.phone_type, help="phone number with +")
        parser_l = subparsers.add_parser("list")
        parser_l.add_argument("list", action=list_all, nargs='?',  help="show all contacts")

        return parser

    def __init__(self):

        self.parser = self.create_parser()
        self.argspace = self.parser.parse_args()



new = superparser()
if str(sys.argv[1]) == "write":
    newcontact = contact(new.argspace.name, new.argspace.date, new.argspace.phone)
    newcontact.addcontact()
