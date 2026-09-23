# Publicação 08 — Música FOSS: clientes com repo e data de pulso — Spotify crackeado não entra

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 08)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── ⚖️ O que não é esta guia
├── 🧬 A genealogia: de ViMusic à família atual
├── 🎧 Os clientes de streaming, ficha por ficha
├── 📻 NewPipe: a espécie à parte
├── 📂 Auxio: sua música, seus arquivos
├── 🎙️ AntennaPod: os podcasts
├── 🆕 Os que faltavam: N-Zik e Gabi
├── 🚫 O que não se cola
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Guia de clientes de música de código aberto, com o pulso de cada projeto medido no dia 14 de setembro e re-verificado ao mudar (15-set). A semana trouxe movimento de verdade nesta família: OuterTune estreou versão neste mês, Metrolist segue em seqüência de lançamentos, e a linhagem completa ficou documentada.

```
STREAMING (YouTube Music como fundo)
SimpMusic      ★11.257   2.1.0 (7-set)     push 11-set   vivo
OuterTune      ★5.390    v0.11.1 (6-set)   push 6-set    vivo
Metrolist      ★12.789   13.7.0 (7-set) · Nightly do dia 14 à vista    vivo          ← a mais ativa
InnerTune      ★6.088    push nov-2025                   dormindo
Harmony-Music  ★3.081    v1.12.2 (dez-25)  multiplataforma
music-you      ★220      vivo              minimalista
InterTune      ★12       fork fixo, nicho

STREAMING (front-end geral)
NewPipe        ★39.682   v0.29.1 (15-ago)  push 31-ago

ARQUIVOS LOCAIS
Auxio          ★4.274    v4.1.5 (4-ago)    push 8-set

PODCASTS
AntennaPod     ★8.153    3.12.1 (5-set)    push 12-set

ViMusic        ★9.480    o ancestral
```

## ⚖️ O que não é esta guia

YouTube e YouTube Music têm seus termos de serviço. Um cliente livre que consulta esses servidores pode chocar com eles — esta guia não é um escritório de advocacia: não diz «é legal» nem «não é». Diz repo, licença (GPL em todas as fichas de hoje, verificadas na sua página), versão e último push. A decisão de o que você usa é sua, com suas conseqüências.

E a frase de sempre: aqui não há APK de «Spotify premium grátis» nem mods de nada. Essa porta tem guia própria — a de lojas — e termina sempre igual.

## 🧬 A genealogia: de ViMusic à família atual

Esta família tem árvore genealógica documentada, e conhecê-la aclara meia dúzia de nomes:

```
   o app que inventou o modelo: streaming de
   YouTube Music com fila, sem o app oficial.
   Hoje arquivado — mas sua idéia pariu tudo isto.
   │
   ├── InnerTune (z-huang)
   │      o herdeiro direto: Material 3, biblioteca
   │      com conta, letras sincronizadas. Seu último
   │      push foi em novembro de 2025 — o criador
   │      se moveu a outros projetos e o repo dorme.
   │      │
   │      ├── OuterTune (seu fork vivo mais sólido)
   │      │      adicionou suporte a ARQUIVOS LOCAIS
   │      │      junto ao streaming. Versão 0.11.1
   │      │      no dia 6 de setembro — no mês passado
   │      │      ainda mostrava uma tag de dezembro;
   │      │      no dia 14-set a fila ficou corrigida.
   │      │
   │      └── Metrolist (★12.789)
   │             a mais instalada da segunda
   │             geração: versão 13.7.0 do dia 7-set
   │             com nightly próprio. Das vivas,
   │             a de cadência mais regular.
   │
   └── SimpMusic (projeto paralelo, mesmo fundo)
          multiplataforma, com uma linha de desenvolvimento
          muito ativa: 2.0.0 no dia 28 de agosto e 2.1.0
          no dia 7 de setembro.
```

Os parentes menores completam a foto: Harmony-Music (★3.081, multiplataforma de desktop e móvel, com sua última estável de dezembro de 2025), music-you (★220, a minimalista) e o caso curioso de InterTune (★12): um fork que ficou ancorado à versão 0.10.1 de OuterTune «por sua tela de reprodução», mantido pelo seu autor para uso próprio e de quem o ache útil. Seu README recomenda, para quem busque manutenção ativa, a Metrolist e a outro projeto chamado ArchiveTune — desse último, não se abriu repo nesta revisão.

## 🎧 Os clientes de streaming, ficha por ficha

### Metrolist — a de cadência regular

https://github.com/mostafaalagamy/Metrolist

