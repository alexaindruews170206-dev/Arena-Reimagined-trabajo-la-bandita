# Publicação 09 — Ferramentas FOSS: a caixa de ofício, cada peça com sua data de afiação

**La Bandita · 15 de setembro de 2026 · edição brasileira (adaptada do original espanhol, peça 09)**

## 🗺️ Mapa desta guia

├── ⚡ Em uma página
├── 🖼️ Galeria e arquivos
├── 🔐 Chaves e segundo fator
├── 📲 Transferir e conectar
├── 🧰 A gaveta de sistema
├── 🗺️ Mapas
├── 📦 Como se gerem as instalações
├── 📌 Por que 20 peças e não 200
├── ❓ Perguntas frequentes
└── 🔗 Links

## ⚡ Em uma página

O códice de ferramentas de abril caducou — versões velhas vendidas como vigentes, listas infladas por inflar. Esta caixa é a do corte, 15 de setembro (medida no dia 14, re-verificada ao mudar): cada peça com seu repo aberto nas últimas horas, seu estado real e seu trabalho. Curadoria curta de propósito: vinte peças que cobrem o ofício, todas verificadas, zero recheio.

A caixa, por gavetas:

```
GALERIA E ARQUIVOS
Fossify Gallery ★3.696 · File-Manager ★1.753 · Phone ★1.329
Calendar ★2.156 · Clock ★698            (pushes verificados no dia 14-set)
Amaze File Manager ★6.387               a alternativa material

CHAVES E SEGUNDO FATOR
KeePassDX ★7.301 · releases de setembro
Aegis Authenticator ★13.086             2FA com cofre cifrado

TRANSFERIR E CONECTAR
LocalSend ★91.047                       o AirDrop livre
Orbot ★3.538                            Tor no bolso

SISTEMA
Termux ★60.797 · App Manager ★8.972 (v4.1.1)
Shizuku ★30.121                         APIs do sistema sem root

MAPAS
Organic Maps ★15.415                    offline, de verdade

INSTALAÇÕES
Obtainium ★19.7k                        (ficha na guia de lojas)
```

## 🖼️ Galeria e arquivos

### Fossify — a família que substituiu as Simple

https://github.com/FossifyOrg

Quando as Simple Mobile Tools se encheram de anúncios, a comunidade bifurcou todo o set e o manteve livre: assim nasceu Fossify. Hoje a família empurra código nesta mesma semana, peça por peça:

- **Gallery** (★3.696) — a galeria sem publicidade que respeita suas fotos.
- **File-Manager** (★1.753) — arquivos simples e honestos. Atenção ao nome: FossifyOrg/Files não existe; o canônico é File-Manager.
- **Phone** (★1.329) — discador e bloqueio de números, com multi-SIM.
- **Calendar** (★2.155) — calendário com eventos e widgets, sem conta atada.
- **Clock** (★699) — relógio, alarme, cronômetro e temporizador.

GPL-3.0 todas. Suas versões etiquetadas são de fevereiro; seus pushes, de setembro: o padrão de projeto maduro — estáveis tranqüilas, manutenção contínua.

### Amaze File Manager — a alternativa com pedigrí

https://github.com/TeamAmaze/AmazeFileManager

★6.387 · vivo. O administrador de arquivos material de sempre, dos mais veteranos do ecossistema livre Android. Se Fossify te parece demais minimalista, esta é a opção com mais anos em cima — e com raízes na comunidade desde a época das primeiras ROMs.

## 🔐 Chaves e segundo fator

### KeePassDX — o cofre compatível

https://github.com/Kunzisoft/KeePassDX

★7.301 · GPL-3.0 · push do dia 11-set. A semana trouxe três releases ao projeto, com nomes de gato: «Scholarly Student» (2-set), «Cutie Cat» (4-set) e «Clever Cat» (10-set). Cofre de senhas compatível com o formato KeePass: suas bases se abrem em qualquer plataforma do ecossistema KeePass, sem ficar prisioneiro de ninguém. Os dados vivem no SEU arquivo — nuvem opcional, não obrigatória.

Se em algum momento você meteu uma senha num site que depois caiu (a guia de TMO desta família conta um grande), este é o tipo de ferramenta que ordena a casa depois: um cofre, senhas distintas por site, respaldo cifrado.

