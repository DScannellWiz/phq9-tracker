import os
import sys


runtime_root = getattr(sys, "_MEIPASS", None)
if runtime_root:
    os.environ["TCL_LIBRARY"] = os.path.join(runtime_root, "_tcl_data")
    os.environ["TK_LIBRARY"] = os.path.join(runtime_root, "_tk_data")
