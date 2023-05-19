from decorators import get_sensitive_data_decorator_error
from decorators import get_sensitive_data_decorator_log
# def get_sensitive_data_decorator_error(function):
#     def wrraper(size):
#         if len(function()) > size:
#             raise Exception('Size is Over')
#     return wrraper
# def get_sensitive_data_decorator_log(function):
#     def wrraper(size):
#         try:
#             function(size)
#         except Exception as e:
#             with open('log.txt', 'w') as file:
#                 file.write(f'{str(e),str(datetime.datetime.now())}')
#     return wrraper
@get_sensitive_data_decorator_log
@get_sensitive_data_decorator_error
def get_sensitive_data():
    user_list = {}
    with open('password.txt') as file:
        for index,value in enumerate(file.readlines()):
            if index == 0:
                continue
            else:
                name,password = value.rstrip().split(',')
                user_list[name] = password
        return user_list

get_sensitive_data(5)


