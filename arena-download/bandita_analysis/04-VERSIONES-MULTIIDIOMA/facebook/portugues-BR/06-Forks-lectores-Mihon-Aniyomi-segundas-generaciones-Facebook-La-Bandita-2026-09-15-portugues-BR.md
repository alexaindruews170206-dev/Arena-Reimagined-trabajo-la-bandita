# Publicação 06 — Forks de leitores: o mapa vivo de Mihon, Aniyomi e suas segundas gerações

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 06)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── ⚖️ A regra: fork não é critério
├── 🌳 A árvore completa de hoje
├── 📱 As fichas dos vivos
├── 🧬 O que é um «fork de verdade» (e o que é um refilho)
├── 🏗️ A infraestrutura que ninguém vê
├── 📜 Licenças, dito sem escritório de advocacia
├── 🚩 Sinais de impostor
├── 🔍 Como ler um repo em dez minutos
├── 🔄 Backups e mudanças de biblioteca
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Tachiyomi — o leitor de mangá livre que marcou uma época — fechou seu núcleo em janeiro de 2024. O que ficou não é «Tachiyomi com outro nome»: é uma família de projetos distintos, com donos, ritmos e licenças próprios. Este mapa se leu HOJE, 14 de setembro, repo por repo:

```
━━ O tronco mangá ━━
Mihon              ★23.601   v0.20.4 (5-ago)    push HOJE (15-set)
TachiyomiSY        ★4.146    1.13.2 (13-jul)    push 13-set    fork
TachiyomiSYPreview ★483      host de previews   push 25-ago
Komikku            ★4.721    v1.14.1 (17-jul)   push 11-set  refilho
Neko               ★2.792    leitor MangaDex    push 14-set     especialista

━━ O ramo anime (mangá + anime) ━━
Aniyomi            ★7.683    push 14-set         ramo mãe
Anikku             ★1.032    v0.2.0 (11-set)    anime, org Komikku
Aniyomi-preview    ★641      host de previews   push 14-set
Animetail          ★579      v0.20.4.0 (5-ago)  push 7-set   fork
Tadami             ★260      v0.62 (12-set)     push 13-set  fork (viva)
```

Nenhuma estrela instala nada. Nenhum parentesco garante nada. A regra vai primeiro.

## ⚖️ A regra: fork não é critério

Que algo seja fork, variante ou rebatizado de um projeto querido não é, por si só, razão para usá-lo. As quatro portas que sim contam:

```
Uso real           alguém de carne e osso o usa
                   e pode contar como é
Unicidade          faz algo que o que você já tem
                   não cobre? «É fork de X» não é
                   uma função
Maturidade pública docs, versões assinadas, um autor
                   que responde. Último push de 2024
                   não passa nesta porta sem marca
Propósito próprio  um ícone novo não é um propósito;
                   uma mudança de motor, sim
```

Esta guia nomeia repos com URL, licença, versão e último push — lidos no dia 14 e relidos ao mudar (15-set). «O melhor» não aparece: não existe no abstrato. Existe o que cobre o que você lê, com oficina aberta.

## 🌳 A árvore completa de hoje

```
Mihon (o tronco vivo do ecossistema)
   ├── Mihon            o sucessor de fato (o maior)
   ├── TachiyomiSY      o fork clássico que segue vivo
   ├── Komikku          refilho com vida própria (repo novo)
   ├── Neko             o especialista em MangaDex
   └── (dezenas de forks sem projeto próprio:
        não se listam por serem forks)

Aniyomi (mangá + anime, da mesma linhagem)
   ├── Animetail        declara-se «Official fork»
   ├── Tadami           mangá + anime + ranobe (o mais jovem)
   └── Anikku           o anime-client da org Komikku

Kotatsu: OUTRA árvore (GPL, parsers próprios)
   → Kotatsu-Redo, Futon, Kototoro, Usagi
   → têm guia própria nesta família
```

## 📱 As fichas dos vivos

### Mihon — o tronco

https://github.com/mihonapp/mihon

★23.601 · versão 0.20.4 (5 de agosto) · push de HOJE (re-verificado 15-set) · Apache-2.0. É o leitor mangá livre maior do mapa, e o sucessor de fato de Tachiyomi. Sua comunidade de traduções empurra código a diario; suas versões saem quando saem — a de agosto é a vigente, e o push de hoje não significa APK novo.

Keiyoushi (a guia de extensões desta família) o nomeia primeiro na sua lista de apps compatíveis.

### TachiyomiSY — o vivo com o nome velho

https://github.com/jobobby04/TachiyomiSY

★4.146 · versão 1.13.2 (13 de julho) · push do dia 13-set · Apache-2.0. O fork clássico — fontes extras, ajustes de leitura — que segue aberto. E o aviso que vale sua entrada: o SY vivo é este — o nome não basta; o dono sim.

Seu projeto mãe mantém além disso um host de builds de prova: TachiyomiSYPreview (★483) — versões experimentais para curiosos, não a via do dia a dia.

### Komikku — o refilho com oficina própria

