from flask import Flask, render_template, request, redirect, url_for, session, flash
from decimal import Decimal
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_segura'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    data_pedido = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    produtos = db.Column(db.Text, nullable=False)  # JSON armazenado como texto
    pagamento = db.Column(db.String(50), nullable=True)

usuarios = {
    "usuario1": "senha123",
    "admin": "admin123"
}


produtos = [
    {
        "id": 1,
        "nome": "Notebook Dell Inspiron",
        "descricao": "Notebook potente com 16GB RAM, SSD 512GB e processador i7.",
        "preco": 3899.90,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2022/06/maxresdefault-12.jpeg"
    },
    {
        "id": 2,
        "nome": "Mouse Gamer RGB",
        "descricao": "Mouse ergonômico com alta precisão e iluminação RGB.",
        "preco": 199.90,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2023/12/oKG8af4ZbJqjttMd2jKGzZ-1200-80.jpeg?x28806"
    },
    {
        "id": 3,
        "nome": "Headset Bluetooth",
        "descricao": "Áudio imersivo com conexão Bluetooth 5.0 e microfone embutido.",
        "preco": 299.90,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2024/02/LogitechG435-3-1024x576-1.jpg?x28806"
    },
    {
        "id": 4,
        "nome": "Monitor 24\" LED",
        "descricao": "Monitor Full HD com painel IPS e taxa de atualização de 75Hz.",
        "preco": 899.99,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2024/10/613YwL0dcL._AC_SL1000_.jpg"
    },
    {
        "id": 5,
        "nome": "Teclado Mecânico RGB",
        "descricao": "Switches azuis, retroiluminação personalizável e design robusto.",
        "preco": 329.90,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2024/05/hyperx-alloy-origins-core-blue-switches-04-195x110.jpg"
    },
    {
        "id": 6,
        "nome": "Câmera Webcam Full HD",
        "descricao": "Perfeita para videochamadas com resolução 1080p e microfone embutido.",
        "preco": 249.99,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2020/05/webcam-logitech-c920-full-hd-1080p-D_NQ_NP_888497-MLB27366384756_052018-F-195x110.jpg"
    },
    {
        "id": 7,
        "nome": "Cadeira Gamer Pro",
        "descricao": "Conforto extremo para longas horas de jogo e trabalho.",
        "preco": 1399.00,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2024/06/210414104643-homall-gaming-chair-1-195x110.jpg"
    },
    {
        "id": 8,
        "nome": "Smartphone Android 128GB",
        "descricao": "Câmera tripla, bateria de longa duração e sistema Android 12.",
        "preco": 2399.00,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2025/07/redmi-note-14-pro-3c-etc-header-195x110.jpg"
    },
    {
        "id": 9,
        "nome": "Impressora Multifuncional",
        "descricao": "Imprime, digitaliza e copia documentos com eficiência.",
        "preco": 749.90,
        "imagem_url": "https://m.media-amazon.com/images/I/71I1x6A9HLL._AC_UL320_.jpg"
    },
    {
        "id": 10,
        "nome": "Roteador Wi-Fi Dual Band",
        "descricao": "Cobertura estável com tecnologia 5GHz para streaming e jogos.",
        "preco": 299.00,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2024/10/640785-195x110.jpg"
    },
    {
        "id": 11,
        "nome": "Echo Dot 5ª Geração",
        "descricao": "Assistente Alexa com som melhorado e design elegante.",
        "preco": 349.90,
        "imagem_url": "https://mmorpgbr.com.br/wp-content/uploads/2024/11/7-reasons-to-purchase-the-new-amazon-echo-pop-195x110.jpg"
    },
    {
        "id": 12,
        "nome": "HD Externo 1TB",
        "descricao": "Armazenamento portátil com conexão USB 3.0.",
        "preco": 399.90,
        "imagem_url": "https://m.media-amazon.com/images/I/61C52uhw-PL._AC_UL640_FMwebp_QL65_.jpg"
    }
]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("usuario_logado"):
            flash("Você precisa estar logado para acessar essa página.", "warning")
            return redirect(url_for("acesso_negado"))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/produto/<int:id>')
