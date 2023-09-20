from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

from core.views import IndexView

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'fj@gmail.com'
        self.assunto = 'Mulher a dias'
        self.mensagem = 'Interessada na vaga'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'),data=self.dados)
        self.assertEqual(request.status_code,302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Ol',
            'assunto': 'yes'
        }
        request = self.cliente.post(reverse_lazy('index'),data=git dados)
        self.assertEqual(request.status_code, 200)
