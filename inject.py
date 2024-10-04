#!/usr/bin/env python3

import lief

target = "libadblockruleparser.so"

libnative = lief.parse(target)
libnative.add_library("libgadget.so") # Injection!

libnative.write(target)
