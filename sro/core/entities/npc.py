from .npc_group import NPCGroup

class NPCPrefix:
    codename = "NPC_{name}"
    namestr_id  = "SN_NPC_{name}"
    shop = "STORE_{name}"
    shopgroup = "GROUP_STORE_{name}"

class NPC:
    def __init__(self):
        self._name = ""
        self._textname = ""
        self._3dmodel_path = ""
        self._groups = []

    def set_textname(self, textname: str):
        self._textname = textname
        return self

    def set_name(self, name: str):
        self._name = name
        return self

    def set_3dmodel_path(self, path: str):
        self._3dmodel_path = path
        return self

    def add_group(self, group: NPCGroup):
        self._groups.append(group)
        return self
    
    @property
    def codename(self):
        return NPCPrefix.codename.format(name=self._name)

    @property
    def namestr_id(self):
        return NPCPrefix.namestr_id.format(name=self._name)

    @property
    def shop(self):
        return NPCPrefix.shop.format(name=self._name)

    @property
    def shopgroup(self):
        return NPCPrefix.shopgroup.format(name=self._name)