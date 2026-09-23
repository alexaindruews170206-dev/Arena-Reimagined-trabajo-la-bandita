# Publicação 16 — Ramo SY/Komikku: o fork clássico e o rebento com organização — TachiyomiSY e Komikku

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 16)**

## 🗺️ Mapa deste guia

├── ⚡ Em uma página
├── 🌳 A árvore deste ramo
├── 📗 TachiyomiSY — o clássico que segue
├── 📘 Komikku — o rebento com org
├── 🔀 As duas escolas de fork (e o contraexemplo)
├── 🧩 As extensões deste ramo
├── 🌲 A rede completa de forks (revisada em 14-set)
├── 🏗️ A infraestrutura: previews e sync
├── ⚖️ SY ou Komikku: como decidir com critério
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Este é o ramo do estilo clássico: TachiyomiSY — o fork que acrescentou as funções extra ao Tachiyomi original, o clássico «SY» da velha guarda — e Komikku, o projeto que nasceu desse linhagem e cresceu até ter organização própria. Verificado HOJE, 14 de setembro:

```
TachiyomiSY        ★4.143   1.13.2 (13-jul)   push 13-set   o clássico
TachiyomiSYPreview ★484     host de previews  push 25-ago
Komikku            ★4.717   v1.14.1 (17-jul)  push 11-set   o rebento
komikku-preview    ★248     canal de testes   push 10-set
```

São os dois grandes vivos do estilo SY do ecossistema — e a comparação entre eles é a lição sobre como um fork se torna projeto com vida própria.

## 🌳 A árvore deste ramo

```
TachiyomiSY (jobobby04)      o clássico vivo
   ├── TachiyomiSYPreview     host de builds de teste
   └── Komikku (komikku-app)  repo novo que herda o
               ├── komikku-preview  código e cresceu com org
               ├── Anikku           o cliente de anime dele
               └── (o ramo dele tem peça própria nesta coleção)
```

Detalhe técnico que se lê na API: o Komikku NÃO figura como fork (é um repo novo); o linhagem é declarado pela própria documentação dele. É a diferença entre o grafo do GitHub e a realidade — por isso se leem os dois.

## 📗 TachiyomiSY — o clássico que segue

https://github.com/jobobby04/TachiyomiSY

```
★4.143 · Apache-2.0
Versão:      1.13.2 (13 de julho de 2026)
Push:        13 de setembro — código de ONTEM
O que é:     o fork clássico: o leitor do tronco
             com as funções extra do estilo SY
             (mais fontes por padrão, mais ajustes
             de leitura, a experiência "completa")
```

O SY é o fork com mais história contínua do ecossistema: existia antes do fechamento do original, sobreviveu a janeiro de 2024 e segue empurrando código — fez isso em 13-set, constância da verificação dele. O ritmo dele não é o de releases mensais: a última estável é de julho e o código se move desde então. O padrão do veterano: menos barulho de versões, mais manutenção silenciosa.

O aviso de identidade: **o SY vivo é o jobobby04** — no dia em que você buscar o SY, instale a partir do repo dele, o que empurra código de ontem. O nome não basta; o dono sim.

O host de builds de teste: jobobby04/TachiyomiSYPreview (★484) — versões experimentais para curiosos e repórteres de bugs, não o caminho do dia a dia.

## 📘 Komikku — o rebento com organização

https://github.com/komikku-app/komikku

```
★4.717 · Apache-2.0
Versão:      1.14.1 (17 de julho de 2026)
Push:        11 de setembro
O que é:     leitor de mangá do linhagem SY que nasceu
             como repo novo e cresceu até
             organização completa:
             - komikku-preview (★248): canal de testes
             - Anikku (★1.028): o cliente de anime dele
             - traduções comunitárias próprias
```

O Komikku é o estudo de caso de como um fork vira instituição: herdou o código do linhagem, nasceu com casa própria e construiu estrutura — org, canal de previews, projeto irmão de anime, comunidade de tradução. As versões vão em cadência regular (1.14.1 em julho, com ramo de desenvolvimento empurrando desde então).

Em estrelas já supera o SY clássico (4.717 vs 4.143). Isso não é veredicto de qualidade — é um dado de comunidade. O que é veredicto verificável: a oficina se move (push de 11-set) e a infraestrutura é a mais completa deste ramo.

## 🔀 As duas escolas de fork (e o contraexemplo)