https://github.com/komikku-app/komikku

★4.721 · versão 1.14.1 (17 de julho) · push do dia 11-set · Apache-2.0. A API do GitHub não o declara fork (é um repo novo); seu README conta a linhagem. São os «refilhos»: projetos que herdam o código e nascem com casa própria. Sua organização também mantém Anikku (abaixo).

### Neko — o especialista

https://github.com/nekomangaorg/Neko

★2.792 · push de ontem (14-set) · «Unofficial MangaDex Reader for Android 8+». Um leitor inteiro dedicado a uma só fonte: MangaDex. É da linhagem dos forks de Tachiyomi, mas seu propósito próprio é claríssimo: fazer uma coisa bem. Para quem vive em MangaDex, é ficha à parte; para o resto, é um martelo com forma de chave de fenda.

### Aniyomi e seus herdeiros

https://github.com/aniyomiorg/aniyomi

★7.683 · push do dia 14-set · Apache-2.0. O ramo mãe do mangá+anime. Quase um ano sem versão nova mas com código se movendo neste mês: ramo maduro, não cadáver. Seu host de previews: aniyomiorg/aniyomi-preview (★641).

**Anikku** — https://github.com/komikku-app/anikku — ★1.032 · versão 0.2.0 publicada em 11 de setembro · release r8932 à vista HOJE 15-set · «anime watcher» da organização Komikku. A mais ativa do ramo anime neste mês.

**Animetail** — https://github.com/Animetailapp/Animetail — ★579 · v0.20.4.0 · push do dia 7-set · Apache-2.0. Declara-se «Official fork of Aniyomi» na sua descrição. A etiqueta ele a põe — não se viu selo de aniyomiorg ratificando; diz-se tal qual.

**Tadami** — https://github.com/andarcanum/Tadami-Aniyomi-fork — ★260 · versão 0.62 (12 de setembro) · push do dia 13-set · Apache-2.0. **Ratificação (15-set, noite): VIVA — ★260, push do dia 13-set; o acta da tarde se equivocou de casa (detalhe na Publicação 13).** A mais jovem do ramo: três versões em um mês (0.60 → 0.62), mangá + anime + romances leves (ranobe). Dos forks declarados, o que mais rápido evolui.

## 🈁 A camada de imersão (guia própria na peça 17)

O mapa de hoje estreia território: dois projetos vivos da camada japonesa do ecossistema. **Chimahon** (★198, GPL-3.0, v2.4.2 de HOJE 15-set) é um fork de Mihon para estudar lendo: dicionário nativo Yomitan, mangá Mokuro, romances EPUB e mineração instantânea para Anki. **Yomi Reader** (★10, Apache-2.0, v0.1.7 do dia 6-set) é o triplo jovem — anime, mangá e romance — compatível com extensões Tadami/Aniyomi. As fichas completas, com Hoshi Reader, Yomikai e o cliente Komga «Koharia», vivem na peça 17.

## 🧬 O que é um «fork de verdade» (e o que é um refilho)

O grafo do GitHub e a realidade nem sempre coincidem:

```
Fork declarado    a API o diz: campo fork = true,
                  com pai visível. Animetail, Tadami. Não se discute.

Refilho           repo NOVO que herda o código e declara
                  a linhagem no seu README. Mihon, Komikku,
                  Anikku. O grafo diz «não é fork»;
                  o README diz de onde vem. Ambos
                  são verdade: por isso se leem os dois.

Host de builds    não é um app: é um aparelho de lançamento
                  de versões de prova do projeto mãe.
                  SYPreview, aniyomi-preview.

Fork de fork      o que monta o contraexemplo: cópia de
                  uma cópia sem oficina própria. Costuma morrer
                  sem anunciar.
```

Quando alguém te recomendar «um fork», a pergunta útil não é de quem é filho? mas sim quem empurra código esta semana?

## 🏗️ A infraestrutura que ninguém vê

Duas peças do ecossistema não são leitores mas sustentam todos:

**SyncYomi** — https://github.com/syncyomi/syncyomi — ★710, push de ontem (14-set) · v1.5.4 (10-set). Sincronização de bibliotecas entre dispositivos e entre forks da linhagem Tachiyomi: seu progresso te segue se você troca de leitor da família. Um servidor leve e o cliente no telefone.

**Suwayomi** — o servidor de desktop do ecossistema (sua biblioteca rodando no PC, lida desde o navegador). Sua extensão se revisou na guia de extensões desta família; o projeto vive com atividade deste mês.

Nomeá-los aqui é evitar o erro clássico: confundir o app com a camada que o acompanha.

## 📜 Licenças, dito sem escritório de advocacia

O que a página de cada repo declarou no dia da verificação (14-set):

- **Apache-2.0** — Mihon, TachiyomiSY, Komikku, Aniyomi, Animetail, Tadami. Em termos gerais: usar, modificar e redistribuir conservando os avisos e a nota de mudanças.
- **GPL-3.0** — a árvore Kotatsu (Kotatsu-Redo, Futon, Usagi, Kototoro na sua licença declarada). Quem redistribui modificações, as distribui com a mesma licença.

