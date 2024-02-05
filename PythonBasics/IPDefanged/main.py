class Solution(object):
    def defangIPaddr(self, address):
        split = address.split(".")
        defanged = "[.]".join(split)

        return defange