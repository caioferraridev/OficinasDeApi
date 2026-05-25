const url = "/livros";

const livrosDiv = document.getElementById("livros");

const mensagem = document.getElementById("mensagem");

async function carregarLivros(){

    const resposta = await fetch(url);

    const livros = await resposta.json();

    renderizarLivros(livros);
}

function renderizarLivros(livros){

    livrosDiv.innerHTML = "";

    livros.forEach(livro => {

        livrosDiv.innerHTML += `
            <div class="card">

                <img src="${livro.imagem}">

                <h2>${livro.titulo}</h2>

                <p><strong>Autor:</strong> ${livro.autor}</p>

                <p><strong>Categoria:</strong> ${livro.categoria}</p>

                <p>${livro.descricao}</p>

                <p><strong>Ano:</strong> ${livro.ano}</p>

                <p><strong>Avaliação:</strong> ⭐ ${livro.avaliacao}</p>

                <button onclick="deletarLivro(${livro.id})">
                    Excluir
                </button>

            </div>
        `;
    });
}

document
.getElementById("formLivro")
.addEventListener("submit", async (e) => {

    e.preventDefault();

    const livro = {
        titulo: titulo.value,
        autor: autor.value,
        categoria: categoria.value,
        descricao: descricao.value,
        ano: ano.value,
        avaliacao: avaliacao.value,
        imagem: imagem.value
    };

    await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(livro)
    });

    mensagem.innerHTML = "Livro cadastrado!";

    carregarLivros();
});

async function deletarLivro(id){

    await fetch(`${url}/${id}`, {
        method: "DELETE"
    });

    mensagem.innerHTML = "Livro removido.";

    carregarLivros();
}

async function buscarLivros(){

    const busca =
    document
    .getElementById("campoBusca")
    .value;

    const resposta =
    await fetch(
    `${url}?titulo=${busca}`
    );

    const livros =
    await resposta.json();

    renderizarLivros(livros);

    mensagem.innerHTML =
    "Busca realizada.";
}

carregarLivros();