Este ramo tem os três arquétipos do ecossistema, vivendo na mesma casa:

```
ESCOLA 1 — manter o sobrenome
TachiyomiSY: continua o fork clássico, conserva
o nome e o estilo, evolui com cuidado.
O valor dele: continuidade. O usuário dele:
o que quer o de sempre, vivo.

ESCOLA 2 — crescer com casa nova
Komikku: herda o código, batiza o próprio nome,
constrói organização e até ramo de anime.
O valor dele: evolução com estrutura. O usuário
dele: o que quer o projeto que mais se move
em estrutura.
```

## 🌲 A rede completa de forks (revisada em 14-set)

Abriram-se em 14-set, fork por fork, as redes do SY (238 forks, três páginas, duas ordens) e do Komikku (200 forks). É a rede mais rica do ecossistema — e a que melhor mostra a diferença entre copiar e aportar:

**Na rede do SY:**

```
Chai (Smol-Ame)          ★12 · push 22-ago
   o fork vivo mais seguido: filtro «lewd» para
   esconder o picante da biblioteca, busca
   por estado de tracking e edição de info do
   mangá — sem releases ainda (só código)

SY com Discord RPC (jeryjs)  ★10 · preview-43 (23-jul)
   presence do Discord enquanto você lê

Faxyomi                  ★4 · v9 (29-ago)
   «para ter DOIS SY no mesmo telefone» —
   o caso de uso mais honesto do ecossistema

Shinyomi ★5 (1.0.0, mai-25) · Mizu ★2 · Dyomi
(build 8-set) · Fukuro (push 4-set) · variante
desktop em obras · o fork da equipe SyncYomi
(push 10-set)
```

**Na rede do Komikku:**

```
Houri (PineappleTwilight)  ★10 · v1.22.1 (HOJE 15-set) *(a v1.22.0 saiu dia 14 — dois dias seguidos: a cadência segue)*
   o fork com proposta própria mais ativo:
   suporte de RELEITURA com trackers conectados
   (rereads por mangá), Discord RPC melhorado que
   respeita subcategorias, filtros por padrão por
   fonte e um feed melhorado opt-in

komikku_img_upscale · r10647 (13-set)
   upscale de imagens de páginas — mais três
   forks a mais do mesmo tema (upscaling/scaling)

mikku (Syncthing integrado) · komikku com
marcadores de página · kokomikku (KOReader) ·
um fork com tracker próprio · komikku2 (13-set)
```

O dado fino: o autor do Houri mantém também um fork do Anikku (anikku-pineapple) — um só dev tecendo entre os dois ramos da casa Komikku.

**A camada que o grafo esconde (cinco casas verificadas em 14-set a pedido dos grupos)**

Esses cinco NÃO aparecem na rede de forks direta do SY nem do Komikku: são forks rebasados com casa nova, ou netos — invisíveis para o grafo do pai. Foram abertos um a um, com as opções próprias lidas dos README:

```
ShinKu (Harrys-HQ)         ★31 · v2.6.9 (13-set)
   «fork modernizado e rebatizado de
   TachiyomiSY/Mihon» — cadência semanal.
   O dele: busca em linguagem natural com
   descoberta assistida («Vibe Search» e
   «For You»), cartão de estatísticas de
   leitura, áudio ambiental que casa com o
   gênero, interface que muda de cor com a
   capa, categorizador automático, escâner
   de fontes mortas para migrar seu mangá, e
   menu para migrar as atualizações
   falhadas.

MihonSY (ruzhe85)          ★13 · v1.0.7 (22-ago)
   fork chinês do SY (o README dele vem em chinês).
   O dele: scroll por toque em webtoon com
   distância ajustável (½, ¾ ou tela
   inteira) e animação regulável, detecção
   automática de webtoon pela resolução da
   imagem, progresso Komga sincronizado capítulo
   a capítulo (não por lotes), melhoria de imagem
   Lanczos3 leve —sem modelos pesados— e
   resolução nativa 1:1.

Pokomi (pokedo0)           ★11 · v1.0.9 (16-ago)
   fork do Komikku com uma ideia própria clara:
   «Author Following» — assinar para
   seguir seus autores. Herda as funções
   únicas do Komikku.

NEXUS (the-nexus-app)      ★3 · v1.2.1 (8-set)
   fork do Komikku: sugestões que leem as
   recomendações do próprio site da
   fonte, categorias ocultas COM
   autenticação para abri-las ou apagá-las, e
   marcadores de capítulos e páginas na
   hora.

bchan (geograms)           ★5 · v1.12.1 (19-jun)
   «fork simplificado de TachiyomiSY/Mihon»:
   extensões Keiyoushi prontas de fábrica,
   leitura webtoon por padrão, downloads que
   pausam e retomam sozinhos entre redes, e
   nomes de arquivo planos e previsíveis.
```

