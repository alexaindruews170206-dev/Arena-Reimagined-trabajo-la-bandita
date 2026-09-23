# Publicação 03 — Verificação de Desenvolvedores: 15 dias para o marco e o relógio rumo a 2027

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 03)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 📅 O cronograma completo
├── 🪪 O que é a verificação (nas palavras do Google)
├── 🛒 Os dois consoles e o fluxo de registro
├── 🏪 As sete lojas do dia 30 de setembro
├── 🎓 Contas de distribuição limitada: a porta dos fundos
├── 🛠️ O fluxo avançado (o da carta de 24 horas)
├── 👤 A quem toca e a quem não toca (ainda)
├── 📜 A carta aberta: as três objeções
├── 📣 A campanha e seu relógio
├── 📗 A leitura contrária: F-Droid
├── 📌 Correções que este tema já sofreu
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

O Google está instalando um censo de desenvolvedores para o Android. O programa se chama «verificação de desenvolvedores do Android» e funciona assim: para que um aplicativo se instale em dispositivos Android certificados, seu desenvolvedor terá que estar registrado e verificado — com identidade real, nomes de pacote declarados e chaves de firma vinculadas.

Hoje é 15 de setembro. Faltam **15 dias** para o primeiro marco público: em 30 de setembro, quatro países e sete lojas entram no filtro. E aqui a edição brasileira tem o que dizer: **o Brasil é um dos quatro países do piloto.** Se você publica nas lojas participantes, sua data é 30 de setembro. Se vive fora do piloto (ou distribui fora dessas lojas), sua data é outra: 2027, quando o filtro alcançar todos os apps de dispositivos certificados.

As vozes estão em dois bandos que esta guia cita pelo nome: o Google, que o vende como prestação de contas contra o malware; e a F-Droid com a campanha Keep Android Open, que o leem como um censo que quebra a distribuição livre de aplicativos. O que todo mundo tem: um relógio. A campanha mantém um contador público: 110 dias constados no dia 14-set — o contador corre sozinho.

## 📅 O cronograma completo

```
Ago 2025        O Google anuncia o programa.

29-set-2025     A F-Droid publica sua análise crítica:
                «o decreto de registro de desenvolvedores».

Mar 2026        O processo se abre a todos os desenvolvedores
                (Play Console e o novo Android Developer
                Console). Blog oficial lido na sua página.

Jun 2026        O Google publica «Building a safer ecosystem
                together»: confirma o arranque em 7 lojas
                e 4 países, apresenta APIs de automação
                e repete o plano global de 2027.

Ago 2026        As contas de distribuição limitada ficam
                disponíveis para todos.

30-set-2026     PRIMEIRO MARCO: 4 países (Brasil, Indonésia,
                Singapura, Tailândia) · 7 lojas · Android 7+
                em dispositivos certificados.

2027            Desdobramento global: todos os apps em
                dispositivos certificados.
~Jan 2027       A campanha situa aqui o bloqueio efetivo
                e o conta com relógio público: 110 dias no corte de 14-set.
```

Os três documentos oficiais (hub do programa, guias e blogs) se abriram hoje; suas datas de atualização são de fins de agosto e começos de setembro. O mapa se move: esta guia leva a data de corte no título por uma razão.

## 🪪 O que é a verificação (nas palavras do Google)

A definição oficial cabe em uma frase: «a verificação de desenvolvedores do Android vincula entidades do mundo real —pessoas e organizações— aos seus aplicativos de Android».

O marco do Google: estabelece responsabilidade (accountability). Desencoraja os atores maliciosos, faz mais difícil que quem fez dano repita sob outro nome, e dá ao usuário mais confiança sobre quem está atrás de um app. A tarifa do registro se compara na própria FAQ com a cota histórica de 25 dólares da loja do Google.

A leitura contrária (F-Droid, Keep Android Open, signatários da carta): isso não é um scanner de malware — é um censo. Não analisa arquivos: analisa pessoas. E põe o peso do registro sobre quem distribui, não sobre quem distribui mal. Ambas as leituras se citam completas mais abaixo; esta guia não escolhe bando por você.

## 🛒 Os dois consoles e o fluxo de registro

Há duas portas, segundo por onde você distribua:

- **Play Console** — se seus apps vivem na loja do Google. O registro se integra ao que já existia.
- **Android Developer Console** — o console novo, para todo o resto: lojas alternativas, distribuição direta, sideload organizado.

O fluxo do console novo, segundo sua guia oficial (aberta hoje), em sete passos:

```
1. Criar a conta
2. Escolher como você distribui seus apps
3. Completar a verificação de identidade
   (os requisitos mudam segundo o tipo de conta)
4. Registrar os nomes de pacote dos seus apps
5. Automatizar o fluxo com as APIs novas
6. Resolver duplicados de nome de pacote
   (quando dois projetos reclamam o mesmo)
7. Revisão
```

