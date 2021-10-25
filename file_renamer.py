import os
import pyperclip as clip

def rename_files():
#! --The Folder To Be Searched Through    
    search_folder = ''
#! --This Is The Text To Be Removed        
    tbr = []
    file_list = os.listdir(search_folder)
    for term in tbr:
        for file in file_list:
            term_slice = len(term)
            if file[0:term_slice].lower() == term.lower():
                if file[-4:] == '.txt':
                    print(f'Current name: {file[:-4]}')
                if file[-5:] == '.epub':
                    print(f'Current name: {file[:-5]}')
                old_path = f'{search_folder}{file}'
                new_name = file[term_slice:]
                new_path = f'{search_folder}{new_name}'
                try:
                    os.rename(old_path , new_path)
                    print(f'New Name: {new_name}')
                    print('\n')
                except:
                    if file[-4:] == '.txt':
                        clip.copy(file[term_slice:-4])
                        manual_name = input('Enter a new name: ')
                        manual_name = manual_name + '.txt'
                        new_path = f'{search_folder}{manual_name}'
                        os.rename(old_path , new_path)
                        print(f'New Name: {manual_name}')
                        print('\n')
                    if file[-5:] == '.epub':
                        clip.copy(file[term_slice:-5])
                        manual_name = input('Enter a new name: ')
                        manual_name = manual_name + '.epub'
                        new_path = f'{search_folder}{manual_name}'
                        os.rename(old_path , new_path)
                        print(f'New Name: {manual_name}')
                        print('\n')

                    
if __name__ == '__main__':
    rename_files()
