# Publicação 13 — Ramo Aniyomi: mangá e anime em um só leitor — Aniyomi, Animetail e Tadami

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 13)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🌳 A árvore deste ramo
├── 🎬 Aniyomi — o ramo mãe
├── 🦋 Animetail — o fork que se declara oficial
├── 🌗 Tadami — o terceiro na conversa
├── 🌲 A rede completa de forks (revisada no dia 14-set)
├── 🧩 As extensões de anime: onde vivem hoje
├── ⚖️ Quando faz sentido este ramo
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

A árvore Tachiyomi/Mihon tem um ramo inteiro dedicado ao anime: leitores que fazem as duas coisas — ler mangá e ver anime — desde o mesmo aplicativo. Esta guia é o mapa desse ramo, aberto HOJE, 14 de setembro, repo por repo:

```
Aniyomi     ★7.683   v0.18.2.1 (14-set)     push do dia 14-set  o ramo mãe
Animetail   ★578     v0.20.4.0 (5-ago)      push 7-set    fork respaldado
Tadami      ★260     v0.62 (12-set)         push 13-set   fork — viva (ratificação ao pé)
```

Os três vivem. E a notícia do dia a dá a mãe: Aniyomi publicou DUAS versões nesse mesmo dia 14 de setembro, depois de onze meses sem releases — o mesmo dia em que sua descendente Animiru fazia o próprio no seu ramo. A família inteira se moveu hoje. O critério para escolher entre elas não muda: o uso real e o repo vivo, como com toda a árvore.

## 🌳 A árvore deste ramo

```
Aniyomi (o ramo mãe: mangá + anime)
   ├── Animetail     declara-se «Official fork of Aniyomi»
   ├── Tadami        mangá + anime + ranobe (romances leves)
   └── Animiru       a versão SÓ anime
                     (tem guia própria: peça seguinte)
```

Um aponte de linhagem que se lê na API: Animetail e Tadami figuram como forks (campo fork = true, pai visível). Animiru também desce de Aniyomi — mas sua história está na peça do seu ramo.

## 🎬 Aniyomi — o ramo mãe

https://github.com/aniyomiorg/aniyomi

```
Qué é:        «An app for manga and anime» — o leitor
              da linhagem Tachiyomi com reprodutor de anime
              integrado (baseado em mpv)
Licença:      Apache-2.0
Versões:      0.18.2.1 e 0.18.2.0 — publicadas no dia 14-set
              (a anterior estável: 0.18.1.2, do dia 28-out-2025)
Push:         14 de setembro de 2026 (dia da verificação)
Android:      8.0+ (segundo sua ficha de download)
Trackers:     MyAnimeList, AniList, Kitsu, MangaUpdates,
              Shikimori, Simkl e Bangumi (seu README)
Organização:  aniyomiorg — mantém além disso seu site,
              o host de previews (aniyomi-preview)
              e a documentação de forks
```

Até esta manhã, sua última versão estável era de outubro de 2025 — onze meses de silêncio de releases, com a dúvida flutuando de se o ramo mãe seguia de pé. A dúvida ficou resolvida HOJE: v0.18.2.0 e v0.18.2.1 saíram no mesmo dia em que sua descendente Animiru também publicava. Os empurrões de código deste mês não eram fumaça: eram preparação. A lição se cumpre outra vez nesta coleção: um repo calado não é um repo morto — e o único que o diz com certeza é a página de releases, aberta no dia em que se decide.

Sua organização fez além disso algo pouco comum: mantém uma página que lista os forks conhecidos do projeto — o índice onde Animiru (ramo seguinte desta série) figura registrado. Um projeto que cartografa seus filhos é um projeto com memória.

## 🦋 Animetail — o fork que se declara oficial

https://github.com/Animetailapp/Animetail

```
Qué é:        «Official fork of Aniyomi» (sua descrição)
Licença:      Apache-2.0
Versão:       0.20.4.0 (5 de agosto de 2026)
Push:         7 de setembro de 2026
Curiosidade:  sua numeração segue Mihon (0.20.4),
              porque sincroniza o núcleo do leitor mangá
              com o tronco — seu histórico de mudanças
              o documenta
Host de provas: Animetail-preview (★75)
```

Animetail é o fork que tomou a decisão técnica mais interessante do ramo: em vez de esperar Aniyomi, traz o núcleo atualizado do leitor de mangá (o de Mihon) dentro do reprodutor de anime — por isso suas versões compartilham número com Mihon, e a página de forks de Aniyomi lhe adiciona uma função concreta: suporte Cast. E há novidade de estatus verificada HOJE: a organização de Aniyomi o lista na sua página de «forks respaldados», junto a Animiru. A etiqueta «Official» já não é só sua: a assina o original. A API confirma a linhagem por seu lado: fork registrado, pai aniyomiorg.

