from hand_sign_detection.logger import logging
from hand_sign_detection.exception import AppException
import sys

try:
    a=1/0
except Exception as e:
    raise AppException("Error occurred",sys)