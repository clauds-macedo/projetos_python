import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enviar_email import enviar
# importar base de dados e visualizá-la
tabela = pd.read_excel('Vendas.xlsx')
pd.set_option('display.max_columns', None)

# # faturamento
faturamento = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# print(faturamento)
#
# # qtd produto por loja
qtd = tabela[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
# print(qtd)
#
# # ticket medio
ticket = (faturamento['Valor Final']/qtd['Quantidade']).to_frame('Ticket')
# print(ticket)

# email c/ relatório
msg = f'''<font color = "black">
<h1>Bom dia, aqui está o relatório de vendas.</h1>
Faturamento:
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})} <br>
Quantidade vendida por loja:
{qtd.to_html()} <br>
Ticket médio por loja:
{ticket.to_html(formatters={'Ticket': 'R${:,.2f}'.format})}
</font>
'''
enviar('email@gmail.com', 'senha', 'enviarPara@gmail.com', 'assunto', msg)