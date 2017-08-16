'''
@Author Tony Tran
@Date 8/15/17
@Project Professional scraper
linkedin_parser.py
Purpose: To parse in CSV files exported from linkedin, and print or export to json
'''
import csv
import json
def print_work_history(list_of_work_history_data):
    pass
def print_projects(list_of_projects):
    pass
def parse_csv_to_list(csv_file):
    file_data = open(csv_file)
    first_line = file_data.readline().strip()
    print(first_line)
    file_data.close()
    data_dict = {}
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0

        for row in reader:
            data_dict[i] = row[first_line]
            print(i, ' ', row[first_line])

            i+=1

    data_to_remote = list(str(input("Is there any data you don't want to export, indicate so with their indices")))

    print(data_to_remote)
    for remove_index in data_to_remote:
        data_dict[remove_index] = None
    print("These are the skills to be exported")
    ret_list = []
    for data_key in data_dict.keys():
        if data_dict[data_key]:
            print(data_dict[data_key])
            ret_list.append(data_dict[data_key])
    return ret_list, first_line
def export_list_to_json(data_list, keyname):
    try:
        with open(keyname + ".json", "w") as outfile:
            json.dump({keyname: data_list}, outfile, indent=4)
    except Exception as e:
        print(e)
        return False
    return True

def print_skills(list_of_skills):
    pass
def print_courses(list_of_courses):
    pass
def print_education_history(list_of_education_information):
    pass
def main():
    file_name = str(input('Enter name of file (,): '))
    data_list, first_line = parse_csv_to_list(file_name)
    exported = export_list_to_json(data_list, first_line)
    if (exported):
        print(file_name, " exported to json successfully!")
    else:
        print("An error occured in the parsing to json of file: ", file_name)
main()
