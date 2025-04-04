import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from back.body import usuario
from back.request import usuario_request
from src.back.request.usuario_request import *
from src.back.body.usuario import *


class TestLoginEPerfil:

    def test_login_sucesso_username(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        time.sleep(2)
        assert "Home" in driver.title
        print("Login com username bem-sucedido.")

    def test_login_sucesso_email(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        time.sleep(2)
        assert "Home" in driver.title
        print("Login com email bem-sucedido.")

    def test_recuperacao_senha(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        driver.find_element(By.LINK_TEXT, "Esqueci minha senha").click()
        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "enviar").click()

        time.sleep(2)
        mensagem = driver.find_element(By.ID, "mensagem_recuperacao").text
        assert "Um email foi enviado" in mensagem
        print("Recuperação de senha iniciada com sucesso.")

    def test_edicao_perfil_sucesso(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        # Simula login prévio
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        time.sleep(2)
        driver.get("http://seu-sistema.com/perfil")

        driver.find_element(By.NAME, "editar").click()
        driver.find_element(By.NAME, "descricao").clear()
        driver.find_element(By.NAME, "descricao").send_keys("Nova biografia")
        driver.find_element(By.NAME, "salvar").click()

        mensagem = driver.find_element(By.ID, "mensagem_sucesso").text
        assert "Perfil atualizado com sucesso" in mensagem
        print("Perfil atualizado com sucesso.")

    def test_edicao_email_invalido(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        # Simula login prévio
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        driver.get("http://seu-sistema.com/perfil")

        driver.find_element(By.NAME, "editar").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys("fulanoemail.com")
        driver.find_element(By.NAME, "salvar").click()

        erro = driver.find_element(By.ID, "erro_email").text
        assert erro == "Formato de email inválido"
        print("Erro de email inválido corretamente exibido.")

    def test_edicao_username_existente(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        # Simula login prévio
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        driver.get("http://seu-sistema.com/perfil")

        driver.find_element(By.NAME, "editar").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "salvar").click()

        erro = driver.find_element(By.ID, "erro_username").text
        assert erro == "Este username já está em uso. Escolha outro."
        print("Erro de username duplicado corretamente exibido.")

    def test_edicao_senha_nao_confere(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        # Simula login prévio
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        driver.get("http://seu-sistema.com/perfil")

        driver.find_element(By.NAME, "editar").click()
        driver.find_element(By.NAME, "nova_senha").send_keys("NovaSenha@123")
        driver.find_element(By.NAME, "confirmar_senha").send_keys(
            "DiferenteSenha@123")
        driver.find_element(By.NAME, "salvar").click()

        erro = driver.find_element(By.ID, "erro_confirmacao_senha").text
        assert erro == "As senhas não coincidem."
        print("Erro de senhas diferentes corretamente exibido.")

    def test_exclusao_conta(self):
        driver = webdriver.Chrome()
        driver.get("http://seu-sistema.com/login")

        usuario_request.register_user(usuario.usuario_put(
            email="fulano@email.com", username="usuario_teste", password="Senha@1234", nomeCompleto="Fulano da Silva", bio="Bio de teste", interesses=["esporte", "anime"]))

        # Simula login prévio
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "login").click()

        driver.get("http://seu-sistema.com/perfil")

        driver.find_element(By.NAME, "excluir_conta").click()
        driver.find_element(
            By.NAME, "senha_confirmacao").send_keys("Senha@1234")
        driver.find_element(By.NAME, "confirmar_exclusao").click()

        time.sleep(2)
        mensagem = driver.find_element(By.ID, "mensagem_exclusao").text
        assert "Conta excluída com sucesso" in mensagem
        print("Conta excluída com sucesso.")
