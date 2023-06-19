Claro! Aqui está a mesma documentação em Markdown reescrita de forma mais elegante:

## Referências
- [Como rodar um banco de dados Postgres com Docker](https://felixgilioli.medium.com/como-rodar-um-banco-de-dados-postgres-com-docker-6aecf67995e1)
- [Astro CLI](https://github.com/astronomer/astro-cli)
- [Running Metabase on Docker](https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-docker)

## Comandos

### Iniciar serviço cron
```shell
sudo service cron start
```

### Configurar crontab
```shell
crontab -e
```

### Criar ambiente virtual e ativar
```shell
python3 -m venv myenv
source myenv/bin/activate
```
OBS: existe um arquivo chamado requirements.txt que irá permitir que você crie um ambiente com as exatas configurações. 
OBS: A versão do python utilizada está escrita em runtime.txt


### Instalar Apache Airflow
```shell
pip install apache-airflow
```

### Inicializar o banco de dados do Airflow
```shell
airflow db init
```

### Iniciar o servidor web do Airflow
```shell
airflow webserver -p 8080
```

### Iniciar o agendador do Airflow
```shell
airflow scheduler
```

### Criar usuário no Airflow
```shell
source myenv/bin/activate
airflow users create --username \<usuario\> --firstname \<nome\> --lastname \<sobrenome\> --role Admin --email \<email\> --password \<senha\>

exemplo:
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin
```

## Pasta para arquivos do Airflow
O local onde os arquivos devem ser colocados para funcionar corretamente é: `~/airflow/dag`
copie o conteudo de __dag__.py presente na pasta 'crawler' e cole aqui

