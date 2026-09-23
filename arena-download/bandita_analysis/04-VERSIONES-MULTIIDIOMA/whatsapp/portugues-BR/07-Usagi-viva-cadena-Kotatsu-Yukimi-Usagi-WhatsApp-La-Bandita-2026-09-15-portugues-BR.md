# Publicação 07 — Usagi está viva: a cadeia Kotatsu → Yukimi → Usagi, verificada

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 07)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🧬 A cadeia completa: Kotatsu → Yukimi → Usagi
├── 🏗️ O que sim se arquivou (e não foi o app)
├── 📱 Ficha: UsagiApp/Usagi
├── 🌳 Os quatro vivos da árvore Kotatsu
├── 🧩 Plugins e parsers: como come esta árvore
├── 🍴 Os forks de Usagi
├── 🎭 Os impostores da semana
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Correu esta semana que «Usagi morreu». Verificado HOJE, 14 de setembro, casa por casa: **Usagi está viva** — ★257, push do dia 14-set, release 1.0 publicada no dia 10 e página na F-Droid carregando. O que sim aconteceu: o original Kotatsu segue arquivado (desde novembro de 2025), a camada velha de plugins de Usagi foi arquivada (dois repos concretos), e a predecessora de Usagi, chamada Yukimi, sim foi descontinuada pelo seu próprio desenvolvedor. Essa história completa vai abaixo, com datas.

## 🧬 A cadeia completa: Kotatsu → Yukimi → Usagi

A árvore Kotatsu tem uma genealogia de três atos. A primeira parte está verificada no GitHub; a transição do meio vem dos reportes da comunidade (fios de novembro de 2025 e começos de 2026):

```
ATO 1 — Kotatsu
KotatsuApp/Kotatsu · ★8.855
ARQUIVADO em 4 de novembro de 2025 (confirmado no dia 14-set)
O original fecha depois da pressão legal da Kakao
Entertainment e, segundo seus próprios autores, também
pela política de verificação de desenvolvedores
que vinha aí. Última versão: 9.4.1.

ATO 2 — Yukimi (reportes da comunidade)
Os mesmos desenvolvedores anunciam uma sucessora:
Yukimi. Semanas depois, seu autor a descontinua
e retira seu site. Os fios da época a dão
por terminada — «the project ended today».
Não ficou repo vivo para verificar naquele dia: por isso
esta guia a conta como história relatada,
não como ficha.

ATO 3 — Usagi
A comunidade continua por outro caminho: Usagi,
com o mesmo espírito Kotatsu mas com uma decisão
de design chave: NÃO traz fontes integradas.
As fontes o usuário traz. Essa decisão
é, provavelmente, a razão pela qual Usagi
segue viva onde outras morreram.
```

Os reportes da época nomeavam também Kotatsu-Redo, Kototoro e Futon como os sobreviventes da árvore. Os quatro vivem — fichas abaixo, todos abertos hoje.

## 🏗️ O que sim se arquivou (e não foi o app)

A organização UsagiApp tem 16 repositórios, abertos hoje. Dois estão arquivados — e são a fonte real do rumor:

```
ARQUIVADOS (a arquitetura velha)
UsagiApp/core-parsers   «biblioteca para o repo de plugins»
UsagiApp/core-exts      «núcleo para carregar plugins externos»

VIVOS (o que os substitui)
UsagiApp/TsukiMix       o núcleo novo para ler e compilar
                        extensões e parsers
UsagiApp/plugins        plugins e exemplo para criadores
UsagiApp/syncserver     servidor de sincronização de dados
                        «para Kotatsu / Usagi»
UsagiApp/Tsuki          a biblioteca compartilhada do ecossistema
```

É o gesto de toda casa viva: demolir o andaime velho enquanto o edifício segue aberto. Quem passou pela organização e viu dois «archived» sem ler nomes, levou o rumor. Os nomes dizem outra coisa: arquivou-se a camada de plugins antiga — o app nem notou por fora.

## 📱 Ficha: UsagiApp/Usagi

https://github.com/UsagiApp/Usagi

