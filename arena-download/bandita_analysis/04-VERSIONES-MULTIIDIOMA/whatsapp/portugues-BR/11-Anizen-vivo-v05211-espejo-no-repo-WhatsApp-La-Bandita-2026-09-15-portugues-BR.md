# Publicação 11 — AniZen está vivo em v0.5.211: o espelho não é o repo e o issue se escreve bem ou não se escreve

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 11)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🧬 A linhagem: Anikku → AniZen
├── 🪞 Canônico vs espelho
├── 🚫 O que NÃO é AniZen (e seu próprio README o diz)
├── 📋 A arte do bom reporte de bug
├── 📵 O caso do diagnóstico velho
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

```
AniZen — verificado HOJE, 14 de setembro
Repositório:   github.com/salmanbappi/AniZen
Estado:        vivo · push do dia 13-set
Versão:        v0.5.211 (publicada no dia 13-set)
               a série: 0.5.209 (23-ago) · 0.5.210 (5-set)
               · 0.5.211 (13-set) — ritmo de correções
               semanal
Estrelas:      182 · Apache-2.0
Pacote:        app.anizen
```

**Pulso de re-verificação (14-set, noite #20):** aberto o repo de novo HOJE: **v0.5.211 segue sendo a última release** — não existe versão mais nova que a de cima. O ritmo real da série recente: cinco releases em três semanas (0.5.207 → 0.5.211) — cadência semanal: a estável não vai a velocidade de trem (a beta é outra história — bloco seguinte) — mas não está parada. E atenção com as lojas: sob o pacote `app.anizen` **não há ficha pública no Google Play** (comprovado HOJE) — se um grupo te mostra uma «versão velha de faz meses», é um espelho, não a casa. O espelho não é o repo: por isso esta guia só dá o link do repo.

**A beta, fichada (14-set, noite #21 — o link que trouxe o dono):** github.com/salmanbappi/anizen-preview — «Automated Preview Builds for AniZen». Aqui está o trem, e de verdade: **981 releases** publicadas em automático (a r4620 é do dia 13 de setembro; oito builds em fila entre o dia 12 e o 13; o commit inicial o assinou «Gemini Automation» — o repo compila e publica sozinho). E o caso do «quase 1000» ficou resolvido com conta: não eram resenhas — eram **releases**: 981 e contando. A estável (acima) viaja semanal; a beta, várias vezes ao dia. Beta para provar o de amanhã; estável para viver o de hoje.

AniZen é um cliente livre de anime para Android, ativo esta mesma semana. Esta guia faz duas coisas com seu nome: te dá o estado real do projeto (acima, de hoje), e ensina a parte que quase ninguém ensina — como se reporta uma falha para que o desenvolvedor possa consertá-la. Porque há diferença entre reclamar num grupo e abrir um reporte que serve.

## 🧬 A linhagem: Anikku → AniZen

Nenhum app nasce do nada, e AniZen tem pedigrí documentado nos seus próprios repos:

```
komikku-app/anikku          ★1.025
   «Free and open source anime watcher for Android»
   A organização de Komikku (um dos leitores
   mangá mais ativos do ecossistema) mantém este
   cliente de anime.
   Versão 0.2.0 publicada no dia 11 de setembro —
   esta mesma semana.

        │  alguém toma esse código

「Anikku Mod」
   uma versão modificada, de outro autor

        │  commit do dia 28 de janeiro de 2026

AniZen
   o rebrand: «transform Anikku Mod into AniZen»,
   consta no histórico do repo. Mesma linhagem
   declarada, casa e nome próprios.
```

O que significa um rebrand, no crioulo? O projeto mudou de nome e de casa — e o declara. Não é um clone (esse aparece do nada com o nome do outro); é uma continuidade documentada: mesmo código base evoluído, autor identificado, histórico público. A diferença entre rebrand e clone é exatamente essa declaração com histórico — a mesma que distingue uma mudança de uma invasão de casa.

Para quem busca o cliente de anime da organização Komikku diretamente: esse é o Anikku, e sua 0.2.0 deste mês é sua versão mais fresca. Duas casas irmãs, dois ritmos: a original com sua organização atrás, a rebatizada com seu desenvolvedor individual empurrando semanalmente.

## 🪞 Canônico vs espelho

```
github.com/salmanbappi/AniZen    ← A CASA
   O repo canônico: aqui empurra o autor,
   aqui saem as versões, aqui se reporta.

github.com/Gaijin81/anizen       ← O ESPELHO
   ★0, cópia sem vida própria. Existe; não manda.
```

A regra que salva meias horas de confusão: **o espelho não é o repo.** Ao espelho não se reportam bugs (ninguém ali os vai ler nem consertar), e suas versões podem ter atraso respeito à casa. Como se sabe qual é a casa? Por onde há atividade real: releases assinadas, push recente, autor que responde. O resto são fotocópias — algumas fiéis, nenhuma com oficina.

## 🚫 O que NÃO é AniZen (e seu próprio README o diz)

A frase está no próprio projeto, e convém sublinhá-la porque o nome circula em conversas onde se espera outra coisa:

**«AniZen does not have or fix any extensions»** — AniZen não traz nem conserta extensões.

O cliente é o app. As fontes são outra camada — a dos parsers do ecossistema — e os problemas de reprodução de uma fonte concreta não se reportam ao repo do app: ali os fecham por fora de alcance, com razão. Antes de abrir qualquer reporte, a primeira pergunta é: isto falha no APP (fecha sozinho, não salva, a interface quebra) ou na FONTE (não carrega tal série, tal servidor vai lento)? A segunda não é problema do app — por mais que doa.

## 📋 A arte do bom reporte de bug

O template do repo pede, com checkboxes incluídos, exatamente o que um desenvolvedor precisa para reproduzir seu problema. A anatomia do reporte que serve:

```
Título:         uma linha, específico
                ✗ "O app não funciona"
                ✓ "Crash ao abrir a aba Histórico
                   com mais de 500 entradas"

Passos:         como chegar à falha, numerado,
                desde app aberto
                1. Abro o AniZen
                2. Vou a Histórico
                3. ...

Esperava:       o que deveria acontecer
Obtive:         o que acontece em seu lugar

Crash log:      se o app se fecha sozinho, o log
                que ele mesmo oferece compartilhar
                (sem dados pessoais de por meio)

Versão:         o número EXATO — a HOJE 15-set, v0.5.211.
                "A última" não é um número: amanhã
                é outra. A aba Sobre o diz.

Telefone:       modelo e versão de Android

Antes de enviar (os checkboxes do template):
   □ Não é duplicado de um issue aberto
   □ O título é específico
   □ Estou na última versão
   □ Os números são específicos
```

E a gramática do canal: os issues deste repo se escrevem em inglês, curtos, sem emojis, UM problema por reporte. Os reportes vagos — «não funciona, consertem» — morrem fechados como «not planned», e o exemplo da casa é o issue #50: uma plantilha do que NÃO é um reporte. Não é maldade de mantenedor: é que um bug que não se pode reproduzir, não se pode consertar.

A regra de fundo desta família: o reporte o escreve uma pessoa, com suas mãos e sua conta — nunca se envia em nome de ninguém nem por ninguém. Um reporte de bug é correio institucional da era digital: com remetente, com dados, com modos.

## 📵 O caso do diagnóstico velho

Nos textos velhos da comunidade existia um diagnóstico de uma falha de AniZen num telefone TECNO. Esse texto circulou incompleto, então aqui não se reconstrói de memória nem se inventam passos — a regra é simples: o que não se pode abrir e verificar, não se receita.

O que sim serve, genérico e verificado pelo senso comum do ofício, é a lista de checagem antes de culpar o app:

```
□ A versão é a de hoje? (v0.5.211)
□ A falha se reproduz duas vezes seguidas
  com os mesmos passos?
□ Acontece também com outra fonte, ou outra série?
  (se só falha uma fonte: é a camada de
  fontes, não o app)
□ Há espaço livre e memória suficiente?
□ O log do crash diz algo coerente?
```

Se a falha passa a lista — reproduz, é do app, em versão vigente — então sim existe um reporte a escrever, com a anatomia de cima. Se não passa, observa-se e anota-se: metade dos «bugs» do mundo são condições, não erros.

E o aviso de privacidade que nunca sobra: ao reportar não viajam seu IMEI, suas capturas com conta nem seu número de telefone. O desenvolvedor precisa do crash log e dos passos — não da sua identidade.

## ❓ Perguntas frequentes

**AniZen é seguro / confiável?**
É um projeto vivo, com licença Apache-2.0, push desta semana e versões semanais. «Confiável» a longo prazo o constrói o histórico: a casa está, a oficina empurra, e a linhagem (Anikku) é de uma organização séria do ecossistema. Cada um abre o repo antes de instalar — como com tudo.

**AniZen ou Anikku?**
Irmãos de código: Anikku é o da organização Komikku (0.2.0 esta semana); AniZen o rebatizado com desenvolvimento individual semanal. Mesma linhagem declarada, casas distintas. O que você preferir seguir — mas desde sua casa.

**Por que minha fonte favorita não carrega? Reporto ao AniZen?**
Não: o app não tem nem conserta extensões (seu README o diz tal qual). A falha de uma fonte é tema da camada de fontes do seu ecossistema.

**Onde baixo a versão boa?**
De Releases na casa: github.com/salmanbappi/AniZen/releases — hoje v0.5.211. Sinta-se livre para reabri-lo no dia em que instalar: essa página é o único relógio que manda.

**O espelho de Gaijin81 serve para algo?**
Para nada que a casa não faça melhor. Não se reporta ali, não se baixa dali, não se cita como fonte.

**Posso pedir funções novas por issue?**
Cada repo tem sua política para isso (os templates o dizem). O universal: um pedido por issue, com caso de uso concreto — «eu gostaria de X porque quando faço Y não posso Z» vale mais que «adicionem X».

**Quem escreve o issue se um grupo inteiro tem o mesmo bug?**
Quem o souber reproduzir melhor. Os demais somam um «me acontece igual, com tal versão e tal telefone» — dado, não ruído.

## 🔗 Links

- AniZen (a casa): https://github.com/salmanbappi/AniZen · https://github.com/salmanbappi/AniZen/releases/latest
- AniZen beta (o trem diário): https://github.com/salmanbappi/anizen-preview
- Anikku (a linhagem original): https://github.com/komikku-app/anikku
- O espelho (nomeado, não usado): https://github.com/Gaijin81/anizen

> A Bandita informa a partir de fontes datadas. O espelho não é o repo, e o reporte que serve tem números, passos e modos.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: re-verificado a HOJE. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.

**Pulso de mudança (15-set):** re-aberto o repo HOJE: v0.5.211 segue sendo a última estável (★182); a preview segue soltando — seu build r4622 é de HOJE mesmo. O dito: o espelho não é o repo.
