from cement import Controller, ex

from sro.core.entities import NPC, NPCGroup, NPCGroupTab
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
        npc = NPC()

        npc.set_name(input("Please enter NPC CodeName: ")
            ).set_textname(input("Please enter NPC Name: ")
            ).set_3dmodel_path(input("Please enter NPC '3D Model' path: "))

        n_groups = int(input("How many Groups would you like to add? "))
        for i in range(1, n_groups + 1):
            npc_group  = NPCGroup()
            npc_group.set_name(input(f"Please enter Group {i} Name: "))

            n_tabs = int(input("How many Tabs would you like In this Group? "))
            for j in range(1, n_tabs + 1):
                group_tab = NPCGroupTab()
                group_tab.set_name(input(f"Please enter Tab {j} Name: "))
                npc_group.add_tab(group_tab)
            npc.add_group(npc_group)

        self._npc_service.add_npc(npc)