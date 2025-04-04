# Acessar a tela de cadastro
import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Tentativa de cadastro com campo 'email' vazio


@pytest.fixture
def preparar_ambiente():
    driver = webdriver.Chrome()
    # Corrigir o link para o correto
    driver.get("http://hobbyfinder.com/login")
    criar_conta_btn = driver.find_element(By.LINK_TEXT, "Criar Conta")
    criar_conta_btn.click()
    return driver


class TestCriaUsuario:

    def test_cria_usuario_test(self, preparar_ambiente: webdriver.Chrome):

        driver = preparar_ambiente

        # Preencher os campos do formulário de cadastro
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(
            By.NAME, "confirmar_senha").send_keys("Senha@1234")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar redirecionamento
        time.sleep(2)

        # Verificar sucesso (pode ser feito com um elemento específico na página)
        mensagem_sucesso = driver.find_element(
            By.ID, "mensagem_sucesso").text

        driver.close()

        assert mensagem_sucesso == "Conta criada com sucesso!", "Teste falhou: Mensagem inesperada."

    def test_tenta_criar_usuario_username_vazio(self, preparar_ambiente: webdriver.Chrome):
        driver = preparar_ambiente

        # Preencher todos os campos, exceto o campo 'Username'
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "confirmar_senha").send_keys("Senha@1234")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(By.ID, "erro_username").text

        driver.close()

        assert mensagem_erro == "O campo Username é obrigatório", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")

    def test_tenta_criar_usuario_email_vazio(self, preparar_ambiente: webdriver.Chrome):
        driver = webdriver.Chrome()
        # Substituir pela URL real
        driver.get("http://seu-sistema.com/cadastro")

        preparar_ambiente(driver)

        # Preencher todos os campos, exceto o campo 'email'
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "confirmar_senha").send_keys("Senha@1234")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(By.ID, "erro_email").text

        driver.close()

        assert mensagem_erro == "O campo email é obrigatório", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")

    def test_tenta_criar_usuario_email_invalido(self, preparar_ambiente: webdriver.Chrome):
        driver = preparar_ambiente

        # Preencher o campo 'Email' com um formato inválido
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "email").send_keys("fulanoemail.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "confirmar_senha").send_keys("Senha@1234")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(By.ID, "erro_email").text

        driver.close()

        assert mensagem_erro == "Formato de email inválido", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")

    def test_tenta_criar_usuario_senha_vazia(self, preparar_ambiente: webdriver.Chrome):
        driver = preparar_ambiente

        # Preencher todos os campos, exceto o campo 'Senha'
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "confirmar_senha").send_keys("Senha@1234")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(By.ID, "erro_senha").text

        driver.close()

        assert mensagem_erro == "O campo Senha é obrigatório", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")

    def test_tenta_criar_usuario_confirmacao_senha_vazia(self, preparar_ambiente: webdriver.Chrome):
        driver = preparar_ambiente

        # Preencher todos os campos, exceto o campo 'Confirmação de Senha'
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(
            By.ID, "erro_confirmacao_senha").text

        driver.close()

        assert mensagem_erro == "O campo Confirmação de Senha é obrigatório", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")

    def test_tenta_criar_usuario_senhas_diferentes(self, preparar_ambiente: webdriver.Chrome):
        driver = preparar_ambiente

        # Preencher todos os campos corretamente, exceto 'Senha' e 'Confirmação de Senha', que devem ser diferentes
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Fulano da Silva")
        driver.find_element(By.NAME, "email").send_keys("fulano@email.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@1234")
        driver.find_element(By.NAME, "confirmar_senha").send_keys(
            "SenhaDiferente@5678")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(By.ID, "erro_senhas").text

        driver.close()

        assert mensagem_erro == "As senhas não coincidem", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")

    def test_tenta_criar_usuario_username_existente(self, preparar_ambiente: webdriver.Chrome):
        driver = preparar_ambiente

        # É NECESSÁRIO CRIAR UM USUÁRIO ANTES DE RODAR ESSE TESTE

        # Preencher os campos com um username já existente
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "nome").send_keys("Ciclano Souza")
        driver.find_element(By.NAME, "email").send_keys("ciclano@email.com")
        driver.find_element(By.NAME, "senha").send_keys("Senha@5678")
        driver.find_element(By.NAME, "confirmar_senha").send_keys("Senha@5678")

        # Clicar no botão "Criar Conta"
        driver.find_element(By.NAME, "criar_conta").click()

        # Aguardar a resposta do sistema
        time.sleep(2)

        # Verificar se a mensagem de erro apareceu
        mensagem_erro = driver.find_element(By.ID, "erro_username").text
        assert mensagem_erro == "Este username já está em uso. Escolha outro.", "Teste falhou: Mensagem inesperada."
        print("Teste passou: Mensagem de erro correta exibida!")
