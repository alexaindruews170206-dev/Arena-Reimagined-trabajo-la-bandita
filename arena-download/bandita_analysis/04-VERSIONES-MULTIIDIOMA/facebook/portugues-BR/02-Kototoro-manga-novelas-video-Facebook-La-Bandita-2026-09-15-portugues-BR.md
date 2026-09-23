# Publicação 02 — Kototoro: mangá, romances e vídeo em uma só biblioteca — v2.1.3 saiu hoje (re-verificada 15-set)

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 02)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── ℹ️ O que é Kototoro
├── 🧭 Estado do projeto (verificado hoje)
├── 📦 A versão de hoje: v2.1.3
├── 🏗️ Como está construído
├── 🔌 Fontes e extensões: o que se conecta
├── 📖 Romances e leitura por JSON
├── 🌳 A vizinhança: Mihon, Aniyomi, Komikku e Tadami
├── ♿ Conforto de leitura e acessibilidade
├── 🛠️ Solução de problemas
├── 🔒 Segurança e cadeia de suprimento
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Kototoro é um aplicativo Android de código aberto que reúne três bibliotecas em uma: mangá, romances e vídeo. Histórico, favoritos e sincronização vivem em um mesmo fluxo, e ainda traz tradução por OCR no próprio telefone, com modelos baixáveis.

A razão desta edição: a versão **v2.1.3** saiu HOJE mesmo, 15 de setembro — um dia depois da 2.1.2 — e já são quatro em cinco dias. Re-verificado na manhã do dia 15: o projeto amanheceu com release nova. O projeto se move a ritmo quase diário, então esta guia traz os números de hoje e te ensina o único relógio que manda: sua página de versões.

A ideia em uma imagem: uma estante de três gavetas onde antes você tinha três móveis separados. Unificar economiza saltos — e multiplica dependências. Esta guia olha o que junta e o que te pede em troca.

## ℹ️ O que é Kototoro

https://github.com/Kototoro-app/Kototoro

Kototoro vem da linhagem dos leitores tipo «fonte»: o aplicativo não traz conteúdo dentro, mas fala com fontes que o usuário adiciona. Sobre essa base, soma duas coisas que o distinguem: os romances (leitura longa por JSON, ao estilo dos leitores chineses de fontes) e o vídeo, no mesmo app.

```
Kototoro em uma caixa
Repositório:  github.com/Kototoro-app/Kototoro
Licença:      Apache-2.0
Pacote:       org.skepsun.kototoro
Android:      8.0 em diante (builds recentes)
Docs:         kototoro-app.github.io/Kototoro
Origem:       linhagem skepsun (kototoro-parsers)
Estrelas:     569 · atividade: hoje mesmo
```

Seu site de documentação está vivo e foi lido hoje: descreve o leitor tudo-em-um (mangá, romances, vídeo, histórico, favoritos e sincronização), a tradução local por OCR com download de modelos, os fluxos de sincronização e a referência de integração de fontes.

## 🧭 Estado do projeto (verificado hoje)

A API do repositório, aberta no dia 14 e reaberta HOJE, 15 de setembro (re-verificação de mudança):

```
Estrelas:         569
Último push:      14-set · release de HOJE (15-set): v2.1.3
Ramo de trabalho: devel (no corte do dia 13-set: 8 ramos,
                  196 tags, ~6.950 commits)
Versões:          v2.1.3 (HOJE, 15-set) · v2.1.2 (14-set) · v2.1.1 (13-set) · v2.1.0 (11-set)
Nightly:          repo Kototoro-Nightly, build N20260914 (14-set)
```

Quatro versões em cinco dias. O Nightly — versão de provas diária — também está vivo, com build do dia 14-set (última constada a HOJE). O que isso significa para você? Que qualquer número desta guia (ou de outra) envelhece rápido: a única referência de versão vigente é a página de versões do projeto, aberta no dia em que instalar.

## 📦 A versão de hoje: v2.1.3

Publicada HOJE, 15 de setembro. Seus pacotes, segundo a API (nenhum foi baixado para esta guia):

```
arm64-v8a      125.446.780 bytes    119 downloads ao meio-dia
armeabi-v7a    117.554.684 bytes      5
universal      312.997.668 bytes     14
x86            140.010.036 bytes      1
x86_64         147.078.128 bytes      2
```

Para quase todos os telefones modernos o arquivo correto é o arm64-v8a. O universal pesa mais do que o dobro porque traz tudo — usa-se em casos especiais.

As notas da versão (lidas hoje) trazem mudança concreta:

- Personalização do fundo de capa (artwork).
- Distância de rolagem por tecla de volume na leitura webtoon.
- Gestão e busca melhorada de categorias nos favoritos.
- Ajustes do leitor em telas largas e recuperação da rolagem de margens ao retomar.

O que uma versão assim NÃO prova: que episódios antigos de respaldos (a série 1.4–1.7) estejam fechados. Se você vem com uma biblioteca grande, a regra não muda: respaldo manual e prova no vazio antes de migrar qualquer coisa.

**Caches e espelhos vão com atraso.** A v2.1.3 saiu há horas: se uma página te mostra versões de julho ou a série 1.x, não é fraude — é atraso. A única referência viva é Releases.

