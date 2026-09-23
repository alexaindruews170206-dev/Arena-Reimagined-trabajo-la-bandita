# Publicação 04 — Extensões das três árvores: hubs vivos e a camada de impostores

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 04)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🧩 O que é uma extensão (as três camadas)
├── 📗 Keiyoushi: o hub principal
├── 📘 Yūzōnō: anime e a prateleira «cursed»
├── 📙 Os demais armazéns vivos
├── 🧬 A convenção KeiSource 1.6 (e o PR que a salvou)
├── 🗂️ Miyomi: o diretório de tudo isto
├── 🎭 A camada de impostores
├── 🧭 Como ler um armazém sem engolir nada
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

As extensões são a camada que conecta um leitor livre às fontes. Não vivem dentro do app: vivem em armazéns com dono, e o estado de cada armazém muda semana a semana. Esta guia revisou hoje — 14 de setembro — todos os armazéns vivos do ecossistema, os que morreram com data, a convenção técnica que mantém tudo funcionando, e uma camada de repos impostores que apareceu esta semana.

O estado da manhã:

```
VIVOS (todos com atividade recente)
Keiyoushi extensions        ★14.980   push 14-set     o principal
Keiyoushi extensions-source ★4.678    vivo a 15-set     o código
Yūzōnō anime                ★432      push 13-set
Yūzōnō cursed               ★185      push 9-set
cuong-tran/manga-repo       ★445      push 14-set
mojuru/cursed-manga-repo    ★160      push 3-ago
Suwayomi/tachiyomi-extension ★327     push 12-set  (para servidor)
Copymanga (comunidade CN)   ★2.753    v1.4.85
ZGQ-inc/source (CN)         ★1.268    megacoleção

tachiyomiorg/extensions       ★546    jan-2024
stevenyomi/copymanga        ★1.918    fev-2024
```

## 🧩 O que é uma extensão (as três camadas)

```
O app          o leitor (Mihon, Komikku, Tadami...)
O armazém      o lugar onde vivem as extensões
               (esta guia)
O índice       a receita que o app usa para ler
               o armazém — um arquivo de instalação
```

A regra desta família de guias sobre a terceira camada: o índice não se cola. Não porque seja segredo — está no README de cada projeto — mas porque colar receitas de instalação num post é exatamente o gesto que converte uma guia numa isca. Quem quiser o índice, que o leia na casa do projeto, no dia em que for usar.

## 📗 Keiyoushi: o hub principal

https://github.com/keiyoushi/extensions
Código: https://github.com/keiyoushi/extensions-source
Site: https://keiyoushi.github.io

O armazém de referência do ecossistema Mihon: mais de mil fontes, bot que atualiza o índice a diario (os «Repository Update» do dia 12, 13 e 14 de setembro se veem no seu histórico), e uma comunidade de tradutores que empurra o código cada dia.

Seu site, aberto hoje, traz o aviso que resolve meia dúvida do mundo: se sua lista de extensões sai vazia, ou todas figuram «obsoletas», com a mensagem «Outdated app» — seu aplicativo já não é compatível com o armazém. Suportam Mihon, TachiyomiSY e Komikku. A solução não é buscar um espelho: é atualizar o app desde seu repo.

Um detalhe de transparência: o armazém de binários não declara licença na sua página (o código sim: Apache-2.0). Diz-se tal qual — sem licença visível, não inventada.

## 📘 Yūzōnō: anime e a prateleira «cursed»

Anime: https://github.com/yuzono/anime-extensions
Código sucessor: https://github.com/yuzono/kohi-den
Site: https://yuzono.github.io

O canal vivo de referência para extensões de anime na árvore Tachiyomi — e junto a ele, o código da casa Kohi-den continua vivo na família Yūzōnō (verificado no dia 14-set). E a regra que manda nesta família: o mapa se anota com o vivo — cada link se reabre no dia em que se usa.

Terceira peça que poucos nomeiam: yuzono/cursed-manga-extensions — a prateleira de conteúdo adulto (NSFW), com atividade do dia 9 de setembro. Nomeia-se porque existe e se atualiza; não se cola seu índice nem se recomenda seu conteúdo. O que cada um lê é tema dele e da sua jurisdição.

## 📙 Os demais armazéns vivos

**cuong-tran/manga-repo** — ★445, push do dia 14-set. Extensões para Komikku/Mihon e forks. Dos armazéns independentes, o mais ativo.

**mojuru/cursed-manga-repo** — ★160, push do dia 3 de agosto. A segunda prateleira «cursed» do ecossistema. Mesmo tratamento: nome sim, índice não.

**Copymanga-copy20** (LittleSurvival) — ★2.753, versão 1.4.85 do dia 8 de setembro e «vomic» 1.4.4 do dia 4-set. A comunidade chinesa de fontes para Mihon/Tachiyomi: seu README enlaza seus grupos de comunidade. Fontes centradas em copymanga e recursos chineses.

**ZGQ-inc/source** — ★1.268. Megacoleção chinesa que junta livros, imagens, regras e até fontes de streaming. Nomeia-se como mapa do ecossistema chinês; o que há dentro não se receita.

**Suwayomi/tachiyomi-extension** — ★327, push do dia 12 de setembro. Caso à parte: não é para o telefone, é a extensão para Suwayomi — o servidor de desktop do ecossistema Tachiyomi (sua biblioteca rodando no PC, lida desde o navegador). Mais uma camada: servidor.

**uchiyomi** — ★37, MPL-2.0, e duas versões publicadas no dia 14-set (v0.32.0 e v0.33.0). O recém-chegado desta camada: um leitor self-hosted que roda como PWA no navegador — webtoon-first, pensado para telas OLED — e que come as MESMAS extensões de Mihon/Tachiyomi. Sua biblioteca no seu servidor, lida de qualquer navegador, com o ecossistema de extensões inteiro atrás. A camada servidor acaba de estrear segunda casa — seguimento aberto.

