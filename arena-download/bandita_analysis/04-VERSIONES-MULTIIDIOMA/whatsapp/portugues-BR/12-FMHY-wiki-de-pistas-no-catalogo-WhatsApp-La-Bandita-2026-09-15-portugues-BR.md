# Publicação 12 — FMHY é uma wiki de pistas, não um catálogo: descoberta ≠ verificação

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 12)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🌐 O que é FMHY e como funciona
├── 🧩 O que sua navegação revela hoje
├── 🔒 O intersticial Base64 (o que é e o que não é)
├── 📦 O repo atrás da wiki
├── 🧭 Descoberta ≠ verificação: o funil completo
├── 🔬 Um exemplo real, de ponta a ponta
├── 📌 A correção à «grande onda» de abril
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

FMHY — «freemediaheckyeah» — apresenta-se como «a maior coleção de coisas grátis da internet». É uma wiki comunitária enorme, viva hoje, e com um papel preciso no mapa do conhecimento: **é um descobridor de primeiro nível e um verificador de nada.**

A diferença importa porque abril o demonstrou com dano: alguém esvaziou uma porção da wiki num fio de 340 mil caracteres e o vendeu como catálogo verificado. Não era. Cada pista de FMHY é um primeiro elo — abrir a casa do projeto, ler sua licença, comprovar sua versão e seu dono é o trabalho que ninguém pode fazer por você, nem esta wiki nem esta guia.

Estado de hoje, 14 de setembro: o site responde com seu post mensal de setembro ativo, sua guia de principiantes carrega, e o repo que a gera soma ★14.592 — com a particularidade de que seu código git não empurra desde maio, e a wiki não por isso está morta. Ambas as coisas, contadas abaixo.

## 🌐 O que é FMHY e como funciona

https://fmhy.net

FMHY é uma wiki mantida por sua comunidade: milhares de entradas de ferramentas, sites e recursos organizados por categorias — privacy, AI, vídeo, áudio, gaming, reading, downloading, torrenting, educational, mobile, linux-macos, non-english, misc, entre outras. Sua mecânica:

- A comunidade propõe e cura entradas continuamente.
- Um changelog registra o que mudou — e seu ritmo é visível: a wiki publica **posts mensais de novidades** (o de setembro de 2026 está em linha hoje).
- Há variante SFW (sem conteúdo adulto) para quem a prefira.
- A cultura do projeto é a de um índice: descreve, enlaza, não garante.

Seu tamanho é sua virtude e seu limite: cobre tudo, não audita nada. É a biblioteca maior do mundo no seu gênero — e como toda biblioteca grande, o valor não está em tê-la toda: está em saber usar o catálogo.

## 🧩 O que sua navegação revela hoje

A barra do site, aberta hoje, é uma lição do que a wiki pensa de si mesma:

```
📑 Changelog    o que mudou e quando
📖 Glossary     o dicionário dos seus termos
💾 Backups      como obter a wiki inteira
🌱 Ecosystem    as variantes e projetos irmãos
❓ FAQs          as perguntas do projeto
✅ SafeGuard    seu capítulo de segurança
🚀 Startpage    sua proposta de página de início
🔎 SearXNG      busca própria
😇 SFW FMHY     a versão sem adulto
🏠 Selfhosting  como se monta no seu servidor
```

Repare no que essa barra diz sem dizer: um projeto que publica seu changelog, mantém glossário, oferece backups de si mesmo e tem capítulo de segurança toma-se a sério como infraestrutura. Segue sendo um índice de pistas — mas dos organizados.

## 🔒 O intersticial Base64 (o que é e o que não é)

Ao entrar, FMHY às vezes mostra um aviso sobre links codificados em Base64. O que há atrás, sem voltas:

```
É:     uma medida de design. Alguns links da
       wiki se publicam codificados para que os
       rastreadores automáticos não os indexem.
       O próprio site oferece um decodificador em página.

Não é: um sistema de segurança, nem um rito obrigatório,
       nem uma instrução desta guia. O usuário
       decide se usa essa via; o decodificador é
       do site e roda no seu navegador.

E não é: motivo para copiar links codificados em
       um post. Aqui vão links em claro ou não vão.
```

A wiki faz sua engenharia para sobreviver aos indexadores; esta família de guias faz a sua para não colar receitas. Cada qual protege o seu.

## 📦 O repo atrás da wiki

https://github.com/fmhy/FMHY

★14.592 · último push do dia 13 de maio de 2026 · licença: sem classificar na sua página (diz-se tal qual — a wiki define sua própria política de conteúdo no seu site).

A curiosidade que ensina algo: o git leva meses quieto e a wiki está viva — re-verificado HOJE, 15-set: carrega com seu post de setembro. Como? A wiki se serve por vias próprias (sua web e seus desdobramentos) e o repo público não reflete cada movimento. A lição geral que você já viu nesta família: **git quieto ≠ projeto morto; projeto vivo ≠ tudo verificado.** Um repo é uma camada, não o projeto inteiro.

