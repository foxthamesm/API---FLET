from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou restrinja para o seu domínio exato
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






numerador = 0
images = []

vendas = {
    1: {"item": "lata", "preço unitario": 4, "quantidade":5},
    2: {"item": "Garraf 2L", "preço unitario": 15, "quantidade":5},
    3: {"item": "Garrafa 750ml", "preço unitario": 10, "quantidade":5},
    4: {"item": "lata mini", "preço unitario": 2, "quantidade":5},
}

@app.get("/")
def home():
    return  {"Vendas: ": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]




@app.post("/cadastrar_produto/")
async def enviar_imagem(file: UploadFile = File(...)):
    conteudo = await file.read()

    print(file.filename)
    nome_arquivo = os.path.basename(file.filename)
    print(nome_arquivo)
    storage_zone = "cadastro-produto"
    api_key = "8be973d4-0766-462a-8be4f79dc955-1fc0-40aa"
    destino = f"uploads/{nome_arquivo}"
    
    
    url = f"https://storage.bunnycdn.com/{storage_zone}/{destino}"
    
    response = requests.put(
        url,
        headers={"AccessKey": api_key},
        data=conteudo
    )
    print(response.status_code)
    # FAZER A LIGAÇÃO COM O BUNNY NET
    
    
    if response.status_code == 201:
        url_publica = f"https://cadastro-produto.b-cdn.net/{destino}"
        return {"status": "sucesso", "url": url_publica}
    else:
        return {"status": "erro", "detalhes": response.text}