E a segunda geração também deu a sua: **Yomiko** (petalya, ★8, push de 12-set), filha do fork de Discord-RPC — a corrente não se corta.

A lição de método fica no texto: a lista de forks do pai não mostra os rebasados nem os netos. Mapear a árvore é caminhar as correntes e ler os créditos de cada README — e quando alguém nomeia uma casa que não saiu na varredura, o enlace manda.

**A expedição profunda (SY: mais de 1.000 membros · Komikku: 244 · anikku: 71 — tudo caminhado em 14-set):** a segunda geração já compila: **leassapie/houri**, filho do Houri, com versão própria v1.21.0 (30 de agosto) — a corrente Houri → o filho, viva. **Yomiko**, a neta do fork de Discord-RPC — matiz datado (corrigido em 15-set por auditoria da casa): a casa mostrava push, mas a versão estável dela (v.1.8.1 — correção datada de 15-set por REST e git: release de 25-set-2025, não ago-2026; e genealogia CERTIFICADA por fork: Yomiko ← SY-Discord-RPC ← TachiyomiSY — linha SY, não J2K). Que a data diga o que a data diz. ShinKu, NEXUS, MihonSY, Pokomi e bchan são por ora folhas: quando deitarem raízes, se anotam com data.

## 🧩 As extensões deste ramo

O ramo SY/Komikku é o que mais armazéns vivos atende. O mapa da fornada do 14 (o guia completo tem peça própria nesta coleção):

```
Keiyoushi              o hub principal
   o armazém mais usado do ecossistema: declara
   suporte para Mihon, TachiyomiSY e Komikku
   (guia completa: Publicação 04 desta coleção)

Yūzōnō manga           ★890 · ESPEJO do Keiyoushi
   espelho automático, sem aportes próprios —
   descontinuado (não arquivado): o «push de
   hoje» é o espelho sincronizando, não vida
   própria. Para mangá, a casa é Keiyoushi

cuong-tran/manga-repo  ★445 · push de 14-set
   «Extensions for Komikku / Mihon & forks»
   (a descrição dele)

Estantes "cursed"      ★185/★158  nome sim, índice não
```

O aviso do Keiyoushi continua sendo a chave do ecossistema: se sua lista de extensões sai vazia com «Outdated app», seu app já não é compatível — atualize-o a partir do repo dele. E a convenção técnica do momento (KeiSource 1.6) se conta no guia de extensões: é a razão pela qual os apps velhos deixam de ver extensões novas.

## 🏗️ A infraestrutura: previews e sync

Duas peças que este ramo compartilha com o ecossistema e que convém conhecer:

- **Os hosts de previews** (SYPreview, komikku-preview) são o canal de testes de cada projeto: builds experimentais para quem reporta bugs. Instalá-los é decisão de tester, não de usuário diário.
- **tracker-extensions** (komikku-app, ★14): as extensões de trackers da casa Komikku — os trackers se servem à parte do núcleo, como extensões (verificado em 14-set).
- **SyncYomi** é a sincronização de bibliotecas entre dispositivos e entre forks da família — útil exatamente para o gesto deste guia: se você prova o SY e o Komikku, seu progresso pode acompanhar você entre ambos. A ficha completa, na coleção de ferramentas desta série.

## ⚖️ SY ou Komikku: como decidir com critério

As quatro portas da casa, aplicadas sem «melhores»:

```
Continuidade          se você vinha do SY de sempre,
                      o jobobby04 é a mesma casa com
                      as luzes acesas.

Estrutura             se você valoriza org, canal de previews,
                      projeto irmão de anime e
                      cadência de releases: Komikku.

Compatibilidade       os dois leem os mesmos armazéns
                      principais (o Keiyoushi o declara
                      para ambos). O critério de desempate
                      não está nas fontes: está no
                      uso que você for dar.

Maturidade            os dois empurraram nesta semana.
                      Nenhum passa pela porta com as
                      mãos nos bolsos.
```

