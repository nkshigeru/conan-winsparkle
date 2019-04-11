#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(settings={"arch": "x86", "build_type": "Release"})
    builder.add(settings={"arch": "x86_64", "build_type": "Release"})
    builder.run()
