# exceptions package
from exceptions_.exeptions_ import DictDatabaseDoesNotExist

# resource package
from resources.resources import DictDatabase

# ui package
from ui.base_ui import Ui_MainWindow
from ui.new_word_ui import Ui_add_new_word

database = DictDatabase(default_path=True)
