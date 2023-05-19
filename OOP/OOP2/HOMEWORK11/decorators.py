import datetime
def get_sensitive_data_decorator_error(function):
    # print('error')
    def wrraper(size):
        if len(function()) > size:
            raise Exception('Size is Over')
    return wrraper
def get_sensitive_data_decorator_log(function):
    def wrraper(size):
        try:
            function(size)
        except Exception as e:
            with open('log.txt', 'w') as file:
                file.write(f'{str(e),str(datetime.datetime.now())}')
    return wrraper