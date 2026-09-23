# Publicação 15 — Ramo J2K: o avô voltou — tachiyomiJ2K, Yōkai, Rokku, Reikai e o fantasma Hayai apareceu

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 15)**

## 🗺️ Mapa deste guia

├── ⚡ Em uma página
├── 🌳 A árvore deste ramo
├── ⚡ tachiyomiJ2K — o avô despertou
├── 👻 Yōkai — o tronco em pausa ativa
├── 🪇 Rokku — o fork de manutenção prática
├── ⛩️ Reikai — mangá e novelas em uma biblioteca
├── 🐇 Hayai — o fantasma tem casa (e dá para abrir)
├── 🌲 A rede completa de forks (revisada em 14-set)
├── 🧬 Os primos menores do ramo
├── 📜 A história que explica este ramo
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

Este é o ramo da interface querido: o que nasceu de tachiyomiJ2K — o fork que redesenhou o Tachiyomi — e pariu uma família inteira. O primeiro que se tem a dizer é a notícia grande: **o tachiyomiJ2K voltou a publicar versões em agosto de 2026 depois de dois anos e meio de silêncio.** E a segunda: **o Hayai — o projeto que por meses foi um fantasma sem repo acessível — hoje tem casa pública e dá para abrir.**

```
tachiyomiJ2K  ★5.383  v1.8.1 (15-ago-2026)  o avô, de volta
Yōkai         ★1.883  v1.10.1 (4-set)     push de ontem (14-set) — o tronco
Rokku         ★51     v1.7.1 (29-ago)     o de manutenção
Reikai        ★27     v0.3.2 (4-set)      mangá + novelas unificadas
Hayai         ★41     v1.13.0 (10-abr)    o que já não é fantasma
```

Todas as fichas foram abertas e verificadas HOJE, 14 de setembro. Onde a vida pessoal dos mantenedores explica os ritmos do projeto, conta-se como eles contaram: citado, datado e sem fofoca.

## 🌳 A árvore deste ramo

```
tachiyomiJ2K (a interface redesenhada)
         │   v1.7.4 (jan-2024) → dois anos de silêncio
         │   → v1.8.0 e v1.8.1 (agosto 2026): VOLTOU
         │
         ├── Yōkai        o fork pessoal de null2264
         │     ├── Rokku    fork de Yōkai: manutenção
         │     ├── Reikai   começou em Yōkai, rebasado em Mihon
         │     └── Hayai    J2K-based, mangá + novelas
         │
         ├── yomu         J2K-based, pequeno
         └── TachiyomiDNP variante pequena, ativa em agosto
```

## ⚡ tachiyomiJ2K — o avô despertou

https://github.com/Jays2Kings/tachiyomiJ2K

```
★5.383 · Apache-2.0
v1.7.4 → janeiro de 2024 (o fechamento da era velha)
v1.8.0 → 9 de agosto de 2026 «Warning: Funny numbers ahead»
v1.8.1 → 15 de agosto de 2026 «Wait, there's more?»
```

Sua história em dois atos: foi O fork da era de ouro — o que inventou o redesign visual que meia família herdou — e depois calou durante dois anos e meio, até agosto de 2026, quando soltou duas versões em uma semana com o humor de sempre nos títulos. A comunidade o considera o pai da migração massiva de bibliotecas: foi o primeiro a mover bibliotecas completas entre leitores.

O retorno não o revive como candidato diário — duas versões não são um ritmo — mas o devolve ao mapa como história viva: o avô não morreu, estava viajando. Quem quiser a experiência J2K «pura», a casa dele está de novo aberta e com versões deste ano.

## 👻 Yōkai — o tronco em pausa ativa

https://github.com/null2264/yokai

```
★1.883 · Apache-2.0 · push de ontem (14-set)
v1.10.0 e v1.10.1 (ambas em 4 de setembro)
Suporte: extension-lib 1.6 · Android 8+ (a nota de versão dele)
```

O Yōkai é o fork pessoal de null2264: pegou a interface J2K e a sustenta sozinho. O próprio mantenedor explicou na nota da versão de setembro, com uma honestidade que vale citar: deu um passo atrás dos projetos por burnout, com a tese e o trabalho em cima, com a esperança de voltar «antes do ano novo» e revisando contribuições de vez em quando. Chamou a própria versão de «bastante pouco polida». E a mesma nota abre com um aviso em maiúsculas que convém respeitar: «BACKUP YOUR DATA» — copie seus dados antes de atualizar.

