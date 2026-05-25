const botao = document.getElementById("buscarBtn");
const usuariosDiv = document.getElementById("usuarios");

botao.addEventListener("click", async () => {

    usuariosDiv.innerHTML = "Carregando...";

    try {

        const resposta = await fetch("/usuarios");

        const usuarios = await resposta.json();

        usuariosDiv.innerHTML = "";

        usuarios.forEach(usuario => {

            usuariosDiv.innerHTML += `
                <div class="card">
                    <h3>${usuario.nome}</h3>
                    <p>Email: ${usuario.email}</p>
                    <p>Telefone: ${usuario.telefone}</p>
                </div>
            `;
        });

    } catch (erro) {

        usuariosDiv.innerHTML = "Erro ao buscar usuários.";

        console.log(erro);
    }
});