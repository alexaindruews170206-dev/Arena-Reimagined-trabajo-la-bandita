# Publicação 14 — Ramo anime puro: Animiru e Anikku — os clientes que tiraram o mangá de cima

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 14)**

## 🗺️ Mapa deste guia

├── ⚡ Em uma página
├── 🌳 A árvore deste ramo
├── 🍥 Animiru — o anime-only que nasceu de Aniyomi
├── 📺 Anikku — o anime da organização Komikku
├── 🌲 A rede de forks dos dois (revisada em 14-set)
├── 🧩 As extensões desses clientes (novidade do dia)
├── ⚖️ Anime puro ou anime+mangá: como decidir
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Há um ramo da árvore anime que tomou a decisão contrária à de Aniyomi: em vez de acrescentar mangá ao player, TIRARAM o mangá para ficar só com o anime. Este guia abriu em 14 de setembro, e as casas desse ramo são:

```
Animiru   ★864    v0.20.0.1 (14-set)   fork anime-only de Aniyomi
Anikku    ★1.028  v0.2.0 (11-set)           anime da organização Komikku
```

Dado do dia: **o Animiru publicou duas versões nesta mesma manhã** (0.20.0.0 e 0.20.0.1). E na frente do Anikku, há armazéns de extensões dedicados a ele com atividade de hoje. O ramo pequeno da árvore é, nesta semana, o que mais se mexeu.

## 🌳 A árvore deste ramo

```
Aniyomi (mangá + anime)
   └── Animiru      tirou o mangá: SOMENTE anime
         └── AnimiruTv  variante para Android TV

Komikku (mangá, com organização)
   └── Anikku       o cliente de anime dele
         └── anikku-preview   o canal de testes
```

Dois caminhos distintos para o mesmo destino: um cliente de anime livre. O Animiru saiu do ramo Aniyomi; o Anikku saiu da organização Komikku. Não são competição direta por nascimento — são duas famílias que chegaram ao mesmo balcão.

## 🍥 Animiru — o anime-only que nasceu de Aniyomi

https://github.com/Quickdesh/Animiru

```
O que é:      fork do Aniyomi que elimina a parte
              do mangá para ser um app SOMENTE de anime
Licença:      Apache-2.0
Versões:      0.20.0.1 e 0.20.0.0 — publicadas em 14-set
              (a anterior: 0.19.8.1, de 9-ago)
Android:      8.0+ (a ficha de download dele)
Player:       construído sobre mpv, configurável
Trackers:     MyAnimeList, AniList, Kitsu, Shikimori,
              Simkl, Bangumi e Hikka (o README dele)
Estrelas:     862
```

Três coisas fazem o Animiru especial dentro da árvore:

**Um: o registro oficial.** O Animiru figura listado na página de forks que a própria organização do Aniyomi mantém (aniyomi.org/forks/Animiru). Não é um clone que apareceu do nada: é um fork registrado no índice do projeto-mãe — a diferença entre a casa reconhecida e a barraca sem dono na beira da estrada.

**Dois: a decisão de design.** Tiraram o mangá de propósito. Menos app, menos peso, um só trabalho bem feito. Para quem nunca lê mangá, é exatamente a ferramenta certa — e para quem lê os dois, é metade de uma solução.

**Três: o ritmo de hoje.** Duas versões publicadas na mesma manhã de hoje. Seja lá o que o autor está ajustando, ele está ajustando agora — o repo se sente vivo pela capa.

A estirpe dele tem galho próprio: existe o AnimiruTv (fork para Android TV) e cópias menores sem atividade. A ficha canônica é Quickdesh/Animiru — o que mantém o ritmo e o registro.

## 📺 Anikku — o anime da organização Komikku

https://github.com/komikku-app/anikku

```
O que é:      «Free and open source anime watcher
              for Android» — o cliente de anime da
              organização que mantém o Komikku
Licença:      Apache-2.0
Versão:       0.2.0 (11 de setembro de 2026)
Push:         14-set (dia da verificação)
Canal de testes: anikku-preview (★112, push 10-set)
Estrelas:     1.028 — a maior deste ramo
```

O Anikku é a aposta institucional: não é projeto de uma pessoa, é a peça de anime de uma organização que já demonstra ofício com o Komikku (um dos leitores de mangá mais ativos do ecossistema, ★4.717). A versão 0.2.0 desta semana o coloca na fase jovem mas patrocinada: tem org por trás, tem canal de previews, tem traduções comunitárias.

O nome, cuidado com a semelhança: existe uma família inteira de clientes com raiz «Ani-» (Aniyomi, Animetail, Animiru, Anikku, e o rebatizado AniZen, que tem guia própria). Cada um com seu repo e seu dono. O nome não herda nada; o repo explica tudo.

## 🌲 A rede de forks dos dois (revisada em 14-set)

O vivo e com proposta nas duas redes (revisado em 14-set, fork por fork):

