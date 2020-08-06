from cement import Controller, ex


class AddNPC(Controller):
    class Meta:
        label = 'add'
        stacked_type = 'embedded'
        stacked_on = 'npc'
    
    @ex(help='An interactive app that creates an NPC from user input.')
    def create(self):
        self.app.log.error("NotYetImplemented")