```
Qué é:        leitor de mangá livre para Android,
              inspirado em Kotatsu, SEM fontes integradas
Licença:      GPL-3.0
Versão:       1.0 (a única estável; rc2 no dia 2-set,
              rc1 no dia 9-ago)
Estrelas:     257 · push do dia 14-set (dia da verificação; release 1.0 do dia 10-set)
Android:      5.0 em diante (badges do README)
Casa:         github.com/UsagiApp/Usagi
Canais:       GitHub, F-Droid (org.draken.usagi),
              Obtainium e OpenAPK segundo seu README
```

Sua página de F-Droid carrega hoje — o app está publicado ali, com seu pacote org.draken.usagi. O Discord e o Telegram que o README exibe não se enlazam aqui: esta família não usa nem recomenda canais de envio, e os links de comunidade o próprio projeto os tem.

Um «1.0» é um número de nascimento, não de maturidade. O app tem release, README, casa e comunidade pequena mas viva. O que não se auditou: quanto responde seu autor aos reportes — abra um par de fios de issues antes de confiar sua biblioteca, como com qualquer projeto jovem.

## 🌳 Os quatro vivos da árvore Kotatsu

### Kotatsu-Redo — o que herdou o nome

https://github.com/Kotatsu-Redo/Kotatsu-Redo

★867 · versão **9.8.3 (6 de setembro)** · GPL-3.0 · vivo. O fork comunitário que a comunidade nomeia primeiro desde que o original arquivou. Sua organização sustenta quatro repos: o app, seus parsers (kotatsu-parsers-redo), um servidor de telemetria e outro de sincronização. Leva o nome «Kotatsu» adiante com versões da série 9.8.x.

### Futon — o do motor próprio

https://github.com/AppFuton/Futon

★427 · versão **9.8.1 (16 de agosto)** · GPL-3.0 · vivo. Sua organização tem oito repos, entre eles sua própria biblioteca de parsers (AppFuton/futon-parsers, arquivada — congelada enquanto o app avança; sinal a vigiar) e até sua landing page. Curiosidade da árvore: os números de versão de Futon e Kotatsu-Redo se parecem — ambos herdaram a numeração do original.

E um aviso de desvio: existe MikuX-Dev/Futon (3 estrelas, outra coisa com o mesmo nome). A ficha válida é AppFuton.

### Kototoro — o que quis tudo junto

https://github.com/Kototoro-app/Kototoro

★569 · **v2.1.2 publicada no dia 14-set — e no dia 15 amanheceu com a v2.1.3** (Publicação 02) · Apache-2.0 na sua licença declarada. Mangá, romances e vídeo em um só app — o mais movimentado da árvore esta semana (três versões em quatro dias). Tem guia completa própria nesta família.

### Usagi — a que não traz fontes

A ficha de cima. Sua diferença de design com os outros três é sua carta de identidade: sem fontes integradas, o usuário traz as suas via plugins.

## 🧩 Plugins e parsers: como come esta árvore

A árvore Kotatsu não usa extensões tipo Mihon: usa bibliotecas de parsers e plugins compilados. As peças do dia:

**Gekkoushi/plugin** — https://github.com/Gekkoushi/plugin — os artefatos prontos para Usagi e apps com estrutura Tsuki. Seu README (reverificado hoje) diz: «Only for the Usagi App», «No updates, 1.3k sources» — mil e trezentas fontes compiladas congeladas no seu estado atual — e o plugin UMA «só para a versão 1.0». Essa última condição encaixa com a realidade de hoje: a única estável de Usagi é a 1.0.

**Gekkoushi/plugin-source** — https://github.com/Gekkoushi/plugin-source — ★90, GPL-3.0, push do dia 13-set, versão 1.2.6. Aqui se contribui e aqui se reportam as fontes quebradas.

**InvalidDavid/UMA** — https://github.com/InvalidDavid/UMA — ★69, GPL-3.0, tags do dia 12 e 13 de setembro. Instalação automática ou manual de plugins para Usagi e outros forks de Kotatsu.

