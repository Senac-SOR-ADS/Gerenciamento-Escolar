if __name__ == "__main__":
    from App import run

    import os
    from dotenv import load_dotenv
    
    # Ele carrega as variaveis no arquivo .env
    load_dotenv(override=True)
    print(os.environ)