from sro.core.db import transaction
from sro.core.entities import NPC

""" ALL @transaction methods should take 
session parameter at the end of the argument list
"""
class NPCService:
    def __init__(self):
        pass

    @transaction
    def add_npc(self, npc: NPC, session):
        pass