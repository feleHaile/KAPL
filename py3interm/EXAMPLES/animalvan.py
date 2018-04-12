#!/usr/bin/python3
class AnimalVan(object):

    def __init__(self,target,action):
        self._target = target
        self._action = action

    def act(self):
        print("Squad! Eyes front! Stand at ease. {0} {1}{2} ...{1}!".format(
            self._target.capitalize(),
            self._action,
            self._get_plural_ending(),
        ))

    def _get_plural_ending(self):    
        ''' Get correct plural ending ''' 
        if self._action.endswith("e"):
            suffix = "rs"
        elif self._action[-1] in "bdfglmnprst":
            suffix = self._action[-1] + "ers"
        else:
            suffix = "ers"
        return suffix
