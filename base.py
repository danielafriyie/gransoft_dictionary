"""
base.py is part of Gransoft Dictionary.

Gransoft Dictionary is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gransoft Dictionary is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Gransoft Dictionary.  If not, see <https://www.gnu.org/licenses/>.
"""

# exceptions package
from exceptions_.exeptions_ import DictDatabaseDoesNotExist

# resources package
from resources import DictDatabase

# ui package
from ui.base_ui import Ui_MainWindow
from ui.new_word_ui import Ui_add_new_word

database = DictDatabase(default_path=True)
