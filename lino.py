import streamlit as st
from streamlit.components.v1 import html
import plotly.express as px
import pandas as pd
dark24 = ['#2E91E5', '#E15F99', '#1CA71C', '#FB0D0D', '#DA16FF', '#222A2A', '#B68100', '#750D86', '#EB663B', '#511CFB', '#00A08B', '#FB00D1']

#st.logo('logo.ico')
# Função para carregar o CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Carregar os dados do arquivo CSV
rio = pd.DataFrame(pd.read_csv('agendamento_fase01_rio.csv'))
kpi_rio = pd.DataFrame(pd.read_csv('rio_agendamentos_eficacia.csv'))

# Carregar o CSS
load_css('style.css')

# Titulo do Dashboard
st.markdown(f"""
    <style>
    .titulo {{
        display: flex;
        justify-content: center;
        align-items:center;
        font-family:Adigiana, sans-serif;
        font-size:2.0rem;
        }}
    </style>
    <div class="titulo">Ação Cidadã - fase 01 trailer Rio</div>
""", unsafe_allow_html=True)

# tab 01
def radios():    
    opcoes = ['total']
    opcoes.extend(kpi_rio['LOCAL'].unique())
    radio = st.radio('Pontos de Atendimento do CastraMóvel RIO',options=opcoes,horizontal=True,label_visibility='visible', key='rad')
    if radio != 'total':
        local_rio = rio.loc[rio['LOCAL']==radio]
        return (dict(local_rio), st.session_state.rad)
    else:
        return (dict(rio), st.session_state.rad)
# tab 02
def kpiradios():    
    kpiopcoes = ['total']
    kpiopcoes.extend(kpi_rio['LOCAL'].unique())
    kpiradio = st.radio('Pontos de Atendimento do CastraMóvel RIO',options=kpiopcoes,horizontal=True,label_visibility='visible',key='kpi')
    if kpiradio != 'total':
        kpi_local_rio = kpi_rio.loc[kpi_rio['LOCAL']==st.session_state.kpi]
        return (dict(kpi_local_rio), st.session_state.kpi)
    else:
        return (dict(kpi_rio), st.session_state.kpi)

# Gerando o HTML completo da página - aqui inclui CSS e HTML
# tab 01
def cards():
    riocards, categoria = (radios())
    riocards = pd.DataFrame(riocards)
    sim_cirurgias = riocards.loc[riocards['cirurgia_realizada']=='sim']
    cirurgias = pd.DataFrame(sim_cirurgias['espec_gener'].value_counts()).reset_index()
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400&display=swap');
            body {{
                background-color: #38B6FF;
                font-family: 'Poppins', sans-serif;
            }}
            .card {{
                background-color: #ffffff;
                width: 100%;
                height: 90px;
                display: flex;
                align-items: center;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0px 2px 4px -2px rgba(0, 0, 0, 0.05), 0px 4px 6px -1px rgba(0, 0, 0, 0.10);
            }}
            .card-text {{
                display: flex;
                flex-direction: column;
            }}

            .card img {{
                width: 56px;
                height: 56px;
                margin-right: 20px;
                margin-left: 15px;
                flex-shrink: 0;
            }}
            .card-header {{
                font-size: 15px;
                color: #4F4F4F;
                text-align: center;
                font-family: 'Poppins', sans-serif;
            }}
            .card-content {{
                font-size: 28px;
                font-family: 'Poppins', sans-serif;
                color: #4F4F4F;
            }}
            .grid-container {{
                display: grid;
                grid-template-columns: repeat(6, 1fr);
                align-items: center;
                gap: 40px;
                margin-right: 15px;
                margin-left: -5px;
                margin-top: -5px;
            }}
            .grid-item {{
                width: 100%;
                background-color: #FFFFFF;
                border-radius: 10px;
                box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.2);
                padding: 10px;
                text-align: left;
                margin-top: 10px;
            }}
            .grid-container-graficos {{
                display: grid;
                justify-items: space-between;
                grid-template-columns: 0.94fr 4.12fr 0.94fr;
                justify-items: center;
                margin-top: 10px;
                gap: 40px;

            }}
            .grid-container-graficos2 {{
                display: grid;
                justify-items: space-between;
                border-radius: 10px;
                grid-template-columns: 1fr;
                justify-items: center;
                align-items: center;
                margin-top: 10px;
                gap: 40px;
            }}
        </style>
    </head>
    <body>
        <div class="grid-container">
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Agendamentos</div>
                <div class='card-content'>{len(riocards)}</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Total de dias</div>
                <div class='card-content'>{sum(pd.DataFrame(riocards[['data','LOCAL']].value_counts()).reset_index()['LOCAL'].value_counts())}</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Cirurgias: {cirurgias['espec_gener'][0]}</div>
                <div class='card-content'>{cirurgias['count'][0]}</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Cirurgias: {cirurgias['espec_gener'][1]}</div>
                <div class='card-content'>{cirurgias['count'][1]}</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Cirurgias: {cirurgias['espec_gener'][2]}</div>
                <div class='card-content'>{cirurgias['count'][2]}</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Cirurgias: {cirurgias['espec_gener'][3]}</div>
                <div class='card-content'>{cirurgias['count'][3]}</div>
                </div>
            </div>
        </div>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(html_content, height=120)
    return (dict(riocards),categoria)

