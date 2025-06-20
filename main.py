import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

cloudinary.config(
    cloud_name = "dce4yjbjs",
    api_key = "933244635788299",
    api_secret = "_EZ33Ok039Ox-vfKTdpoMjKPgAg"
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
    resultado = cloudinary.uploader.upload(conteudo, resource_type="image")
    url = resultado.get("secure_url")
    images.append(url)
    print(images)
    return {"url": url}

@app.get("/pegar_imagem/{id_img}")
async def mostrar_imagem(id_img: int):
    return {"img":  images[id_img]}


