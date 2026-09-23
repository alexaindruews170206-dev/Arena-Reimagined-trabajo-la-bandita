# Publicação 01 — Lojas de APK: a loja legal, a placa de mods e o relógio de 2027

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 01)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🏪 As lojas que sim (ficha por ficha)
├── 🧰 Os instaladores que trazem as lojas até você
├── ⚠️ As placas de mods (se nomeiam, não se receitam)
├── 🕐 O relógio de 2027 e a porta dos fundos
├── 🧭 O que olhar antes de instalar qualquer APK
├── 🚩 Sinais de isca
├── ❓ Perguntas frequentes
├── 📚 Palavras-chave desta guia
└── 🔗 Links

## ⚡ Em uma página

Uma loja de APK é um lugar com dono conhecido que te deixa instalar aplicativos fora da loja oficial do telefone. Há de duas classes: as que revisam, assinam e se fazem responsáveis pelo que publicam — e as que vivem de tráfego de mods, onde o «premium grátis» chega com presente surpresa dentro do arquivo.

Esta guia percorre as lojas legítimas do ecossistema livre, uma por uma, com seu estado real a 15 de setembro de 2026: qual está sob ameaça, qual estreou versão ontem, qual mudou de casa há dias. E termina com o relógio: a política de verificação de desenvolvedores do Google já tem contagem regressiva pública.

Se você veio por «Spotify premium grátis» ou «jogos com tudo desbloqueado», esta guia não vai te acompanhar: isso não é uma loja, é um anzol com carteira.

## 🏪 As lojas que sim (ficha por ficha)

### F-Droid — a casa-mãe

https://f-droid.org

A loja histórica do software livre no Android. Tudo o que publica passa por compilação reprodutível: o arquivo que você baixa pode ser reconstruído desde o código público, e se não coincide, não sai. Essa é a promessa de fundo, e é a que nenhuma loja de mods pode igualar.

Visto no dia 14-set: o site mantém seu banner de campanha — «F-Droid is under threat» — no marco do programa de verificação de desenvolvedores do Google que esta mesma guia cronometra mais abaixo. O instalador da própria loja se baixa direto do seu site.

Se você só vai escolher uma loja desta lista, escolha esta. É a mais velha, a mais revisada e a que tem o padrão de publicação mais exigente do ecossistema livre.

```
F-Droid em uma caixa
Qué é:      loja e repositório de apps livres
Promessa:   compilação reprodutível, sem rastreadores declarados
Estado no seu dia (14-set): viva, com campanha ativa «under threat»
Para quem:  todo mundo; é o ponto de entrada natural
```

### IzzyOnDroid — o anexo respeitado

https://apt.izzysoft.de/fdroid

O repositório complementar mais conhecido do ecossistema F-Droid: muitos apps que ainda não entram no canal principal se publicam primeiro aqui. É um armazém de confiança dentro da comunidade, mantido há anos.

Visto no dia 14-set: o site responde; sua carga depende de JavaScript, então o navegador o monta no seu ritmo. Nada alarmante: é o mesmo site de sempre.

### Droid-ify — o cliente F-Droid moderno

Repositório canônico: https://codeberg.org/droidify/client
Espelho no GitHub: https://github.com/Droid-ify/client

Um cliente para consumir catálogos tipo F-Droid com interface moderna. A versão 0.7.8 saiu em 12 de setembro: traz correção do repositório após importá-lo, importar por código QR, instalador para quem tem root e tema adaptativo Material You.

Detalhe que importa: o projeto declara que sua casa oficial é Codeberg e que sua página no GitHub é só espelho. Quando um projeto nomeia canônico outro domínio, esse é o link que manda — a regra desta guia é simples: o canônico primeiro.

```
Droid-ify em uma caixa
Qué é:    cliente de repositórios F-Droid
Última:   0.7.8 — 12 de setembro de 2026
Casa:     codeberg.org/droidify/client (GitHub é espelho)
Extras:   QR, instalador root, tema dinâmico
```

### Neo-Store — o cliente com bússola de rastreadores

https://github.com/NeoApplications/Neo-Store