#tab 02
def kpicards():
    kpiriocards, categoria = (kpiradios())
    kpiriocards = pd.DataFrame(kpiriocards)
    sim_cirurgias = kpiriocards.loc[kpiriocards['cirurgia_realizada']=='sim']
    cirurgias = pd.DataFrame(sim_cirurgias['espec_gener'].value_counts()).reset_index()
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400&display=swap');
            body {{
                background-color: #38B6FF;
                font-family: 'Poppins', sans-serif;
            }}
            .card {{
                background-color: #ffffff;
                width: 100%;
                height: 90px;
                display: flex;
                align-items: center;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0px 2px 4px -2px rgba(0, 0, 0, 0.05), 0px 4px 6px -1px rgba(0, 0, 0, 0.10);
            }}
            .card-text {{
                display: flex;
                flex-direction: column;
            }}

            .card img {{
                width: 56px;
                height: 56px;
                margin-right: 20px;
                margin-left: 15px;
                flex-shrink: 0;
            }}
            .card-header {{
                font-size: 15px;
                color: #4F4F4F;
                text-align: center;
                font-family: 'Poppins', sans-serif;
            }}
            .card-content {{
                font-size: 28px;
                text-align: center;
                font-family: 'Poppins', sans-serif;
                color: #4F4F4F;
            }}
            .grid-container {{
                display: grid;
                grid-template-columns: repeat(6, 1fr);
                align-items: center;
                gap: 40px;
                margin-right: 15px;
                margin-left: -5px;
                margin-top: -5px;
            }}
            .grid-item {{
                width: 100%;
                background-color: #FFFFFF;
                border-radius: 10px;
                box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.2);
                padding: 10px;
                text-align: center;
                margin-top: 10px;
            }}
            .grid-container-graficos {{
                display: grid;
                justify-items: space-between;
                grid-template-columns: 0.94fr 4.12fr 0.94fr;
                justify-items: center;
                margin-top: 10px;
                gap: 40px;

            }}
            .grid-container-graficos2 {{
                display: grid;
                justify-items: space-between;
                border-radius: 10px;
                grid-template-columns: 1fr;
                justify-items: center;
                align-items: center;
                margin-top: 10px;
                gap: 40px;
            }}
        </style>
    </head>
    <body>
        <div class="grid-container">
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>KPI Eficácia: Agendamentos</div>
                <div class='card-content'>{round((kpiriocards['count'].sum()/(len(kpiriocards['data'].unique()))/20*100),2)}%</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'>Total de dias</div>
                <div class='card-content'>{sum(pd.DataFrame(kpiriocards[['data','LOCAL']].value_counts()).reset_index()['LOCAL'].value_counts())}</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'><b>Cirurgias Realizadas</b> Mediana da Eficácia: <b>{cirurgias['espec_gener'][0]}</b></div>
                <div class='card-content'>{list(round(kpiriocards.loc[(kpiriocards['cirurgia_realizada']=='sim')&(kpiriocards['espec_gener']==cirurgias['espec_gener'][0]),['count']].median()/5*100,2))[0]}%</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'><b>Cirurgias Realizadas</b> Mediana da Eficácia: <b>{cirurgias['espec_gener'][1]}</b></div>
                <div class='card-content'>{list(round(kpiriocards.loc[(kpiriocards['cirurgia_realizada']=='sim')&(kpiriocards['espec_gener']==cirurgias['espec_gener'][1]),['count']].median()/5*100,2))[0]}%</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'><b>Cirurgias Realizadas</b> Mediana da Eficácia: <b>{cirurgias['espec_gener'][2]}</b></div>
                <div class='card-content'>{list(round(kpiriocards.loc[(kpiriocards['cirurgia_realizada']=='sim')&(kpiriocards['espec_gener']==cirurgias['espec_gener'][2]),['count']].median()/5*100,2))[0]}%</div>
                </div>
            </div>
            <div class='card'>
                <div class='card-text'>
                <div class='card-header'><b>Cirurgias Realizadas</b> Mediana da Eficácia: <b>{cirurgias['espec_gener'][3]}</b></div>
                <div class='card-content'>{list(round(kpiriocards.loc[(kpiriocards['cirurgia_realizada']=='sim')&(kpiriocards['espec_gener']==cirurgias['espec_gener'][3]),['count']].median()/5*100,2))[0]}%</div>
                </div>
            </div>
        </div>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(html_content, height=120)
    return (dict(kpiriocards),categoria)

            

