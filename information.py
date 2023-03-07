from pathlib import Path

### relative path
path = Path(__file__).parent

### document path
file_dir = f"{path}/data_source"

### wanted columns for dataframe
wanted_columns = ['Employee ID', 
'Tier' ,
'Question #',
'Role',
'Element',
'Question Type',
'Question',
'Response']

			
					