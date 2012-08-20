#Exportar informacões de um mural de disciplina

Implementação de um exemplo de aplicação que consome os dados de um mural de disciplina usando a dev api do redu.
foram utilizados:
- Python 2.7
- rauth
- simple json

#Uso

instale as dependencias
```
$ pip install -r requirements.txt
```

Altere o raquivo ``export-csv`` colocando o seu ``consumer_key`` e ``consumer_secret`` nos devidos lugares. Caso ainda não possua estas chaves envie um e-mail para contato@redu.com.br requisitando.

Execute o arquivo ``export-csv``

```
$ python export-csv.py
```

Copyright (c) 2012 Redu Educational Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.