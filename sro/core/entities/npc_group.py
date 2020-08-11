from .npc_group_tab import NPCGroupTab

class NPCGroupPrefix:
    codename = "STORE_{npc_name}_{name}"
    namestr_id  = "SN_STORE_{npc_name}_{name}"

class NPCGroup:
    def __init__(self):
        self._name = ""
        self._textname = ""
        self._tabs = []

    def set_name(self, name: str):
        self._name = name
        return self

    def set_textname(self, textname: str):
        self._textname = textname
        return self

    def add_tab(self, tab: NPCGroupTab):
        self._tabs.append(tab)
        return self