- **AnimiruTv** continua sendo a variante canônica para Android TV.
- **Vidi** é a única variante do Animiru com builds próprios e frescos: v0.19.12, de 4 de setembro.
- Na rede do anikku: a **porta para macOS** segue em obra (push de agosto) e o **anikku-pineapple** tece com o Houri no ramo mangá — o mesmo autor nos dois ramos da casa Komikku (veja o guia SY/Komikku).

O resto das duas redes (32 e 68 forks) são cópias sem funções próprias declaradas: não se anotam. O mapa é do que vive e aporta — e no dia em que alguém aportar, entra com data.

## 🧩 As extensões desses clientes (novidade do dia)

Um cliente de anime sem fontes não faz nada — e nesta semana o ramo estreou armazéns próprios. Verificados hoje:

```
salmanbappi/extensions-repo      ★40 · push de HOJE (re-verificado 15-set)
   «Repositório de extensões de anime
   dedicado ao Anikku» — conforme a descrição

salmanbappi/aniyomi-extensions   ★15 · push 12-jan
   «Extensões para Anikku / Aniyomi & forks»
```

O detalhe que conecta guias: o autor desses armazéns é o mesmo desenvolvedor do AniZen — o rebrand do Anikku Mod que tem guia própria nesta coleção. Há um ecossistema pequeno se construindo em volta do cliente da organização Komikku: cliente, canal de previews e armazéns de extensões. Isso, ainda de fraldas, é como nasce um ramo sério.

O contexto histórico, com data: o armazém oficial de anime do Aniyomi arquivou em agosto de 2024 e o comunitário (Kohi-den) em maio de 2026 — que esses repos novos existam é a resposta do ecossistema a esses vazios. Os índices de instalação não se colam aqui: leem-se no README de cada armazém, no dia do uso.

## ⚖️ Anime puro ou anime+mangá: como decidir

```
Só anime e NUNCA toca no mangá?
   → Animiru ou Anikku: o app pesa menos,
     a interface não estorba com a metade
     que você não usa.

Anime e mangá, com humores distintos?
   → O ramo anterior (Aniyomi/Animetail/Tadami):
     as duas coisas em uma mão.

Anime na TV?
   → AnimiruTv existe — com o aviso de sempre:
     fork pequeno, verifique no dia em que
     for testar.

Já usa Komikku para mangá?
   → O Anikku tem a lógica da mesma equipe:
     a família se sente na interface.
```

As duas fichas de hoje passam pelas portas da casa: uso real (comunidades ativas), unicidade (anime puro é o nicho delas), maturidade (releases desta semana, estrutura de org em um caso) e propósito próprio (tirar o mangá É o propósito — não é cosmético).

## ❓ Perguntas frequentes

**O Animiru é «Aniyomi sem mangá» e ponto?**
A base é Aniyomi e a diferença é essa — mas soma detalhes próprios (o set de trackers inclui Simkl e Hikka, o player mpv vai afinado a cada versão). Duas versões em uma manhã dizem que o «e ponto» está sendo trabalhado.

**Por que o Anikku vai no 0.2 se o Komikku vai no 1.14?**
São apps distintos: o mangá leva anos de vantagem. 0.2 com organização por trás é fase normal de um projeto jovem — o canal de previews e as traduções são sinais de estrutura, não de brinquedo.

**Anikku e AniZen são a mesma coisa?**
Família, não gêmeos: o AniZen se declara rebrand de «Anikku Mod» (a guia dele conta com datas). O Anikku é o original da organização. Mesma linhagem declarada, casas distintas.

**Qual extensão serve no Animiru?**
As do ecossistema Aniyomi — é herança dele — com o mapa vivo do guia anterior. Para o Anikku, os armazéns dedicados de cima. Em ambos os casos: o índice se lê na casa do armazém, não em um post.

**Têm versão para TV ou desktop?**
AnimiruTv (TV, fork pequeno). Anikku: não se conhecem variantes — a org dele se concentra no celular. O que existir amanhã, as organizações dirão.

**Qual das duas fichas vai mais rápido?**
O Animiru, sem discussão: duas releases hoje. Mas velocidade não é o critério — repo vivo é, e os dois vivem.

## 🔗 Links

- Animiru: https://github.com/Quickdesh/Animiru · registro de forks do Aniyomi: https://aniyomi.org/forks/Animiru/
- AnimiruTv: https://github.com/Znabil/AnimiruTv
- Anikku: https://github.com/komikku-app/anikku · testes: https://github.com/komikku-app/anikku-preview
- Armazéns novos: https://github.com/salmanbappi/extensions-repo · https://github.com/salmanbappi/aniyomi-extensions
- Guia cruzada: ramo Aniyomi/Animetail (Publicação 13) · AniZen (Publicação 11) desta coleção

> A Bandita informa a partir de fontes datadas. Tirar o mangá também é um propósito — e nesta semana ele foi publicado duas vezes.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Animiru ★864, extensions-repo push de HOJE. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
