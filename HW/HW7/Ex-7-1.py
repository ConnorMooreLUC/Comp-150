'''
TITLE: Ex-7-1
AUTHOR: Connor Moore
DATE: 3/20/17
DESCRIPTION: Create Three different dictionaries that can be parsed,
and a lookup function, and place the information in a formated string.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/20

'''
def lookup(string, fn, ln, tele):
    return "Name: "+fn[string]+' '+ln[string]+" |  Email: "\
           +string+" | Telephone: "+tele[string]
def main():
    fn={'ctuckey@luc.edu':'Chris', 'president@whitehouse.gov':'Barack',
        'bill@microsoft.com':'Bill',
        'santa@northpole.arc':'Santa',
        'chunkylover53@aol.com':'Homer'}        
    ln={'ctuckey@luc.edu':'Tuckey','president@whitehouse.gov':'Obama',
        'bill@microsoft.com':'Gates',
        'santa@northpole.arc':'Claus',
        'chunkylover53@aol.com':'Simpson'}
    tele={'ctuckey@luc.edu':'700-288-2539',
          'president@whitehouse.gov':'888-the-prez',
          'bill@microsoft.com':'999-555-0001',
          'santa@northpole.arc':'867-000-0000',
          'chunkylover53@aol.com':'888-555-1212'}
    string = input("Enter an email to search the directory: \n")
    print(lookup(string,fn,ln,tele))
    
main()
    
    
