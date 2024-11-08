const apiUrl = 'http://127.0.0.1:5000/produtos';


// Função para listar os produtos
async function listarProdutos() {
    const response = await fetch(apiUrl);
    const produtos = await response.json();

    const tabela = document.querySelector('#produtos-tabela tbody');
    tabela.innerHTML = '';

    produtos.forEach(produto => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${produto.id}</td>
            <td>${produto.nomeProduto}</td>
            <td>${produto.preco}</td>
            <td>${produto.quantidade}</td>
            <td>
                <button class="editar" onclick="editarProduto(${produto.id})">Editar</button>
                <button class="deletar" onclick="deletarProduto(${produto.id})">Deletar</button>
                
            </td>
        `;
        tabela.appendChild(row);
    });
}

// Função para cadastrar um produto
document.querySelector('#form-produto').addEventListener('submit', async (event) => {
    event.preventDefault();

    const nomeProduto = document.querySelector('#nomeProduto').value;
    const preco = document.querySelector('#preco').value;
    const quantidade = document.querySelector('#quantidade').value;

    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nomeProduto, preco, quantidade })
    });

    const result = await response.json();
    alert(result.message || result.error);
    listarProdutos();
    document.querySelector('#form-produto').reset();
});

// Função para deletar um produto
async function deletarProduto(id) {
    const response = await fetch(`${apiUrl}/${id}`, {
        method: 'DELETE'
    });
    const result = await response.json();
    alert(result.message || result.error);
    listarProdutos();
}

// Função para editar um produto
async function editarProduto(id) {
    const nomeProduto = prompt('Novo nome do produto:');
    const preco = prompt('Novo preço:');
    const quantidade = prompt('Nova quantidade:');

    if (nomeProduto && preco && quantidade) {
        const response = await fetch(`${apiUrl}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nomeProduto, preco, quantidade })
        });
        const result = await response.json();
        alert(result.message || result.error);
        listarProdutos();
    }
}

// Carregar a lista de produtos ao carregar a página
document.addEventListener('DOMContentLoaded', listarProdutos);
