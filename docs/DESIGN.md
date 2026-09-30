# Por que o v4 é diferente

O repositório original do mtbinloader2 já possui dois mecanismos separados:

1. substituição de arquivos arbitrários via `FAFAFILES` + hooks de `AAssetManager`;
2. carregamento de arquivos de Resource Packs via `ResourcePackManager`.

Para este mod, precisamos apenas do primeiro.

O v4 registra `pm5_vvu/tiers.bin` diretamente em `FAFAFILES` na inicialização e não executa `find_signatures()` nem instala o hook `rpm_ctor`. Isso elimina a dependência do padrão de bytes do ResourcePackManager que falhou no Minecraft 1.26.52.3.

O `AAssetManager_open` abre o asset normal, e o restante do mtbinloader2 usa o buffer embutido para `read`, `seek`, `length`, `getBuffer` e demais operações.
