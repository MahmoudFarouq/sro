from cement import Controller, ex


class NPC(Controller):
    class Meta:
        label = 'npc'
        stacked_type = 'nested'

        # text displayed at the top of --help output
        description = 'NPC Manipulation tools'

        # text displayed at the bottom of --help output
        epilog = 'Usage: sro npc create'