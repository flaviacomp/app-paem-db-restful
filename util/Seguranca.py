import bcrypt

class Seguranca(object):

    def valida_senha(self, senha, hashed_password):
        return bcrypt.checkpw(senha.encode('utf8'), hashed_password)

    def criptografa_senha(self, senha):
        return bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())

