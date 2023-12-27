"""
This module contains routes for API endpoints.
The modules are dynamically imported
"""
import importlib
import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    importlib.import_module("server.routes." + module[:-3])
del module

from server.global_data import GlobalData

# A dict of users.
GLOBAL_DATA = GlobalData()
