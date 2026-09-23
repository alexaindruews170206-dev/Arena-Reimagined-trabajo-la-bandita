# Publicação 17 — A camada de imersão: os leitores que ensinam japonês enquanto você lê — e o cliente Komga que faltava

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 17)**

## 🗺️ Mapa deste guia

├── ⚡ Em uma página
├── 🦋 Chimahon — o fork de Mihon que mina o Anki
├── 📚 Hoshi Reader — o EPUB japonês com mil ferramentas
├── 🎐 Yomikai — OCR, vozes e o mini-player flutuante
├── 🌗 Yomi Reader — o triplo anime/mangá/novela
├── 🏛️ Koharia — seu servidor Komga, no seu bolso
├── 🧩 As oficinas por trás (dicionários compartilhados e mais)
├── ⚖️ Para quem é esta camada?
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Há uma camada do ecossistema que os mapas grandes quase não veem: a de quem lê em japonês APRENDENDO-O — dicionários na ponta do dedo, cartões de Anki na hora, texto vertical, mangá Mokuro, voz por cima da página. Este guia ficha os cinco projetos vivos dessa camada, todos verificados HOJE, 14 de setembro — **dois publicaram versão hoje mesmo**:

```
Hoshi Reader   ★378   v1.3.3 (13-ago)   EPUB japonês + Yomitan + Anki + e-ink
Chimahon       ★198   v2.4.2 (HOJE, 15-set)   fork de Mihon: dicionário, Mokuro, Anki
Koharia        ★148   v0.5.0 (14-set)      cliente Android para servidores Komga
Yomi Reader    ★10    v0.1.7 (6-set)    anime + mangá + novela, compat. Tadami
Yomikai        ★0     v1.9.84 (HOJE, 15-set)  OCR + vozes + mini-player flutuante
```

Estrelas pequenas, oficinas grandes: aqui os números de fama não contam a história — a cadência e as funções contam.

## 🦋 Chimahon — o fork de Mihon que mina o Anki

https://github.com/Chimahon/chimahon

```
★198 · GPL-3.0
v2.4.2 (HOJE, 15-set) · v2.4.1 · v2.4.0 (11-set) — três em quatro dias
O que é: «fork de imersão de Mihon» (a descrição dele):
dicionário nativo (Yomitan), mangá Mokuro e anime,
leitor de novelas EPUB, e mineração instantânea para o Anki
```

É Mihon com sala de aula dentro: você lê seu mangá de sempre e, ao tocar uma palavra, o dicionário abre ali mesmo; o que quiser guardar, voa para o seu baralho do Anki sem sair do capítulo. A oficina dele mantém ainda os componentes: Chimahon-ffmpeg e Chimahon-local-models (processamento local), e usa os dicionários do Hoshi — a camada se tece entre si.

## 📚 Hoshi Reader — o EPUB japonês com mil ferramentas

https://github.com/HuangAntimony/Hoshi-Reader-Android

```
★378 · GPL-3.0
v1.3.3 (13-ago) — o maior da camada
O que é: leitor de EPUB japonês com busca
Yomitan, mineração para o Anki, leitura acompanhada de
audiolivro e suporte a tinta eletrônica
```

O README dele (lido em 14-set) lista o que é dele: EPUB individuais ou por lote com progresso visível, estantes próprias, texto vertical ou horizontal com paginação ou scroll contínuo, dicionários Yomitan que se importam e atualizam dentro do app, busca recursiva (toca em uma palavra dentro de uma definição e segue), modo de foco imersivo, passagem de página com as teclas de volume e opções específicas para leitores e-ink. E é a ponta de uma oficina completa: o autor mantém os dicionários (hoshidicts), uma gramática japonesa de referência, ferramentas para novelas web (narou-py) e contribui no Yomitan e no mpvacious. A camada de imersão tem centro de gravidade, e se chama HuangAntimony.

## 🎐 Yomikai — OCR, vozes e o mini-player flutuante

