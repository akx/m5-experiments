#!/bin/bash

wget -O - http://firmware-repo-list.m5stack.com/file/known_firmware.json | jq . > known_firmware.json
jq -r '.[]|"http://firmware-repo-list.m5stack.com/firmware/" + .name + "-v" + .version + ".zip"' known_firmware.json | \
	wget -nc -i -