Isto não é assessoria legal: é o campo de licença de cada página, lido hoje. Se alguém vai redistribuir um APK com modificações, que abra o texto completo da licença nesse dia. E um aviso que vale ouro: um APK «SY mod premium» numa loja de mods NÃO herda a confiança de Apache-2.0 do repo — herda a da loja.

## 🚩 Sinais de impostor

- Estrelas altas, último commit de 2024, README que promete «active development».
- Mesmo nome, outro dono — e os impostores de SEO desta semana (títulos de anúncio, estrelas clônicas).
- APK no Telegram «mais atualizado que o GitHub». O atualizado vive em Releases, com tag e data.
- «Nightly» sem CI, sem tag, sem registro de compilação.
- Fork de um projeto arquivado que não declara seu parentesco.
- Pede para colar um índice de extensões na primeira tela.

Nenhum sinal sozinho basta. Vários juntos, para.

## 🔍 Como ler um repo em dez minutos

```
1. Abre o HTML do repo, não um recorte de um grupo.
2. Diz Archived? Os mortos se leem igual de rápido.
3. Licença: o campo da página (ou o arquivo LICENSE).
4. Releases: tag e data da última versão.
   O push de hoje não é uma versão nova.
5. pushed_at ≠ release: um repo pode empurrar
   traduções o mês todo sem tirar APK.
6. É fork? O campo fork da página/da API o diz;
   se é refilho, o README o conta.
7. O autor responde issues? Olhe em dois fios ao acaso
   antes de confiar sua biblioteca.
```

## 🔄 Backups e mudanças de biblioteca

O que se pode dizer sem receitar nada:

- Cada leitor da família tem seu formato de respaldo; os formatos se parecem, não se garante que sejam iguais entre versões nem entre primos.
- Um respaldo de 2024 não está verificado contra a versão de agosto de 2026 — de nenhum leitor.
- «Exporta e pronto» é uma promessa de publicidade, não de engenharia: prove SEMPRE em cópia, nunca sobre sua única biblioteca.
- Se seu progresso te importa, SyncYomi (acima) existe para isso — e também respalda o respaldar: exportação manual periódica.
- O episódio de respaldos de Kototoro (série 1.4–1.7) está documentado na sua própria guia; vale como lembrança de que as migrações grandes se ensaiam no vazio.

## ❓ Perguntas frequentes

**Qual instalo?**
O que você usar e verificar. Mangá em geral: Mihon é o tronco com mais comunidade. Estilo clássico SY com extras: TachiyomiSY de jobobby04. MangaDex exclusivamente: Neko. Anime além do mangá: Aniyomi ou seus herdeiros (Anikku é a que mais se moveu este mês). Nenhuma recomendação substitui abrir o release no dia em que instala.

**Mihon é Tachiyomi?**
Não. Tachiyomi fechou. Mihon é outro repo, vivo hoje, que herdou o modelo.

**Komikku ou TachiyomiSY?**
Dois vivos com estilo distinto. Hoje Komikku tem mais estrelas (4.721 vs 4.146); SY empurrou no dia 13-set e Komikku no 11 — constâncias do dia 14, ambos vivos a 15. Nenhum número escolhe por você.

**Anikku é AniZen?**
Não — mas é família. AniZen declara-se rebrand de «Anikku Mod» (tem guia própria nesta família). Anikku é o app da organização Komikku, com versão 0.2.0 do dia 11 de setembro. Parentela declarada, repos distintos.

**Neko serve para tudo?**
Para MangaDex, maravilhosamente. Para o resto do universo mangá, use um leitor geral.

**Os hosts de «preview» são para instalar?**
São para provar e reportar. Para o dia a dia, a versão estável do repo mãe.

**E os 200 forks que você não listou?**
Ser fork não pontua. Os que têm projeto próprio estão acima; os que não têm, são cópias com relógio.

**Discord?**
Esta família não tem canal de envio por Discord. Suas guias vivem aqui.

## 🔗 Links

- Mihon: https://github.com/mihonapp/mihon
- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY · previews: https://github.com/jobobby04/TachiyomiSYPreview
- Komikku: https://github.com/komikku-app/komikku · Anikku: https://github.com/komikku-app/anikku
- Neko: https://github.com/nekomangaorg/Neko
- Aniyomi: https://github.com/aniyomiorg/aniyomi · previews: https://github.com/aniyomiorg/aniyomi-preview
- Animetail: https://github.com/Animetailapp/Animetail · Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- SyncYomi: https://github.com/syncyomi/syncyomi
- Extensões do ecossistema: guia 04 desta família · Árvore Kotatsu: guia 07

> A Bandita informa a partir de fontes datadas. Um fork não é uma razão. O repo vivo sim. E o dono, mais.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: 8 fichas re-contadas (Mihon ★23.601, Komikku ★4.721, SY ★4.146, Neko ★2.792, Anikku ★1.032 + r8932) e ratificação Tadami (viva). O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