★12.789 · versão **13.7.0 (7 de setembro)** · GPL · vivo. A segunda geração mais estável da linhagem InnerTune: versões mensais, nightly próprio, e uma base de usuários que a pôs entre as recomendações fixas das comunidades do tema. Se você vem de InnerTune dormindo, esta é a casa natural. Pulso de hoje: além da 13.7.0, o repo publica **Nightly** — compilação diária vista HOJE, 14 de setembro. *Mudança certificada no dia 15-set: a casa agora é a organização MetrolistGroup (os links velhos redirecionam) — a dinastia completa na Publicação 27.*

### OuterTune — a que une streaming e arquivos

https://github.com/OuterTune/OuterTune

★5.390 · versão **0.11.1 (6 de setembro)** · GPL · vivo. O fork que agregou à linha InnerTune a leitura de arquivos locais: sua música baixada e o catálogo de streaming no mesmo reprodutor. Material 3, tema dinâmico. No mês passado sua última tag era de dezembro — esta guia o registrava assim; no dia 6-set corrigiu a foto. Assim de rápido caduca um número.

### SimpMusic — a multiplataforma incansável

https://github.com/maxrave-dev/SimpMusic

★11.257 · **2.1.0 (7-set)** e 2.0.0 (28-ago) · GPL · vivo. Duas versões maiores em dez dias. Sua aposta: o mesmo fundo de YouTube Music com funções extras — letras sincronizadas, áudio sem perdas declarado na sua ficha, multiplataforma. A de desenvolvimento mais inquieto da família.

### InnerTune — o ancestral que descansa

https://github.com/z-huang/InnerTune

★6.088 · push do dia 13 de novembro de 2025 · GPL · sem arquivar mas dormindo: quase dez meses sem código novo, releases de 2024. Seu lugar na história está garantido — é a fonte de que bebe meia família. Para instalar hoje, seus herdeiros fazem o trabalho.

### Harmony-Music e music-you — as alternativas

https://github.com/anandnet/Harmony-Music — ★3.081 · v1.12.2 (7-dez-2025) · multiplataforma (Android e desktop), GPL. Ritmo lento mas projeto sério.

https://github.com/DanielSevillano/music-you — ★220 · GPL · a opção minimalista da família, para quem quer o justo.

### InterTune — o caso de nicho

https://github.com/ItzSkyeYT/InterTune — ★12 · GPL · vivo por decisão do seu autor: ancorado à versão 0.10.1 de OuterTune para conservar uma tela de reprodução concreta. «Uso a diario e o deixo público porque a alguns serviu», diz seu README. A honestidade também é um traço de projeto sadio — e sua recomendação de alternativas ativas (Metrolist) o confirma.

## 📻 NewPipe: a espécie à parte

https://github.com/TeamNewPipe/NewPipe

★39.682 · v0.29.1 (15 de agosto) · push do dia 31-ago · GPL · vivo. NewPipe não é um cliente de YouTube Music: é um front-end livre de TODO o universo YouTube — vídeos, música, subscrições, sem conta e sem publicidade. Em música pede menos comodidade de biblioteca que os clientes de cima; em troca, cobre todo o resto. É dos projetos mais veteranos e respeitados do software livre Android. Seu canal histórico de distribuição é F-Droid — a ficha da loja dessa família se aplica.

## 📂 Auxio: sua música, seus arquivos

https://github.com/OxygenCobalt/Auxio

★4.274 · v4.1.5 (4 de agosto) · push do dia 8-set · GPL · vivo. Para a música que você JÁ tem: reprodutor local, racional, sem se conectar a nenhum catálogo nem a nenhuma nuvem. Se sua biblioteca vive no telefone (copiada com as ferramentas da guia de arquivos desta família), esta é a ficha. Sem conta, sem streaming, sem sustos.

## 🎙️ AntennaPod: os podcasts

https://github.com/AntennaPod/AntennaPod

★8.153 · 3.12.1 (5-set) · push do dia 12-set · GPL · vivo. Gestor de podcasts completo: feeds RSS, downloads automáticos, velocidade variável, capítulos. Não compete com nenhum de cima: outra categoria que os fios velhos misturavam com a música em mil caracteres de ruído. Aqui, cada coisa na sua gaveta.

## 🆕 Os que faltavam (adição de 14 de setembro)

### N-Zik — o filho multilíngüe de Kreate

https://github.com/N-Zik-Group/N-Zik · v7.5.1-f (1 de setembro; a HOJE 15-set seu releases dança com um dev v8.0.0) · loja: https://appteka.store/app/4abr315772

