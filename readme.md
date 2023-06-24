# Projeto de Scraping de Dados com Airflow, Postgres e Metabase

- [ ] Falta testa a consistencia do metabase!

## Visão Geral
Este projeto realiza o scraping de dados de anúncios de celulares em sites de venda online usando o Airflow e armazena esses dados em um banco de dados Postgres. Além disso, os dados coletados podem ser visualizados e analisados usando o Metabase. O Airflow é usado para agendar e gerenciar a execução do script de scraping, o Postgres é usado como banco de dados e o Metabase é usado para a visualização dos dados.

## Como usar

### Pré-requisitos
- [Docker](https://www.docker.com/products/docker-desktop) e [Docker Compose](https://docs.docker.com/compose/install/) instalados na sua máquina.

### Passos

1. Clone este repositório no seu computador.

```bash
git clone https://link_para_o_repositorio.git
cd nome_do_repositorio
```

2. Inicialize os serviços usando Docker Compose.

```bash
docker-compose up
```

### Como acessar os serviços

- **Airflow**: Abra um navegador e acesse `localhost:8080`. O Airflow irá agendar e executar a tarefa de scraping.

- **Postgres**: O Postgres estará disponível na porta 5432. Você pode conectar-se a ele usando o usuário `postgres` e a senha `123456789`.

- **Metabase**: Abra um navegador e acesse `localhost:3000`. Na primeira vez que você acessar o Metabase, será solicitado que você crie uma conta. Use esta conta para acessar o Metabase nas próximas vezes. Você pode conectar o Metabase ao Postgres para visualizar os dados coletados.

### Persistência de Dados

Os dados do Metabase são persistentes e serão armazenados na pasta `metabase-data` no mesmo diretório do seu arquivo `docker-compose.yml`.