**Tsuki e TsukiMix** — as bibliotecas compartilhadas da própria organização: Tsuki (a da era plugins) e TsukiMix (a evolução atual). Com syncserver, a organização cobre todo o sanduíche: app, camada de carga, parsers e sincronização.

A regra de sempre sobre downloads: os artefatos se nomeiam, não se colam. O clique de instalação o dá cada um na casa do projeto, no dia em que for usar.

## 🍴 Os forks de Usagi

A lista pública de forks mostra hoje 30 na sua primeira página, com atividade majoritariamente recente — e nenhum com projeto próprio. Um fork sem identidade é uma cópia de segurança com data: existe, não sucede. Se algum crescer, terá ficha no dia em que a merecer.

## 🎭 Os impostores da semana

A busca desta semana trouxe uma camada com o mesmo traje — estrelas infladas e idênticas (115–120 mil), nascimento no dia 13-set, títulos de classificado: «usagi-nightly», «usagi-sora-vn-sources», «komikku-scans», «translation-hub-stringsets». Nenhum é fork de Usagi nem fonte verificada: são ímãs de clique com nome emprestado.

```
O traje do impostor
★ idênticas entre vários repos
Título de anúncio, não de projeto
Sem histórico: nasceram esta semana
Pressa para que você clique «antes de que apaguem»
```

Se «o novo fork de Usagi» que te passarem termina num destes, aí é exatamente onde entra o malware. A casa de Usagi é uma e tem dono: UsagiApp.

## ❓ Perguntas frequentes

**Usagi está morta?**
Não. Push de hoje, organização ativa, F-Droid publicada. O arquivado foi a camada velha de plugins; a descontinuada foi Yukimi, sua predecessora. Cada coisa com sua data acima.

**Qual é «o novo fork» então?**
Da árvore Kotatsu vivem hoje quatro: Kotatsu-Redo, Futon, Kototoro e Usagi. Não há sucessor de Usagi porque não fez falta.

**Usagi ou Kotatsu-Redo?**
Designs distintos: Usagi sem fontes integradas (você as traz); Kotatsu-Redo hereda o modelo do original. A que cobrir seu uso, com o repo que você abrir nesse dia.

**Futon e Kotatsu-Redo são o mesmo pelos números de versão?**
Compartem herança de numeração, não repositório. Fichas separadas, casas separadas.

**Onde estão as fontes de Usagi?**
Na camada de plugins: Gekkoushi/plugin (artefatos), plugin-source (código), UMA (instalador). Sem receitas coladas aqui — a casa do projeto as explica.

**Posso pôr extensões de Mihon?**
Não: outra árvore, outro protocolo. As árvores não se enxertam por descuido.

**E se me passarem um APK «Usagi Plus»?**
Se não sai de UsagiApp ou de F-Droid (org.draken.usagi), é uma placa. Os impostores da semana são a razão pela qual essa regra existe.

**Por que F-Droid importa tanto aqui?**
Porque sua publicação passou pelo processo da loja: pacote identificado, compilação verificável. É a diferença entre «baixa deste link» e «está numa casa com processo».

## 🔗 Links

- Usagi: https://github.com/UsagiApp/Usagi · F-Droid: https://f-droid.org/en/packages/org.draken.usagi/
- Organização: https://github.com/orgs/UsagiApp/repositories
- Plugins: https://github.com/Gekkoushi/plugin · https://github.com/Gekkoushi/plugin-source · https://github.com/InvalidDavid/UMA
- Kotatsu-Redo: https://github.com/Kotatsu-Redo/Kotatsu-Redo
- Futon: https://github.com/AppFuton/Futon
- Kotatsu original (arquivado): https://github.com/KotatsuApp/Kotatsu
- Kototoro: https://github.com/Kototoro-app/Kototoro

> A Bandita informa a partir de fontes datadas. O app vive; o andaime velho, não. E o rumor, já viu, viaja mais rápido que o changelog.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Usagi ★257 viva, Kotatsu ★8.855, Redo ★867, Futon ★427, Kototoro v2.1.3. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