Bifurcação multilíngüe de Kreate declarada no seu próprio README: transmite e guarda em cachê música de YouTube Music, com downloads sem conexão, letras sincronizadas palavra por palavra, visualizador, Discord Rich Presence, widgets e suporte Android Auto/TV/Automotive. Alterna a interface moderna N-Zik com a clássica de ViMusic — a genealogia viva desta guia. Qualidade Premium opcional entrando com conta de YouTube Music. Atualizações OTA. Honestidade do autor, incluída: desenvolve assistido por IA com revisão humana, o declara, e recomenda alternativas mais maduras (Metrolist, VIVI Music, RiPlay) se você prefere estabilidade provada. Esse aviso é sinal de ofício, não fraqueza. Pulso de fechamento (14-set, noite): o repo já cozinha a **v8.0.0-dev de HOJE** — a estável da loja segue sendo a 7.5.1-f.

### Gabi — o baixador de mil sites

https://github.com/Hotaro26/gabi · v4.6.1 «YouTube 403 Fix» (1 de setembro) · loja: https://appteka.store/app/b4cr315682

Baixador de mídias em Material 3 e Jetpack Compose que roda yt-dlp e gallery-dl: vídeos, áudio e galerias de mais de 1.000 sites — YouTube, TikTok, Instagram, Twitter/X, Reddit, SoundCloud, Pixiv e a lista segue. Baixa desde a área de transferência com um toque (botão Instant), compartilha o link de qualquer app e o Gabi o recolhe, qualidade até 1080p/máxima, extração a MP3, vista prévia com título e peso estimado, e temas com cores dinâmicas Material You. O complemento natural desta guia: para escutar, os clientes de cima; para levar, o Gabi.

Ambas se conseguem na Appteka — a loja da Publicação 01. O APK direto não se cola: a casa de cada app é seu repo.

## 🚫 O que não se cola

APK de mods «premium» de qualquer app · listas copiadas de wikis de download · convites de grupos · receitas de URLs. Cada um abre o README do projeto no dia em que for usar — a casa de cada ficha está nos links de baixo.

## ❓ Perguntas frequentes

**Qual instalo para começar?**
Se sua música é catálogo: Metrolist (a de cadência mais regular) ou OuterTune (se além disso você tem arquivos locais). Se sua música é sua coleção: Auxio. Se quer todo o YouTube sem conta: NewPipe. Se vive de podcasts: AntennaPod.

**Estes apps são legais?**
Esta guia não é um escritório de advocacia e não diz isso. Diz que projeto existe, com que licença, e em que estado. Os termos de cada serviço se leem na sua casa.

**Por que InnerTune segue nas listas se está dormindo?**
Porque é o ancestral vivo de meia família — e porque seus herdeiros (OuterTune, Metrolist) levam seu código adiante. Ficha-se por história e por quem o use igual.

**Metrolist ou OuterTune?**
Ambas vivas e ativas neste mês. Metrolist: cadência mensal provada. OuterTune: arquivos locais integrados. A que cobrir seu uso — e as duas se abrem no dia em que instala, porque os números caducam.

**E o que aconteceu com RiMusic?**
Arquivada em julho de 2025. O fio de 340 mil caracteres de abril a tratava como viva: inflar não verifica. Sua ficha diz: história.

**Estes apps consomem muita bateria?**
O que esta guia pode dizer sem laboratório: são reprodutores, não jogos; o consumo depende do uso (download vs streaming). O que NÃO pode dizer: números de bateria — não se mediram aqui, e não se inventam.

**Há versão para iPhone?**
Desta família: Harmony-Music declara multiplataforma (desktop e móvel). O resto das fichas é Android. O ecossistema iOS livre de música é outro mapa.

**Discord ou grupo para suporte?**
Cada projeto tem sua casa de comunidade no seu README — abre-se ali, não se cola aqui. Esta família não usa canais de envio.

## 🔗 Links

- Metrolist: https://github.com/mostafaalagamy/Metrolist
- OuterTune: https://github.com/OuterTune/OuterTune
- SimpMusic: https://github.com/maxrave-dev/SimpMusic
- InnerTune: https://github.com/z-huang/InnerTune
- Harmony-Music: https://github.com/anandnet/Harmony-Music · music-you: https://github.com/DanielSevillano/music-you · InterTune: https://github.com/ItzSkyeYT/InterTune
- NewPipe: https://github.com/TeamNewPipe/NewPipe
- Auxio: https://github.com/OxygenCobalt/Auxio
- AntennaPod: https://github.com/AntennaPod/AntennaPod
- N-Zik: https://github.com/N-Zik-Group/N-Zik · loja: https://appteka.store/app/4abr315772
- Gabi: https://github.com/Hotaro26/gabi · loja: https://appteka.store/app/b4cr315682
- Arquivados: https://github.com/vfsfitvnm/ViMusic · https://github.com/fast4x/RiMusic

> A Bandita informa a partir de fontes datadas. A linhagem também se verifica: os ancestrais explicam os vivos.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: SimpMusic ★11.257, Metrolist ★12.789 (+Nightly), OuterTune ★5.390, InnerTune ★6.088, dev N-Zik v8.0.0. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
