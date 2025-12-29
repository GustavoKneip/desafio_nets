# Desafio Netshoes

## 📌 Visão Geral

Este projeto é uma solução para o **Desafio Netshoes**, utilizando **Apache Kafka** para processamento e distribuição de eventos.  
A aplicação recebe um payload via API, publica a mensagem em um tópico Kafka principal e, a partir disso, um **processor** consome e divide esse payload em múltiplos tópicos, que são então consumidos por diferentes consumidores (simulados por scripts *demo*).

A arquitetura foi pensada para ser **escalável, desacoplada e extensível**, permitindo fácil adaptação para novos payloads ou novos tipos de eventos.

---

## 🏗️ Arquitetura

- **API**: Responsável por receber o payload via HTTP e produzir a mensagem no Kafka.
- **Processor**: Consome o tópico principal, processa o payload e o divide em múltiplos tópicos.
- **Kafka + Zookeeper**: Responsáveis pela mensageria e orquestração dos eventos.
- **Consumers Demo**: Simulam consumidores finais para cada tópico gerado.
- **Shared**: Código compartilhado entre API e Processor (schemas, producers, consumers e configurações).

Cada aplicação roda em seu **próprio container Docker**, seguindo boas práticas de arquitetura orientada a eventos.

---

## 📁 Estrutura do Projeto

```

desafio_nets
├── create_env.bat           # Script para criação do ambiente virtual Python
├── run_demo.bat             # Script para subir o projeto e executar os consumidores demo
├── app/
│   ├── docker-compose.yml   # Configuração dos containers (Kafka, Zookeeper, API e Processor)
│   ├── requirements.txt     # Dependências do projeto
│   ├── api/
│   │   ├── Dockerfile       # Dockerfile da API
│   │   └── main.py          # Implementação da API
│   ├── demo/
│   │   ├── itemConsumerDemo.py
│   │   ├── orderConsumerDemo.py
│   │   ├── orderProducerDemo.py
│   │   └── paymentInfoConsumerDemo.py
│   ├── processor/
│   │   ├── Dockerfile       # Dockerfile do Processor
│   │   └── main.py          # Implementação do Processor
│   └── shared/
│       ├── config/          # Configurações do Kafka
│       ├── consumers/       # Consumers base
│       ├── data/            # Payloads de exemplo fornecidos no desafio
│       ├── producers/       # Producers base
│       └── schemas/         # Schemas dos tópicos Kafka
└── tests/
├── test_base_consumer.py
├── test_base_processor.py
└── test_base_producer.py

````

---

## ▶️ Como Rodar o Projeto

### Pré-requisitos

Antes de iniciar, certifique-se de que possui:

1. **Python 3.10 ou superior**
2. **Docker** e **Docker Compose** instalados e em execução
3. Sistema operacional **Windows** (scripts `.bat`)

---

### Execução

Para rodar o projeto, execute o seguinte arquivo na raiz do repositório:

```bash
run_demo.bat
````

Este script irá:

* Criar o ambiente virtual Python
* Instalar as dependências
* Subir os containers Docker (Zookeeper, Kafka, API e Processor)
* Executar os consumidores *demo* para simulação do processamento

---

## 🔄 Fluxo de Execução

1. O usuário envia um payload JSON para a API.
2. A API publica a mensagem no tópico Kafka **`main`**.
3. O Processor consome o tópico **`main`**.
4. O Processor divide o payload com base nos **schemas** definidos.
5. Cada parte do payload é publicada em seu respectivo tópico.
6. Os consumidores *demo* consomem esses tópicos e exibem os dados processados.

> ⚠️ A API retorna apenas a confirmação de produção da mensagem no Kafka.
> Não há retorno do processamento dos consumidores.

---

## 🌐 Endpoints da API

### Enviar evento para processamento

```
POST http://localhost:8000/events/main
```

* **Body**: JSON
* **Content-Type**: `application/json`
* Produz a mensagem no tópico `main`

---

### Health Check

```
GET http://localhost:8000/health
```

* Retorno: `200 OK`
* Usado para verificação de disponibilidade da API

---

## 🧪 Testes

O projeto possui testes unitários para as principais entidades:

* Producers
* Consumers
* Processor

Os testes foram implementados utilizando **pytest**.

### Executando os testes

A partir do diretório `app`, execute:

```bash
pytest -v
```

---

## 🚀 Considerações Finais

* Arquitetura orientada a eventos com Kafka
* Código genérico e extensível para novos payloads
* Separação clara de responsabilidades
* Uso de Docker para padronização de ambiente
* Testes unitários para garantir estabilidade da solução

---

**Autor:** Gustavo Cunha
**Desafio:** Netshoes