Outro cliente do ecossistema F-Droid, com detalhes de usabilidade que sua comunidade cuida. Seu movimento mais recente (commit de 13 de setembro) é uma joia de design: está substituindo o bloco estático de rastreadores de cada ficha por ações de controle — e te dá um atalho para o Exodus Privacy para auditar qualquer app instalada.

Isso é uma ideia de loja madura: não só te deixar instalar, mas te dar o instrumento para saber o que instala. A versão estável é a 1.2.6.

### Komi Store — a que mudou de casa (e o diz aos gritos)

https://github.com/komi-store/komi-store
Site: https://komistore.app

Esta ficha existe porque a mudança de casa confunde. Komi Store antes se chamava «GitHub Store» e vivia em outra organização; migrou para a organização komi-store, estreou domínio próprio (komistore.app) e vai na versão 1.9.3 (código 22). O movimento está declarado pelo próprio projeto em seu repositório — 18.500 estrelas e atividade de começos de setembro.

A diferença entre «migrou» e «clonaram ele» é esta: a migração o dono anuncia, no repo, com histórico. O clone aparece do nada, com o nome do outro e pressa para que você instale. Komi fez o primeiro.

### Aurora Store — a porta para outro catálogo

https://gitlab.com/AuroraOSS/AuroraStore

O cliente livre que consulta o catálogo da loja do Google sem entregar sua conta: sessões anônimas, buscas e atualizações, sem expor sua identidade principal. É das peças mais instaladas do ecossistema livre e tem infraestrutura séria atrás.

Visto no dia 14-set: a versão etiquetada mais recente é a 4.8.4, com atividade de repositório das últimas semanas. E um detalhe que diz muito do projeto: seu commit mais recente de documentação é exatamente isto — «declarar o uso de IA no desenvolvimento». Transparência declarada de forma voluntária. Isso, numa loja de mods, não existe nem vai existir.

### Accrescent — a jovem de padrões altos

https://accrescent.app

A loja mais jovem da lista, em fase alpha, com Android 10 como mínimo. Não é «mais uma F-Droid»: sua aposta é segurança de entrada — verificação estrita de assinaturas (key pinning), metadados assinados, atualizações automáticas sem privilégios adicionais no Android 12 ou superior, suporte a APKs divididos e zero contas.

Também se encontra dentro da loja do GrapheneOS, que é um bom termômetro de quem a comunidade paranoica por boas razões faz caso.

```
Accrescent em uma caixa
Qué é:   loja centrada em segurança, em alpha
Mínimo:  Android 10
Firma:   key pinning + metadados assinados
Contas:  nenhuma
Via:     site próprio e loja do GrapheneOS
```

### Appteka — o mercado de comunidade (com lupa)

https://appteka.store

Código do cliente: https://github.com/solkin/appteka-android

Um mercado gerido por comunidade com catálogo grande (declara 320.000 aplicativos) e cliente próprio: a versão oficial do cliente é a 23.0, pesa menos de 4 MB e pede Android 6 em diante. O site vive e responde.

Entra na lista de «sim» mas com lupa: por ser catálogo de comunidade, o padrão de publicação não é o de F-Droid. Serve, e em troca pede o que toda esta guia repete: olhar o dono do arquivo antes de instalar.

Dentro da Appteka vivem fichas de apps concretas que esta guia cita como exemplo de estado — por exemplo, as páginas dos dois projetos Rebuild, abertas hoje com a versão 23.0 do cliente visível nos títulos. Citam-se como exemplo de vida do mercado, não como recomendação dessas apps concretas.

## 🧰 Os instaladores que trazem as lojas até você

Os últimos anos trouxeram uma figura nova: ferramentas que não são lojas com vitrine, mas instaladores que constroem sua própria loja à medida, seguindo os repositórios que você lhes aponta.

### Obtainium — o app que vigia os repositórios por você

https://github.com/ImranR98/Obtainium

A mais popular da sua espécie: você diz quais repositórios te importam e ela vigia seus lançamentos, baixando e instalando as versões novas mal saem. A HOJE 15-set soma perto de 19.700 estrelas e commits de ontem — dos projetos mais vivos de todo este mapa.

Seu próprio README credencia o ObtainX como o instalador externo do ecossistema. Isso também é sinal de maturidade: saber nomear os vizinhos.

### ObtainX — o braço instalador

https://github.com/bikram-agarwal/ObtainX

