# MIT License

# Copyright (c) 2019 Georgios Papachristou

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from jarvis._version import __version__


class OutputStyler:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


user_input = OutputStyler.CYAN + ':-$ ' + OutputStyler.ENDC


def add_dashes(text='='):
    """
    Add dashes based on terminal length
    """
    process = os.popen('stty size', 'r')
    result = process.read()
    process.close()
    if result:
        rows, columns = result.split()
        text_length = len(text)
        remaining_places = int(columns) - text_length
        if remaining_places > 0:
            return '=' * (remaining_places // 2 - 1) + ' ' + text + ' ' + '=' * (remaining_places // 2 - 1)
        else:
            return text
    else:
        return text


def print_console_header(text='-'):
    """
    Create a dynamic header based on terminal length.
    """
    print(add_dashes(text))


jarvis_logo = "\n" \
              "      ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗\n" \
              "      ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝\n" \
              "      ██║███████║██████╔╝██║   ██║██║███████╗\n" \
              " ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║\n" \
              " ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║\n" \
              "  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝\n"
start_text =" -  Voice Assistant Platform  " + "v" + __version__ + "  -"
