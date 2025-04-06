import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Configurações
CONFIG = {
    "url_base": "http://localhost:8080",
    "usuarios": {
        "participante": {"username": "user_participante", "password": "Senha@123"},
        "organizador": {"username": "user_organizador", "password": "Senha@123"},
        "novo_participante": {"username": "user_novo", "password": "Senha@123"}
    }
}

@pytest.fixture
def driver():
    """Configuração do WebDriver"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def fazer_login(driver, usuario_tipo):
    """Realiza login no sistema"""
    usuario = CONFIG["usuarios"][usuario_tipo]
    driver.get(f"{CONFIG['url_base']}/login")
    driver.find_element(By.ID, "username").send_keys(usuario["username"])
    driver.find_element(By.ID, "password").send_keys(usuario["password"])
    driver.find_element(By.ID, "btn-login").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/home"))

class TestNotificacoesPerfis:

    def test_rt052_acessar_notificacoes(self, driver):
        """
        RF-24: Visualizar Notificações
        RT-052: Acessar Notificações
        """
        fazer_login(driver, "participante")
        
        # 1-2: Acessar notificações
        driver.find_element(By.ID, "btn-notificacoes").click()
        
        # Verificação
        notificacoes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "notificacao-item"))
        )
        assert len(notificacoes) > 0
        # Verifica ordenação (mais recente primeiro)
        timestamps = [notif.find_element(By.CLASS_NAME, "notificacao-timestamp").text for notif in notificacoes]
        assert timestamps == sorted(timestamps, reverse=True)

    def test_rt053_notificacao_mudanca_evento(self, driver):
        """
        RF-25: Notificações de Mudanças no Evento
        RT-053: Notificação de Mudança no Evento
        """
        fazer_login(driver, "participante")
        
        # Simular recebimento de notificação
        driver.execute_script("""window.postMessage({type: 'nova-notificacao', data: {tipo: 'mudanca-evento', mensagem: 'Data do evento alterada'}})""")
        
        # 1-3: Clicar na notificação
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notificacao-item')][contains(.,'Data do evento alterada')]"))
        ).click()
        
        # Verificações
        assert "notificacoes" in driver.current_url
        assert "Data do evento alterada" in driver.page_source

    def test_rt054_notificacao_solicitacao_evento_privado(self, driver):
        """
        RF-26: Notificações de Solicitações em Evento Privado
        RT-054: Notificação de Solicitação para Evento Privado
        """
        fazer_login(driver, "organizador")
        
        # Simular solicitação
        driver.execute_script("""window.postMessage({type: 'nova-notificacao', data: {tipo: 'nova-solicitacao', mensagem: 'Nova solicitação para seu evento'}})""")
        
        # 1-2: Clicar na notificação
        notificacao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notificacao-item')][contains(.,'solicitação')]"))
        )
        notificacao.click()
        
        # Verificações
        assert "notificacoes" in driver.current_url
        assert "Nova solicitação para seu evento" in driver.find_element(By.ID, "detalhes-notificacao").text

    def test_rt055_notificacao_aprovacao_evento_privado(self, driver):
        """
        RF-27: Notificação de Aprovação em Evento Privado
        RT-055: Notificação de Aprovação de Solicitação
        """
        # Primeiro faz login como novo participante para solicitar
        fazer_login(driver, "novo_participante")
        driver.find_element(By.ID, "btn-eventos").click()
        driver.find_element(By.XPATH, "//div[contains(@class,'evento-privado')][1]").click()
        driver.find_element(By.ID, "btn-solicitar-participacao").click()
        
        # Agora faz login como organizador para aprovar
        fazer_login(driver, "organizador")
        driver.find_element(By.ID, "btn-notificacoes").click()
        driver.find_element(By.XPATH, "//div[contains(@class,'notificacao-item')][contains(.,'nova solicitação')]").click()
        driver.find_element(By.ID, "btn-aprovar-solicitacao").click()
        
        # Verifica notificação de aprovação enviada
        fazer_login(driver, "novo_participante")
        notificacao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notificacao-item')][contains(.,'solicitação aprovada')]"))
        )
        notificacao.click()
        assert "Sua solicitação foi aprovada" in driver.page_source

    def test_rt056_notificacao_confirmacao_presenca(self, driver):
        """
        RF-28: Notificação de Confirmação de Presença
        RT-056: Notificação de Confirmação de Presença
        """
        # Configuração: usuário confirmando presença
        fazer_login(driver, "novo_participante")
        driver.find_element(By.ID, "btn-meus-eventos").click()
        driver.find_element(By.XPATH, "//div[contains(@class,'evento-aprovado')]").click()
        driver.find_element(By.ID, "btn-confirmar-presenca").click()
        
        # Verifica notificação no organizador
        fazer_login(driver, "organizador")
        notificacao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notificacao-item')][contains(.,'confirmou presença')]"))
        )
        notificacao.click()
        assert "confirmou presença no evento" in driver.page_source

    def test_rt057_visualizar_perfil_outro_usuario(self, driver):
        """
        RF-29: Visualizar Perfil de Outros Usuários
        RT-057: Visualizar Perfil de Outro Usuário
        """
        fazer_login(driver, "organizador")
        
        # 1-7: Navegação até o perfil de participante
        driver.find_element(By.ID, "btn-perfil").click()
        driver.find_element(By.ID, "tab-meus-eventos").click()
        driver.find_element(By.XPATH, "//div[contains(@class,'evento-card')][1]").click()
        driver.find_element(By.ID, "btn-participantes").click()
        participante = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'participante-card')][1]"))
        )
        participante.find_element(By.CLASS_NAME, "foto-perfil").click()
        
        # Verificações
        assert "perfil" in driver.current_url
        assert "Bio:" in driver.page_source
        assert "Senha" not in driver.page_source  