Publica checksums SHA-256 por arquitetura em suas releases — a boa prática de sempre: o arquivo e sua pegada, juntos.

## 🌗 Tadami — o terceiro na conversa

> **Acta (15-set):** a casa original — andarcanum/Tadami-Aniyomi-fork — devolve 404 desde a reverificação de HOJE. Ficam seu site oficial (tadami.qzz.io) vivo e forks órfãos. Método da casa: **o espelho não é o repo** — Tadami não se receita até que sua casa diga onde vive. O anotado aqui fica como história datada.

> **Ratificação (15-set, noite):** o dono constatou a casa viva e o verificador re-abriu ao vivo: **andarcanum/Tadami-Aniyomi-fork responde — ★260, v0.62 (12-set), push do dia 13-set. VIVA.** O 404 da tarde foi real, mas de outra porta: o slug `anandnet/…` que o censo arrastava — e o erro foi atribuir-lhe a queda a esta casa. E notícia nova do corte: o projeto estreou organização própria — **tadamiorg/tadami** (★56, com carril de releases próprio: v1.9.3 do dia 26-jul). Duas casas do mesmo nome: a palavra sobre qual manda a tem o dono.

https://github.com/andarcanum/Tadami-Aniyomi-fork *(viva — ratificação acima)*

```
Qué é:        «An app for manga, anime and ranobe» —
              o que somou os romances leves à fórmula
Licença:      Apache-2.0
Versão:       0.62 (12 de setembro de 2026)
Push:         13 de setembro de 2026
Ritmo:        três versões em um mês (0.60 → 0.62)
Estrelas:     258 — o mais jovem e o menor
```

Tadami é a aposta fresca: fork de Aniyomi que adiciona leitura de ranobe (romances leves) e se move rápido — versões do dia 20 de agosto, 29 de agosto e 12 de setembro. Seu tamanho pequeno é sua ficha honesta: comunidade jovem, desenvolvimento pessoal, cadência alta. Para saber se vai a sério, o método de sempre: abrir seus issues, olhar se o autor responde, e seguir-lhe o rastro umas semanas. O que hoje é verificável: vive, empurra, e publica versões com data recente.

## 🌲 A rede completa de forks (revisada no dia 14-set)

Este ramo não são só três fichas: a rede de forks das três casas se revisou no dia 14-set, fork por fork, na API do GitHub. O panorama, com os bastidores abertos:

```
aniyomi     1ª página de forks mais novos: 100
            a maioria: cópias pessoais ★0 com a
            descrição de fábrica — sem mudanças próprias

Animetail   30 forks — todos «não oficiais», ★0-1
Tadami      31 forks — 6 renomeados com propósito
```

**Os que sim trazem algo próprio (verificado hoje):**

- **Kuro** (Zykrave/aniyomi-Kuro, ★21) — «uma biblioteca multimídia e reprodutor redesenhados ao moderno» segundo seu README: o fork mais seguido da rede, v1.0.0 do dia 13 de agosto. Rebrand completo, não remendos.
- **MeMedia** (FunMan1995/MeMedia, v0.21.2 do dia 22-ago) — a ideia mais curiosa da rede: leitor mangá de Mihon + reprodutor anime de Aniyomi em um só app, com abas separadas que Mihon não tem. Seu README explica o «porquê deste fork» com bibliotecas independentes por mídia.
- **aniyomi-revived** (Blackyfi, ★1) — «fork atualizado para se manter em dia»: duas releases no mesmo dia 3 de setembro (v0.18.1.32/33). Cumpre o que o nome promete.
- **anteiku** (Heavenofficial) — a variante «mangá, anime e filmes».
- Em Tadami: **mugen** (h80r, v0.72.81 do dia 1-set), **Nattyflix** (anime+mangá+filmes) e um fork de localização que promete «conserto de inglês e overhaul de gestos» do leitor de romances (sem releases ainda). E dado de lealdade: um fork de Tadami publicou sua v0.62.0 no mesmo HOJE que o pai — a rede segue os releases ao vivo.
- Em Animetail, o único com função própria declarada: um fork que adiciona **Discord Rich Presence** ao re-focar o app.

O resto da rede são cópias sem funções próprias: não se anotam — o mapa é do que vive e aporta.

