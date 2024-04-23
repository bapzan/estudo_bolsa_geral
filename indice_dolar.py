### Bibliotecas
import yfinance as yf
from datetime import datetime, timedelta

### Dados

# Defina os ativos
ticker1 = 'USDBRL=X'
ticker2 = '^BVSP'

# Calcule a data de 20 anos atrás
end_date = datetime.now()
start_date = end_date - timedelta(days=20*365)

# Download dos dados do primeiro ticker
data1 = yf.download(ticker1, start=start_date, end=end_date)

# Selecione apenas a coluna CLOSE
close_price1 = data1['Close']

# Download dos dados do segundo ticker
data2 = yf.download(ticker2, start=start_date, end=end_date)

# Selecione apenas a coluna CLOSE
close_price2 = data2['Close']

print(close_price1)
print(close_price2)


### Gráficos

import matplotlib.pyplot as plt

# Plota os preços de fechamento do USDBRL
plt.figure(figsize=(14,7))
plt.plot(close_price1)
plt.title('Preço de fechamento de ' + ticker1)
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
plt.grid(True)
#plt.show()

# Plota os preços de fechamento do Ibovespa
plt.figure(figsize=(14,7))
plt.plot(close_price2)
plt.title('Preço de fechamento de ' + ticker2)
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
plt.grid(True)
#plt.show()

### Correlação
# Importando a biblioteca necessária
import pandas as pd

# Supondo que close_price1 e close_price2 são Series do pandas com os preços de fechamento
correlation = close_price1.corr(close_price2)

print(f'A correlação entre {ticker1} e {ticker2} é {correlation}')

# Interpretação: A correlação de 0.7758686242653083 entre USD/BRL e Ibovespa indica uma forte correlação positiva. Isso significa que, em geral, quando o valor do USD/BRL aumenta, o valor do Ibovespa também tende a aumentar, e vice-versa.


### Teste de Granger

# Importando a biblioteca necessária
from statsmodels.tsa.stattools import grangercausalitytests

# Criando um DataFrame com as duas séries
df = pd.concat([close_price1, close_price2], axis=1)
df.columns = ['USD/BRL', 'Ibovespa']

# Removendo valores NaN e infinitos
import numpy as np
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

# Agora você pode continuar com o teste de Granger
granger_test = grangercausalitytests(df, maxlag=10)


### Teste de Causalidade de Toda


### Teste de Cointegração de Johansen


### Modelos de Vetores Autorregressivos (VAR)