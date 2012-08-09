#Exportar informacões de um mural de disciplina

Implementação de um exemplo de aplicação que consome os dados de um mural de disciplina usando a dev api do redu.
foram utilizados:
- Python 2.7
- rauth
- simple json

#Uso

instale o rauth
```
$ pip install rauth
```
ou 

```
$ easy_install rauth
```

instale o simplejson
```
$ pip install simplejson
```
ou

```
$ easy_install simplejson
```

Altere o raquivo ``export-csv`` colocando o seu ``consumer_key`` e ``consumer_secret`` nos devidos lugares. Caso ainda não possua estas chaves envie um e-mail para contato@redu.com.br requisitando.

Execute o arquivo ``export-csv``

```
$ python export-csv.py
```