Vivo (constado no dia 14-set). Complemento de instalação do ecossistema Obtainium: o elo entre «detectei uma versão nova» e «fica instalada no telefone».

### Omnify — o cliente F-Droid sem barulho

https://github.com/Victor-root/Omnify
Site: https://victor-root.github.io/Omnify/

Vivo no seu dia (14-set), com sua landing carregando: apresenta-se como «um cliente F-Droid sem desordem que instala aplicativos de qualquer lugar». Das apostas novas por tornar o consumo de catálogos livres mais amável.

```
Os três em uma frase
Obtainium: vigia releases e te avisa
ObtainX:   executa a instalação
Omnify:    cliente F-Droid leve
Nenhum dos três te pede para sair da via legal.
```

## ⚠️ As placas de mods (se nomeiam, não se receitam)

Estes nomes existem para que você os reconheça, não para que os visite:

- **Espacio APK** — site vivo (constado no dia 14-set), catálogo de «apps e jogos populares». Seu produto real: mods com promessas premium.
- **HappyMod** — respondeu no dia 14-set sem título legível (escudo anti-bot). Seu modelo de negócio: subir mods subidos por qualquer um, sem cadeia de custódia séria.
- **Liteapks** — vivo (constado no dia 14-set), anuncia-se como «#1 em MOD APK». O número um em mods é, por definição, o número um em arquivos sem revisão.

O padrão comum: prometem o de pago de graça, pedem permissões que o app original não pede, e se algo der errado não há nem repo nem dono a quem reclamar. O «mod» muitas vezes nem é o app original: é outro app fantasiado com seu ícone.

Aqui não vão links. O nome já cumpre sua função: se te aparecer num grupo com «baixe daqui», você já sabe o que é.

## 🕐 O relógio de 2027 e a porta dos fundos

O marco que muda tudo isto tem data e relógio público.

O plano do Google — «verificação de desenvolvedores do Android» — exige que os apps de dispositivos certificados estejam registrados por desenvolvedores verificados. Em 30 de setembro de 2026 toca o primeiro marco: quatro países (Brasil, Indonésia, Singapura, Tailândia), sete lojas (Google Play, HONOR, OPPO, Galaxy Store, Palm Store, V-Appstore e GetApps), Android 7 em diante.

Em 2027 o filtro chega a todos os apps de dispositivos certificados. A campanha Keep Android Open mantém hoje seu contador público: 110 dias — e seu FAQ já situa o bloqueio perto de janeiro de 2027. Dois calendários, a mesma mensagem: o tempo do sideloading tal como o conhecemos está contado.

A porta dos fundos que o Google abriu este mês: as contas de distribuição limitada. Para estudantes, docentes e aficionados — até 20 dispositivos, sem identificação governamental e sem tarifa. É um alívio pequeno com teto duro: vinte aparelhos não sustentam um projeto comunitário.

```
O relógio, em duas linhas
30-set-2026: 4 países, 7 lojas, Android 7+
2027:        todos os apps, dispositivos certificados
Contador da campanha (a 14-set): 110 dias
```

O que isto significa para o ecossistema livre: F-Droid com seu banner de ameaça, Accrescent construindo segurança desde hoje, e cada loja desta guia sabendo que seu modelo se joga o futuro nos próximos meses. Ninguém desta lista fica quieto — e essa é, talvez, a melhor sinal de todas.

## 🧭 O que olhar antes de instalar qualquer APK

```
1. De onde sai?
   Repo ou site com histórico > link de um grupo.
2. Quem assina?
   O projeto declara sua firma; se o arquivo não
   coincide com essa firma, é outra coisa.
3. O que pede?
   Permissões que o app original não pede = motivo.
4. Está em mais de uma loja séria?
   F-Droid + repo próprio + IzzyOnDroid = tripla via.
   Só num site de mods = nenhuma via.
5. O que dizem os auditores?
   Exodus (rastreadores), VirusTotal (múltiplos motores),
   o repo do projeto (issues reais de usuários).
6. Tem pressa?
   «Últimas 24 horas com este link» é a gramática
   da isca. O bom continua ali amanhã.
```

## 🚩 Sinais de isca

