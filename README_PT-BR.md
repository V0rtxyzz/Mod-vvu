# PandaMine VVU Unlocker para LeviLauncher

Alvo: Minecraft Bedrock Android ARM64, 1.26.52.3.

## O que mudou nesta versão

Esta build usa diretamente o código do repositório original `mcbegamerxx954/mtbinloader2` fornecido para esta adaptação.

O loader original localiza o `ResourcePackManager` por assinatura de máquina. O padrão que acompanha o repositório é para 26.50 e esse caminho causou o `Abort message: "No signature was found"` no seu Minecraft 1.26.52.3.

Nesta adaptação, esse caminho é removido da execução. O `tiers.bin` é registrado diretamente na tabela `FAFAFILES` já existente no mtbinloader2 e a biblioteca instala somente os hooks do `AAssetManager`.

Isso significa que a build não depende da assinatura específica do `ResourcePackManager` para 26.50.

## Build

Envie esta pasta inteira para o GitHub e execute:

`Actions -> Build PandaMine VVU Levi 26.52.3 -> Run workflow`

O artefato será:

`PandaMine-VVU-Levi-26.52.3.levipack`

## Instalação

Importe o `.levipack` no LeviLauncher.

Desative qualquer outro mod que também seja uma instância do mtbinloader2 e que instale os mesmos hooks de `AAssetManager`.

## Sobre o tiers.bin

O `tiers.bin` foi extraído do pack PandaMine VVU que você forneceu. Ele é identificado como 26.50, portanto a compatibilidade com 1.26.52.3 deve ser tratada como experimental.

Esta adaptação não altera o APK do Minecraft.
