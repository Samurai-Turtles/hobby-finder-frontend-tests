from carregar_configuracao import carregar_configuracao

class ApiConsts:
    Base = carregar_configuracao()["url"]

class UsuarioRotas:
    Base              = "user"
    Post              = Base
    Put               = Base
    Get               = Base
    Delete            = Base + "/delete"    
    login             = Base + "/login"    
    logout            = Base + "/logout"    
    recovery_password = Base + "/recover-password"    

class EventoRotas:
    Base              = "event"
    Post              = Base
    Get_By_Auth       = Base
    Get_By_User_Id    = Base + "/" + UsuarioRotas.Base
    Get_By_Id         = Base 
    Put               = Base
    Delete            = Base

class SolicitacaoRotas:
    Base              = "request"
    Post              = Base
    Get_By_Evento     = Base
    Get_By_User       = UsuarioRotas.Base + "/" + Base
    Accept            = Base    
    Reject            = Base
    Delete_By_User    = Get_By_User

class ParticipacaoRotas:
    Base                     = "participation"
    Get_By_Evento            = Base
    Delete_By_Id             = Base
    Management_Participation = Base
    Delete_By_User           = Base
    Update_BY_User           = Base
    Get_All_By_User          = UsuarioRotas.Base + "/" + Base
    
class AvaliacaoRotas:
    Base = "evaluation"
    Post = Base
    Get  = Base

class NotificacaoRotas:
    Base = "notifications"
    Get  = Base

class SituacaoRotas:
    Base = "situation"

class FotoRotas:
    Base         = "photo"
    Get_By_Auth  = Base
    Get_By_Event = Base
    Get_By_Id    = Base