O que dizia o dado do 14: o ramo não está abandonado — o repo fez push ontem (14-set). O que também diz: é um projeto de uma pessoa com uma vida em cima, e o ritmo dele será marcado por essa vida. A lição do ramo inteiro sai daqui: mantenedores são pessoas; o burnout é real; e a honestidade de um changelog vale mais que um roadmap falso.

## 🪇 Rokku — o fork de manutenção prática

https://github.com/rokku-app/rokku

```
★51 · Apache-2.0
v1.6.1 (15-ago) · v1.7.0 (23-ago) · v1.7.1 (29-ago)
— três versões em duas semanas: cadência firme
Nasce de: Yōkai, para mantê-lo em dia com o
ecossistema de extensões e dependências
```

O Rokku existe pela razão mais prática do mundo: quando o Yōkai entrou em pausa, alguém decidiu manter a experiência viva e em dia — extensões modernas, correções de desempenho, o trabalho sujo e necessário. As notas de agosto dele se concentram em exatamente isso: ajustes de desempenho e de downloads, compatibilidade com a biblioteca de extensões moderna e cuidados herdados da interface — o trabalho que não sai em print mas mantém um app vivo.

É a ficha menor em estrelas do ramo e a que mais se mexe em consertos. O estelar mede fama; a cadência mede oficina. E há mais sinal de oficina viva: o Rokku tem canal noturno próprio (rokku-nightly) com builds quase diários — o último visto era de ontem. *(Reverificado em 15-set: o último nightly é o r7091, de 13-set — a cadência segue; a data, atualizada.)* Quando uma casa compila de noite, trabalha de dia.

## ⛩️ Reikai — mangá e novelas em uma biblioteca

https://github.com/unseensnick/Reikai · Site: https://reikai.app

```
★28 · Apache-2.0 · push de 14-set (dia da verificação) · v0.3.2 (4-set)
v0.3.2 (4-set) · v0.3.1 (9-ago) · v0.3.0 (16-jul)
Nasce de:     começou como fork de Yōkai — o grafo do
              GitHub ainda o anota assim — e o projeto
              dele conta que o código foi rebasado depois
              sobre o Mihon
Tem: versão FOSS à parte (sem relatórios de crash nem
analítica) — reikai-foss nos releases dele
```

O Reikai é a ideia mais diferenciada do ramo: UMA biblioteca onde a mesma série de mangá e de novela leve vivem juntas. As funções declaradas: agrupamento multi-fonte (dobra a mesma série de sites distintos em uma entrada), fusão manual quando os títulos não coincidem, leitura fundida com lista de capítulos unificada, sincronização de trackers compartilhada no grupo, e biblioteca de novelas de primeira linha com suporte ao leitor do LNReader.

Sua filosofia, dita pelo autor: construído primeiro para o uso diário dele — o desenvolvimento é esporádico e as funções seguem os gostos dele. Essa honestidade define o que ele é: um projeto pessoal muito bem documentado (o site completo dele confirma), não um produto com promessas de equipe.

## 🐇 Hayai — o fantasma tem casa (e dá para abrir)

https://github.com/HayaiApp/hayai

```
★41 · Apache-2.0
v1.13.0 (10 de abril de 2026) · push de 6-set
O que é: «Hayai é um leitor Android baseado no
TachiyomiJ2K com mangá e novelas leves»
(conforme a própria descrição)
```

Aqui está a surpresa deste ramo: por meses, o Hayai foi o projeto fantasma — mencionado em listas e em changelogs alheios, com o repo inacessível, impossível de avaliar. Hoje o repo abre, dá para ler, e diz o que é: baseado em J2K, mangá e novelas leves, com versão de abril e atividade do mês passado.

