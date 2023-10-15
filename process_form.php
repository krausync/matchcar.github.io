<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $telefone = $_POST["telefone"];
    $duvidas = $_POST["duvidas"];

    $dados = "Nome: $nome\nE-mail: $email\nTelefone: $telefone\nDúvidas: $duvidas\n";

    // Abre ou cria um arquivo para armazenar os dados
    $file = fopen("dados_formulario.txt", "a");

    if ($file) {
        // Escreve os dados no arquivo
        fwrite($file, $dados);

        // Fecha o arquivo
        fclose($file);

        echo "Os dados foram armazenados com sucesso!";
    } else {
        echo "Não foi possível armazenar os dados. Por favor, tente novamente mais tarde.";
    }
}
?>
