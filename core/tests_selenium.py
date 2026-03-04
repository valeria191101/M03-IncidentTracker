from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class SecurityRegressionTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json'] # Càrrega de dades (Punt 2.2.2)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.add_argument("--headless") # mode Headless (Punt 2.2.1)
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_role_restriction(self):
        """AUDITORIA: L'analista no ha d'entrar a /admin/"""
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        username_input = self.selenium. find_element(By.NAME, "username") # [cite: 68]
        username_input.send_keys("hacker_local")

        password_input = self.selenium. find_element(By.NAME, "password")
        password_input.send_keys("Super1234") # Contrasenya del teu JSON


#        self.selenium.find_element(By.XPATH, '//button[@type="submit"]').click() # Intentar forçar URL d'admin self.selenium.get('%s%s' % (self.live_server_url, '/admin/')) # ASSERT de Seguretat (Punt 2.2.3) # Si el títol és "Site administration...", vol dir que ha entrat -> EL TEST HA DE FALLAR self.assertNotEqual(self.selenium.title, "Site administration | Django site admin")

# Intentar forçar URL d'admin
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
  
        # ASSERT de Seguretat (Punt 2.2.3)
        self.assertNotEqual(self.selenium.title, "Site administration | Django site admin")
