from asyncio import events
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from back.body import usuario
from back.request import usuario_request
from back.request import event_request
from src.back.request.usuario_request import *
from src.back.body.usuario import *
from src.back.request.event_request import *
from src.back.body.evento import *


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestEventos:

    def login(self, driver):
        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        driver.get("http://localhost:8000/login")
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "password").send_keys("Senha@1234")
        driver.find_element(By.ID, "btn-login").click()

    def test_rt017_exibir_eventos_por_proximidade(self, driver):
        self.login(driver)
        event_request.post_evento(evento.evento(
            name="Festa da Lua",
            begin="2023-10-01T20:00:00",
            end="2023-10-01T23:00:00",
            local="Rua das Flores",
            privacidade='privado',
            descricao="Uma festa incrível!",
            maximum=100
        ))
        eventos = driver.find_elements(By.CLASS_NAME, "evento-item")
        assert len(eventos) > 0
        for evento in eventos:
            distancia = evento.find_element(By.CLASS_NAME, "distancia")
            assert "km" in distancia.text

    def test_rt018_evento_privado_restrito(self, driver):
        self.login(driver)

        event_request.post_evento(evento.evento(
            name="Festa da Lua",
            begin="2023-10-01T20:00:00",
            end="2023-10-01T23:00:00",
            local="Rua das Flores",
            privacidade='privado',
            descricao="Uma festa incrível!",
            maximum=100
        ))

        eventos = driver.find_elements(By.CLASS_NAME, "evento-item")
        for evento in eventos:
            privacidade = evento.find_element(By.CLASS_NAME, "privado")
            if privacidade.text == "Privado":
                assert "Local:" not in evento.text
                assert "Distância" in evento.text

    def test_rt019_busca_evento_por_nome(self, driver):
        self.login(driver)

        event_request.post_evento(evento.evento(
            name="Festa da Lua",
            begin="2023-10-01T20:00:00",
            end="2023-10-01T23:00:00",
            local="Rua das Flores",
            privacidade='privado',
            descricao="Uma festa incrível!",
            maximum=100
        ))
        campo_busca = driver.find_element(By.ID, "campo-busca")
        campo_busca.send_keys("Festa da Lua")
        campo_busca.send_keys(Keys.RETURN)
        resultados = driver.find_elements(By.CLASS_NAME, "evento-item")
        assert any("Festa da Lua" in r.text for r in resultados)

    def test_rt020_filtrar_eventos(self, driver):
        self.login(driver)
        driver.find_element(By.ID, "filtro-distancia").click()
        driver.find_element(By.ID, "filtro-privacidade-publico").click()
        driver.find_element(By.ID, "filtro-tags-musica").click()
        eventos = driver.find_elements(By.CLASS_NAME, "evento-item")
        assert all("Musica" in e.text or "musica" in e.text.lower()
                   for e in eventos)

    def test_rt021_eventos_usuario(self, driver):
        self.login(driver)
        driver.find_element(By.ID, "btn-perfil").click()
        driver.find_element(By.ID, "tab-meus-eventos").click()
        criados = driver.find_element(By.ID, "eventos-criados")
        participados = driver.find_element(By.ID, "eventos-participados")
        assert criados.is_displayed()
        assert participados.is_displayed()

    def test_rt022_participar_evento_publico(self, driver):
        self.login(driver)
        evento = driver.find_element(By.CLASS_NAME, "evento-publico")
        evento.find_element(By.CLASS_NAME, "btn-participar").click()
        sucesso = driver.find_element(By.CLASS_NAME, "mensagem-sucesso")
        assert "participante" in sucesso.text.lower()

    def test_rt023_cancelar_participacao(self, driver):
        self.login(driver)
        driver.find_element(By.ID, "btn-perfil").click()
        driver.find_element(By.ID, "tab-meus-eventos").click()
        driver.find_element(By.ID, "filtro-participando").click()
        evento = driver.find_element(By.CLASS_NAME, "evento-item")
        evento.find_element(By.CLASS_NAME, "btn-cancelar").click()
        botao = evento.find_element(By.CLASS_NAME, "btn-participar")
        assert botao.is_displayed()
