# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_CLI_TOKEN
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo:** João Paulo Mendes de Souza
- **GitHub:** https://github.com/JPauloMendes

---

## Visão Geral da Solução

Descreva, em poucas palavras:

- Qual é o objetivo do seu projeto: O objetivo é simular um sistema de monitoramento ambiental e de acesso para ambientes controlados. O sistema dispara alertas caso uma porta fique aberta por muito tempo ou se houver uma variação brusca na temperatura do local.
- O que o sistema embarcado simulado faz: Ele lê continuamente os dados térmicos do sensor MPU6050 e o estado físico de um botão. Se a porta ficar aberta por mais de 5 segundos, ou se a temperatura variar 3°C em relação à temperatura de referência inicial, alarmes são ativados. O sistema também é capaz de se "normalizar" sozinho quando as condições voltam ao ideal.
- Como o usuário interage com ele (se aplicável): O usuário pressiona o botão no Wokwi para simular o fechamento da porta (estado 1) ou solta para simular a abertura (estado 0). A temperatura é alterada manipulando o próprio sensor no simulador.

---

## Arquitetura do Sistema Embarcado

Explique a arquitetura lógica do seu projeto, abordando:

- Fluxo principal do programa (`main.py`): O script começa capturando uma temperatura base (temperatura_referencia) e depois entra em um loop infinito. Dentro do loop, ele realiza três blocos principais de checagem: o estado da porta, a variação térmica (delta_t) e a verificação de normalização.
- Estrutura de estados, loops ou temporizações: Para a porta, uso a função time.ticks_diff() para contar o tempo de abertura de forma não-bloqueante, disparando o alerta ao atingir o limite de 5000ms. Quando o sistema detecta que os alarmes podem ser desligados, ele usa um pequeno time.sleep(0.6) apenas para garantir a estabilidade antes de resetar o status.
- Como os componentes interagem entre si: O microcontrolador (ESP32) lê a tensão do botão (GPIO 4) e solicita diretamente os registradores de memória do MPU6050 (via I2C) para calcular a temperatura em graus Celsius através de decodificação de bytes.

Se desejar, utilize tópicos ou um pequeno diagrama em texto.

---

## Componentes Utilizados na Simulação

Liste os principais componentes definidos no `diagram.json`, por exemplo:

- Tipo de placa utilizada: ESP32 (Microcontrolador principal que executa a lógica em MicroPython).
- Sensor (MPU6050): Alimentado pelo 3V3 do ESP32 e conectado aos pinos 21 (SDA) e 22 (SCL). Utilizado exclusivamente para capturar a temperatura do ambiente.
- Botão (Pushbutton verde): Conectado no pino 3V3 de um lado e no GPIO 4 do outro. Foi configurado no código com um resistor interno (Pin.PULL_DOWN), o que significa que ele lê 0 (aberto) quando solto e 1 (fechado) quando pressionado.

---

## Decisões Técnicas Relevantes

Explique brevemente decisões importantes tomadas durante o desenvolvimento, como:

- Leitura direta da memória: Em vez de usar bibliotecas pesadas de terceiros para o MPU6050, optei por ler os bytes brutos da memória I2C (i2c.readfrom_mem) e decodificá-los com a biblioteca struct. Isso deixa o firmware mais leve e direto.
- Tolerância a falhas: Implementei blocos try/except na leitura do sensor. Caso ocorra alguma falha de comunicação no barramento I2C durante o loop, o código assume a temperatura de referência para não quebrar a execução ou gerar falsos positivos.
- Constantes de calibração: Os limites de ativação foram abstraídos em constantes (LIMITE_TEMPO_X = 5000 e LIMITE_VARIACAO_Y = 3.0), o que facilita muito a manutenção ou a mudança da "regra de negócio" do monitoramento no futuro.

---

## Resultados Obtidos

Descreva o comportamento final do sistema:

- O que funciona corretamente: A detecção de tempo de porta aberta e o cálculo de variação térmica em tempo real funcionam perfeitamente. O sistema entra em estado de alerta e consegue resetar (Status: Sistema Normalizado) sozinho quando a porta fecha e a temperatura estabiliza.
- Quais requisitos foram atendidos: O monitoramento contínuo, a lógica de temporização não-bloqueante para a porta e a integração do I2C foram 100% cumpridos.
- Resultado observado na simulação do Wokwi: O circuito no Wokwi reflete perfeitamente as regras propostas, exibindo os alertas corretos no terminal Serial quando as variáveis ultrapassam as constantes estabelecidas.

---

## Comentários Adicionais (Opcional)

Utilize este espaço para comentar, se desejar:

- Dificuldades encontradas: Manipular dados brutos (bytes) via I2C e convertê-los matematicamente para graus Celsius usando a equação técnica do datasheet do MPU6050 exigiu um pouco mais de atenção aos detalhes do que usar uma biblioteca pronta.
- Melhorias que você faria com mais tempo: Implementaria um display ou um LED RGB físico no circuito para dar feedback visual instantâneo dos alarmes, sem depender exclusivamente da saída de texto no terminal.
- Principais aprendizados durante o desafio: Foi uma ótima oportunidade para lidar com leitura de baixo nível (registradores de memória do hardware) e criar uma lógica robusta de tolerância a falhas (try/except) em sistemas embarcados.

---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
