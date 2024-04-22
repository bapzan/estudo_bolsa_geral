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

### Regressão Linear
# Importando as bibliotecas necessárias
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Reshape os dados para o formato correto
X = close_price1.values.reshape(-1,1)
y = close_price2.values.reshape(-1,1)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Treinando o algoritmo
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

# Fazendo previsões
y_pred = regressor.predict(X_test)

# Comparando os valores reais e previstos
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)


