#! /bin/env bash

# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

set -e

read -r -p "This script requires root permissions, please acknowledge that it is being run as root. [y|n]: "

if ! [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborting"
    exit 1
fi

echo "Updating script permissions..."
chmod u+x src/format_all.py

echo "Linking to bin..."
sudo ln src/format_all.py /usr/local/bin/format_all

echo "Done, Enjoy :)"
