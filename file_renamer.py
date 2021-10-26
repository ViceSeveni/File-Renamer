import os

def get_filetype(filename=''):
    if filename == '':
        filename = input('Enter A File Name: ')

    period = '.'
        
    if period not in filename:
        raise Exception('Invalid File Name. Must end with file type ".jpg"')
        
    if period in filename:
        file_info = filename.split('.')
        file_type = period + file_info[-1]
        return file_type

def rename_files():
#! --The Folder To Be Searched Through    
    search_folder = r"C:\PythonScripts\testing\test1\\"
    
#! --This Is The Text To Be Removed        
    tbr = ['[oceanofpdf.net]' , 'OceanOfPDF.org_' , 'oceanofpdf.org-']
    
    file_list = os.listdir(search_folder)
    
    for file in file_list:
        for term in tbr:
            term_slice = len(term)
            if term.lower() in file.lower():
                file_type = get_filetype(file)
                type_slice = int(len(file_type))
                file_name = file[: -type_slice]
                print(f'Current name: {file_name}')
                    
                    
                old_path = f'{search_folder}{file}'
                new_name = file_name[term_slice:]
                new_path = f'{search_folder}{new_name}'
                
                try:
                    os.rename(old_path , new_path)
                    print(f'New Name: {new_name}')
                    print('\n')
                    
                except:
                    new_name = new_name + '-1'
                    new_path = f'{search_folder}{new_name}'
                    os.rename(old_path , new_path)
                    print(f'New Name: {new_name}')
                    print('\n')
                        
if __name__ == '__main__':
    rename_files()
