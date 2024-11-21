from tkinter import*
from tkinter import filedialog
from tkinter import messagebox as messbox
import sqlite3
import os

def check_error():
    if text_1.get() == '': messbox.showerror(title = 'ERROR', message = 'Поле із шляхом до папки, з якої відбуватиметься копіювання, не повинно бути порожнім!'); return True
    if text_2.get() == '': messbox.showerror(title = 'ERROR', message = 'Поле із шляхом до папки, в яку відбуватиметься копіювання, не повинно бути порожнім!'); return True

    if int(text_3_1.get()) > 12 or int(text_3_1.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість місяців не повинна перевищувати 12, і не повинно бути менше 0'); return True
    if int(text_3_2.get()) > 30 or int(text_3_2.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість днів не повинна перевищувати 30, і не повинно бути менше 0'); return True
    if int(text_3_3.get()) > 24 or int(text_3_3.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість годин не повинна перевищувати 24, і не повинно бути менше 0'); return True
    if int(text_3_4.get()) > 60 or int(text_3_4.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість хвилин не повинна перевищувати 60, і не повинно бути менше 0'); return True

    if int(text_4_1.get()) > 12 or int(text_4_1.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість місяців не повинна перевищувати 12, і не повинно бути менше 0'); return True
    if int(text_4_2.get()) > 30 or int(text_4_2.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість днів не повинна перевищувати 30, і не повинно бути менше 0'); return True
    if int(text_4_3.get()) > 24 or int(text_4_3.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість годин не повинна перевищувати 24, і не повинно бути менше 0'); return True
    if int(text_4_4.get()) > 60 or int(text_4_4.get()) < 0: messbox.showerror(title = 'ERROR', message = 'Кількість хвилин не повинна перевищувати 60, і не повинно бути менше 0'); return True


def create_write_db():
    if check_error() == True: return

    dir_export = '\'' + text_1.get() + '\''
    dir_import = '\'' + text_2.get() + '\''

    if int(text_3_1.get()) < 10:
        ttext_3_1 = '0' + text_3_1.get()
    else: ttext_3_1 = text_3_1.get()
    if int(text_3_2.get()) < 10:
        ttext_3_2 = '0' + text_3_2.get()
    else: ttext_3_2 = text_3_2.get()
    if int(text_3_3.get()) < 10:
        ttext_3_3 = '0' + text_3_3.get()
    else: ttext_3_3 = text_3_3.get()
    if int(text_3_4.get()) < 10:
        ttext_3_4 = '0' + text_3_4.get()
    else: ttext_3_4 = text_3_4.get()
    time_min = '0000' + ttext_3_1[:-1] + ttext_3_2[:-1] + ttext_3_3[:-1] + ttext_3_4[:-1] + '10'
    time_min = time_min.lstrip('0')

    if int(text_4_1.get()) < 10:
        ttext_4_1 = '0' + text_4_1.get()
    else: ttext_4_1 = text_4_1.get()
    if int(text_4_2.get()) < 10:
        ttext_4_2 = '0' + text_4_2.get()
    else: ttext_4_2 = text_4_2.get()
    if int(text_4_3.get()) < 10:
        ttext_4_3 = '0' + text_4_3.get()
    else: ttext_4_3 = text_4_3.get()
    if int(text_4_4.get()) < 10:
        ttext_4_4 = '0' + text_4_4.get()
    else: ttext_4_4 = text_4_4.get()
    time_max = '0000' + ttext_4_1[:-1] + ttext_4_2[:-1] + ttext_4_3[:-1] + ttext_4_4[:-1] + '60'
    time_max = time_max.lstrip('0')

    time_sleep = '\'' + text_5_1.get() + '\''
    Logs = text_logs.get()

    dir_export = dir_export if dir_export[:-1] != '\n' else dir_export[:-1]
    dir_import = dir_import if dir_import[:-1] != '\n' else dir_import[:-1]
    time_min = time_min if time_min[:-1] != '\n' else time_min[:-1]
    time_max = time_max if time_max[:-1] != '\n' else time_max[:-1]
    time_sleep = time_sleep if time_sleep[:-1] != '\n' else time_sleep[:-1]

    with sqlite3.connect('SettingsCF_db.db') as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS SettingsCopyFile (
                       path_export TEXT,
                       path_import TEXT,
                       time_min INTEGER,
                       time_max INTEGER,
                       time_sleep INTEGER,
                       logs INTEGER)""")
        cursor.execute(f"INSERT INTO SettingsCopyFile (path_export, path_import, time_min, time_max, time_sleep, logs) VALUES({dir_export}, {dir_import}, {time_min}, {time_max}, {time_sleep}, {Logs})")
        db.commit()

    if os.path.isfile('.\Settings_CF_Open.dat') == True:
        os.remove('Settings_CF_Open.dat')
    else: ...
    with open('Settings_CF_Open.dat', 'w') as sett_file:
 
        text_1_ = text_1.get() if text_1.get()[-1:] != '\n' else text_1.get()[:-1]
        text_2_ = text_2.get() if text_2.get()[-1:] != '\n' else text_2.get()[:-1]
        sett_file.write(f'{text_1_}\n')
        sett_file.write(f'{text_2_}\n\n')

        text_3_1_ = text_3_1.get() if text_3_1.get()[-1:] != '\n' else text_3_1.get()[:-1]
        text_3_2_ = text_3_2.get() if text_3_2.get()[-1:] != '\n' else text_3_2.get()[:-1]
        text_3_3_ = text_3_3.get() if text_3_3.get()[-1:] != '\n' else text_3_3.get()[:-1]
        text_3_4_ = text_3_4.get() if text_3_4.get()[-1:] != '\n' else text_3_4.get()[:-1]
        sett_file.write(f'{text_3_1_}\n')
        sett_file.write(f'{text_3_2_}\n')
        sett_file.write(f'{text_3_3_}\n')
        sett_file.write(f'{text_3_4_}\n\n')

        text_4_1_ = text_4_1.get() if text_4_1.get()[-1:] != '\n' else text_4_1.get()[:-1]
        text_4_2_ = text_4_2.get() if text_4_2.get()[-1:] != '\n' else text_4_2.get()[:-1]
        text_4_3_ = text_4_3.get() if text_4_3.get()[-1:] != '\n' else text_4_3.get()[:-1]
        text_4_4_ = text_4_4.get() if text_4_4.get()[-1:] != '\n' else text_4_4.get()[:-1]
        sett_file.write(f'{text_4_1_}\n')
        sett_file.write(f'{text_4_2_}\n')
        sett_file.write(f'{text_4_3_}\n')
        sett_file.write(f'{text_4_4_}\n\n')
        
        text_5_1_ = text_5_1.get() if text_5_1.get()[-1:] != '\n' else text_5_1.get()[:-1]
        sett_file.write(f'{str(text_5_1_)}\n\n')

        sett_file.write(str(Logs))

    if messbox.askyesno(title = 'SettingsCopyFile.dat', message = 'Налаштування успішно збережено!\n\nЗакрити програму?') == True: exit()


def open_file_and_information():
    if os.path.isfile('.\Settings_CF_Open.dat') == True:
        with open('Settings_CF_Open.dat', 'r') as sett_file:
            context = sett_file.readlines()
            text_1.set(context[0]), text_2.set(context[1])
            text_3_1.set(context[3]), text_3_2.set(context[4]), text_3_3.set(context[5]), text_3_4.set(context[6])
            text_4_1.set(context[8]), text_4_2.set(context[9]), text_4_3.set(context[10]), text_4_4.set(context[11])
            text_5_1.set(context[13])
            text_logs.set(context[15])
    else: ...

def select_directory_dialog_export():
    directory_export = filedialog.askdirectory()
    text_1.set(directory_export)

def select_directory_dialog_import():
    directory_import = filedialog.askdirectory()
    text_2.set(directory_import)

def do_more_less(number, number_2, which):
    if which == 0:
        if number == 1:
            i = text_3_1.get()
            if number_2 == 0:
                if int(i) < 12:
                    text_3_1.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_3_1.set(int(i)-1)
        if number == 2:
            i = text_3_2.get()
            if number_2 == 0:
                if int(i) < 30:
                    text_3_2.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_3_2.set(int(i)-1)   
        if number == 3:
            i = text_3_3.get()
            if number_2 == 0:
                if int(i) < 24:
                    text_3_3.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_3_3.set(int(i)-1)
        if number == 4:
            i = text_3_4.get()
            if number_2 == 0:
                if int(i) < 60:
                    text_3_4.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_3_4.set(int(i)-1)

    elif which == 1:
        if number == 1:
            i = text_4_1.get()
            if number_2 == 0:
                if int(i) < 12:
                    text_4_1.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_4_1.set(int(i)-1)
        if number == 2:
            i = text_4_2.get()
            if number_2 == 0:
                if int(i) < 30:
                    text_4_2.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_4_2.set(int(i)-1)   
        if number == 3:
            i = text_4_3.get()
            if number_2 == 0:
                if int(i) < 24:
                    text_4_3.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_4_3.set(int(i)-1)
        if number == 4:
            i = text_4_4.get()
            if number_2 == 0:
                if int(i) < 60:
                    text_4_4.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_4_4.set(int(i)-1)
    elif which == 2:
        if number == 1:
            i = text_5_1.get()
            if number_2 == 0:
                if int(i) < 60:
                    text_5_1.set(int(i)+1)
            elif number_2 == 1:
                if int(i) >= 1:
                    text_5_1.set(int(i)-1)


def default():
    text_1.set(''), text_2.set('')
    text_3_1.set(0), text_3_2.set(0), text_3_3.set(0), text_3_4.set(1)
    text_4_1.set(0), text_4_2.set(0), text_4_3.set(0), text_4_4.set(31)
    text_5_1.set(10)
    text_logs.set(1)


root = Tk()
root.title('SettingsCopyFile')
root.geometry('600x400')
root.resizable(0, 0)
root.config(background = 'light grey')
root.iconbitmap('CopyFileICO.ico')

label = Label(root,
    text = 'Налаштування CopyFile',
    font = ('Times New Roman', 20, 'bold'),
    relief = FLAT,
    background = 'light grey'
).place(x = 40, y = 5, width = 350, height = 40)


label_1 = Label(root,
    text = 'Виберіть шлях до папки, з якої буде відбуватися копіювання:',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_1.place(x = 19, y = 50, width = 414, height = 20)
text_1 = StringVar() 
entry_1 = Entry(root, font = ('Times New Roman', 15), textvariable = text_1)
entry_1.place(x = 20, y = 70, width = 400, height = 22)
but_1 = Button(root, 
               text = 'Огляд', 
               font = ('Times New Roman', 12),
               background = 'light grey',
               activebackground = 'grey',
               command = lambda:(
                   select_directory_dialog_export()
               )
)
but_1.place(x = 440, y = 70, width = 100, height = 22)

label_2 = Label(root,
    text = 'Виберіть шлях до папки, в яку буде відбуватися копіювання:',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_2.place(x = 19, y = 100, width = 414, height = 20)
text_2 = StringVar() 
entry_2 = Entry(root, font = ('Times New Roman', 15), textvariable = text_2)
entry_2.place(x = 20, y = 120, width = 400, height = 22)
but_2 = Button(root, 
               text = 'Огляд', 
               font = ('Times New Roman', 12),
               background = 'light grey',
               activebackground = 'grey',
               command = lambda:(
                   select_directory_dialog_import()
               )
)
but_2.place(x = 440, y = 120, width = 100, height = 22)





label_3 = Label(root,
    text = 'Введіть мінімальний час існування файлу, який буде перевірено:',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_3.place(x = 19, y = 150, width = 442, height = 20)
label_3_1 = Label(root,
    text = 'міс     доб    год    хвл',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_3_1.place(x = 19, y = 170, width = 160, height = 20)


text_3_1 = StringVar()
entry_3_1 = Entry(root, font = ('Times New Roman', 15), textvariable = text_3_1)
entry_3_1.place(x = 20, y = 190, width = 24, height = 22)
text_3_1.set(0)
but_3_1_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(1, 0, 0)
                 )
)
but_3_1_1.place(x = 44, y = 190, width = 11, height = 11)
but_3_1_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(1, 1, 0)
                 )
)
but_3_1_2.place(x = 44, y = 201, width = 11, height = 11)


text_3_2 = StringVar() 
entry_3_2 = Entry(root, font = ('Times New Roman', 15), textvariable = text_3_2)
entry_3_2.place(x = 63, y = 190, width = 24, height = 22)
text_3_2.set(0)
but_3_2_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(2, 0, 0)
                 )
)
but_3_2_1.place(x = 87, y = 190, width = 11, height = 11)
but_3_2_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(2, 1, 0)
                 )
)
but_3_2_2.place(x = 87, y = 201, width = 11, height = 11)


text_3_3 = StringVar() 
entry_3_3 = Entry(root, font = ('Times New Roman', 15), textvariable = text_3_3)
entry_3_3.place(x = 106, y = 190, width = 24, height = 22)
text_3_3.set(0)
but_3_3_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(3, 0, 0)
                 )
)
but_3_3_1.place(x = 130, y = 190, width = 11, height = 11)
but_3_3_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(3, 1, 0)
                 )
)
but_3_3_2.place(x = 130, y = 201, width = 11, height = 11)


text_3_4 = StringVar() 
entry_3_4 = Entry(root, font = ('Times New Roman', 15), textvariable = text_3_4)
entry_3_4.place(x = 149, y = 190, width = 24, height = 22)
text_3_4.set(1)
but_3_4_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(4, 0, 0)
                 )
)
but_3_4_1.place(x = 173, y = 190, width = 11, height = 11)
but_3_4_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(4, 1, 0)
                 )
)
but_3_4_2.place(x = 173, y = 201, width = 11, height = 11)





label_4 = Label(root,
    text = 'Введіть максимальний час існування файлу, який буде перевірено:',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_4.place(x = 19, y = 220, width = 459, height = 20)
label_4_1 = Label(root,
    text = 'міс     доб    год    хвл',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_4_1.place(x = 19, y = 240, width = 160, height = 20)


text_4_1 = StringVar()
entry_4_1 = Entry(root, font = ('Times New Roman', 15), textvariable = text_4_1)
entry_4_1.place(x = 20, y = 260, width = 24, height = 22)
text_4_1.set(0)
but_4_1_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(1, 0, 1)
                 )
)
but_4_1_1.place(x = 44, y = 260, width = 11, height = 11)
but_4_1_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(1, 1, 1)
                 )
)
but_4_1_2.place(x = 44, y = 271, width = 11, height = 11)


text_4_2 = StringVar() 
entry_4_2 = Entry(root, font = ('Times New Roman', 15), textvariable = text_4_2)
entry_4_2.place(x = 63, y = 260, width = 24, height = 22)
text_4_2.set(0)
but_4_2_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(2, 0, 1)
                 )
)
but_4_2_1.place(x = 87, y = 260, width = 11, height = 11)
but_4_2_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(2, 1, 1)
                 )
)
but_4_2_2.place(x = 87, y = 271, width = 11, height = 11)


text_4_3 = StringVar() 
entry_4_3 = Entry(root, font = ('Times New Roman', 15), textvariable = text_4_3)
entry_4_3.place(x = 106, y = 260, width = 24, height = 22)
text_4_3.set(0)
but_4_3_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(3, 0, 1)
                 )
)
but_4_3_1.place(x = 130, y = 260, width = 11, height = 11)
but_4_3_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(3, 1, 1)
                 )
)
but_4_3_2.place(x = 130, y = 271, width = 11, height = 11)


text_4_4 = StringVar() 
entry_4_4 = Entry(root, font = ('Times New Roman', 15), textvariable = text_4_4)
entry_4_4.place(x = 149, y = 260, width = 24, height = 22)
text_4_4.set(31)
but_4_4_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(4, 0, 1)
                 )
)
but_4_4_1.place(x = 173, y = 260, width = 11, height = 11)
but_4_4_2 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(4, 1, 1)
                 )
)
but_4_4_2.place(x = 173, y = 271, width = 11, height = 11)





label_4 = Label(root,
    text = 'Час через який програма закриватиметься після виконання (сек):',
    font = ('Times New Roman', 12),
    relief = FLAT,
    background = 'light grey'
)
label_4.place(x = 19, y = 290, width = 445, height = 20)

text_5_1 = StringVar() 
entry_5_1 = Entry(root, font = ('Times New Roman', 15), textvariable = text_5_1)
entry_5_1.place(x = 20, y = 310, width = 24, height = 22)
text_5_1.set(10)
but_5_1 = Button(root,
                 background = 'light grey',
                 text = '⋀',
                 command = lambda:(
                     do_more_less(1, 0, 2)
                 )
)
but_5_1.place(x = 44, y = 310, width = 11, height = 11)
but_5_1 = Button(root,
                 background = 'light grey',
                 text = '⋁',
                 command = lambda:(
                     do_more_less(1, 1, 2)
                 )
)
but_5_1.place(x = 44, y = 321, width = 11, height = 11)





but_6_1 = Button(root, 
               text = 'За замовчуванням', 
               font = ('Times New Roman', 12),
               background = 'light grey',
               activebackground = 'grey',
               command = lambda:(
                   default()
               )
)
but_6_1.place(x = 20, y = 355, width = 150, height = 22)

but_6_1 = Button(root, 
                text = 'Зберегти налаштування', 
                font = ('Times New Roman', 12),
                background = 'light grey',
                activebackground = 'grey',
                command = lambda:(
                   create_write_db()
                )
)
but_6_1.place(x = 190, y = 355, width = 390, height = 22)


text_logs = IntVar()
text_logs.set(1)
but_check = Checkbutton(root,
                        text = 'Logs',
                        font = ('Times New Roman', 15),
                        background = 'light grey',
                        activebackground = 'light grey',
                        onvalue = 1,
                        offvalue = 0,
                        variable = text_logs
)
but_check.place(x = 480, y = 8)

open_file_and_information()
root.mainloop()