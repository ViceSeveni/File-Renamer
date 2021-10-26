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
    search_folder = r""
    
#! --This Is The Text To Be Removed        
    tbr = []
    
    file_list = os.listdir(search_folder)
    
    for file in file_list:
        for term in tbr:
            if term.lower() in file.lower():
                
                file_type = get_filetype(file)
                
                file_name = file.replace(file_type , '')
                new_name = file_name.replace(term , '')
                                        
                old_path = f'{search_folder}{file}'
                new_path = f'{search_folder}{new_name}'
                
                print(f'Current name: {file_name}')
                
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
