from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou restrinja para o seu domínio exato
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/cadastrar_produto/")
async def enviar_imagem(file: UploadFile = File(...)):
    conteudo = await file.read()


    # FAZER A LIGAÇÃO COM O BUNNY NET
    
    
    return {"url": ''}

@app.get("/pegar_imagem/{id_img}")
async def mostrar_imagem(id_img: int):
    return {"img":  images[id_img]}


