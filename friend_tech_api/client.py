from friend_tech_api.api import APIBase, NonRest, Users

class FriendTechClient:
    def __init__(self):
        api_base = APIBase()
        self.non_rest = NonRest(api_base)
        self.users = Users(api_base)