def graficos():
    tab1, tab2 = st.tabs(['Informações Gerais','Indicadores (KPI)'])
    with tab1:
        rio, categoria = (cards())
        rio = pd.DataFrame(rio)
        plot1,plot2 = st.columns(2)
        if len(rio) > 1000:
            df = pd.DataFrame(rio['espec_gener'].value_counts()).reset_index()
            df.rename(columns={'count':'nº de Agendamentos'},inplace=True)
            cirurgias = pd.DataFrame(rio['cirurgia_realizada'].value_counts()).reset_index()
            cirurgias.rename(columns={'count':'nº de Agendamentos'}, inplace=True)
        else:
            df = pd.DataFrame(rio[['espec_gener']].value_counts()).reset_index()
            df.rename(columns={'count':'nº de Agendamentos'},inplace=True)
            cirurgias = pd.DataFrame(rio['cirurgia_realizada'].value_counts()).reset_index()
            cirurgias.rename(columns={'count':'nº de Agendamentos'}, inplace=True)
        with plot1:
            if (df['espec_gener'][0]=='felino_f' or df['espec_gener'][0]=='canino_f') and (df['espec_gener'][1]=='felino_f' or df['espec_gener'][1]=='canino_f'):
                cores = ['#FB00D1', '#E15F99','#511CFB', '#2E91E5']
                figcol1 = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'Quantidade de Agendamentos em {categoria} referente a Espécie-Gênero')
            elif (df['espec_gener'][0]=='felino_f' or df['espec_gener'][0]=='canino_f') and (df['espec_gener'][1]=='felino_m' or df['espec_gener'][1]=='canino_m') and (df['espec_gener'][2]=='felino_f' or df['espec_gener'][2]=='canino_f'):
                cores = ['#FB00D1','#511CFB', '#E15F99', '#2E91E5']
                figcol1 = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'Quantidade de Agendamentos em {categoria} referente a Espécie-Gênero')
            elif (df['espec_gener'][0]=='felino_f' or df['espec_gener'][0]=='canino_f') and (df['espec_gener'][1]=='felino_m' or df['espec_gener'][1]=='canino_m') and (df['espec_gener'][2]=='felino_m' or df['espec_gener'][2]=='canino_m'):
                cores = ['#FB00D1','#511CFB', '#2E91E5', '#E15F99']
                figcol1 = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'Quantidade de Agendamentos em {categoria} referente a Espécie-Gênero')
            elif (df['espec_gener'][0]=='felino_m' or df['espec_gener'][0]=='canino_m') and (df['espec_gener'][1]=='felino_f' or df['espec_gener'][1]=='canino_f') and (df['espec_gener'][2]=='felino_f' or df['espec_gener'][2]=='canino_f'):
                cores = ['#511CFB','#FB00D1', '#E15F99', '#2E91E5']
                figcol1 = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'Quantidade de Agendamentos em {categoria} referente a Espécie-Gênero')
            elif (df['espec_gener'][0]=='felino_m' or df['espec_gener'][0]=='canino_m') and (df['espec_gener'][1]=='felino_m' or df['espec_gener'][1]=='canino_m') and (df['espec_gener'][2]=='felino_f' or df['espec_gener'][2]=='canino_f'):
                cores = ['#511CFB', '#2E91E5','#FB00D1', '#E15F99']
                figcol1 = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'Quantidade de Agendamentos em {categoria} referente a Espécie-Gênero')
            else:
                cores = ['#511CFB','#FB00D1', '#2E91E5', '#E15F99']
                figcol1 = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'Quantidade de Agendamentos em {categoria} referente a Espécie-Gênero')     
            st.plotly_chart(figcol1, theme=None,use_container_width=True)
        with plot2:
            figcol2 = px.pie(cirurgias,values=cirurgias.columns[1], names=cirurgias.columns[0], color=cirurgias.columns[0],title='Agendamentos agrupados por Cirurgias Realizadas')
            st.plotly_chart(figcol2, theme=None, use_container_width=True)
    with tab2:
        kpirio, kpicategoria = (kpicards())
        kpirio = pd.DataFrame(kpirio)
        plot1,plot2 = st.columns(2)
        if len(kpirio) > 1000:
            kpidf = pd.DataFrame(kpirio['espec_gener'].value_counts()).reset_index()
            kpidf.rename(columns={'count':'nº de Agendamentos'},inplace=True)
            cirurgias = pd.DataFrame(kpirio['cirurgia_realizada'].value_counts()).reset_index()
            cirurgias.rename(columns={'count':'nº de Agendamentos'}, inplace=True)
        else:
            kpidf = pd.DataFrame(kpirio[['espec_gener']].value_counts()).reset_index()
            kpidf.rename(columns={'count':'nº de Agendamentos'},inplace=True)
            cirurgias = pd.DataFrame(kpirio['cirurgia_realizada'].value_counts()).reset_index()
            cirurgias.rename(columns={'count':'nº de Agendamentos'}, inplace=True)
        with plot1:
            if (kpidf['espec_gener'][0]=='felino_f' or kpidf['espec_gener'][0]=='canino_f') and (kpidf['espec_gener'][1]=='felino_f' or kpidf['espec_gener'][1]=='canino_f'):
                cores = ['#FB00D1', '#E15F99','#511CFB', '#2E91E5']
                figcol1 = px.bar(kpidf, x=kpidf.columns[0], y=kpidf.columns[1], color=kpidf.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'-                   Quantidade de Agendamentos de Espécie-Gênero')
            elif (kpidf['espec_gener'][0]=='felino_f' or kpidf['espec_gener'][0]=='canino_f') and (kpidf['espec_gener'][1]=='felino_m' or kpidf['espec_gener'][1]=='canino_m') and (kpidf['espec_gener'][2]=='felino_f' or kpidf['espec_gener'][2]=='canino_f'):
                cores = ['#FB00D1','#511CFB', '#E15F99', '#2E91E5']
                figcol1 = px.bar(kpidf, x=kpidf.columns[0], y=kpidf.columns[1], color=kpidf.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'-                   Quantidade de Agendamentos de Espécie-Gênero')
            elif (kpidf['espec_gener'][0]=='felino_f' or kpidf['espec_gener'][0]=='canino_f') and (kpidf['espec_gener'][1]=='felino_m' or kpidf['espec_gener'][1]=='canino_m') and (kpidf['espec_gener'][2]=='felino_m' or kpidf['espec_gener'][2]=='canino_m'):
                cores = ['#FB00D1','#511CFB', '#2E91E5', '#E15F99']
                figcol1 = px.bar(kpidf, x=kpidf.columns[0], y=kpidf.columns[1], color=kpidf.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'-                   Quantidade de Agendamentos de Espécie-Gênero')
            elif (kpidf['espec_gener'][0]=='felino_m' or kpidf['espec_gener'][0]=='canino_m') and (kpidf['espec_gener'][1]=='felino_f' or kpidf['espec_gener'][1]=='canino_f') and (kpidf['espec_gener'][2]=='felino_f' or kpidf['espec_gener'][2]=='canino_f'):
                cores = ['#511CFB','#FB00D1', '#E15F99', '#2E91E5']
                figcol1 = px.bar(kpidf, x=kpidf.columns[0], y=kpidf.columns[1], color=kpidf.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'-                   Quantidade de Agendamentos de Espécie-Gênero')
            elif (kpidf['espec_gener'][0]=='felino_m' or kpidf['espec_gener'][0]=='canino_m') and (kpidf['espec_gener'][1]=='felino_m' or kpidf['espec_gener'][1]=='canino_m') and (kpidf['espec_gener'][2]=='felino_f' or kpidf['espec_gener'][2]=='canino_f'):
                cores = ['#511CFB', '#2E91E5','#FB00D1', '#E15F99']
                figcol1 = px.bar(kpidf, x=df.columns[0], y=kpidf.columns[1], color=kpidf.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'-                   Quantidade de Agendamentos de Espécie-Gênero')
            else:
                cores = ['#511CFB','#FB00D1', '#2E91E5', '#E15F99']
                figcol1 = px.bar(kpidf, x=kpidf.columns[0], y=kpidf.columns[1], color=kpidf.columns[0],template='plotly_dark', barmode='relative', color_discrete_sequence=cores, title=f'-                   Quantidade de Agendamentos de Espécie-Gênero')     
            st.plotly_chart(figcol1, theme=None,use_container_width=True)
        with plot2:
            figcol2 = px.pie(cirurgias,values=cirurgias.columns[1], names=cirurgias.columns[0], color=cirurgias.columns[0],title='Agendamentos agrupados por Cirurgias Realizadas')
            st.plotly_chart(figcol2, theme=None, use_container_width=True)

graficos()        