## 🏗️ Como está construído

Kototoro herda a arquitetura da sua linhagem: o aplicativo em Kotlin consumia uma biblioteca de parsers própria — hoje independente — chamada kototoro-parsers (github.com/skepsun/kototoro-parsers, versão 1.8, com atividade do dia 10-set). Essa separação app/parsers é o padrão do ecossistema: a casa (app) e as ruas (fontes) se mantêm por separado.

Dentro do app, cada aba (Mangá / Romances / Vídeo) fala com seu tipo de fonte:

- Mangá: fontes tipo leitor (extensões compatíveis com o ecossistema Mihon).
- Romances: fontes JSON ao estilo Legado — livros de regras que dizem onde está cada coisa.
- Vídeo: fontes de streaming por JSON, incluídos perfis tipo TVBox.

Essa mistura é sua promessa e seu risco: três tipos de fonte, três tipos de falha possível. A seção de solução de problemas abaixo existe por isso.

## 🔌 Fontes e extensões: o que se conecta

As extensões de mangá do Kototoro são compatíveis com o formato do ecossistema Mihon. Os armazéns desse ecossistema, com seu estado verificado hoje:

```
Keiyoushi          ★14.980  push 14-set      o hub principal
   https://github.com/keiyoushi/extensions
   (código: keiyoushi/extensions-source, ★4.678, vivo a 15-set)
Yūzōnō anime       ★432     push 13-set
   https://github.com/yuzono/anime-extensions
manga-repo         ★445     push 14-set      para Komikku/Mihon
   https://github.com/cuong-tran/manga-repo
Copymanga (CN)     ★2.753   v1.4.85 (8-set)
   https://github.com/LittleSurvival/copymanga-copy20
```

A regra desta família de guias sobre armazéns: nomeia-se o projeto e sua página oficial; a receita de instalação (o índice que se cola no app) cada um lê no README do projeto, no dia em que for usar. Não se copia aqui.

## 📖 Romances e leitura por JSON

Aqui Kototoro fala o idioma dos leitores chineses de fontes:

**Legado 3.0** — github.com/gedoor/legado — ★47.074, o gigante do modelo «livro de fontes»: cada fonte é um JSON que diz como buscar, onde está o texto e como paginar.

**Yuedu (阅读)** — github.com/XIU2/Yuedu — ★12.268, coleção comunitária de fontes de leitura.

Kototoro importa esses fluxos JSON e lhes soma sua camada de tradução: OCR sobre a imagem, com modelos baixáveis que rodam no telefone, ou via API se preferir um serviço externo. Para o vídeo, importa ainda perfis estilo TVBox — listas JSON que apontam a mídias, com distintos níveis de complexidade (links diretos, listas de reprodução, CMS simples, e perfis que dependem de JavaScript ou componentes remotos, nessa ordem de prova).

## 🌳 A vizinhança: Mihon, Aniyomi, Komikku e Tadami

Kototoro não está sozinho. Os leitores do ecossistema livre, com seus números de hoje:

```
Mihon        ★23.601  v0.20.4 (5-ago)   push HOJE (15-set)      mangá
Aniyomi      ★7.683   push 14-set                      mangá+anime
Komikku      ★4.721   v1.14.1 (17-jul)  push 11-set   mangá
Tadami       ★260     v0.62 (12-set)    push 13-set · viva     mangá+anime+ranobe
Kototoro     ★569     v2.1.3 (HOJE)     push HOJE     mangá+romances+vídeo
```

Mihon é o tronco da árvore mangá (o sucessor de fato de Tachiyomi, fechado em 2024). Aniyomi e Tadami somam anime. Komikku é o fork com vida própria. Kototoro é o ramo que quis tudo junto. Nenhum é «o melhor» no abstrato: o bom é o que cobre o que você lê, com repo vivo.

E atenção com a tentação de misturar: as extensões de uma árvore não servem na outra. Kotatsu, Usagi e seus parentes usam parsers próprios (outra família de guias cobre essa árvore).

## ♿ Conforto de leitura e acessibilidade

O que o app traz de fábrica para o olho e a mão:

- Leitores por modo: página, contínuo e webtoon, com ajuste de rolagem (agora também por volume, segundo a v2.1.2 do dia 14-set).
- OCR de tradução em dois níveis (básico e avançado) com modelos locais baixáveis — útil para mangá sem tradução oficial.
- Histórico, favoritos e categorias unificados (a v2.1.2 do dia 14-set melhorou justamente a gestão de categorias).
- Sincronização do próprio fluxo de leitura entre sessões.

O conselho de sempre para a vista: brilho alto em páginas de margens brancas, modo noite para webtoon, e baixar antes de ler em viagem — os três leitores do ecossistema permitem.

## 🛠️ Solução de problemas

**As fontes não aparecem.**
Revise em ordem: a extensão está instalada? o repositório foi agregado e sincronizado? você está na aba correta (Mangá / Romances / Vídeo)? atualizou a tela de extensões? A cura clássica: reinstalar a extensão e atualizar.

