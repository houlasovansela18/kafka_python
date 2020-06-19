# cook your dish here
class Operation:
    
    def __init__(self,plate_id):
        
        self.plate_id = plate_id
        self.char_to_digid = {
    
                'O': '0',
        		'L': '1',
        		'Z': '2',
        		'A': '4',
        		'S': '5',
        		'G': '6',
        		'T': '7',
        		'B': '8',
        		'R': '9'
	}
	
        self.digid_to_char = {
        
        		'0': 'O',
        		'1': 'L',
        		'2': 'Z',
        		'4': 'A',
        		'5': 'S',
        		'6': 'G',
        		'7': 'T',
        		'8': 'B',
        		'9': 'R'
        }


    def operation_plate(self):
    
        if len(self.plate_id)==6:
            
            for i in range(6):
                if i == 1:
                    if self.plate_id[i].isdigit():self.plate_id = self.plate_id[:i] + self.digid_to_char[self.plate_id[i]] + self.plate_id[i + 1:]
                    else:pass
                else:
                    if self.plate_id[i].isdigit():pass
                    else:self.plate_id = self.plate_id.replace(self.plate_id[i],self.char_to_digid[self.plate_id[i]])
            
        elif len(self.plate_id)==7:
            for i in range(7):
                if i == 1 or i == 2:
                    if self.plate_id[i].isdigit():self.plate_id = self.plate_id[:i] + self.digid_to_char[self.plate_id[i]] + self.plate_id[i + 1:]
                    else:pass
                else:
                    if self.plate_id[i].isdigit():pass
                    else:self.plate_id = self.plate_id.replace(self.plate_id[i],self.char_to_digid[self.plate_id[i]])
        return self.plate_id
    
    def check_format(self):
        import re
    
        rex = re.compile("[1-5][A-Z]{1,2}[0-9]{4}$")
        plate_op = Operation(plate_id).operation_plate()
        if rex.match(plate_op):
            result_plate = plate_op[:-4]+" "+plate_op[len(plate_op)-4:]
            return result_plate
    
    

plate_id = "110097"

print(Operation(plate_id).check_format())
    