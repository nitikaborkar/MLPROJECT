import sys
import logging

def error_msg_detail(msg, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(msg))
    return error_message

class CustomException(Exception):  # inherits the parent exception
    def __init__(self, msg, error_detail: sys):  # overwritten the init method
        self.error_message = error_msg_detail(msg, error_detail)  # setting the error message
        super().__init__(self.error_message)  # calling the parent class init method
        
    def __str__(self):  # overwritten the str method
        return self.error_message  # returning the error message
