from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from sqlite import get_projects_name_for_user
from upload_google_drive import get_list_of_current_project_files

ikb_file = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('\U00002795 Добавить вложения...',
                                                                       callback_data='with_file')],
                                                 [InlineKeyboardButton('Без вложений',
                                                                       callback_data='without_file')]])

ikb_cancel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Вернуться в главное меню',
                                                                         callback_data='cancel')]])


def get_inline_keybord_for_edit(user_id):
    edit_ikeyboard = InlineKeyboardMarkup(row_width=1)
    for group in get_projects_name_for_user(user_id):
        btn_text = group[0]
        btn_callback = group[0]
        edit_ikeyboard.add(InlineKeyboardButton(text=btn_text, callback_data=btn_callback))
    return edit_ikeyboard


ikb_done_or_not = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Да', callback_data='yes')],
                                                        [InlineKeyboardButton('Нет', callback_data='no')]])

ikb_edit_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('\U0000270F Описание',
                                                                            callback_data='edit_description'),
                                                       InlineKeyboardButton('\U0000270F Дата оповещения',
                                                                            callback_data='edit_notice_date')],

                                                      [InlineKeyboardButton('\U0000270F Периодичность',
                                                                            callback_data='edit_periodic'),
                                                       InlineKeyboardButton('\U0000270F Время оповещения',
                                                                            callback_data='edit_time')],
                                                      [InlineKeyboardButton('\U0000270F Файлы',
                                                                            callback_data='edit_files'),

                                                       InlineKeyboardButton('\U0000270F Состояние',
                                                                            callback_data='edit_state')]])

ikb_files = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('\U00002795 Загрузить ещё...',
                                                                        callback_data='add_more_files'),
                                                   InlineKeyboardButton('Закрыть окно загрузки',
                                                                        callback_data='end_add_files')]])

ikb_add_delete_files = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('\U0000274C Удалить файлы',
                                                                                   callback_data='delete_files')],
                                                             [InlineKeyboardButton('\U00002795 Прикрепить '
                                                                                   'дополнительные файлы...',
                                                                                   callback_data='upload_new_files')]])

ikb_after_delete = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('\U0001F501 Продолжить удаление '
                                                                               'файлов...',
                                                                               callback_data='delete_more_files')],
                                                         [InlineKeyboardButton('\U000026D4 Закончить удаление',
                                                                               callback_data='end_deleting_files')]])


def get_files_from_disk(user_id, project_name):
    del_file_ikeyboard = InlineKeyboardMarkup(row_width=1)
    for file in get_list_of_current_project_files(user_id, project_name):
        btn_text = file['title']
        btn_callback = file['id']
        del_file_ikeyboard.add(InlineKeyboardButton(text=btn_text, callback_data=btn_callback))
    return del_file_ikeyboard
