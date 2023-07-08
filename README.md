# Pesquisa-de-Satisfação-com-Power-Automate

## Resumo
Os principais objetivos da pesquisa de satisfação são avaliar a qualidade dos serviços de saúde prestados, medir a satisfação dos pacientes em relação ao atendimento recebido e identificar áreas de melhoria.

Para isso, é utilizado o Google Forms como plataforma de pesquisa online, criando um questionário conciso e fácil de responder. Um novo fluxo de trabalho é configurado no Power Automate, sendo acionado pelo horário programado para consultar a planilha de prontuários no Excel. Se houver registro de alta médica, o Power Automate envia um e-mail personalizado ao paciente com o questionário.

As respostas coletadas são integradas em um Google Sheets e, em seguida, são processadas no Microsoft Power BI. Após um processo de ETL (Extração, Transformação e Carga) dos dados, eles são apresentados em um Dashboard, permitindo a extração de insights e análise dos resultados da pesquisa de satisfação.

![sequências de etapas do robô](https://github.com/PhD-Anibal/Automa-na-Extra-de-Dados/assets/128927981/1167e394-ef06-4071-a1a0-cfdbece71ead)

## O processo ocorre da seguinte maneira:
A clínica "Saúde Total" possui uma planilha em Microsoft Excel com os dados dos pacientes internados. Em um horário determinado o Microsoft Power Automate consulta a planilha se algum paciente recebeu alta.
O Power Automate envia um e-mail personalizado para o paciente dado de alta com um link para um formulário de feedback do atendimento, criado no Google Forms.
As respostas do formulário preenchem uma planilha do Google Sheets, que está conectada ao Microsoft Power BI para apresentar os resultados em um Dashboard.
O Dashboard feito inclui dados como o Net Promoter Score (NPS), a quantidade de pacientes que receberam o e-mail, a quantidade de pacientes que responderam o formulário e a porcentagem de respostas. Além disso, são apresentados gráficos sobre a qualidade do atendimento e a acessibilidade aos serviços, pudendo todos os dados serem filtrados por datas em que foram recebido os Feedbacks.
