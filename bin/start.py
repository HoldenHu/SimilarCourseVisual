import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from lib.global_variable import MAIN_FUNCTION_PATH

if sys.argv[1] == "drawWords":
    os.system("python " + MAIN_FUNCTION_PATH + " drawWords")

if sys.argv[1] == "drawModules":
    os.system("python " + MAIN_FUNCTION_PATH + " drawModules")

