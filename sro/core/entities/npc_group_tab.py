class NPCGroupTabPrefix:
    codename = "STORE_{npc_name}_{name}"

class NPCGroupTab:
    def __init__(self):
        self._name = ""
        self._strid = ""
        self._textname = ""

    def set_name(self, name: str):
        self._name = name
        return self

    def set_strid(self, strid: str):
        self._strid = strid
        return self

    def set_textname(self, textname: str):
        self._textname = textname
        return self
