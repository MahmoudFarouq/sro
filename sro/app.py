import os
from cement.utils import fs
from cement import App, TestApp, init_defaults

from sro.controllers.base import Base
from sro.controllers.npc import NPC, AddNPC

# configuration defaults
CONFIG = init_defaults('sro')
CONFIG['sro']['foo'] = 'bar'

class Sro(App):
    """Sro primary application."""

    class Meta:
        label = 'sro'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,

            NPC,
            AddNPC
        ]


class SroTest(TestApp,Sro):
    """A sub-class of Sro that is better suited for testing."""

    class Meta:
        label = 'sro'

