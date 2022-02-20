file_path = 'D:\pythonProjects\src\Python-Life\\text_file\pi_digits'
with open(file_path, 'a') as file_object:
    wifes_name = ['qiyana', 'mei', 'bronya']
    for wife_name in wifes_name[:]:
        reason = input("Please input why you like "+wife_name.title()+"\n")
        file_object.write(reason+'\n')



