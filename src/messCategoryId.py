from enum import Enum
class MessCategory(Enum):
    PLAYERINFO = '1'
    DATEINFO = '2'
if __name__=="__main__":
    for messId in MessCategory:
        print(f"{messId}=>{messId.name}:{messId.value}")