class ErrorHandler:


    @staticmethod
    def safe_get(data,key,default=None):

        try:
            return data.get(key,default)

        except:

            return default