from cement import Controller, ex

from sro.core.services import NPCService, CharacterService

class AddNPC(Controller):
    class Meta:
        label = 'add'
        stacked_type = 'embedded'
        stacked_on = 'npc'
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self._npc_service = NPCService()
        self._char_service = CharacterService()

    @property
    def banner(self):
        return """
            This Command Handles the Creation of NPCs,
            You will be asked to answer some Questions in order to 
            properly Create your new NPC,
            Some needed values are a MUST, some others are optional with defaults.

            First we will take the NPC data,
            then ask for the number of groups and take each ones data,
            then for each group we will ask for their tabs data.

            As an alternate method, we will take this data in a json file instead.
        """


    @ex(help='An interactive app that creates an NPC from user input.')
    def create(self):
        self.app.log.info(self.banner)
        npc_name = input("Please enter NPC Name: ")
        self.app.log.info(f"You entered: {npc_name}")