Os pontos delicados que a documentação confirma: o registro exige declarar TODOS os nomes de pacote que você distribui, e evidência de que controla as chaves de firma. Ou seja: não é um formulário — é um inventário completo do que você publicou.

## 🏪 As sete lojas do dia 30 de setembro

O marco do dia 30 de setembro não toca «todas as lojas»: toca as participantes declaradas.

```
1.  Google Play
2.  Galaxy Store   (Samsung)
3.  GetApps        (Xiaomi)
4.  HONOR Store
5.  OPPO Store
6.  Palm Store
7.  V-Appstore     (vivo)
```

Quatro países no piloto: **Brasil**, Indonésia, Singapura e Tailândia. Dispositivos certificados com Android 7 ou superior. Se seu app vive nessas lojas e nesses países, o dia 30 de setembro precisa que seu desenvolvedor esteja verificado. Se você vive fora do piloto, seu calendário é o de 2027 — mas o processo pode se adiantar, e o Google o recomenda.

O que NÃO muda no dia 30 de setembro: o sideload direto de um APK (instalar um arquivo à mão), a F-Droid e as lojas alternativas fora da lista. Esse é o tema de 2027.

## 🎓 Contas de distribuição limitada: a porta dos fundos

A novidade do mês, confirmada hoje em três fontes oficiais (a FAQ, a guia dedicada e o blog de junho):

```
Para quem:    estudantes, docentes, aficionados,
              quem aprende
O que permite: registrar apps e compartilhá-los com até
              20 dispositivos — que o usuário final
              autoriza explicitamente
O que pede:   nem identificação governamental, nem tarifa
Sua guia traz: datas-chave, o que a conta pode fazer,
              custo, como funciona compartilhar, se é
              para você, e o que precisa para se registrar
```

É uma janela real para a sala de aula, a oficina e o hobby. Com teto duro: vinte dispositivos não sustentam um projeto comunitário nem uma distribuição aberta. É a porta para aprender, não a porta para viver.

## 🛠️ O fluxo avançado (o da carta de 24 horas)

Para quem não pode ou não quer passar pelo registro completo, existe um fluxo avançado. Segundo a documentação da campanha (verificada também na semana passada), funciona assim:

- Nove passos, descritos na guia.
- Uma espera de aproximadamente 24 horas.
- Corre através de Play Services — do serviço do Google, não do sistema operacional aberto.

Esse último ponto é o que mais discussão gera: o caminho alternativo passa pelo mesmo componente proprietário do caminho padrão. Se Play Services não está — telefones sem Google — o fluxo não se aplica.

A FAQ oficial mantém sua seção «Advanced flow» como via reconhecida.

## 👤 A quem toca e a quem não toca (ainda)

```
Sua situação                                  Muda no 30-set?
Publica nas 7 lojas, país piloto             Sim: dev verificado
                                             ou seu app não entra
Publica nas 7 lojas, fora do piloto          Sua data é 2027
Instala APK à mão (sideload)                 Não. Ainda. Seu tema: 2027
Usa F-Droid                                  Não. Ainda. A campanha
                                             diz que sua data de
                                             impacto não está publicada
Telefone sem certificação do Google          Outro mundo: o filtro
                                             vai sobre certificados
```

A frase que resume tudo: quem distribui dentro do mundo certificado, está dentro do censo — hoje em quatro países, amanhã em todos. Quem vive fora desse mundo, tem um ano mais de janela.

## 📜 A carta aberta: as três objeções

Keep Android Open organizou uma carta aberta ao Google (lida hoje na sua página). Sua estrutura são três blocos:

**1. Nossas preocupações.** O registro com identidade converte a distribuição de software num ato identificado diante de uma corporação; o impacto cai sobre desenvolvedores pequenos, projetos anônimos por segurança e comunidades fora dos circuitos formais.

**2. As medidas existentes bastam.** Play Protect já escaneia; as lojas já filtram; os mecanismos de segurança do sistema já existem. O censo não adiciona um scanner: adiciona um registro de pessoas.

**3. O pedido.** Que o Google retire a exigência de registro com identidade como condição de distribuição.

As cifras que a própria carta mostra: 71 signatários, 23 países. Entre os visíveis: AdGuard, Aurora Store, BEUC, Brave, Calyx, CCC, Codeberg, F-Droid, FUTO, GrapheneOS, IzzyOnDroid, KDE, microG, Nextcloud, Obtainium, Tor, Vivaldi e a Fundação Karisma, entre outros. Aparecer na lista não é recomendação de instalar nada — é o mapa de quem assinou.

## 📣 A campanha e seu relógio

https://keepandroidopen.org

