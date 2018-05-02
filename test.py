#!/usr/bin/python2
import argparse
import os, sys

class contact:
    def __init__(self, Name, Date, Phone):
        self.Name = Name
        self.Date = Date
        self.Phone = Phone

    def show(self):
        print self.Name, self.Date, self.Phone

    def addcontact(self):
        f = open("base.txt","a")
        f.write(self.Name + " " + str(self.Date) + " " + str(self.Phone) + "\n")
        f.close()

    def list_contact(self):
        f = open("base.txt","r")
        print f.read()
        f.close()


class list_all(argparse.Action):
    def __call__(self, parser, *args, **kwargs):
        rew = contact('fake', 'fake', 'fake')
        rew.list_contact()


class superparser:

    def name_type(self,string):
        qwe = string
        return qwe

    def date_type(self,string):
        qwe = string
        return qwe

    def phone_type(self,string):
        qwe = string
        return qwe

    def create_parser(self):

        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(help='choose type of action')

        parser_w = subparsers.add_parser("write")
        parser_w.add_argument("name", metavar=('[name]'), type=self.name_type)
        parser_w.add_argument("date", metavar=('[date]'), type=self.date_type)
        parser_w.add_argument("phone", metavar=('[phone]'), type=self.phone_type)

        parser_l = subparsers.add_parser("list")
        parser_l.add_argument("list", action=list_all, nargs='?',  help="show all contacts")

        return parser


    def __init__(self):

        self.parser = self.create_parser()
        self.argspace = self.parser.parse_args()


ololo = superparser()
if str(sys.argv[1]) == "write":
    wert = contact(ololo.argspace.name, ololo.argspace.date, ololo.argspace.phone)
    wert.addcontact()

