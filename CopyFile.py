import os.path, shutil
from datetime import datetime
from colorama import init
from colorama import Fore, Style
init()
import sqlite3

col_reset = Style.RESET_ALL

green_col = Fore.GREEN
yellow_col = Fore.YELLOW
cyan_col = Fore.CYAN
red_col = Fore.RED

date_1 = str(datetime.now())[:19]
date_2 = ''
for i in date_1:
    if i == ':': date_2 += '-'
    else: date_2 += i

str6 = 0
def write_to_file_log(text, OpenText = 'a', NewLine = '\n', Type = 'DEBUG'):            #DEBUG, INFO, ERROR
    if str6 == 1:
        with open(f'.\Logs\Logs CopyFile {date_2}.txt', OpenText) as file:
            spaces = 4 if Type == "INFO" else 3
            file.write(NewLine + str(datetime.now())[:19] + '   ' + Type + ' '*spaces + text)
    else: ...



try:
    with sqlite3.connect('SettingsCF_db.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM SettingsCopyFile")
        all_results = cursor.fetchall()
        sstr1 = all_results[-1][0] # export
        sstr2 = all_results[-1][1] # import
        str3 = all_results[-1][3] # min
        str4 = all_results[-1][2] # max
        str5 = all_results[-1][4] # sleep
        str6 = all_results[-1][5] # logs
        if int(str3) < 110: str3 = 110

        str1, str2 = '', ''
        for i in sstr1:
            if i == '\n': ...
            else: str1 += i
        for i in sstr2:
            if i == '\n': ...
            else: str2 += i

        write_to_file_log('Програма стартувала...', OpenText = 'w', NewLine = '', Type = 'INFO')
except sqlite3.OperationalError:
    print(f'{red_col}У вас немає збережених налаштувань!\nЗапустіть файл "SettingsCopyFile" та встановіть налаштування!{col_reset}')
    write_to_file_log('Збережені налаштування відсутні! Їх потрібно додати до "SettingsCopyFile"!', Type = 'ERROR')
    os.system('TIMEOUT \t 15'), exit()

print(f'{cyan_col}Експорт файлів з:{col_reset} {str1}\n{cyan_col}Імпорт файлів у:{col_reset} {str2}\n{cyan_col}Максимальний час існування файлу для копіювання:{col_reset} {str3}\n{cyan_col}Мінімальний час існування файлу для копіювання:{col_reset} {str4}\n{cyan_col}Час, через який програма буде закриватися після завершення копіювання:{col_reset} {str5}'
      f'\n\n{red_col}--------------------------------------------------{col_reset}')
write_to_file_log(f'Експорт файлів з: {str1}'), write_to_file_log(f'Імпорт файлів у: {str2}'), write_to_file_log(f'Максимальний час існування файлу для копіювання: {str3}')
write_to_file_log(f'Мінімальний час існування файлу для копіювання: {str4}'), write_to_file_log(f'Час, через який програма буде закриватися після завершення копіювання: {str5}')

path = str1
path_copy = str2
nums_massive, time_folder, final_time_folder, files_interval, is_file, is_folder = '0123456789', [], [], [], [], []



timenow = datetime.now()

timenow_massive = []
timenow_count = 0

for i in str(timenow):
    timenow_massive.append(i)
    timenow_count += 1
    if timenow_count == 19:
        break
    
final_timenow = ''
for i in range(len(list(timenow_massive))):
    if i != ',':
        final_timenow += list(timenow_massive)[i]


        
difference_timenow_massive = []
for i in timenow_massive:
    for num in nums_massive:
        if i == num:
            difference_timenow_massive.append(num)

final_diff_timenow = ''
for i in range(len(list(difference_timenow_massive))):
    if i != ',':
        final_diff_timenow += (list(difference_timenow_massive)[i])



def _FileNotFoundError_(path):
    print(f'\n\n{red_col}',
        '          ***********************************************************\n',
        '          *                                                         *\n',
        '          *             Вказана папка не була знайдена!             *\n',
        '          *                                                         *\n',
        '          ***********************************************************\n',
        '          *                                                         *\n',
        '          *   Вкажіть правильну папку у файлі налаштувань програми  *\n',
        '          *            Або зверніться до адміністратора!            *\n',
        '          *                                                         *\n',
        '          ***********************************************************\n',
        f'{col_reset}\n')
    write_to_file_log(f'FileNotFoundError: Системі не вдається знайти вказаний шлях: {path}', Type = 'ERROR')
    os.system('TIMEOUT \t 15'), exit()

try:
    folder_massive = os.listdir(path)
except FileNotFoundError:
    _FileNotFoundError_(path)

count_folder = 0
for i in folder_massive:
    filename = f'{path}/{folder_massive[count_folder]}'    
    count_folder += 1



    if os.path.exists(filename) == True:
        if os.path.isfile(filename) == True:
            is_file.append(i)
        elif os.path.exists(filename) == True:
            is_folder.append(i)
        


        filetime = os.path.getmtime(filename)
        filetime_readable = datetime.fromtimestamp(filetime)

        filetime_massive = []
        filetime_count = 0
        for i in str(filetime_readable):
            filetime_massive.append(i)
            filetime_count += 1        
            if filetime_count == 19:
                break

        final_timefile = ''
        for i in range(len(list(filetime_massive))):
            if i != ',':
                final_timefile += list(filetime_massive)[i]

        difference_filetime_massive = []
        for i in filetime_massive:
            for num in nums_massive:
                if i == num:
                    difference_filetime_massive.append(num)

        final_diff_filetime = ''
        for i in range(len(list(difference_filetime_massive))):
            if i != ',':
                final_diff_filetime += (list(difference_filetime_massive)[i])
        time_folder.append(int(final_diff_filetime))
                


        final_time = ''
        countt = 0
        for i in range(1):
            final_time += str(int(final_diff_timenow) - int(final_diff_filetime))
            countt += 1
        final_time_folder.append(int(final_time))
    else: pass



else_massive = []
for i in final_time_folder:
    if i >= int(str4):
        if i <= int(str3):
            files_interval.append(i)
        else: pass
    else: 
        else_massive.append(i)



namef = []
names_files = []
for i in files_interval:
    for g in final_time_folder:
        if i == g:
            index_time = final_time_folder.index(i)
            names_files.append(folder_massive[index_time])
            namef.append(folder_massive[index_time])



final_info = []
count = 1
if folder_massive != []:
    print(f'\n{cyan_col}Усі файли в папці:{col_reset}')
    print(f'\n{yellow_col}Назви всіх файлів:{col_reset} {green_col}{(len(folder_massive))}{col_reset}\n{folder_massive}\n') # Назва всіх файлів  +
    write_to_file_log(f'Кількість всіх файлів у папці: {(len(folder_massive))}'), write_to_file_log(f'Назви всіх файлів: {str(folder_massive)}')
if folder_massive == []:
    final_info.append(count)
    count += 1
    
if final_time_folder != []:
    print(f'{yellow_col}Час існування файлів:{col_reset} {green_col}{(len(final_time_folder))}{col_reset}\n{final_time_folder}\n') # Віднімення часу всіх файлів +
    print(f'{red_col}--------------------------------------------------{col_reset}')
    write_to_file_log(f'Кількість існуючих файлів: {(len(final_time_folder))}'), write_to_file_log(f'Час існуючих файлів: {str(final_time_folder)}')
if final_time_folder == []:
    final_info.append(count)
    count += 1
    
if files_interval != []:
    print(f'\n{cyan_col}Доступні файли для копіювання:{col_reset}\n')
    print(f'{yellow_col}Назви файлів:{col_reset} {green_col}{(len(names_files))}{col_reset}\n{names_files}\n') #  Назви файлів виставлений проміжок часу +
    write_to_file_log(f'Кількість доступних файлів для копіювання: {(len(names_files))}'), write_to_file_log(f'Назви доступних файлів для копіювання: {str(names_files)}')
if files_interval == []:
    final_info.append(count)
    count += 1
if names_files != []:
    print(f'{yellow_col}Час існування файлів:{col_reset} {green_col}{(len(files_interval))}{col_reset}\n{files_interval}\n') # Файлові числа виставлений проміжок часу  +
    print(f'{red_col}--------------------------------------------------{col_reset}')
    write_to_file_log(f'Час існування всіх доступних файлів: {(len(files_interval))}'), write_to_file_log(f'Час існування файлів: {str(files_interval)}')
if names_files == []:
    final_info.append(count)
    count += 1



from pprint import pprint
if os.path.isdir(path_copy) == True:
    for h in range(len(names_files)):
        for i in names_files:
            for g in (os.listdir(path_copy)):
                if i == g:
                    names_files.remove(i)
                else: pass
else: pprint(path_copy), _FileNotFoundError_(path_copy)



def zero_file():
    print(f'\n{yellow_col}Не було знайдено файли для копіювання!{col_reset}')
    write_to_file_log('Не було знайдено файли для копіювання!')

error, else_m, folder_zero = [], [], []
if not(names_files) == []:
    print(f'\n{yellow_col}Файли, які будуть скопійовані ({green_col}{len(names_files)} шт.{col_reset}{yellow_col}):{col_reset}\n')
    write_to_file_log(f'Файли, які будуть скопійовані: {len(names_files)} шт.')
    coun = 1
    for i in names_files:
        print(f'{cyan_col}{coun}){col_reset} {i}')
        write_to_file_log(f'{count}) {i}')
        coun += 1
    for i in names_files:
        if i in is_file:
            shutil.copy2(f'{path}/{i}', f'{path_copy}')
        elif i in is_folder:
            shutil.copytree(f'{path}/{i}', f'{path_copy}/{i}')
    ready = []
    for i in names_files:
        for g in (os.listdir(path_copy)):
            if i == g:
                ready.append(i)
    if ready != []:
        print(f'\n\n{green_col}',
            '          ********************************************************\n',
            '          *                                                      *\n',
            '          *          Готово! Усі файли були скопійовані!         *\n',
            '          *                                                      *\n',
            '          ********************************************************\n',
            f'{col_reset}')
        write_to_file_log('Готово! Усі файли були скопійовані!')
    else: pass
else:
    if final_info != []: 
        if (max(final_info)) == 4:
            print(f'\n{yellow_col}У папці немає файлів!{col_reset}')
            write_to_file_log('У папці немає файлів!')
            folder_zero.append(1)
        else: pass
    if namef == []:
        if not(max(final_info)) == 4:
            if folder_massive == []:
                print(f'\n\n{red_col}',
                    '          **********************************************************\n',
                    '          *                                                        *\n',
                    '          *                 У вас збій програми!                   *\n',
                    '          *                                                        *\n',
                    '          **********************************************************\n',
                    '          *                                                        *\n',
                    '          *              Зверніться до адміністратора!             *\n',
                    '          *                Або до творця програми!                 *\n',
                    '          *                                                        *\n',
                    '          **********************************************************\n',
                    f'{col_reset}\n')
                write_to_file_log('Збій програми! Зверніться до адміністратора!', 'ERROR')
                error.append(1)
        else: pass
    else:
        zero_file()
        else_m.append(1)

if namef == []:
    if else_massive != []:
        zero_file()
        else_m.append(2)
else: pass
if names_files == []:
    if else_m == []:
        if error == []:
            if folder_zero == []:
                zero_file()
else: pass

os.system('TIMEOUT /t ' + str(str5))
write_to_file_log('Програма завершила роботу успішно!', Type = 'INFO')