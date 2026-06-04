# PDF RAG Pipeline

### 📌 Visão Geral

>O **PDF RAG Pipeline** é uma plataforma de processamento documental e recuperação inteligente de conhecimento baseada em **Retrieval-Augmented Generation (RAG)**.
>
>Este projeto surgiu como uma evolução do projeto **[PDF Parser Pipeline](https://github.com/GabrielSousaFarias/PDF_Parser_Pipeline)**, cuja proposta inicial era realizar o processamento assíncrono de documentos PDF utilizando FastAPI, Apache Kafka e Python. Nesta nova versão, a solução expande significativamente suas capacidades ao incorporar uma camada de Inteligência Artificial capaz de transformar documentos em uma base de conhecimento pesquisável.
>
>Após o processamento dos arquivos, o conteúdo é extraído, estruturado, segmentado em unidades menores de informação (*chunks*), convertido em embeddings vetoriais e armazenado em um banco vetorial. A partir desse momento, os documentos deixam de ser apenas arquivos estáticos e passam a compor uma base de conhecimento capaz de responder perguntas em linguagem natural por meio de busca semântica.
>
>O projeto demonstra conceitos modernos de Engenharia de Dados, IA Generativa, Processamento de Documentos e Arquiteturas Orientadas a Conhecimento, simulando cenários reais encontrados em assistentes corporativos, plataformas de suporte à decisão e sistemas de busca inteligente.



### 🎯 Objetivo

Construir uma solução escalável para processamento documental e recuperação semântica de informações, permitindo transformar documentos PDF em uma base de conhecimento pesquisável e pronta para integração com Large Language Models (LLMs).

### 🚀 Problema Resolvido

Empresas acumulam diariamente grandes volumes de documentos contendo informações relevantes para suas operações:

* Manuais técnicos
* Contratos
* Relatórios
* Procedimentos internos
* Documentação de sistemas
* Materiais de treinamento

Embora essas informações estejam disponíveis, muitas vezes sua localização é lenta e depende de consultas manuais.

O PDF RAG Pipeline resolve esse problema ao permitir que os documentos sejam pesquisados por significado e contexto, reduzindo o tempo necessário para localizar informações e aumentando o aproveitamento do conhecimento organizacional.



### 🏗 Arquitetura da Solução

```text
Usuário
   │
   ▼
FastAPI
   │
   ▼
PDF Upload
   │
   ▼
Parser Engine
   │
   ▼
Text Chunking
   │
   ▼
Embedding Model
   │
   ▼
Vector Database
   │
   ▼
Semantic Search
   │
   ▼
RAG Response
```


### 🔄 Fluxo de Processamento

1. O usuário envia um documento PDF.
2. O conteúdo textual é extraído.
3. O texto é dividido em chunks.
4. Cada chunk é convertido em embedding vetorial.
5. Os embeddings são armazenados em um banco vetorial.
6. O usuário realiza perguntas em linguagem natural.
7. O mecanismo de busca semântica recupera os trechos mais relevantes.
8. As informações recuperadas são utilizadas para compor a resposta do sistema.


### 📚 Base de Conhecimento Utilizada

Para demonstração do pipeline, foi utilizado o livro:

**Lógica de Programação para Iniciantes**

O material permite validar consultas semânticas relacionadas a:

* Algoritmos
* Lógica de programação
* Estruturas condicionais
* Estruturas de repetição
* Conceitos fundamentais de desenvolvimento de software

Exemplos de perguntas:

```text
O que é um algoritmo?

Qual a diferença entre compilador e interpretador?

Como funcionam estruturas de repetição?

Por que aprender lógica de programação?
```


### ⚙ Tecnologias Utilizadas

- Backend
    * Python
    * FastAPI
    * Uvicorn
- Processamento de Documentos
    * PyMuPDF
- Inteligência Artificial
    * Sentence Transformers
    * Embeddings
    * Retrieval-Augmented Generation (RAG)
- Banco Vetorial
    * ChromaDB
- Infraestrutura
    * Docker
    * Docker Compose
- Arquitetura
    * Knowledge Retrieval
    * Semantic Search
    * Vector Search
    * AI Ready Architecture
    * Microservices Ready


### 📊 Principais Benefícios

#### Busca Semântica

Permite localizar informações com base no significado e contexto das perguntas.

#### Reaproveitamento do Conhecimento

Transforma documentos estáticos em bases de conhecimento reutilizáveis.

#### Escalabilidade

Novos documentos podem ser adicionados continuamente sem necessidade de reprocessar toda a base.

#### Integração com IA

Estrutura preparada para utilização com Large Language Models.

#### Flexibilidade

Pode ser utilizado em diferentes cenários corporativos, educacionais e analíticos.


### 💼 Casos de Uso

* Assistentes corporativos
* Busca inteligente em documentação técnica
* Consulta de manuais operacionais
* Bases de conhecimento internas
* Plataformas educacionais
* Sistemas de suporte ao cliente
* Pesquisa em contratos e regulamentos
* Chatbots especializados


#### 🚧 Próximas Evoluções

* Integração com LLMs locais utilizando Ollama
* Suporte a múltiplos documentos simultaneamente
* OCR com Tesseract
* Extração automática de entidades
* Reranking de resultados
* Banco vetorial distribuído
* Observabilidade com OpenTelemetry
* Deploy em Kubernetes
* Interface Web para consultas
* Sistema de autenticação e autorização
* Histórico de conversas e consultas


### 💡 Competências Demonstradas

Este projeto demonstra conhecimentos em:

* Engenharia de Dados
* Inteligência Artificial Generativa
* Retrieval-Augmented Generation (RAG)
* Processamento de Documentos
* Embeddings Vetoriais
* Bancos Vetoriais
* FastAPI
* Python
* ChromaDB
* Arquiteturas Escaláveis
* Busca Semântica
* Arquiteturas Orientadas a Conhecimento

## 👨‍💻 Autor

<p align="left">
  <img align="left" width="150" src="https://raw.githubusercontent.com/GabrielSousaFarias/GabrielSousaFarias/main/Analista%20de%20dados%20senior.png">
 <br>
  Sou <strong>Gabriel Sousa - Analista de Dados Sênior</strong> apaixonado por dados, automação e tecnologia.

  Atuo na construção de soluções que transformam dados em decisões estratégicas por meio de dashboards, pipelines de dados, automações e aplicações baseadas em Inteligência Artificial.

  Possuo experiência em Inteligência Artificial, Machine Learning, RAG, LLM's, Business Intelligence, Engenharia de Dados, Python, SQL, Databricks, Airflow, DBT e Power BI, sempre buscando desenvolver soluções escaláveis, eficientes e orientadas a resultados.
</p>

Este projeto foi desenvolvido para explorar padrões amplamente utilizados em ambientes corporativos modernos.

📫 Vamos nos conectar:

- LinkedIn: [Acessar](https://www.linkedin.com/in/gabriel-sousa/)
- GitHub: [Acessar](https://github.com/GabrielSousaFarias)

⭐ Se o projeto foi útil, deixe uma estrela no repositório.
