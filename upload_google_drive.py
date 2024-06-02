from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from log_file import logger_http


def gogle_auth():
    gauth = GoogleAuth()

    # пробуем загрузить сохраненные данные о пользователе, чтобы не проходить ручную аутентификацию
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # входим, если не вошли по сохраненным данным
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})

        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    # сохраняем пользовательские данные для последующих автоматических аутентификаций
    gauth.SaveCredentialsFile("mycreds.txt")

    # logger_http.info("q: gauth  -  "
    #                  f"r: {gauth}")
    return gauth


def another_way(folderName, folderName_create):
    # print("Зашел в another way")
    gauth = gogle_auth()
    # logger_http.info("q: gauth  -  "
    #                  f"r: {gauth}")
    # print(gauth)
    upload_file_in_specific_folder(folderName, folderName_create, gauth=gauth)


# итерируемся по каталогам и ищем нужный
def upload_file_on_drive(user_id, project_name, file_name):
    # print("Зашел в upload_file_on_drive")
    gauth = gogle_auth()
    drive = GoogleDrive(gauth)
    # logger_http.info("q: gauth and drive  -  "
    #                  f"r: {gauth}, {drive}")
    fileID = ''
    fileList = drive.ListFile({'q': f"'root' in parents and trashed=false"}).GetList()
    logger_http.info("q: 'root' in parents and trashed=false  -  "
                     f"r: {fileList}")

    for file in fileList:
        if file['title'] == f"add_to_reminder":
            # print("_____________________\nзашел в папку проека")
            # print(file['title'])
            # print("_____________________\n")
            fileID = file['id']
            break
    str = "\'" + fileID + "\'" + " in parents and trashed=false"

    file_list = drive.ListFile({'q': str}).GetList()
    logger_http.info(f"q: {str}  -  "
                     f"r: {file_list}")

    for file in file_list:
        if file['title'] == f"{user_id}":
            # print("_____________________\n")
            # print("зашел в папку юзера")
            # print(file['title'])
            # print("_____________________\n")
            fileID = file['id']
            break

    str = "\'" + fileID + "\'" + " in parents and trashed=false"
    # print(str)
    file_list = drive.ListFile({'q': str}).GetList()

    logger_http.info(f"q: {str}  -  "
                     f"r: {file_list}")

    for file in file_list:
        if file['title'] == f"{project_name}":
            # print("_____________________\n")
            # print("зашел в папку дела")
            # print(file['title'])
            # print("_____________________\n")
            fileID = file['id']
            file1 = drive.CreateFile({'parents': [{'id': fileID}], 'title': file_name})

            logger_http.info("q: create_file 'parents': [{'id': fileID}], 'title': file_name  -  "
                             f"r: {file1}")
            # print(file_name)
            file1.SetContentFile(file_name)
            file1.Upload()
            # print('УРАААА файл успешно загружен!!!!')
            break


# создаем папку
def upload_file_in_specific_folder(folderName, folderName_create, gauth):
    # print("Зашел в upload_file_in_specific_folder")

    drive = GoogleDrive(gauth)
    folders = drive.ListFile(
        {
            'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"})\
        .GetList()

    logger_http.info(f"q: title= {folderName} and mimeType='application/vnd.google-apps.folder' and trashed=false  -  "
                     f"r: {folders}")
    if not folders:
        # print("no folders")
        fileID = ''
        fileList = drive.ListFile({'q': f"'root' in parents and trashed=false"}).GetList()

        logger_http.info(f"q: 'root' in parents and trashed=false  -  "
                         f"r: {fileList}")
        for file in fileList:
            # print(file['title'])
            if file['title'] == f"add_to_reminder":
                fileID = file['id']
                break
        create_folder(fileID, folderName, drive)

    folders = drive.ListFile(
        {
            'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"})\
        .GetList()

    logger_http.info(f"q: title= {folderName} and mimeType='application/vnd.google-apps.folder' and trashed=false  -  "
                     f"r: {folders}")
    for folder in folders:
        # print("TITLE", folder['title'])
        # print("ID", folder['id'])
        if folder['title'] == folderName:
            create_folder(folder['id'], folderName_create, drive)


def create_folder(folder_id, folderName, drive):
    # print("Зашел в create_folder")
    file_metadata = {
        'title': folderName,
        'parents': [{'id': folder_id}],  # parent folder
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive.CreateFile(file_metadata)
    folder.Upload()
    logger_http.info(f"q: create folder  -  "
                     f"r: {file_metadata}")


# список файлов в текущем проекте
def get_list_of_current_project_files(user_id, project_name):
    gauth = gogle_auth()
    drive = GoogleDrive(gauth)
    fileID = ''
    fileList = drive.ListFile({'q': f"'root' in parents and trashed=false"}).GetList()
    logger_http.info(f"q: 'root' in parents and trashed=false  -  "
                     f"r: {fileList}")

    for file in fileList:
        if file['title'] == f"add_to_reminder":
            fileID = file['id']
            break

    str = "\'" + fileID + "\'" + " in parents and trashed=false"

    file_list = drive.ListFile({'q': str}).GetList()
    logger_http.info(f"q: {str}   -  "
                     f"r: {file_list}")
    for file in file_list:
        if file['title'] == f"{user_id}":
            fileID = file['id']
            break
    str = "\'" + fileID + "\'" + " in parents and trashed=false"

    file_list = drive.ListFile({'q': str}).GetList()
    logger_http.info(f"q: {str}   -  "
                     f"r: {file_list}")

    for file in file_list:
        if file['title'] == f"{project_name}":
            fileID = file['id']
            break
    str = "\'" + fileID + "\'" + " in parents and trashed=false"

    file_list = drive.ListFile({'q': str}).GetList()
    logger_http.info(f"q: {str}   -  "
                     f"r: {file_list}")

    for file in file_list:
        print(file['title'])

    file_list = drive.ListFile({'q': str}).GetList()
    return file_list


def delete_files_from_google_disk(file_id):
    gauth = gogle_auth()
    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({'id': file_id})
    logger_http.info(f"q: delete file  -  "
                     f"r: ")
    file1.Trash()  # убираем файл в корзину
