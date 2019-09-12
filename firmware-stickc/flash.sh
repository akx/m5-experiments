#!/bin/bash

esptool.py --chip esp32 --port $TTY_PORT --baud 750000 --before default_reset --after no_reset write_flash -z \
--flash_mode dio --flash_freq 80m --flash_size detect \
0x1000 bootloader_0x1000.bin \
0x8000 partitions_0x8000.bin \
0x10000 application_0x10000.bin \
0x1F0000 fatfsImg_0x1f0000.img
