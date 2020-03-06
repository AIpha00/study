import logging
import os
from logging import handlers


def _logging(**kwargs):
    level = kwargs.pop('level', None)
    filename = kwargs.pop('filename', None)
    datefmt = kwargs.pop('datefmt', None)
    format = kwargs.pop('format', None)
    fileList = kwargs.pop('fileList', None)
    if level is None:
        level = logging.DEBUG
    if filename is None:
        filename = 'default11.log'
    if datefmt is None:
        datefmt = '%Y-%m-%d %H:%M:%S'
    if format is None:
        format = '%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s'

    log = logging.getLogger(filename)
    format_str = logging.Formatter(format, datefmt)
    #
    cmd = logging.StreamHandler()
    cmd.setFormatter(format_str)
    cmd.setLevel(level)
    log.addHandler(cmd)

    for filename in fileList:
        if '.log' not in filename:
            continue
        th = handlers.TimedRotatingFileHandler(filename=filename, when='S', backupCount=0, interval=1,
                                               encoding='utf-8')

        def namer(filename):
            return filename.split('.log')[0] + '.log'

        th.namer = namer
        th.suffix = "%Y-%m-%d.log"
        th.setFormatter(format_str)
        th.setLevel(logging.INFO)
        log.addHandler(th)
        log.setLevel(level)
    return log


filePath = '.'


def list_dir(filePath, list_name=[]):
    for file in os.listdir(filePath):
        file_path = os.path.join(filePath, file)
        if os.path.isdir(file_path):
            list_dir(file_path, list_name)
        else:
            list_name.append(file_path)
    return list_name


os.makedirs('./logs', exist_ok=True)
logger = _logging(fileList=list_dir(filePath))
logger.info('日志清理....')