## 🧬 A convenção KeiSource 1.6 (e o PR que a salvou)

As extensões não são arquivos soltos: seguem uma convenção técnica do ecossistema. A vigente se chama KeiSource, versão de biblioteca 1.6. O documento de contribuição do ecossistema (aberto hoje, 1.813 linhas) o diz claro: as fontes novas estendem KeiSource com libVersion 1.6, e a base antiga (HttpSource, 1.4) fica legado.

Por que importa para quem só lê? Porque quando um app «não vê» as extensões novas, quase sempre é isto: o app é velho para a convenção. É a outra cara do aviso «Outdated app» de Keiyoushi.

O caso que confirmou a transição: o PR #448 do Animetail — «resolve 1.6+ extension loading» — abriu hoje e figura fundido. Os leitores que não migram a tempo ficam fora dos armazéns que adotam a convenção.

## 🗂️ Miyomi: o diretório de tudo isto

https://miyomi.app
Código do site: https://github.com/miyomiorg/Miyomi

Um diretório comunitário que cataloga apps, armazéns de extensões e guias do ecossistema inteiro — a capa se lê hoje, e seu front-end é uma aplicação web viva (seus contos internos não puderam ser re-contados hoje por essa mesma razão: o catálogo vive na sessão do navegador, não num JSON público).

Seu repo: ★189, licença AGPL-3.0, com seu próprio código aberto. O projeto declara que não hospeda conteúdo e que não garante segurança nem legalidade de terceiros — um índice de índices, com a honestidade de quem sabe que catalogar não é auditar.

«Aprovado» no Miyomi significa «está no seu catálogo hoje». Não significa aval de ninguém.

## 🎭 A camada de impostores

A busca desta semana detectou repos com o mesmo traje: estrelas idênticas entre si (115–120 em vários casos), atividade do mesmo dia, e títulos de anúncio classificado — «Best Manga Reader App 2026», «Top Komikku Open Source Alternative», «Ultimate Multilanguage Hub for Usagi».

```
O traje do impostor
★ idênticas entre si (115–120 em vários casos)
Título de propaganda, não de projeto
Sem histórico próprio: nasceram no dia 13-set
Nome de projeto conhecido + palavra de venda
```

Não são armazéns nem forks nem fontes: são ímãs de cliques — e, razoavelmente, suspeita-se, de instalações envenenadas. A regra prática que não falha: se o título soa a anúncio e as estrelas não batem com a história do projeto, não se abre, não se enlaza, não se instala.

## 🧭 Como ler um armazém sem engolir nada

```
1. Quem o mantém?
   Um bot de uma org com histórico > uma conta
   sem cara que nasceu neste mês.

2. Desde quando empurra?
   Histórico de commits de meses/anos > atividade
   de uma só semana.

3. O código está à vista?
   extensions-source publicado > só binários.

4. Seu site avisa o que não sabe?
   Keiyoushi avisa quais apps já não suporta.
   Quem confessa limites merece mais confiança
   que quem promete infinito.

5. A instalação sai da casa?
   O índice se lê no README do projeto,
   nunca num post de terceiros. Nem neste.
```

## ❓ Perguntas frequentes

**Que armazém uso com Mihon?**
Keiyoushi: o declara o seu próprio site (Mihon, TachiyomiSY, Komikku). Se sua lista sai vazia com «Outdated app», o problema é a versão do seu app.

**E para anime?**
Yūzōnō anime-extensions é o canal vivo de referência; o oficial de Aniyomi arquivou em agosto de 2024 e Kohi-den em maio de 2026.

**As prateleiras «cursed» são perigosas?**
Seu risco não está no mecanismo mas no conteúdo e na sua jurisdição. Nomeiam-se para completar o mapa; o índice de instalação não se cola nesta família de guias, para nenhum.

**As extensões de Keiyoushi servem em Usagi ou Kotatsu?**
Não: outra árvore, outro protocolo de parsers. Esses vivem nas suas próprias casas e têm guia própria.

**Um armazém «approved» no Miyomi é confiável?**
É catalogado, não auditado. A diferença é exatamente a do telefone na guia de contato: está na lista, não passou no exame.

**De quanto em quanto reviso que meu armazém siga vivo?**
Cada vez que algo deixar de se atualizar. Por isso esta guia só anota o vivo — e cada link se reabre no dia em que se usa.

**Onde reporto uma extensão quebrada?**
No repo do código da extensão (para Keiyoushi: extensions-source), com versão de app, fonte e passos. Os mantenedores respondem melhor a passos que a queixas.

## 🔗 Links

- Keiyoushi: https://github.com/keiyoushi/extensions · https://github.com/keiyoushi/extensions-source · https://keiyoushi.github.io
- Yūzōnō: https://github.com/yuzono/tachiyomi-extensions · https://github.com/yuzono/anime-extensions · https://github.com/yuzono/cursed-manga-extensions · https://yuzono.github.io
- Armazéns: https://github.com/cuong-tran/manga-repo · https://github.com/mojuru/cursed-manga-repo
- Ecossistema chinês: https://github.com/LittleSurvival/copymanga-copy20 · https://github.com/ZGQ-inc/source
- Servidor de desktop: https://github.com/Suwayomi/tachiyomi-extension
- Miyomi: https://miyomi.app · https://github.com/miyomiorg/Miyomi

> A Bandita informa a partir de fontes datadas. O mapa vai com o vivo.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: 7 armazéns re-contados a HOJE (Keiyoushi ★14.980, Yūzōnō ★432, manga-repo ★445). O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
