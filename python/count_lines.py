import sys
if len ( sys . argv ) != 2:
    sys.exit(" ERROR : this script expect exactly 1 argument .")
print (" Argument is : {}". format ( sys.argv [1]))

file_name = sys.argv[1]
size = 0
with open ( file_name , "r") as f_in :
    size = len ( f_in.readlines())
    print ("{} contains {} lines .". format ( file_name , size ))