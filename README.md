# Data Mission - Fluxo de Dados e Dashboard

Este projeto automatiza a ingestão de dados da API Data Mission, processa-os usando dbt e DuckDB, e apresenta um dashboard analítico com Streamlit.

## Componentes

1.  **APScheduler (Scheduler):** Gerencia o download periódico de dados brutos da API.
2.  **dbt (Data Build Tool):** Transforma os arquivos JSON brutos em tabelas relacionais (DuckDB) com lógica de negócio (prioridades e atrasos).
3.  **DuckDB:** Banco de dados analítico embarcado onde as tabelas processadas pelo dbt são armazenadas.
4.  **Streamlit:** Interface visual para monitoramento em tempo real das entregas.

---

## Passo a Passo para Execução

### 1. Preparação do Ambiente

Crie e ative o ambiente virtual, depois instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuração

Crie um arquivo `.env` na raiz do projeto (ou edite o existente):

```env
API_BASE_URL=https://api.datamission.com.br
DEFAULT_PROJECT_ID=seu_projeto_id
JOB_INTERVAL_MINUTES=60
```

### 3. Execução do Fluxo Completo

O serviço principal inicia o agendador que baixa os dados e aciona o dbt automaticamente:

```bash
# Terminal 1: Iniciar o Agendador e Ingestão
python main.py
```

### 4. Visualização do Dashboard

Com os dados processados, inicie o Streamlit:

```bash
# Terminal 2: Iniciar o Dashboard
streamlit run app.py
```

---

## Estrutura de Modelagem dbt

- **Staging (`stg_deliveries`):** Lê os arquivos JSON da pasta `downloads/` usando a função `read_json_auto` do DuckDB.
- **Marts (`fct_deliveries`):** Aplica macros de lógica de negócio:
    - **Prioridade:** Calculada com base no tempo restante até o deadline (CRITICAL, HIGH, MEDIUM, LOW).
    - **Status:** Determina se a entrega está no prazo, atrasada ou pendente.
    - **Atraso:** Cálculo em minutos entre o deadline e a entrega real.

---

## Logs e Auditoria

- Metadados de cada download (tamanho, status, erros) são salvos em `logs/execution_metadata.jsonl`.
- Dados brutos versionados são salvos em `downloads/dataset_{project_id}_{timestamp}.json`.