- O anúncio do topo do buscador «baixe X» paga mais caro que o resultado legítimo. Quem paga o anúncio não é o projeto.
- «Versão modificada», «premium desbloqueado», «tudo ilimitado»: alguém modificou algo — o que não te diz é o que mais meteu dentro.
- A página te pede para desativar a proteção do telefone para «completar a instalação». Nenhuma loja séria precisa que você baixe as calças de segurança.
- Comentários clonados em várias páginas com as mesmas frases.
- O cadeado do navegador: só diz que a conexão está cifrada. O banco o tem, e o phishing também.

## ❓ Perguntas frequentes

**Com qual começo se venho do zero?**
F-Droid. É a porta com mais história, mais revisão e mais comunidade. Daí pendura o resto: IzzyOnDroid como anexo, e o cliente que preferir (Droid-ify ou Neo-Store) para manejar o catálogo com comodidade.

**Os apps da F-Droid são 100% seguros?**
Nenhuma loja promete isso. F-Droid promete transparência: compilação reprodutível e política declarada. É o padrão mais alto do ecossistema livre, não uma varinha.

**Por que há duas casas para o Droid-ify (Codeberg e GitHub)?**
Porque o projeto o declara assim: Codeberg é canônico, GitHub espelho. Quando um projeto declara sua casa, a casa manda. É a mesma lógica de «o repo vivo sim» que esta família de guias repete.

**Komi Store e «GitHub Store» são a mesma?**
Sim — migrou de organização e o documenta no seu repo, com domínio próprio. A migração o dono conta; o clone não tem dono que conte.

**Aurora Store é «a loja do Google ilegal»?**
Não. É um cliente livre que consulta esse catálogo sem sua conta. O projeto o declara e o mantém com atividade recente — até declara em sua documentação quando usa IA no desenvolvimento.

**As contas de distribuição limitada servem para «distribuir» meu app ao grupo?**
Vinte dispositivos é um circuito fechado: provas, aula, casa. Para algo mais largo, a via é outra (e cada via exige o seu).

**E os mods? Nunca?**
Esta guia não os receita nem os enlaza. Se alguém insistir, que seja com a firma revisada e o risco assinado por quem insiste — que nunca é quem vai perder os dados.

**O dia 30 de setembro bloqueia meu telefone?**
Não. Esse marco toca lojas participantes em quatro países. Sua mudança chega com o desdobramento global de 2027. Reabra esta guia no dia em que decidir algo: o mapa se move.

## 📚 Palavras-chave desta guia

```
APK          o pacote instalável de um app Android
Sideload     instalar fora da loja do sistema
Reprodutível o arquivo sai igual recompilado desde o código
Key pinning  a firma do projeto está atada de antemão
Split APKs   o pacote vem em partes por arquitetura
Exodus       auditoria pública de rastreadores em apps
Repo         repositório: a casa do código (e da verdade)
```

## 🔗 Links

- F-Droid: https://f-droid.org
- IzzyOnDroid: https://apt.izzysoft.de/fdroid
- Droid-ify (canônico): https://codeberg.org/droidify/client · espelho: https://github.com/Droid-ify/client
- Neo-Store: https://github.com/NeoApplications/Neo-Store
- Komi Store: https://github.com/komi-store/komi-store · https://komistore.app
- Aurora Store: https://gitlab.com/AuroraOSS/AuroraStore
- Accrescent: https://accrescent.app
- Appteka: https://appteka.store · cliente: https://github.com/solkin/appteka-android
- Obtainium: https://github.com/ImranR98/Obtainium · ObtainX: https://github.com/bikram-agarwal/ObtainX
- Omnify: https://github.com/Victor-root/Omnify · https://victor-root.github.io/Omnify/
- Verificação de desenvolvedores: https://developer.android.com/developer-verification
- Campanha: https://keepandroidopen.org

> A Bandita informa a partir de fontes datadas. A loja legal te dá algo que o mod nunca dá: um dono a quem cobrar.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: data de estado. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.

**Nota da verificação final (15-set, noite):** o site próprio do Omnify (victor-root.github.io/Omnify) devolve 404 nesta hora, constado ao vivo; a casa GitHub segue viva (★20, v1.0.5-beta.6 do dia 4-set). Os links se reabrem no dia em que se usam — regra da casa.