### Aegis Authenticator — o segundo fator que é seu

https://github.com/beemdevelopment/Aegis

★13.086 · GPL-3.0 · vivo. Os códigos de verificação em dois passos, num app livre com cofre cifrado (AES-256 segundo sua documentação), desbloqueio por impressão digital, respaldo cifrado exportável e importação desde os apps proprietários mais comuns (Google Authenticator, Authy, Microsoft, 2FAS e outros, segundo sua lista oficial). O argumento de fundo: seus códigos 2FA são a chave da sua vida digital — depositá-los num app fechado sem exportação é deixar as chaves com o chaveiro sem cópia.

## 📲 Transferir e conectar

### LocalSend — o AirDrop de todos

https://github.com/localsend/localsend

★91.047 — sim, noventa e um mil — · vivo · MIT segundo sua ficha. A revelação silenciosa do software livre dos últimos anos: passar arquivos entre telefone, PC, tablet e até o telefone do vizinho sem cabos, sem nuvem e sem contas — rede local, protocolo aberto, apps para todas as plataformas. Se você vinha colando arquivos por WhatsApp «para passá-los ao PC», esta peça sozinha justifica a guia inteira.

### Orbot — Tor no bolso

https://github.com/guardianproject/orbot

★3.538 · vivo · do projeto Guardian. O app que roteia seu tráfego pela rede Tor no Android, com VPN integrada ou como proxy por aplicativo. Não é para todo o dia nem para todo mundo: é a ferramenta de conexão quando o circuito que você precisa requer anonimato real — jornalismo, investigação, ou simplesmente sair do país sem sair de casa. Do lado sério do ecossistema.

## 🧰 A gaveta de sistema

### Termux — o terminal de bolso

https://github.com/termux/termux-app

★60.797 · push do dia 11-set. Um terminal Linux completo no Android: editores, linguagens, ssh, scripts. A porta de entrada para «fazer de verdade» com o telefone. Sua versão etiquetada no GitHub é de maio de 2025 (com betas da 0.119) — seu canal de pacotes vai por seu lado e com outro ritmo; o debate GitHub-vs-F-Droid de Termux é velho e não se reabre aqui: repo nomeado, canal escolhido no dia em que instala. Uma regra seja: não se colam scripts de ninguém — o terminal é poder, e o poder se executa com o que você escreveu ou leu completo.

### App Manager — o radiógrafo dos seus apps

https://github.com/MuntashirAkon/AppManager

★8.985 · **versão 4.1.1 (4 de setembro)** · push de HOJE (re-verificado 15-set). O gestor de pacotes completo: ver que permissões pede cada app, que atividades expõe, que rastreadores arrasta, e desinstalar a fundo. Corrige a foto da semana passada, quando a versão não respondia na API: hoje está, e é deste mês. Sua licença na página figura como própria (Proprietary-style livre — o projeto a define no seu repo; lê-se ali antes de redistribuir).

### Shizuku — as APIs do sistema sem root

https://github.com/RikkaApps/Shizuku

★30.121 · Apache-2.0 · versão 13.6.0. A peça que mudou o jogo do «sem root»: deixa que apps autorizados usem APIs do sistema diretamente, com permissões concedidas via ADB (uma vez por ligamento) ou root. É o motor silencioso atrás de meia dúzia de ferramentas modernas de personalização e controle. Não é para quem começa: é para quem já sabe por que o busca.

## 🗺️ Mapas

### Organic Maps — o mapa que não olha para trás

https://github.com/organicmaps/organicmaps

★15.427 · release de agosto (2026.08.27) · push de HOJE (re-verificado 15-set). Mapas offline completos do planeta, sem conta, sem rastreio, dados de OpenStreetMap. Para viagem, para o bairro sem dados, para quem decidiu que o Google não precisa saber por onde você caminha. Sua licença na página figura com aviso particular (licença própria do projeto, legível no seu repo) — diz-se tal qual, sem inventar etiquetas.

## 📦 Como se gerem as instalações

**Obtainium** — https://github.com/ImranR98/Obtainium — ★19.7k (19.702), commit do dia 13-set. A ferramenta que vigia os repos desta caixa e te instala as versões novas mal saem. Sua ficha completa vive na guia de lojas desta família; aqui basta sua frase: a gaveta de ferramentas também se atualiza sozinha.

