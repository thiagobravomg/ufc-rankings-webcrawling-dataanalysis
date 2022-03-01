# ufc-rankings-webcrawling-dataanalysis
<h3>Web Crawling e Scraping com Scrapy e análise de informações de atletatas ranqueados no UFC com Pandas.</h3

<p>*o objetivo do projeto demonstrar a implementação básica de webscrawling e scraping com Scrapy. Assim como exemplificar como os dados adquiridos podem ser processados com Pandas a fim de extrair informação.</p>

<h3> Aqui você vai encontrar: </h3>
<ul>
  <li>Crawler e Scraper básico com Python e Scrapy que lista os atletas ranqueados do UFC.</li>
  <li>Processamento de dados com Pandas que indica quais países têm mais atletas ranqueados no UFC e qual é a idade mais comum de atletas nesta condição.</li>
</ul>

<h3> Informações encontradas: </h3>
<ul>
  <li>Países com mais atletas ranqueados no UFC: Estados Unidos, seguidos de Brasil e então Rússia.</li>
  <li>Idade mais comum: entre 27 e 34 anos.</li>
</ul>


<h3> Para utilizar o código (instruções gerais): </h3>
<ul>
  <li>Instale o Python na sua máquina.</li>
  <li>Clone o repositório.</li>
  <li>Instale os 'requirements.txt'.</li>
</ul>
<p>Para acumular os dados:</p>

    scrapy crawl ufc -O ufc.csv
    
<p>Para processar os dados:</p>

    python.exe pandaslist.py

<h3> Preview: </h3>
<ul>
  <li>![scrapy1](https://user-images.githubusercontent.com/53627206/156222237-c4bc8d7c-1f78-4a65-aca4-f3865a88f637.png)</li>
  <img src="https://user-images.githubusercontent.com/53627206/156222237-c4bc8d7c-1f78-4a65-aca4-f3865a88f637.png">
  <li>![pandas1](https://user-images.githubusercontent.com/53627206/156222279-c9ca7b42-0651-46aa-86c5-dde596e54ac4.png)</li>
  <img src="https://user-images.githubusercontent.com/53627206/156222279-c9ca7b42-0651-46aa-86c5-dde596e54ac4.png">
  <li>![pandas2](https://user-images.githubusercontent.com/53627206/156222303-d04a12fa-2d0a-43e0-9658-29ba971d89a8.png)</li>
  <img src="https://user-images.githubusercontent.com/53627206/156222303-d04a12fa-2d0a-43e0-9658-29ba971d89a8.png">
  <li>![pandas3](https://user-images.githubusercontent.com/53627206/156222313-bd1f071c-a059-4b1a-800c-6b20dd9025c8.png)</li>
  <img src="https://user-images.githubusercontent.com/53627206/156222313-bd1f071c-a059-4b1a-800c-6b20dd9025c8.png">
</ul>
