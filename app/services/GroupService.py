from models import Group,db

class GroupService:

    @staticmethod
    def save_group(group):
        db.session.add(group)
        db.session.flush()
        message = "Se guardo el grupo con exito"
        return message,group,201