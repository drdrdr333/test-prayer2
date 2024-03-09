'''
    Pastor model
    for pastors of prayer app
'''

# pylint:  disable=W1514,C0209,R1733,C0103,W0612,E0401

class Pastor:
    '''
        Represents a pastor
    '''
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.church_name = data['church_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
