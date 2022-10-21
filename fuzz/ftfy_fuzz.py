#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    import ftfy

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    ftfy.fix_text(fdp.ConsumeUnicode(len(data)))


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()