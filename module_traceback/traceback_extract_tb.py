import traceback
import sys
import os

from module_traceback.traceback_example import produce_exception


template = "{filename:<23}:{linenum}:{funcname}:\n    {source}"

try:
    produce_exception()
except Exception as err:
    exc_type, exc_value, exc_tb = sys.exc_info()
    for tb_info in traceback.extract_tb(exc_tb):
        filename, linenum, funcname, source = tb_info
        if funcname != "<module>":
            funcname = funcname + "()"
        print(
            template.format(
                filename=os.path.basename(filename),
                linenum=linenum,
                source=source,
                funcname=funcname,
            )
        )