O resto é gosto pessoal — e o uso real: quem usa e comprova. As estrelas (4.717 vs 4.143) são o dado de fama do dia, não uma recomendação.

## ❓ Perguntas frequentes

**SY e Komikku são o mesmo código?**
Compartilham o linhagem, não o repo nem o dono. A API não declara o Komikku como fork; a própria documentação dele conta de onde vem. Parentela declarada, casas separadas.

**Qual tem mais fontes?**
As fontes vivem nos armazéns (Keiyoushi, Yūzōnō…), não no app — e os armazéns principais declaram suporte para ambos. O desempate real está no app que melhor caiba na sua mão.

**E os repos com o mesmo letreiro que já não se movem?**
Não se anotam: o mapa é do que vive. A regra prática: instale o SY a partir do repo do jobobby04 — e mais ninguém.

**E os repos que se anunciam como «o leitor de 2026»?**
No escaneio de 14-set apareceu outra fornada do padrão já conhecido: repos novos com nomes de projetos sérios — um «komikku-scans», um «Neko-Manga-Pearl» que toma emprestado o nome do fork real do MangaDex, um «kumo-surreal» que se diz Mihon otimizado — criados os três no mesmo dia, com estrelas quase idênticas entre si e o ano «2026» na descrição. A fornada cresce enquanto isso: um «weeb-index» («Best Otaku Directory 2026») e um «manga-zen-reader» («Best Alternatives 2026») repetem o traje com as mesmas estrelas de mentira. Se nomeiam sem enlace: é SEO para colher downloads de quem busca rápido. O projeto real não precisa pôr o ano no nome.

**E forks com nomes que soam japoneses que a gente menciona (tipo «ShinKu»)?**
Fichados acima, com data: o ShinKu existe (★31, v2.6.9 com cadência semanal, do linhagem SY/Mihon) — no repasso anterior não apareceu porque os forks rebasados e os netos não saem na rede de forks do pai. Duas regras ficam para o leitor: um nome sem enlace não se verifica nem se descarta — e o enlace, sempre, fecha o caso.

**O Komikku saiu do SY ou do Tachiyomi?**
A documentação dele declara o linhagem do ecossistema; o grafo do GitHub o mostra como repo novo. As duas coisas são certas: herança declarada, casa própria.

**Posso ter os dois instalados?**
Tecnicamente sim (pacotes distintos). A pergunta útil é a de sempre: o que o segundo aporta que o primeiro não cubra? Se a resposta for «nada», um leitor basta.

**E o Anikku?**
É o cliente de anime da organização Komikku — tem guia própria nesta coleção (ramo anime puro). A família se estende: mangá (Komikku), anime (Anikku), e o rebatizado AniZen no ramo à parte dele.

**Qual sacou a versão mais recente?**
Nenhum dos dois em setembro: SY 1.13.2 e Komikku 1.14.1 são de julho — com código dos dois se movendo neste mês. O push não etiqueta: o release se abre no dia em que se instala.

## 🔗 Links

- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY · https://github.com/jobobby04/TachiyomiSYPreview
- Komikku: https://github.com/komikku-app/komikku · https://github.com/komikku-app/komikku-preview
- Destacados da rede: https://github.com/PineappleTwilight/houri · https://github.com/Smol-Ame/Chai · https://github.com/jeryjs/TachiyomiSY-with-discord-RPC · https://github.com/Viel0320/komikku_img_upscale · https://github.com/nas3ts/mikku
- A camada que o grafo esconde: https://github.com/Harrys-HQ/ShinKu · https://github.com/ruzhe85/MihonSY · https://github.com/pokedo0/Pokomi · https://github.com/the-nexus-app/NEXUS · https://github.com/geograms/bchan
- Armazéns do ramo: https://github.com/keiyoushi/extensions · https://github.com/yuzono/tachiyomi-extensions · https://github.com/cuong-tran/manga-repo
- Sincronização: https://github.com/syncyomi/syncyomi
- Guias irmãs: extensões (Publicação 04) · forks do tronco (Publicação 06) · anime puro (Publicação 14) desta coleção

> A Bandita informa a partir de fontes datadas. Duas escolas, um mesmo linhagem — e o letreiro, você já sabe, não instala nada.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Houri v1.22.1 de HOJE, manga-repo ★445, SY/Komikku re-contados. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
