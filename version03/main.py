# The main file

import Functions
import atexit

# Initialize lists []
project_queue = []
project_list = []
project_completed = []

# file variables and their values
file_info = "id,name,size,priority"
required_csv = "required.csv"
done_csv = "done.csv"

############################
# main() function call
if __name__ == "__main__":
    Functions.main()
############################

# Mark writer completed=True upon exit
atexit.register(Functions.writer)