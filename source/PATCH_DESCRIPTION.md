# Como a adaptação funciona

O carregador base já instala hooks de `AAssetManager` e mantém um mapa de assets substituídos. A adaptação adiciona um caso especial para qualquer asset cujo nome de arquivo seja `tiers.bin`.

Quando o Minecraft abre esse arquivo, o mod deixa o `AAsset*` original existir, mas registra um `Cursor<Vec<u8>>` contendo o `tiers.bin` embutido. As chamadas de leitura, tamanho, seek e buffer do carregador passam então a usar esses bytes em vez do conteúdo original do APK.

Isso evita editar e reinstalar o APK.