A campanha mantinha na capa seu contador público: **110 dias** (constado no dia 14-set) — rumo ao que sua FAQ chama o bloqueio, situando-o perto de janeiro de 2027. Sua frase de capa: «Your phone is about to stop being yours».

O que a campanha documenta do registro padrão: tarifa, identificação governamental, evidência de posse da chave de firma, e a declaração de todos os nomes de pacote. Sua consigna — «Do not sign up» — é da campanha; esta guia a cita, não a dita.

Sua FAQ também aclara a pergunta que a comunidade mais repete: setembro NÃO inclui a F-Droid; a data em que o filtro alcança a F-Droid não está publicada. O contador da campanha é a única contagem regressiva pública que existe sobre 2027 — por isso esta guia a cita com sua data.

## 📗 A leitura contrária: F-Droid

https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html

A análise da F-Droid (publicada em 29 de setembro de 2025, aberta hoje) intitula o programa «o decreto de registro de desenvolvedores do Google» e o desarma em quatro seções:

- **O movimento para quebrar a distribuição livre** — a tese: sem identidade, não há distribuição; sem distribuição, não há software livre no Android.
- **O chamariz da segurança** — o malware já se combate com análise; o censo não analisa arquivos, analisa autores.
- **O direito de executar** — seu telefone, seu software: a linha de fundo que a carta defende.
- **O que propõem** — alternativas que não passem pelo registro com identidade.

A F-Droid mantém ainda seu banner «under threat» em todo o seu site, com a campanha ativa. Para o ecossistema livre, este é O tema do ano.

## 📌 Correções que este tema já sofreu

Este assunto corrige versões anteriores de si mesmo. Histórico do que se acreditou e deixou de ser certo:

```
Acreditava-se antes         O confirmado depois
«O 30-set bloqueia APKs»    30-set = 4 países, 7 lojas.
                            O bloqueio amplo é 2027.
«Android 8+»                Android 7+.
«6 lojas»                   7.
«Anunciado em nov-2025»     Agosto de 2025.
«O fluxo avançado demora    É de uma só vez:
24 h por cada APK»          9 passos + uma espera de ~24 h.
«Limited = sem ID e pronto» Sem ID, mas com perfil de pagos,
                            2FA e conta Google para operar.
«O blog de junho não se     Foi lido: confirma 7 lojas,
pode ler»                   4 países, APIs e plano 2027.
```

A lição do assunto: cada mês traz sua correção. Reabra as fontes no dia em que decidir algo — as de cima são de hoje.

## ❓ Perguntas frequentes

**O dia 30 de setembro me bloqueia instalar APKs à mão?**
Não. Esse marco toca as lojas participantes em quatro países. O sideload direto e a F-Droid ficam fora — por enquanto. Seu relógio sério é 2027.

**Preciso fazer algo HOJE?**
Se você publica nessas lojas no Brasil: sim, verificar. Se não: não — mas convém conhecer o processo antes que seja sua vez.

**A verificação custa?**
O registro se compara na FAQ aos 25 dólares da Play. As contas de distribuição limitada não pagam tarifa nem pedem ID.

**E se só faço apps para mim?**
Vinte dispositivos é o mundo das contas limitadas: sem ID, sem tarifa. Para um círculo íntimo, alcança.

**Isso mata a F-Droid em setembro?**
Não — e não está publicado quando, se ocorrer. É a pergunta mais repetida e a resposta honesta é: ninguém fora do Google tem essa data.

**O que é isso de «dispositivos certificados»?**
Os que saem de fábrica com os serviços do Google. Um telefone sem certificação vive fora do alcance do filtro — com todo o resto que isso implica.

**O contador de 110 dias é oficial?**
É da campanha, não do Google. Sua data — o bloqueio em torno de janeiro de 2027 — é sua leitura do calendário. O Google diz «2027» a seco. Dois relógios, duas vozes.

**Onde leio as fontes sem a interpretação de ninguém?**
Nos links de baixo: hub, guias, FAQ e blogs são do Google; a carta e a FAQ são da campanha; a análise, da F-Droid. Tudo se abre hoje.

## 🔗 Links

- Hub oficial: https://developer.android.com/developer-verification
- FAQ oficial: https://developer.android.com/developer-verification/guides/faq
- Distribuição limitada: https://developer.android.com/developer-verification/guides/limited-distribution
- Console novo: https://developer.android.com/developer-verification/guides/android-developer-console
- Blog de março: https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html
- Blog de junho: https://android-developers.googleblog.com/2026/06/android-developer-verification.html
- Campanha: https://keepandroidopen.org · https://keepandroidopen.org/faq/ · https://keepandroidopen.org/open-letter
- F-Droid: https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html

> A Bandita informa a partir de fontes datadas. O relógio corre; quem lê as fontes a tempo, escolhe a tempo.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: relógio: faltam 15 dias; contador 110 constado no dia 14. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
