import pandas as pd
import os
import information


class company_data:
    def __init__(self, company_name , data):
        try:
            self.company_name = company_name
        except:
            print(f"File : {company_name} file name error!")
        
        try:
            self.df = data
        except:
            print(f"File : {company_name} data initiate error!")


def create_company_data(file_name , directory):
    df = pd.read_csv(f"{directory}/{file_name}")
    company_name = file_name.split('.')[0]
    company = company_data(company_name , df)
    return company


def execute_company_data_import(information):
    ### get file_directory
    file_dir = information.file_dir

    ### get all files under directory
    files = os.listdir(file_dir)
    
    ### list for storing company
    company_data_list = []
    
    ### initiate company data
    for f in files:
        if ".csv" in f: ### for all csv files
            company_data_list.append(create_company_data(f , file_dir))    

    return company_data_list

if __name__ == "__main__":
    print("questionaire module imported")