## 🧭 Descoberta ≠ verificação: o funil completo

A regra da casa cabe numa linha — encontrar não é verificar. Desdobrado, o funil que converte uma pista em algo citável:

```
1. DESCOBRIMENTO
   FMHY (ou um grupo, ou um amigo) diz:
   «este app é bom».
   ── isto vale exatamente zero como verificação.

2. ABERTURA
   Abre-se a casa do projeto — seu repo ou site —
   NESSE DIA. Não o recorte do grupo: a casa.

3. LEITURA
   Quem é o dono? Desde quando existe?
   Que licença declara? Quando foi sua última
   versão e seu último push? Está arquivado?

4. CONTRASTE
   Outras fontes independentes o nomeiam?
   Sua comunidade responde issues?
   Sua firma/checksums são públicos?

5. USO REAL
   Alguém de carne e osso o usa e pode
   contar como lhe vai? O uso real é a última
   porta — e a única que ninguém pode abrir por você.

6. FICHA
   Só então: uma ficha com data, numa
   guia como esta. E com data de caducidade.
```

Qualquer atalho que se salte passos — «está no FMHY, ponto», «recomendam no Telegram, ponto» — é o gesto exato que fez do fio de abril um estorvo de 340 mil caracteres.

## 🔬 Um exemplo real, de ponta a ponta

Para que o funil não fique na teoria, o percurso que esta família já fez com uma entrada real:

```
1. A wiki (e meia internet) menciona «Mihon»
   como leitor de mangá.

2. Abre-se a casa: github.com/mihonapp/mihon

3. Lê-se: 23.575 estrelas · Apache-2.0 ·
   versão 0.20.4 de agosto · push de HOJE ·
   organização mihonapp com histórico desde 2024.

4. Contrasta-se: Keiyoushi (o armazém de
   extensões) o lista primeiro entre os apps
   suportados; seus issues têm atividade; a
   comunidade do ecossistema o nomeia como o
   sucessor de fato de Tachiyomi.

5. Uso real: a gente da banda que o usa,
   com sua opinião.

6. Ficha: hoje Mihon tem guia própria dentro de
   desta família (a de forks de leitores), com sua
   data de corte.
```

Seis passos. Tudo o que faz falta para que «Mihon» passe de pista a informação. E tudo o que NÃO aconteceu no dia em que alguém colou uma wiki inteira num fio.

## 📌 A correção à «grande onda» de abril

```
O que fez abril                  O que faz esta família
Esvaziar FMHY num post           Abrir a casa de cada pista
Vender a wiki como verificação   Apresentar a wiki como descobrimento
340 mil caracteres sem dono      Fichas curtas, datadas, com casa
Índices de instalação colados    O índice se lê na casa do
                                 projeto, nunca num post
«Tudo grátis, tudo seguro»       Cada ficha com seu limite e sua data
```

A wiki não era o problema. O problema era o gesto: apresentar acumulação como verificação. Esse gesto é o que esta família de guias existe para não repetir.

## ❓ Perguntas frequentes

**Posso usar FMHY?**
Você pode lê-la: é pública e seu papel como índice é legítimo. O que esta guia não faz é mandar-te aos seus destinos nem esvaziá-la aqui. Cada clique dentro dela é um descobrimento — a verificação vai à parte, com o funil de cima.

**É mais segura que googlar?**
Não se afirma. É outra lista, curada por outra gente, com outros incentivos. Os buscadores mandam-te a anúncios pagos; as wikis, ao que a comunidade anotou. Nenhuma das duas portas verifica por você.

**Sua seção de Android substitui a guia de lojas desta família?**
Não. A guia de lojas abriu cada projeto no dia do corte; uma seção de wiki é uma lista com outra data e outro critério.

**E sua seção de música?**
Mesma resposta: a família tem guia de música com as fichas verificadas. A wiki pode apontar ao mesmo — ou a coisas que ninguém abriu ainda.

**O repo diz maio mas a wiki está viva, qual é a verdade?**
As duas: a wiki se serve por desdobramentos próprios e o repo não reflete cada mudança. Git quieto não é projeto morto — já o dizia a lição do repo.

**Base64 é pirataria?**
É codificação de texto — a mesma técnica que seu telefone usa para mandar imagens por correio. O uso que cada um lhe dê aos links é assunto dele e sua lei. Aqui não se decodifica nada para ninguém.

**Então para que serve FMHY, afinal?**
Para o que disse sua definição: o índice maior do ecossistema. Como mapa do que EXISTE, não tem rival. Como prova do que funciona e é seguro, não vale nada — e não pretende valer.

## 🔗 Links

- A wiki: https://fmhy.net
- Guia de principiantes: https://fmhy.net/beginners-guide
- Post de setembro: https://fmhy.net/posts/sept-2026
- O repo: https://github.com/fmhy/FMHY

> A Bandita informa a partir de fontes datadas. A wiki de pistas não é um catálogo — e quem descobre, ainda não verificou.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: wiki re-verificada viva a HOJE. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
