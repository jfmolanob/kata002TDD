from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest (TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test02_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(90000)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Jose Miguel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Suarez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('317302478')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/jose/Documents/DatosMac/Jose/Trabajo/Cupitaller/FotoCierreCupiTaller201520.JPG')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('jm.suarez201')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('jjjjjjjj')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(4000)
        span = self.browser.find_element(By.XPATH, '//span[text()="Jose Miguel Suarez"]')
        self.assertIn("Jose Miguel Suarez", span.text)

    def test03_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Jose Miguel Suarez"]')
        span.click()

        self.browser.implicitly_wait(5000)

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Jose Miguel Suarez"]')
        self.assertIn("Jose Miguel Suarez", h2.text)

    def test04_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(4000)

        nombreUsuario = self.browser.find_element_by_id('id_username_login')
        nombreUsuario.send_keys('jm.suarez201')

        password = self.browser.find_element_by_id('id_password_login')
        password.send_keys('jjjjjjjj')

        botonLogin = self.browser.find_element_by_id('id_but_login')
        botonLogin.click()

        self.browser.implicitly_wait(2000)

        bienvenida = self.browser.find_element_by_id('id_bienvenida')
        self.assertIsNotNone(bienvenida)

    def test05_editar(self):
        self.test04_login();
        link = self.browser.find_element_by_id('id_editar')
        link.click()
        self.browser.implicitly_wait(4000)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear();
        nombre.send_keys('John')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Molano')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('317302478')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/jose/Documents/DatosMac/Jose/Trabajo/Cupitaller/FotoCierreCupiTaller201520.JPG')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(4000)
        div = self.browser.find_element_by_id('user-name-edit')
        self.assertIn("John", div.text)

    def test06_comentario(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('trabajador-John')
        link.click()
        self.browser.implicitly_wait(4000)

        correo = self.browser.find_element_by_id('correo')
        correo.clear();
        correo.send_keys('jm.suarez2014@uniandes.edu.co')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.clear()
        comentario.send_keys('Mi comentario 1')

        self.browser.implicitly_wait(10000)
        link = self.browser.find_element_by_id('comment-button')
        self.browser.implicitly_wait(10000)
        link.click()
        self.browser.implicitly_wait(4000)

        div = self.browser.find_element(By.XPATH, '//p[text()="Mi comentario 1"]')

        self.assertIn("Mi comentario 1", div.text)