def produto(id):
    produto = next((p for p in produtos if p["id"] == id), None)
    if not produto:
        return "Produto não encontrado", 404
    return render_template('produto.html', produto=produto)

@app.route('/comprar/<int:id>')
@login_required
def comprar(id):
    produto = next((p for p in produtos if p["id"] == id), None)
    if not produto:
        return "Produto não encontrado", 404

    carrinho = session.get("carrinho", [])
    for item in carrinho:
        if item["produto_id"] == id:
            item["quantidade"] += 1
            break
    else:
        carrinho.append({"produto_id": id, "quantidade": 1})

    session["carrinho"] = carrinho
    flash(f'Produto "{produto["nome"]}" adicionado ao carrinho.', 'success')
    return redirect(url_for("carrinho_view"))

@app.route('/carrinho')
@login_required
def carrinho_view():
    carrinho = session.get("carrinho", [])
    carrinho_detalhado = []
    total = Decimal("0.00")

    for item in carrinho:
        produto = next((p for p in produtos if p["id"] == item["produto_id"]), None)
        if produto:
            preco = Decimal(str(produto["preco"]))
            subtotal = preco * item["quantidade"]
            total += subtotal
            carrinho_detalhado.append({
                "produto": produto,
                "quantidade": item["quantidade"],
                "subtotal": f"{subtotal:.2f}"
            })

    return render_template("carrinho.html", carrinho=carrinho_detalhado, total=f"{total:.2f}")

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        endereco = request.form.get('endereco')
        cep = request.form.get('cep')
        pagamento = request.form.get('pagamento')

        carrinho = session.get("carrinho", [])
        if not carrinho:
            flash("Seu carrinho está vazio.", "warning")
            return redirect(url_for('index'))

        total = 0
        for item in carrinho:
            produto = next((p for p in produtos if p["id"] == item["produto_id"]), None)
            if produto:
                total += produto["preco"] * item["quantidade"]

        produtos_json = json.dumps(carrinho)

        pedido = Pedido(
            nome=nome,
            sobrenome=sobrenome,
            endereco=endereco,
            cep=cep,
            total=total,
            produtos=produtos_json,
            pagamento=pagamento
        )
        db.session.add(pedido)
        db.session.commit()

        session.pop("carrinho", None)
        flash("Pedido realizado com sucesso!", "success")
        return redirect(url_for('index'))

    # GET
    carrinho = session.get("carrinho", [])
    carrinho_detalhado = []
    total = Decimal("0.00")

    for item in carrinho:
        produto = next((p for p in produtos if p["id"] == item["produto_id"]), None)
        if produto:
            preco = Decimal(str(produto["preco"]))
            subtotal = preco * item["quantidade"]
            total += subtotal
            carrinho_detalhado.append({
                "produto": produto,
                "quantidade": item["quantidade"],
                "subtotal": f"{subtotal:.2f}"
            })

    return render_template('checkout.html', carrinho=carrinho_detalhado, total=f"{total:.2f}")

@app.route('/pedidos')
@login_required
def pedidos():
    pedidos = Pedido.query.all()

    # Para cada pedido, converte o campo produtos JSON string para lista
    for pedido in pedidos:
        pedido.produtos_json = json.loads(pedido.produtos)

    return render_template('pedidos.html', pedidos=pedidos, produtos=produtos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario_logado'] = usuario
            flash(f'Bem-vindo, {usuario}!', 'success')
            proxima = request.args.get('proxima')
            return redirect(proxima or url_for('index'))
        else:
            flash('Usuário ou senha inválidos.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for('index'))

@app.route('/acesso-negado')
def acesso_negado():
    return render_template('acesso_negado.html')

@app.route('/debug-pedidos')
def debug_pedidos():
    pedidos = Pedido.query.all()
    resultado = ""
    for p in pedidos:
        resultado += f"<p>Pedido {p.id}: {p.nome} {p.sobrenome}, total: {p.total}, produtos: {p.produtos}</p>"
    return resultado or "Nenhum pedido encontrado."

@app.route("/health")
def health():
    return "OK", 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)