#!/usr/bin/env python3
class Logger(object):

    def __init__(self, message):
        self.usuario = str(message.author)
        self.data = str(message.created_at)
        if message.content:
            self.conteudo = str(message.content)
        else:
            self.conteudo = ""
        if message.attachments:
            self.anexo = str(message.attachments.url)
        else:
            self.anexo = []

    def save_file(self):
        texto = ""
        texto = "Usuario: "+self.usuario
        texto = "\n"+"Data: "+self.data
        texto = "\n"+"Conteudo: "+self.conteudo
        texto = "\n"+"Link anexo: "+self.anexo
        with open("log.txt", "w") as file:
            file.writelines()