O que hoje é verificável: a casa existe, a licença está declarada, há release etiquetada. E o README dele —lido inteiro HOJE— precisa a receita com uma honestidade rara: arquitetura J2K declarada como base e fonte de verdade, suporte de fontes adult+ reconstruído sobre os contratos do TachiyomiSY, plugins de novelas ao estilo LNReader, e «importação defensiva» do banco de dados do Hayai velho — o arquivo da era fantasma segue cuidando de quem o usou. O que ainda não: se o desenvolvimento dele é sustentado — a última versão tem cinco meses, embora o repo tenha se mexido na semana passada. Ficha nova, seguimento aberto: ao fantasma dá-se um mês de vida pública antes de qualquer veredicto. É a regra da casa — o rumor se comprova na casa do projeto, e às vezes a casa aparece.

**E a família Hayai cresceu pelo lado que ninguém olhava:** a mesma org publicou o **HayaiTTS** (★39) — um motor de texto-para-voz neural OFFLINE para Android: se registra no sistema inteiro e traz 186 vozes (Piper e Kokoro, via sherpa-onnx). Última versão: 2.5.1, de 15 de junho. A peça que faltava do quebra-cabeça: ler a novela… ou escutá-la. Para quem lê novelas leves no ônibus, isto é o fechamento do círculo.

## 🌲 A rede completa de forks (revisada em 14-set)

As redes dos cinco projetos foram abertas fork por fork hoje na API do GitHub — incluindo a do J2K, que esconde o parente rico que quase ninguém nomeia:

**Na rede do J2K:**

- **TachiyomiS97** (Saud-97, ★125) — o príncipe deste ramo e o fork mais seguido dele: «uma versão mais rápida do Tachiyomi». As funções próprias, do README: atualizações globais até 5× mais rápidas, downloads até 3× mais rápidos, progresso multi-dispositivo via trackers (experimental), download automático do próximo capítulo enquanto você lê, e busca por URL no global search. E a história se repete: v1.7.5 de 1º de agosto de 2026 após calar desde janeiro de 2024 — o par do avô: ambos despertaram este ano.

**Na rede do Yōkai (100+ forks):**

- **yurei** (NotBlankyu, v1.10.1 de 21-ago) — a variante com ambição: mangá + webnovels, modo texto que renderiza o capítulo como texto em vez de imagens, filtro NSFW herdado do SY, e leitura local que agora lê ComicInfo.xml por capítulo.
- **yokai-T** (KakarottoCake, v1.0.2 de 4-jul) — streaming e download por torrent, a aposta própria dele.
- Um fork com **pastas personalizadas** (coleções multi-série com ordenação e backup) fez push em 14-set (constância do dia) — sem releases ainda.
- Rede completa com nomes próprios: kagura, Mekuri (local-first), Miko, Karasu, e uma variante Komga+galeria. Mais as cópias ★0 de fábrica, que são a maioria.

**E as redes pequenas:** o Rokku tem 3 forks (todos ★0, um fez push em 14-set — rede recém-nascida); o Reikai tem 5, com o **Nekoumy** (Zykrave, o mesmo autor do Kuro: «uma biblioteca para mangá e novelas», push de 12-set); o Hayai tem 4, todas cópias ★0. Quanto mais jovem é a casa, menor é a estela dela — por enquanto.

**A expedição profunda (J2K: 999 membros · Yōkai: 125 — caminhadas em 14-set até as folhas):** na camada funda dessas redes, o vivo com proposta própria: o **yurei** já tem um filho ativo — o fork para usuários **MIUI/HyperOS**, que corrige o que a otimização de fábrica da Xiaomi estorba, e vai no v1.11.0. Na linha Yōkai, folhas com nome e pulso: **Miko**, **Karasu**, **kagura**, **Mekuri** (local-first), **shuo** (novelas) e **MiruKan** (com versão própria, v1.0.1 de maio). E a oficina Hayai se completa: canal noturno com builds desta semana (hayai-nightly) *(reverificado em 15-set: o último build datado do canal é o r6674, de 6-set)* ao lado do **HayaiTTS** fichado acima. O resto da camada profunda são cópias sem aportes: fora do mapa.

## 🧬 Os primos menores do ramo

Para completar o mapa, os repos pequenos que a busca de hoje trouxe — nomeados com o tamanho real deles:

```
yomu (HugoFMiranda)          ★3   J2K-based, push jul-2026
TachiyomiDNP                 ★4   variante, push 16-ago
Hiirbaf/yokai                ★3   fork de Yōkai, push de 13-set
```

