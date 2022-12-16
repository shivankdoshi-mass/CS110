import csv

# Task 1
# Function 1
def read_dna(dna_filename):
    textfile = open(dna_filename,'r')
    return textfile.read()

# Function 2
def dna_length(dna_filename):
    textfile = open(dna_filename,'r')
    textfile1 = textfile.read()
    length = len(textfile1)
    return length

# Task 2
# Function 1
def read_strs(str_filename):
    strlist = []
    with open(str_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader :
            strlist.append(row)
    return strlist

# Function 2
def get_strs(str_profile):
    items = list(str_profile.items())
    items.pop(0)
    strprofile = [(k, int(v)) for k, v in items]
    return strprofile

# Task 3
# Function 1
def longest_str_repeat_count(str_frag, dna_seq):    
    i = 0
    count = 0
    longest_count = count
    while i < len(dna_seq):
        if dna_seq[i:i+4] == str_frag:
            count +=1 
            i += 4
            if count>longest_count:          
                longest_count = count            
        else:
            i += 1
            count = 0
    return longest_count



# Task 4
# Function 1
def find_match(str_profile, dna_seq):
    pass


# Task 5
# Function 1
def dna_match(str_filename, dna_filename):
    pass



# Task 6
if __name__ == '__main__':
    print(read_strs('data/str_profiles.csv'))
    print(read_dna('data/dna_1.txt'))
    print(dna_length('data/dna_1.txt'))

    csvfile = input()
    txtfile = input()

    if csvfile[-4:] == ".csv" and txtfile[-4:] == ".txt" :
        dna_match(csvfile, txtfile)
    else:
        print('Usage: python dna.py STR_FILE DNA_FILE')
