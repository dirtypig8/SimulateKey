from MainWindow import MainWindow  
from PyQt5.QtWidgets import QApplication
from PyQt5 import sip
import sys
from SystemInitializer.InitializeConfigDictionary import InitializeConfigDictionary
from SystemInitializer.InitializeLogWritter import InitializeLogWriter
from SystemInitializer.StartServing import StartServing
from ArgParser import ArgParser
from CoreConfig.ConfigDictionary import ConfigDictionary

if __name__ == '__main__':
    commandline_args = ArgParser().get_args()
    InitializeConfigDictionary().execute(commandline_args.config_path)
    InitializeLogWriter.execute()
    StartServing().execute()

    app = QApplication([])

    main_window = MainWindow().get_main_window()
    main_window.setFixedSize(1024, 768)
    main_window.show()
    sys.exit(app.exec_())
