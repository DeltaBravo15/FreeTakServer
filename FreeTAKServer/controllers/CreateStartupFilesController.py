import os
from configuration.DataPackageServerConstants import DataPackageServerConstants
from configuration.LoggingConstants import LoggingConstants
from pathlib import PurePath
class CreateStartupFilesController:
    def __init__(self):
        self.file_dir = os.path.dirname(os.path.realpath(__file__))
        self.dp_directory = PurePath(self.file_dir, DataPackageServerConstants().DATAPACKAGEFOLDER)
        self.logs_directory = PurePath(self.file_dir, LoggingConstants().LOGDIRECTORY)
        self.createFolder()
    def createFolder(self):
        try:
            os.mkdir(self.dp_directory)
        except:
            pass
        try:
            os.mkdir(self.logs_directory)
        except:
            pass
        WARNINGLOG = open(LoggingConstants().WARNINGLOG, "w")
        WARNINGLOG.close()
        HTTPLOG = open(LoggingConstants().HTTPLOG, "w")
        HTTPLOG.close()
        DEBUGLOG = open(LoggingConstants().DEBUGLOG, "w")
        DEBUGLOG.close()
        INFOLOG = open(LoggingConstants().INFOLOG, "w")
        INFOLOG.close()