**A expedição profunda (a rede inteira, 649 membros, caminhada no dia 14-set):** o bosque não termina na primeira página. A rede completa de Aniyomi — que é a mesma de Animiru, família por API — caminhou-se membro a membro: 93 carregam nome próprio. Na camada profunda, as raridades que valem menção: **kikuyomi**, um fork de Aniyomi para escutar **audiolivros**; **jishoyomi**, para estudar com o anime (ferramentas de aprendizado); **Anichibi**, o fork lúdico com versões V2 e V3; e uma árvore dentro da árvore: **Kuukiyomi**, projeto pessoal com sete membros de rede próprios. O resto da camada profunda são cópias com README de fábrica: fora do mapa. Com essa régua, o mapa fica completo.

## 🧩 As extensões de anime: onde vivem hoje

O capítulo delicado deste ramo são suas extensões. O mapa de hoje:

```
Yūzōnō anime            ★428 · push 13-set
   hoje, o canal vivo de referência:
   github.com/yuzono/anime-extensions

Yūzōnō / kohi-den       vivo, verificado no dia 14-set
   o código da casa Kohi-den continua
   na família Yūzōnō:
   github.com/yuzono/kohi-den

Novos armazéns dedicados        push do dia 14-set
   existem repos novos centrados nos clientes
   anime da família Anikku/AniZen — vão na
   peça desse ramo, onde lhes toca.
```

A regra da casa: os índices de instalação não se colam — leem-se no README de cada armazém, no dia em que se usam. O que esta guia dá é o mapa: quem vive, quem morreu, com data.

## ⚖️ Quando faz sentido este ramo

Com o critério da casa (uso real, unicidade, maturidade, propósito próprio):

```
Vê anime E lê mangá, e quer um só app?
   → O terreno natural deste ramo: as três
     fichas cobrem esse caso, com estilos distintos.

Só anime?
   → Este ramo é mais do que precisa:
     a peça seguinte (Animiru/Anikku) é o
     ramo de anime puro.

Só mangá?
   → O tronco (Mihon e família, guia própria)
     pesa menos e sobra menos.

Romances leves além disso?
   → Tadami os traz de fábrica; Reikai (ramo
     J2K) é a outra via mangá+romances.
```

Nenhuma das três fichas é «a melhor». A boa é a que cobre seu uso, com repo vivo no dia em que instala — e essa comprovação se faz abrindo seus releases nesse dia.

## ❓ Perguntas frequentes

**Aniyomi deixou de se desenvolver?**
A pergunta ficou respondida no dia 14 de setembro: v0.18.2.0 e v0.18.2.1, publicadas no dia 14 de setembro depois de onze meses sem releases — com o código empurrando durante o mês. A organização segue ativa. Quando duvidar de um projeto, o relógio é sua página de releases, aberta nesse dia.

**Animetail é «oficial de verdade»?**
Tripla verificação: o declara sua descrição, a API confirma o parentesco direto e — desde hoje verificado — a página de forks respaldados de aniyomi.org o lista junto a Animiru, com suporte Cast entre suas funções. Seu histórico (migrar o núcleo de Mihon, releases com checksums) é de projeto sério.

**Por que as versões de Animetail levam o número de Mihon?**
Porque sincroniza o leitor de mangá com o tronco: é sua proposta de valor — anime + leitor atualizado sem esperar ninguém.

**Tadami não é pequeno demais?**
É jovem. Pequeno não é inválido: é a porta de maturidade pendente de demonstrar. Com cadência de releases desta semana, vai a caminho.

**As extensões do armazém velho ainda servem?**
As já instaladas, seguem; as novas, saem pelos armazéns vivos. O oficial parou em agosto de 2024 — a data manda.

**Animiru entra nesta guia?**
Compartilha avô, mas seu ramo tem peça própria (a seguinte): ali vive sua ficha completa, com as duas versões que publicou no dia 14-set.

## 🔗 Links

- Aniyomi: https://github.com/aniyomiorg/aniyomi · https://github.com/aniyomiorg/aniyomi-preview
- Animetail: https://github.com/Animetailapp/Animetail · https://github.com/Animetailapp/Animetail-preview
- Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- Destacados da rede: https://github.com/Zykrave/aniyomi-Kuro · https://github.com/FunMan1995/MeMedia · https://github.com/Blackyfi/aniyomi-revived
- Extensões de anime vivas: https://github.com/yuzono/anime-extensions · sucessão de Kohi-den: https://github.com/yuzono/kohi-den
- Forks respaldados por Aniyomi: https://aniyomi.org/forks/
- Arquivados (história): https://github.com/aniyomiorg/aniyomi-extensions · https://github.com/kohi-den/extensions-source

> A Bandita informa a partir de fontes datadas. Mangá e anime na mesma mão — com o repo vivo adiante da etiqueta.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Aniyomi ★7.683 + acta e ratificação Tadami. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