https://github.com/sj0404-collab/yomikai
(o «yomihon-custom» que circula: https://github.com/sj0404-collab/yomihon-custom)

```
Apache-2.0
v1.9.84 (HOJE, 15-set) · v1.9.83 (madrugada do 15) · v1.9.79 (14-set) · v1.9.78/76 (13-set)
— cadência diária de verdade
O que é: leitor de mangá com OCR e ovoz
(papéis e vozes), dicionários, e um
mini-player flutuante sobre todos os apps
```

A descrição (do russo original) diz inteiro: mangá com OCR de texto, ovoz por papéis, dicionários e um player mini que flutua sobre qualquer aplicativo — você escuta a voz do capítulo enquanto lê em outro lugar. Dois apontes de mapa: o projeto raiz é o **Yomihon** (yomihon/yomihon, ★125, «agora com OCR», v0.4.0 de 30-jul) — o nome do repo «yomihon-custom» vem daí — e a casa ativa é o Yomikai, com irmã web (yomikai-pwa, React+TSX, com navegador e chat de IA dentro). Não ter estrelas não significa nada: publica versões todos os dias.

## 🌗 Yomi Reader — o triplo anime/mangá/novela

https://github.com/codegeasse1/yomi-reader

```
★10 · Apache-2.0
v0.1.7 (6-set) — jovem, no 0.1
O que é: «leitor de código aberto de anime,
mangá e novelas para Android (compatível
Tadami/Aniyomi)» — a descrição dele
```

A aposta do triplo no linhagem Aniyomi: as três mídias em um app, comendo extensões compatíveis com o Tadami. Vai no 0.1 — idade honesta — e a oficina dele traz mais: Nekoread (leitor de mangá, v2.2.5 de 10-set) e hikari (streaming universal com addons de Stremio e plugins CloudStream, v0.3.67 de 13-set). Um construtor com cinco ferros na fogueira — seguimento aberto para todos.

## 🏛️ Koharia — seu servidor Komga, no seu bolso

https://github.com/Mister-album/Koharia

```
★147 · Apache-2.0
v0.5.0 (14-set) · v0.4.5 (6-set)
O que é: «leitor Android independente de
terceiros para navegar e ler conteúdo de
servidores Komga» — a descrição (do chinês)
```

Komga é o servidor de biblioteca que os grandes leitores já sincronizam; o Koharia é o app dedicado a ele: seu servidor, seu app, com o leitor feito sob medida. v0.5.0 publicada em 14-set. Do mesmo autor: a web do projeto e o fork dele próprio do servidor komga — quem constrói o cliente entende o servidor, e vice-versa.

**A outra metade da camada, verificada esta noite por exploração livre:** o **Komga** (gotson/komga, ★6.659, MIT, 1.26.3 de 12 de agosto) — servidor de comics, mangás e eBooks com API, OPDS e sincronização Kobo e KOReader; e o **Kavita** (Kareadita/Kavita, ★11.677, GPL-3.0, v0.9.1.4 de 2-set), o servidor de leitura multiplataforma. O Koharia vive porque estes vivem — e vice-versa: o servidor sem clientes é um arquivo, o cliente sem servidor é uma casca.

## 🧩 As oficinas por trás (dicionários compartilhados e mais)

A camada se sustenta em infraestrutura compartilhada que convém nomear: os **dicionários hoshidicts** também são usados pelo Chimahon; o **Yomitan** (o dicionário-pop-up do navegador, referência absoluta do nicho) conecta com todos; e na observação desta semana ficou um companheiro pequeno mas vivo: **android-koreader-companion** (★9, MIT, versão de 14-set) — mostra o que você lê no KOReader e no Mihon, o progresso entre os dois mundos.

## ⚖️ Para quem é esta camada?

```
Lê mangá em japonês e estuda?
   → Chimahon (se você vem de Mihon) ou
     Yomikai (se quer voz e OCR).

Lê novelas leves em EPUB japonês?
   → Hoshi Reader: é o TERRENO dele, com
     e-ink incluído para o leitor de tinta.

Anime + mangá + novela em um só app
(e o japonês não é seu foco)?
   → Yomi Reader — e olhe o Tadami (Publicação 13),
     o triplo do linhagem Aniyomi com anos em cima.

Tem um servidor Komga?
   → Koharia, o app dedicado.
```

Nenhuma ficha passa por fama: passa por cadência, funções próprias e repo aberto — e os cinco vivem, re-verificados a HOJE 15-set.

## ❓ Perguntas frequentes

**Eles substituem o Mihon/Komikku/Aniyomi?**
Não: são camadas em cima ou ao lado. O Chimahon É um fork de Mihon (sua biblioteca migra com as regras de sempre); o Koharia precisa de um servidor Komga; o Hoshi é para EPUB japonês; o Yomikai e o Yomi Reader são casas à parte. Cada um cobre o que o tronco não cobre.

**E as extensões? Servem as de sempre?**
O Yomi Reader declara compatibilidade Tadami/Aniyomi; o Chimahon, por ser fork de Mihon, herda o ecossistema Mihon. O Hoshi (EPUB) e o Koharia (Komga) não começam por extensões: começam por livros e servidores. O Yomikai constrói as fontes próprias dele — o README dele manda no dia em que você usar.

**Por que estrelas tão pequenas se são tão ativos?**
Porque nicho é nicho: quem estuda japonês com mangá são milhares, não milhões. A régua da casa nunca foi a fama — é a cadência e o aporte próprio, e aqui sobra.

**Funcionam sem saber japonês?**
Chimahon, Hoshi e Yomikai EXISTEM para aprendê-lo — o dicionário e a voz são o ponto. Para leitura em português/inglês, os troncos das Publicações 13–16 seguem sendo a casa.

## 🔗 Links

- Chimahon: https://github.com/Chimahon/chimahon
- Hoshi Reader: https://github.com/HuangAntimony/Hoshi-Reader-Android
- Yomikai: https://github.com/sj0404-collab/yomikai · gêmea web: https://github.com/sj0404-collab/yomikai-pwa · raiz do nome: https://github.com/yomihon/yomihon
- Yomi Reader: https://github.com/codegeasse1/yomi-reader · irmãos: https://github.com/codegeasse1/Nekoread
- Koharia: https://github.com/Mister-album/Koharia
- Companheiro de progresso: https://github.com/woxakv/android-koreader-companion
- Os servidores: https://github.com/gotson/komga · https://github.com/Kareadita/Kavita

> A Bandita informa a partir de fontes datadas. Ler com o dicionário na mão — agora, no mesmo dedo.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Chimahon v2.4.2, Yomikai 1.9.84, Koharia ★148 (todas de HOJE). O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
