'''
    Prayer model for
    users of prayer app
'''
# pylint:  disable=W1514,C0209,R1733,C0103,W0612,E0401
from datetime import datetime
import csv

class Prayer:
    '''
        Prayer from a user
    '''
    def __init__(self, data):
        self.content = data['content']
        self.user_name = data['user_name']
        self.pastor_name = data['pastor_name']
        self.created_at = datetime.now()
        self.answered = None

    @staticmethod
    def add_prayer(data):
        '''
            Accepts data
            Creates prayer obj from data
            Adds to a spreadsheet
            returns prayer obj
        '''
        prayer_obj = Prayer(data)
        with open("proj_app\\data\\prayer.csv", 'a+', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=['content','user_name','pastor_name','created_at','answered'])
            writer.writerow(data)
        f.close()
        return prayer_obj
    
    @classmethod
    def get_all_prayers(cls):
        '''
            Gets all prayers from csv
            Creates an instance of Prayer
            returns all Prayers as a list
        '''
        with open("proj_app\\data\\prayer.csv", 'r', newline="") as f:
            reader = csv.DictReader(f)
            
            prayers = []

            for row_num,row in enumerate(reader):
                if row_num == 0:
                    pass
                prayers.append(cls(row))
        f.close()
        return prayers
