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



docker build -t my-airflow-image . 

docker run --rm --name my_airflow_container -p 8080:8080 my-airflow-image
docker run -it --name my_airflow_container my-airflow-image bash


docker run -d -p 8080:8080 my-airflow-image


Histórico
1820  clear
 1821  git config --global user.name
 1822  git config --global user.name "henrique-personal"
 1823  git config --global user.name
 1824  git status
 1825  git add .
 1826  git commit -m 'changes'
 1827  git push -u origin main
 1828  git remote add origin github-pessoal:git@github.com:rickymal/solid-fiesta.git
 1829  git remote remove origin
 1830  git remote add origin github-pessoal:git@github.com:rickymal/solid-fiesta.git
 1831  git push -u origin master
 1832  git push -u origin main
 1833  git remote remove origin
 1834  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1835  git push -u origin main
 1836  git remote remove origin
 1837  git remote add origin git@github.com:rickymal/solid-fiesta.git
 1838  git push -u origin main
 1839  git remote remove origin
 1840  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1841  git push -u origin main
 1842  git remote add origin git@github.com-pessoal:rickymal/solid-fiesta.git
 1843  git remote remove origin
 1844  git remote add origin git@github.com-pessoal:rickymal/solid-fiesta.git
 1845  git status
 1846  git config --global
 1847  git config --global user.name
 1848  git config user.name
 1849  git config user.email
 1850  git push -u origin main
 1851  exit
 1852  es1
 1853  git remote remove origin
 1854  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1855  git push -u origin main
 1856  ssh-add ~/.ssh/id_ed_for_github_01
 1857  GIT_SSH_COMMAND='ssh -i ~/.ssh/id_ed_for_github_01' git push -u origin main
 1858  alias gitp='GIT_SSH_COMMAND='ssh -i ~/.ssh/id_ed_for_github_01' git push -u origin main'
 1859  git push -u origin main
 1860  git status
 1861  git branch -l
 1862  git fetch
 1863  git branch -l
 1864  git push -u origin main
 1865  cd .ssh
 1866  ls
 1867  cat id_ed_for_github_01
 1868  cat id_ed_for_github_01.pub
 1869  ls
 1870  nano config
 1871  ls
 1872  nano config
 1873  cat config
 1874  nano config
 1875  cat config
 1876  git remote remove origin
 1877  nano config
 1878  cat config
 1879  nano config
 1880  cat config
 1881  sl | grep m_
 1882  sl
 1883  ls -la
 1884  cat config
 1885  chmod 600 config
 1886  ls -la
 1887  ls -l
 1888  chmod 600 id_ed_for_github_01
 1889  ssh -T git@github-pessoal
 1890  ssh -Tv git@github-pessoal
 1891  git config core.sshCommand
 1892  ssh-add ~/.ssh/id_ed_for_github_01
 1893  ls -la
 1894  cat id_ed25519.pub
 1895  cat id_ed_for_github_01.pub
 1896  cat config
 1897  ls -la
 1898  cat config
 1899  cd
 1900  cd ~/.ssh
 1901  ls
 1902  ls -la
 1903  nano config
 1904  clear
 1905  es1
 1906  xit
 1907  exit
 1908  irb
 1909  clear
 1910  rvm list
 1911  clear
 1912  exit
 1913  wsl
 1914  cd ~
 1915  cd .ssh
 1916  ls
 1917  ls -la
 1918  cat edgmail.pub
 1919  nano con
 1920  nano config
 1921  ls
 1922  nano sshd_config
 1923  ls -la
 1924  ls
 1925  nano config
 1926  clear
 1927  ls
 1928  nano config
 1929  mkdir crawler
 1930  cd crawler/
 1931  git clone git@github.com:rickymal/solid-fiesta.git
 1932  ls
 1933  cd solid-fiesta/
 1934  cd ..
 1935  code .
 1936  cd solid-fiesta/
 1937  code .
 1938  ls
 1939  git commit -a -m "changes"
 1940  git add .
 1941  git status
 1942  git commit -m 'changes'
 1943  git push -u origin main
 1944  ls
 1945  git branch 0
 1946  git branch l
 1947  git branch -l
 1948  git push -u origin master
 1949  cd ..
 1950  rm solid-fiesta/
 1951  rm -r solid-fiesta/
 1952  ls
 1953  ls -al
 1954  git clone git@github.com-pessoal:rickymal/solid-fiesta.git
 1955  ssh-add ~/.ssh/id_ed_for_github_01
 1956  eval "$(ssh-agent -s)"
 1957  ssh-add ~/.ssh/id_ed_for_github_01
 1958  ls
 1959  ls -la
 1960  git@github.com-pessoal:rickymal/solid-fiesta.git
 1961  git clone git@github.com-pessoal:rickymal/solid-fiesta.git
 1962  git clone git@github.com:rickymal/solid-fiesta.git
 1963  ls
 1964  cd solid-fiesta/
 1965  git remote remove origin
 1966  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1967  ls
 1968  git branch -0l
 1969  git branch -l
 1970  ls
 1971  touch readme.md
 1972  ls
 1973  nano readme.md
 1974  cat readme.md
 1975  git branch -l
 1976  git push -u origin main
 1977  git status
 1978  git add .
 1979  git commit -m 'changes'
 1980  git branch -l
 1981  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1982  cd .
 1983  ls -la
 1984  cd .git/
 1985  ls
 1986  cat config
 1987  git push -u origin master
 1988  cd ..
 1989  code .
 1990  docker-compose --version
 1991  es1
 1992  clear
 1993  es1
 1994  clear
 1995  es1
 1996  exit
 1997  clear
 1998  docker build -t my-airflow-image .
 1999  ls -la
 2000  docker build -t my-airflow-image .
 2001  docker run -p 8080:8080 my-airflow-image
 2002  docker build -t my-airflow-image .
 2003  docker run -p 8080:8080 my-airflow-image
 2004  docker build -t my-airflow-image .
 2005  docker run -p 8080:8080 my-airflow-image
 2006  docker build -t my-airflow-image .
 2007  docker run -p 8080:8080 my-airflow-image
 2008  clear
 2009  docker run --name my-airflow -p 8080:8080 my-airflow-image
 2010  clear
 2011  docker run --name my-airflow -p 8080:8080 my-airflow-image
 2012  docker build -t my-airflow-image .
 2013  ls -la
 2014  docker build -t my-airflow-image .
 2015  docker run --name my-airflow -p 8080:8080 my-airflow-image
 2016  docker rm my-airflow
 2017  docker build -t my-airflow-image .
 2018  docker run --name my-airflow -p 8080:8080 my-airflow-image
 2019  ls -la
 2020  clear
 2021  docker build -t my-airflow-image .
 2022  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 2023  docker build -t my-airflow-image .
 2024  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 2025  docker run --rm --name my_airflow_container -p 8080:8080 my-airflow-image
 2026  docker rm my_airflow_container
 2027  docker run --rm --name my_airflow_container -p 8080:8080 my-airflow-image
 2028  ls -la
 2029  docker build -t my-airflow-image .
 2030  docker rm my_airflow_container
 2031  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 2032  docker exec my_airflow_container cat /var/log/airflow/webserver.log
 2033  docker rm my_airflow_container
 2034  docker build -t my-airflow-image .
 2035  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 2036  docker run -it --name my_airflow_container my-airflow-image bash
 2037  docker rm my_airflow_container
 2038  docker run -it --name my_airflow_container my-airflow-image bash
 2039  clear
 2040  docker rm my_airflow_container
 2041  docker build -t my-airflow-image .
 2042  docker run -it --name my_airflow_container my-airflow-image
 2043  docker exec -it my_airflow_container bash
 2044  docker run -it --name my_airflow_container my-airflow-image bash
 2045  docker rm my_airflow_container
 2046  docker run -it --name my_airflow_container my-airflow-image bash
 2047  ls -la
 2048  clear
 2049  docker rm my_airflow_container
 2050  docker build -t my-airflow-image .
 2051  docker run -it --name my_airflow_container my-airflow-image
 2052  docker ps -a
 2053  docker logs 94b10cc53dcb
 2054  docker exec -it 94b10cc53dcb airflow scheduler
 2055  docker start 94b10cc53dcb
 2056  docker exec -it 94b10cc53dcb airflow scheduler
 2057  docker exec -it 94b10cc53dcb airflow db init
 2058  docker exec -it 94b10cc53dcb bash
 2059  clear
 2060  ./docker.sh


 0  git branch -l
 1841  git push -u origin master
 1842  cd ..
 1843  rm solid-fiesta/
 1844  rm -r solid-fiesta/
 1845  ls
 1846  ls -al
 1847  git clone git@github.com-pessoal:rickymal/solid-fiesta.git
 1848  ssh-add ~/.ssh/id_ed_for_github_01
 1849  eval "$(ssh-agent -s)"
 1850  ssh-add ~/.ssh/id_ed_for_github_01
 1851  ls
 1852  ls -la
 1853  git@github.com-pessoal:rickymal/solid-fiesta.git
 1854  git clone git@github.com-pessoal:rickymal/solid-fiesta.git
 1855  git clone git@github.com:rickymal/solid-fiesta.git
 1856  ls
 1857  cd solid-fiesta/
 1858  git remote remove origin
 1859  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1860  ls
 1861  git branch -0l
 1862  git branch -l
 1863  ls
 1864  touch readme.md
 1865  ls
 1866  nano readme.md
 1867  cat readme.md
 1868  git branch -l
 1869  git push -u origin main
 1870  git status
 1871  git add .
 1872  git commit -m 'changes'
 1873  git branch -l
 1874  git remote add origin git@github-pessoal:rickymal/solid-fiesta.git
 1875  cd .
 1876  ls -la
 1877  cd .git/
 1878  ls
 1879  cat config
 1880  git push -u origin master
 1881  cd ..
 1882  code .
 1883  docker-compose --version
 1884  es1
 1885  clear
 1886  es1
 1887  clear
 1888  es1
 1889  exit
 1890  clear
 1891  es1
 1892  clear
 1893  es1
 1894  clear
 1895  es1
 1896  exit
 1897  es1
 1898  exit
 1899  cd
 1900  ls
 1901  cd Ubuntu\ Workspace/
 1902  ls
 1903  cd Speedio/
 1904  ls
 1905  cd ..
 1906  ls
 1907  git clone git@github.com:SPD-Atlas-App/Atlas-Api-V3.git atlas-backend-rails
 1908  cd atlas-backend-rails/
 1909  ls
 1910  code .
 1911  clear
 1912  es1
 1913  exit
 1914  clear
 1915  es1
 1916  clear
 1917  es1
 1918  exit
 1919  docker stop my_airflow_container
 1920  dockerp s
 1921  docker ps
 1922  docker stop my-airflow-image
 1923  docker stop thirsty_hermann
 1924  docker stop my-airflow
 1925  cslear
 1926  clear
 1927  docker stop my-airflow
 1928  docker rm my-airflow
 1929  docker stop my-airflow
 1930  docker ps
 1931  docker logs c7fa105f32a4
 1932  clear
 1933  docker build -t my-airflow-image .
 1934  ls -la
 1935  docker build -t my-airflow-image .
 1936  docker run -p 8080:8080 my-airflow-image
 1937  docker build -t my-airflow-image .
 1938  docker run -p 8080:8080 my-airflow-image
 1939  docker build -t my-airflow-image .
 1940  docker run -p 8080:8080 my-airflow-image
 1941  docker build -t my-airflow-image .
 1942  docker run -p 8080:8080 my-airflow-image
 1943  clear
 1944  docker run --name my-airflow -p 8080:8080 my-airflow-image
 1945  clear
 1946  docker run --name my-airflow -p 8080:8080 my-airflow-image
 1947  docker build -t my-airflow-image .
 1948  ls -la
 1949  docker build -t my-airflow-image .
 1950  docker run --name my-airflow -p 8080:8080 my-airflow-image
 1951  docker rm my-airflow
 1952  docker build -t my-airflow-image .
 1953  docker run --name my-airflow -p 8080:8080 my-airflow-image
 1954  ls -la
 1955  clear
 1956  docker build -t my-airflow-image .
 1957  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 1958  docker build -t my-airflow-image .
 1959  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 1960  docker run --rm --name my_airflow_container -p 8080:8080 my-airflow-image
 1961  docker rm my_airflow_container
 1962  docker run --rm --name my_airflow_container -p 8080:8080 my-airflow-image
 1963  ls -la
 1964  docker build -t my-airflow-image .
 1965  docker rm my_airflow_container
 1966  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 1967  docker exec my_airflow_container cat /var/log/airflow/webserver.log
 1968  docker rm my_airflow_container
 1969  docker build -t my-airflow-image .
 1970  docker run --name my_airflow_container -p 8080:8080 my-airflow-image
 1971  docker run -it --name my_airflow_container my-airflow-image bash
 1972  docker rm my_airflow_container
 1973  docker run -it --name my_airflow_container my-airflow-image bash
 1974  clear
 1975  docker rm my_airflow_container
 1976  docker build -t my-airflow-image .
 1977  docker run -it --name my_airflow_container my-airflow-image
 1978  docker exec -it my_airflow_container bash
 1979  docker run -it --name my_airflow_container my-airflow-image bash
 1980  docker rm my_airflow_container
 1981  docker run -it --name my_airflow_container my-airflow-image bash
 1982  ls -la
 1983  clear
 1984  docker rm my_airflow_container
 1985  docker build -t my-airflow-image .
 1986  docker run -it --name my_airflow_container my-airflow-image
 1987  docker ps -a
 1988  docker logs 94b10cc53dcb
 1989  docker exec -it 94b10cc53dcb airflow scheduler
 1990  docker start 94b10cc53dcb
 1991  docker exec -it 94b10cc53dcb airflow scheduler
 1992  docker exec -it 94b10cc53dcb airflow db init
 1993  docker exec -it 94b10cc53dcb bash
 1994  clear
 1995  ./docker.sh
 1996  history
 1997  ./docker.sh
 1998  clear
 1999  ./docker.sh
 2000  clear
 2001  docker-compose up -d
 2002  docker-compose ps
 2003  docker-compose down
 2004  docker-compose up --build -d
 2005  docker-compose up -d
 2006  docker-compose ps
 2007  docker-compose restart airflow
 2008  docker-compose down
 2009  docker-compose up -d+
 2010  docker-compose up -d
 2011  source myenv/bin/activate
 2012  python crawler/__dag__.py
 2013  clear
 2014  python crawler/__dag__.py
 2015  clear
 2016  python crawler/__dag__.py
 2017  docker-compose down
 2018  docker-compose up -d
 2019  docker-compose ps
 2020  python crawler/__dag__.py
 2021  history