Nenhum alcança a porta de maturidade para ser recomendado como alternativa diária — mas se nomeiam porque existir também é informação, e porque qualquer um deles pode ser o próximo Rokku (que seis meses atrás era igual de pequeno). As cópias sem dono ativo, nem isso: cópias com relógio.

## 📜 A história que explica este ramo

Este ramo é a melhor aula de história do ecossistema: a da herança que se reparte.

```
2019–2023   o tachiyomiJ2K define a interface
            moderna do leitor de mangá livre.
            A migração massiva de bibliotecas
            nasce aqui.

jan-2024    O Tachiyomi original fecha (pressão
            legal). O J2K cala. Os usuários da
            interface J2K ficam órfãos.

2024–2025   O Yōkai recolhe a herança da interface.

2026        A família se ramifica por necessidade:
            o Rokku mantém, o Reikai une formatos,
            o Hayai sai da sombra, e o avô
            mesmo volta em agosto.
```

Cinco projetos vivos onde havia um calado. A lição do ramo: quando uma oficina fecha, não é o fim do ofício — é a partilha das ferramentas.

## ❓ Perguntas frequentes

**O tachiyomiJ2K «voltou» de verdade ou foi uma coisa pontual?**
Duas versões em uma semana de agosto, com etiquetas e notas — é um retorno real de atividade. Se haverá cadência, o outono dirá; a página de releases dele é o relógio.

**Yōkai ou Rokku se eu vinha da interface J2K?**
O Yōkai é o tronco com o mantenedor original em pausa ativa; o Rokku é o ramo de manutenção com cadência de agosto. A diferença prática está no ritmo — e ambos se abrem no dia em que se decide.

**O Reikai substitui meu leitor de mangá normal?**
Ele não vem para substituir: traz a função que quase ninguém tem — mangá e novelas em UMA biblioteca, com a mesma série agrupada mesmo vindo de fontes distintas. Se você não lê novelas, é mais app do que você precisa.

**O Hayai era um mito então?**
Era um projeto real sem porta. Hoje a porta existe, a licença está declarada e há versão etiquetada. O mito ficou em história — e essa correção é exatamente o motivo de os guias levarem data.

**Qual tem a versão mais fresca do ramo?**
Yōkai e Reikai: 4 de setembro. Rokku: 29 de agosto. Hayai: 10 de abril. J2K: 15 de agosto. Os números caducam — a página de releases de cada um não.

**E o fork «mais rápido» (TachiyomiS97)?**
É o fork mais seguido da rede do J2K (★125) e as promessas dele estão escritas no README: reviveu em agosto de 2026 com otimizações de atualizações e downloads. A regra não muda: os números de desempenho de qualquer fork se comprovam em uso próprio — e a página de releases dele, aberta no dia em que se decide.

**Os primos menores (yomu, DNP)?**
Se nomeiam, se medem, não se recomendam: ainda não passam na porta de maturidade. Amanhã pode ser outro conto — com data, se dirá.

**Por que tanto «o próprio mantenedor diz» neste guia?**
Porque em um ramo de projetos pessoais, a palavra do mantenedor É a fonte primária: o Yōkai explicou a pausa, o Reikai explica a filosofia, o J2K assina com humor os retornos. Citá-los com data é verificá-los.

## 🔗 Links

- tachiyomiJ2K: https://github.com/Jays2Kings/tachiyomiJ2K
- Yōkai: https://github.com/null2264/yokai
- Rokku: https://github.com/rokku-app/rokku
- Reikai: https://github.com/unseensnick/Reikai · https://reikai.app
- Hayai: https://github.com/HayaiApp/hayai
- Destacados da rede: https://github.com/Saud-97/TachiyomiS97 · https://github.com/NotBlankyu/yurei · https://github.com/KakarottoCake/yokai-T · https://github.com/Zykrave/Nekoumy
- Primos: https://github.com/HugoFMiranda/yomu · https://github.com/theordinaryguy23/TachiyomiDNP · https://github.com/cuong-tran/tachiyomiJ2K

> A Bandita informa a partir de fontes datadas. O avô voltou, o fantasma tem casa — e o ramo inteiro se verificou hoje.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: Yōkai ★1.883 (push de 14), Reikai ★28 (v0.3.2 de 4-set), redes pequenas re-datadas. O J2K e seus 999 membros de rede, constados no seu dia (14-set). Acta completa: Registro #71.
