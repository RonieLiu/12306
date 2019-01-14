import time
import datetime
import config.logger
import traceback
import sys

from config import configCommon


def getTodayDateStr():
    return str(datetime.datetime.now())
    return time.strftime("%Y-%m-%d %H:%m:%s ", time.localtime(configCommon.getNowTimestamp()))


def log(msg):
    try:
        if isinstance(msg, Exception):
            echoStack(msg)
        else:
            echo(msg)
    except Exception as e:
        echoStack(e)


def echo(msg):
    prefix = getTodayDateStr();
    out = prefix + "\t" + msg;
    config.logger.log(out);
    print(out);


def echoStack(e):
    echo("")
    print(e)
    exc_type, exc_value, exc_traceback_obj = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=10, file=sys.stdout)
