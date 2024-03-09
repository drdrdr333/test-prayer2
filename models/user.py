'''
    User model
    for users of paryer app
'''
# pylint:  disable=W1514,C0209,R1733,C0103,W0612,E0401

from flask import flash
import re
from datetime import datetime
import csv

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PHONE_REGEX = re.compile(r'^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')

class User:
    '''
        Represents a user
    '''
    def __init__(self, data):
        self.user_name = data['user_name']
        self.phone_number = data['phone_number']
        self.email = data['email']
        self.created_at = datetime.now()
    
    @staticmethod
    def check_users_exists(user_data):
        '''
            Determines if a record for
                user data coming from
                form exists already
        '''
        exists = False
        with open("proj_app\\data\\user.csv", 'r') as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader):
                if row['user_name'] == user_data['user_name']:
                    if row['email'] == user_data['email']:
                        exists = True
            f.close()
        return exists

    @staticmethod
    def validate_user(user_data):
        '''
            Creates a bool for testing
            Adds messages to list if tests fail
            Name > 3 characters
            Email valid format with @ & .com/.net
            Phone must have valid format ***-****
        '''
        is_valid = True
        if len(user_data['user_name']) < 3:
            flash("Name needs to be longer than 3 characters...")
            is_valid = False
        if not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email pattern, please supply a valid email...")
            is_valid = False
        if not PHONE_REGEX.match(user_data['phone_number']):
            print('got to invalid number')
            flash("Invalid phone number format... ***-***** accepted.")
            is_valid = False
        return is_valid
        # placeholder for getting user by email matchup...
    
    @staticmethod
    def add_user(user_data):
        '''
            Accepts user_data as dict
            creates them as a User obj
            adds them to spreadsheet via
            csv
            returns the User instance
        '''
        the_user = User(user_data)
        with open("proj_app\\data\\user.csv", 'a+', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=['user_name','phone_number','email', "created_at"])
            writer.writerow(user_data)
            f.close()
        return the_user

    @classmethod
    def get_user_by_name(cls, user_name):
        '''
            Accepts a user_name as str
            Searches the csv for the matching
                user_name
            Returns the row for that user_name
                as a User obj
        '''
        with open("proj_app\\data\\user.csv", 'r', newline="") as _f:
            ret = None
            reader = csv.DictReader(_f)
            for row in reader:
                if row['user_name'] == user_name:
                    ret = row
        _f.close()
        return ret