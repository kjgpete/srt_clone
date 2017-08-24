"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import argparse
import logging
import logging.config

class ClientArguments(object):

    DEFAULT_BOT_ROOT = "."
    DEFAULT_LOGGING = logging.DEBUG
    DEFAULT_CONFIG_NAME = "config.yaml"
    DEFAULT_CONFIG_FORMAT = "yaml:"
    DEFAULT_NOLOOP = False
    DEFAULT_BOTTYPE = 0 # 0 = text type, 1 = listen speech

    def __init__(self, client, parser=None):
        self._bot_root = ClientArguments.DEFAULT_BOT_ROOT
        self._logging = ClientArguments.DEFAULT_LOGGING
        self._config_name = ClientArguments.DEFAULT_CONFIG_NAME
        self._config_format = ClientArguments.DEFAULT_CONFIG_FORMAT
        self._no_loop = ClientArguments.DEFAULT_NOLOOP
        self._bot_type = ClientArguments.DEFAULT_BOTTYPE

    def parse_args(self):
        pass

    @property
    def bot_root(self):
        return self._bot_root

    @bot_root.setter
    def bot_root(self, root):
        self._bot_root = root

    @property
    def logging(self):
        return self._logging

    @property
    def config_filename(self):
        return self._config_name

    @property
    def config_format(self):
        return self._config_format

    @property
    def noloop(self):
        return self._no_loop

    @property
    def bot_type(self):
        return self._bot_type

class CommandLineClientArguments(ClientArguments):

    def __init__(self, client, parser=None):
        ClientArguments.__init__(self, client)

        if parser is None:
            self.parser = argparse.ArgumentParser(description=client.get_description())
        else:
            self.parser = parser
        self.parser.add_argument('--bot_root', dest='bot_root', help='root folder for all bot configuration data')
        self.parser.add_argument('--config', dest='config', help='configuration file location')
        self.parser.add_argument('--cformat', dest='cformat', help='configuration file format (yaml|json|ini)')
        self.parser.add_argument('--logging', dest='logging', help='logging configuration file')
        self.parser.add_argument('--noloop', dest='noloop', action='store_true', help='do not enter conversation loop')
        self.parser.add_argument('--bot_type', dest='bot_type', help='texting or talking bot type', type=int, default=0)
        client.add_client_arguments(self.parser)

    def parse_args(self):
        self.args = self.parser.parse_args()

        self._bot_root = self.args.bot_root
        self._logging = self.args.logging
        self._config_name = self.args.config
        self._config_format = self.args.cformat
        self._no_loop = self.args.noloop
        self._bot_type = self.args.bot_type


