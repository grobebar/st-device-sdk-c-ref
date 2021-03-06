#!/usr/bin/env python
#-*- coding: utf-8 -*-

import platform
import os
import sys

REPLACE_LIST = [
    ["esp32", "esp32_v3.3"]
]

STDK_REF_PATH = os.path.dirname(os.path.abspath(__file__))
STDK_CORE_PATH = os.path.join(STDK_REF_PATH, "iot-core")

os.environ["STDK_REF_PATH"] = STDK_REF_PATH
os.environ["STDK_CORE_PATH"] = STDK_CORE_PATH

def print_usage():
    print("")
    print("Usage: python build.py apps/[BSP_NAME]/[APP_NAME]")
    print("                 or")
    print("       python build.py [BSP_NAME] [APP_NAME]")
    print("--------------------------------------------------")
    print("  ex) python build.py apps/esp32_v4.x/switch_example")
    print("  ex) python build.py esp32_v4.x light_example")
    print("")

def find_build_script(bsp_name):
    if os.path.exists(os.path.join("tools", bsp_name, "build_"+bsp_name+".py")):
        return "python " + os.path.join("tools", bsp_name, "build_"+bsp_name+".py")
    if "SHELL" in os.environ:
        if os.path.exists(os.path.join("tools", bsp_name, "build_"+bsp_name+".sh")):
            return os.path.join("tools", bsp_name, "build_"+bsp_name+".sh")
    print("Fail to find build script")
    print_usage()
    exit()

if len(sys.argv) == 1:
    print_usage()
    exit()

if os.path.exists(sys.argv[1]):
    # assume that input type is apps/[BSP_NAME]/[APP_NAME]
    BSP_NAME = os.path.split(os.path.split(os.path.abspath(sys.argv[1]))[0])[1]
    APP_NAME = os.path.split(os.path.abspath(sys.argv[1]))[1]
    EXTRA_ARGS = sys.argv[2:]
else:
    if len(sys.argv) < 3:
        print("Error : Fail to find app path")
        print_usage()
        exit()
    BSP_NAME = sys.argv[1]
    APP_NAME = sys.argv[2]
    EXTRA_ARGS = sys.argv[3:]

for item in REPLACE_LIST:
    if BSP_NAME == item[0]:
        BSP_NAME = item[1]

build_script = find_build_script(BSP_NAME)
build_cmd = build_script + " " + BSP_NAME + " " + APP_NAME
for args in EXTRA_ARGS:
    build_cmd = build_cmd + " " + args
ret_val = os.system(build_cmd)
if ret_val:
    print_usage()
