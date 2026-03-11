import bcrypt

class Criptografia:

    @classmethod
    def gerarHash(cls, senha):
        
        senha = bytes(senha, "utf-8")
        hash = bcrypt.hashpw(senha, bcrypt.gensalt())
        return hash.decode('utf-8')

    @classmethod
    def compararSenha(cls, senha, hash):
        try:
            senha = bytes(senha, "utf-8")
            hash = bytes(hash, "utf-8")
            return bcrypt.checkpw(senha, hash)
        except:
            return False

if __name__ == "__main__":
    senha = "123"
    senha_criptografada = Criptografia.gerarHash(senha)
    print (f"senha normal {senha}")
    print (f"senha crip {senha_criptografada}")
    result = Criptografia.compararSenha(senha, senha_criptografada)
    print(f"Resultado é {result}")
