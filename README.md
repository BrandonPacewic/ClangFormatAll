# Clang Format All

Clang format all is a script used to more efficiently call clang-format on a large number of files from the command line.

## Usage

```bash
> format_all
```

```Output
> Formatted 0 files in 0.000
```

The clang-format tool will automatically take the formatting options stored in the `.clang-format` file.

## What file types will be formatted?

The base list of file suffixes is:

- `.cpp`
- `.h`
- `.hpp`
- `.cc`
- `.cxx`

To expand this list edit the `format_all.py` file and change the `FILE_TARGETS` list.
There is currently no way to edit this list from the command line but this option may become available in the future.

## Installation

Please note that this is a linux specific script.

### Prerequisites

- The clang-format llvm tool.
- The python3 interpreter.

### Commands

```bash
sudo ./install.sh
```

## License

Copyright (c) Brandon Pacewic

SPDX-License-Identifier: MIT
