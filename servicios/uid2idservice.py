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
        if d_rsp.get('rsp','ERR') == 'OK':
            id = d_rsp['id']
            if id is None:
                self.logger.info( f'No uid2dlgid rcd for uid={uid}')
            else:
                if isinstance(id, bytes):
                    id = id.decode()
            d_rsp = {'rsp':'OK', 'id': id}
        
        return d_rsp
    

    def set_id_and_uid(self, uid=None, id=None):
        """
        """
        self.logger.debug("")
        return self.repo.set_id_and_uid(uid, id)
        