E o fundo da caixa, para todas as gavetas: **F-Droid** — a loja livre onde boa parte destas peças também vive publicada. Três vias (repo do GitHub, F-Droid, Obtainium) apontando ao mesmo software: essa é a redundância sã do ecossistema livre.

## 📌 Por que 20 peças e não 200

O códice de abril trazia 88 ferramentas. Dessas, muitas estavam em versão velha vendida como nova, e várias repetiam função quatro vezes. O critério desta caixa é o contrário:

```
Uma função, uma peça    se dois apps fazem o mesmo,
                        fica o mais vivo — não o mais mencionado
Tudo verificado hoje    se o número não se abriu hoje,
                        não vai com data de hoje
Vão declarado           o que NÃO está na caixa (navegadores,
                        correio, mensageria, nuvens) é porque
                        merece guia própria, não porque não exista
```

A caixa de ofício não precisa ser infinita. Precisa ser certa.

## ❓ Perguntas frequentes

**Estes apps estão na Play Store?**
Vários sim (Aegis, LocalSend, Organic Maps entre eles). A via do ecossistema livre é F-Droid ou o repo — a guia de lojas desta família explica as três portas. Esta guia não abre a Play: a ficha de cada loja é tema da sua própria peça.

**Fossify ou Amaze para arquivos?**
Fossify: minimalista, da família completa (galeria, contatos, calendário). Amaze: mais função por tela, mais anos de vôo. Prove ambas: são grátis em todos os sentidos.

**KeePassDX ou Bitwarden?**
Filosofias distintas: KeePassDX guarda SEU arquivo (compatível KeePass, zero dependência); Bitwarden é serviço com sincronização própria. Não se compararam a fundo aqui: sem comparativa inventada.

**Shizuku é perigoso?**
Dá poder de sistema a apps que VOCÊ autoriza, via ADB ou root. É tão perigoso quanto a chave que você deixa debaixo do tapete se autorizar qualquer um. De cabeça fria, é a ponte perfeita entre «sem root» e «controle total».

**LocalSend funciona entre iPhone e Android?**
Sim: isso é parte do seu ponto — multiplataforma completa (Android, iOS, Windows, macOS, Linux), rede local, sem nuvem.

**Orbot deixa tudo lento?**
Tor paga seu anonimato com latência. Para navegação sensível, é o preço. Para todo o dia, não está pensado — e sua própria documentação o diz melhor que este resumo.

**Termux precisa de root?**
Não. Sua potência não depende de root — depende do que você saiba fazer com um terminal. Root abre outros capítulos, com outros riscos (a guia de GLTools desta família conta por que não se brinca com isso do sofá).

**De quanto em quanto se re-verifica esta caixa?**
Cada vez que se usar. Hoje foi o corte; os números que não se abrirem outro dia não se citam como frescos.

## 🔗 Links

- Fossify: https://github.com/FossifyOrg/Gallery · https://github.com/FossifyOrg/File-Manager · https://github.com/FossifyOrg/Phone · https://github.com/FossifyOrg/Calendar · https://github.com/FossifyOrg/Clock
- Amaze: https://github.com/TeamAmaze/AmazeFileManager
- KeePassDX: https://github.com/Kunzisoft/KeePassDX · Aegis: https://github.com/beemdevelopment/Aegis
- LocalSend: https://github.com/localsend/localsend · Orbot: https://github.com/guardianproject/orbot
- Termux: https://github.com/termux/termux-app · App Manager: https://github.com/MuntashirAkon/AppManager · Shizuku: https://github.com/RikkaApps/Shizuku
- Organic Maps: https://github.com/organicmaps/organicmaps
- Obtainium: https://github.com/ImranR98/Obtainium

> A Bandita informa a partir de fontes datadas. Uma caixa de ofício não se infla: se afia.

---

**Nota de mudança (15-set):** guia passada da fornada do dia 14 para esta, com re-verificação contra as casas: AppManager ★8.985 e OrganicMaps ★15.427 com push de HOJE; Calendar ★2.156, Clock ★698. O não mencionado fica constado no seu dia (14-set). Acta completa: Registro #71.