**Um JSON de romances não importa.**
Primeiro: é uma fonte Legado ou um perfil TVBox? São formatos distintos e se importam por menus distintos. Segundo: o JSON é válido? a URL responde? Terceiro: prove primeiro importando de arquivo local — elimina metade das variáveis.

**Um perfil TVBox importa mas não carrega.**
A escada de prova, do simples ao complexo: mídias diretas → listas de reprodução → CMS simples → perfis que dependem de JavaScript → perfis com componentes remotos. Um JSON pode importar perfeito e ainda assim falhar porque uma dependência externa mudou ou morreu. Isso não é culpa do app.

**A tradução não arranca.**
Lista curta: modo local ou só-API segundo o que queira usar; idiomas origem/destino corretos; nível de OCR (básico/avançado); modelos efetivamente baixados; e se usa API, endpoint, chave e modelo bem escritos. O 80% dos casos é um modelo que nunca foi baixado.

**O app consome espaço.**
É grande por design: parsers de três mídias + modelos de OCR. Se o telefone é justo, comece sem baixar modelos avançados e sem modo universal.

## 🔒 Segurança e cadeia de suprimento

O que o projeto declara: seus desenvolvedores não têm afiliação com provedores de conteúdo nem governam repositórios de extensões — as fontes o usuário põe. O app é um instrumento; o conteúdo é sua decisão e sua responsabilidade legal.

No corte da semana passada, o repo não publicava política de segurança nem código de conduta (sim guia de contribuição e licença). Não implica insegurança — mas num aplicativo que carrega runtimes e fontes de terceiros, é uma sinal a vigiar. Builds concretos distribuídos por lojas alternativas passaram escaneios (ClamAV, APKiD, Quark-Engine) sem ameaças: isso vale para esse arquivo exato, não para a cadeia completa.

A regra da casa: não confie numa fonte só porque está numa lista da internet. Repo, commit, etiqueta e firma se olham antes de instalar. E as estrelas não instalam nada.

## ❓ Perguntas frequentes

**Qual é a versão boa hoje?**
A que disser Releases no dia em que instalar — hoje é a v2.1.2, publicada nesta mesma manhã. Amanhã pode ser outra; três releases em quatro dias dizem tudo.

**Posso ter mangá, romances e vídeo no mesmo app?**
Sim, é seu ponto. O preço: três tipos de fonte com três tipos de falha. Respaldo por separado e paciência com a escada de diagnóstico.

**É compatível com as extensões de Mihon?**
O formato de extensões de mangá, sim. As de anime/romances têm seu próprio caminho (JSON). O que não: as fontes de Kotatsu/Usagi são outra árvore, não entram.

**Venho da série 1.x, como migro?**
Com respaldo manual e prova no vazio. O episódio de respaldos 1.4–1.7 está documentado na comunidade; que a série 2.x vá rápida não prova por si só que esse capítulo esteja fechado.

**A tradução OCR precisa de internet?**
O modo local não: roda no telefone com modelos baixáveis. O modo API sim, e depende do serviço que você configurar.

**E TVBox, isso o que é?**
Listas JSON que apontam a mídias de vídeo. Importar é fácil; que carreguem depende de que as coisas a que apontam sigam vivas. Comece sempre pelo simples da escada.

**Quanto pesa?**
O pacote arm64 da v2.1.2 ronda os 125 MB, e o universal passa de 300 MB. A isso some modelos de OCR se os baixar.

**As 569 estrelas significam algo?**
Comunidade pequena mas em pleno crescimento, com um ritmo de desenvolvimento que poucos apps do mapa igualam hoje. As estrelas não instalam: medem fama, não qualidade.

## 🔗 Links

- Repositório: https://github.com/Kototoro-app/Kototoro
- Versões: https://github.com/Kototoro-app/Kototoro/releases
- Nightly: https://github.com/Kototoro-app/Kototoro-Nightly
- Documentação: https://kototoro-app.github.io/Kototoro/
- Parsers da origem: https://github.com/skepsun/kototoro-parsers
- Keiyoushi: https://github.com/keiyoushi/extensions · https://keiyoushi.github.io
- Yūzōnō anime: https://github.com/yuzono/anime-extensions
- manga-repo: https://github.com/cuong-tran/manga-repo
- Copymanga: https://github.com/LittleSurvival/copymanga-copy20
- Legado: https://github.com/gedoor/legado · Yuedu: https://github.com/XIU2/Yuedu
- Mihon: https://github.com/mihonapp/mihon · Aniyomi: https://github.com/aniyomiorg/aniyomi
- Komikku: https://github.com/komikku-app/komikku · Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork

> A Bandita informa a partir de fontes datadas. A estante é livre; o que você põe nela, também é sua decisão.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Kototoro re-verificado (v2.1.3 de HOJE), Mihon ★23.601, Keiyoushi ★14.980, Yūzōnō ★432, manga-repo ★445. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.

**Nota da verificação final (15-set, noite):** a documentação própria (kototoro-app.github.io/Kototoro) devolve 404 nesta hora, constado ao vivo; a casa GitHub segue viva (★569, v2.1.3 de HOJE). O site pode estar em mudança; o link se reabre no dia em que for usado.
