#!/home/pablo/Spymovil/python/proyectos/APICOMMS_2025/.venv/bin/python

class Uid2IdService:
    """
    """
    def __init__(self, repositorio, logger):
        self.repo = repositorio
        self.logger = logger

    def get_id_from_uid(self, uid=None):
        """
        """
        self.logger.debug("")
        d_rsp = self.repo.get_id_from_uid(uid)
        #
        if d_rsp.get('status_code',0) == 200:
            id = d_rsp['id']
            if isinstance(id, bytes):
                id = id.decode()
            d_rsp = {'status_code':200, 'id': id}
        
        return d_rsp
    

    def set_id_and_uid(self, uid=None, id=None):
        """
        """
        self.logger.debug("")
        d_rsp = self.repo.set_id_and_uid(uid, id)
        if d_rsp.get('status_code',0) == 200:
            d_rsp = {'status_code':200, 'uid': uid}
        
        return d_rsp

