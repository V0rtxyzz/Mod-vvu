# PandaMine VVU Unlocker para LeviLauncher

Versão alvo: **Minecraft Bedrock 26.52.3 / Android ARM64**.

Este projeto transforma o `tiers.bin` do PandaMine's Vibrant Visuals Unlocker em uma biblioteca nativa para o LeviLauncher. A biblioteca intercepta a abertura de `tiers.bin` e entrega ao Minecraft a cópia embutida no mod.

## O que você precisa fazer

1. Crie um repositório no GitHub.
2. Envie **todos os arquivos desta pasta** para o repositório, mantendo a estrutura.
3. Abra a aba **Actions** e execute `Build PandaMine VVU Levi`.
4. Quando terminar, baixe o artefato `PandaMine-VVU-Levi-26.52.3`.
5. Dentro dele estará o arquivo `.levipack` para importar no LeviLauncher.

O workflow baixa a versão do `mtbinloader2-levi` usada como base, aplica automaticamente o patch do PandaMine e compila para `aarch64-linux-android`.

## No LeviLauncher

Importe o `.levipack` como um mod nativo.

**Não use simultaneamente outro `mtbinloader2-levi` com a mesma finalidade**, porque os dois podem instalar os mesmos hooks do `AAssetManager`.

## Observação importante sobre 26.52.3

O `tiers.bin` fornecido neste projeto veio do pack do PandaMine identificado como **26.50**. Portanto, esta é uma adaptação experimental para 26.52.3, não uma versão oficialmente publicada pelo autor do pack para 26.52.3.

O mod foi configurado para carregar apenas em **26.52.3** no manifesto do Levi. Se o jogo mudar a forma como abre `tiers.bin` ou se as assinaturas do carregador nativo deixarem de funcionar, o mod pode simplesmente não ativar a substituição.

## O que este projeto NÃO faz

Ele não modifica o APK do Minecraft, não reinstala o jogo e não exige que você use MT Manager para editar `assets/assets/tiers.bin`.

## Arquivo original

O `tiers.bin` foi extraído do `.mcpack` fornecido pelo usuário para esta conversão privada. O aviso de licença original foi preservado em `source/PandaMine_LICENSE.txt`.
