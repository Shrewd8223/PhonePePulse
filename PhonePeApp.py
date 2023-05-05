import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

#?DATA GROUP 1
#!code -
        # TODO -- nitish_sawant
        # TODO -- shreedhar_gehlot




#! page icon set
icon = Image.open(
    'phonepe-logo-icon.png')
st.set_page_config(page_title="PhonePe Pulse", page_icon=icon,
                   layout="wide", initial_sidebar_state="expanded")


#Logo PhonePe Pulse(nitish)
st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""<nav class="navbar navbar-dark justify-content-center" style="background-color: #2c1942; height:60px" >
        <a class="navbar-brand" href="#" style="margin: 0px;background-color:#2c1942;">
            <img src="data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMzAgOTAiPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojZmZmO30uY2xzLTJ7ZmlsbDojNWYyNDlmO308L3N0eWxlPjwvZGVmcz48Y2lyY2xlIGNsYXNzPSJjbHMtMSIgY3g9IjUwLjM0IiBjeT0iNDQuOTIiIHI9IjQyLjQyIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNNTQuNSw1NC4xNmExMy4xNCwxMy4xNCwwLDAsMS00LjcxLjk0Yy0zLjg4LDAtNS42Mi0xLjk0LTUuNjItNi4yOVYzNy4zNkg1NC41Wm0xNS0yMC4zOGEzLDMsMCwwLDAtMy0zSDYwLjlsLTEzLTE1QTQuNzEsNC43MSwwLDAsMCw0MywxNC4zNmwtNC41LDEuMzNhLjk0Ljk0LDAsMCwwLS4zNywxLjU4TDUyLjI3LDMwLjgySDMwLjU3YTEuMTEsMS4xMSwwLDAsMC0xLjEzLDEuMTFWMzQuNGEzLDMsMCwwLDAsMywzaDMuMzFWNDguODNjMCw4LjU0LDQuNTUsMTMuNjUsMTIuMTksMTMuNjVhMTYuOTMsMTYuOTMsMCwwLDAsNi41Ni0xLjE3djcuNjNhMy43NSwzLjc1LDAsMCwwLDMuNzQsMy43NmgzLjNBMS40MSwxLjQxLDAsMCwwLDYzLDcxLjI5aDBWMzcuMzZoNS40NGExLjEyLDEuMTIsMCwwLDAsMS4xMS0xLjEzWiIvPjxwYXRoIGNsYXNzPSJjbHMtMSIgZD0iTTI4NCw0Mi42NWMwLTMuNzQtMi41MS01LjYzLTYuMjItNS42M2ExMS4yNywxMS4yNywwLDAsMC0zLjY4LjY1VjUzLjNhNi44Myw2LjgzLDAsMCwwLDMuNzQsMWMzLjY2LDAsNi4xNi0yLDYuMTYtNS42MVptOC41LDZjMCw3LjY4LTUuNzQsMTIuODQtMTMuMjcsMTIuODRhMTMuODMsMTMuODMsMCwwLDEtNS4xMy0uODlWNzEuMjZhMS40LDEuNCwwLDAsMS0xLjM5LDEuNDFoLTUuNTdhMS40MSwxLjQxLDAsMCwxLTEuNDEtMS40MWgwVjMzLjU0YTIuMTUsMi4xNSwwLDAsMSwxLjQzLTIsMzMuOSwzMy45LDAsMCwxLDEwLjg4LTEuOTJjOC41MSwwLDE0LjQ5LDUuMTcsMTQuNDksMTMuMlptLTE2MS43OC02YzAtMy43NC0yLjUyLTUuNjMtNi4yMy01LjYzYTExLjIxLDExLjIxLDAsMCwwLTMuNjcuNjVWNTMuM2E2Ljc0LDYuNzQsMCwwLDAsMy43NCwxYzMuNjYsMCw2LjE2LTIsNi4xNi01LjYxWm04LjQ5LDZjMCw3LjY4LTUuNzQsMTIuODQtMTMuMjYsMTIuODRhMTMuODMsMTMuODMsMCwwLDEtNS4xMy0uODlWNzEuMjZhMS40MSwxLjQxLDAsMCwxLTEuMzYsMS40MWgtNS42YTEuNDIsMS40MiwwLDAsMS0xLjQtMS40MVYzMy41NGEyLjEyLDIuMTIsMCwwLDEsMS40Mi0yLDM0LDM0LDAsMCwxLDEwLjg5LTEuOTJjOC41MSwwLDE0LjQ5LDUuMTcsMTQuNDksMTMuMlptNTIuOTEsNC4wOWMwLTMtMS43NS00LjY0LTQuODItNC42NHMtNC44NCwxLjczLTQuODQsNC42OHY4Ljg2YzAsMi45MiwxLjcxLDQuNTMsNC44Miw0LjUzczQuODItMS42MSw0LjgyLTQuNTNabTguMzcsMFY2MS42YzAsNy4yNi01LjA2LDExLjc4LTEzLjE5LDExLjc4cy0xMy4yMy00LjUxLTEzLjIzLTExLjc4VjUyLjc4YzAtNy4zNiw1LjA2LTEyLDEzLjIzLTEyczEzLjE2LDQuNjQsMTMuMTYsMTJabS0zNS44MSwxOS45aDMuMzZhMS40LDEuNCwwLDAsMCwxLjQyLTEuMzdWNTMuNjhjMC04LTQuMy0xMi44NS0xMS41LTEyLjg1YTE2LjQsMTYuNCwwLDAsMC01Ljg5LDFWMzMuMTRhMy41MywzLjUzLDAsMCwwLTMuNTItMy41NGgtMy4zMmExLjQxLDEuNDEsMCwwLDAtMS40MiwxLjRoMFY3MS4yNmExLjQxLDEuNDEsMCwwLDAsMS40MSwxLjQxaDUuNDNhMS40MSwxLjQxLDAsMCwwLDEuNDEtMS40MWgwVjQ4Ljg3YTExLDExLDAsMCwxLDQuMDgtLjc5YzMuNDQsMCw1LDEuNzMsNSw1LjYxVjY5LjE1YTMuNTYsMy41NiwwLDAsMCwzLjU0LDMuNTNabTEzOS41Ny0xOGg5LjA3VjUyLjI3YzAtMy0xLjY2LTQuNjUtNC41NC00LjY1cy00LjUzLDEuNjYtNC41Myw0LjY1djIuMzhabS4xOCw1LjJoLS4xOFY2MmMwLDIuODgsMS44Myw0LjUzLDUsNC41M2ExMy44OCwxMy44OCwwLDAsMCw2Ljg5LTEuODQsMS40LDEuNCwwLDAsMSwuNzUtLjE3LDEuMzksMS4zOSwwLDAsMSwxLC41bC44MywxYTMuNTksMy41OSwwLDAsMSwuOTMsMi40NkEzLjMxLDMuMzEsMCwwLDEsMzE4LDcxLjMxLDE4LjU5LDE4LjU5LDAsMCwxLDMwOSw3My40MmExNC41MywxNC41MywwLDAsMS05LjI2LTIuODgsMTAuNzMsMTAuNzMsMCwwLDEtMy44LTguNjZ2LTkuMmMwLTcuNDIsNC44Mi0xMS44MywxMi45MS0xMS44Myw3Ljg4LDAsMTIuMzgsNC4zMiwxMi4zOCwxMS44M3Y1Ljc3YTEuNCwxLjQsMCwwLDEtMS4zOSwxLjQxSDMwNC41Wm0tNjAuNTctNS4ySDI1M1Y1Mi4yN2MwLTMtMS42Ni00LjY1LTQuNTQtNC42NXMtNC41NCwxLjY2LTQuNTQsNC42NXYyLjM4Wm0uMTksNS4yaC0uMTlWNjJjMCwyLjg4LDEuODQsNC41Myw1LDQuNTNhMTMuODUsMTMuODUsMCwwLDAsNi44OC0xLjg0LDEuNTQsMS41NCwwLDAsMSwuNzYtLjE3LDEuMzksMS4zOSwwLDAsMSwxLC41bC44MywxYTMuNTQsMy41NCwwLDAsMSwuOTIsMi40NiwzLjI4LDMuMjgsMCwwLDEtMS43MywyLjgzLDE4LjU5LDE4LjU5LDAsMCwxLTguOTUsMi4xMSwxNC40NiwxNC40NiwwLDAsMS05LjI2LTIuODgsMTAuNzMsMTAuNzMsMCwwLDEtMy44LTguNjZ2LTkuMmMwLTcuNDIsNC44Mi0xMS44MywxMi45LTExLjgzLDcuODksMCwxMi4zOSw0LjMyLDEyLjM5LDExLjgzdjUuNzdhMS40LDEuNCwwLDAsMS0xLjM5LDEuNDFIMjQ0Wm0tMjEuNDEsOS4zVjUzLjc0YzAtMy44OC0xLjUyLTUuNi00LjkzLTUuNmExNC4yMywxNC4yMywwLDAsMC00LjE1LjU2VjcxLjI3YTEuMzksMS4zOSwwLDAsMS0xLjM3LDEuNDFoLTUuNDZhMS40LDEuNCwwLDAsMS0xLjQxLTEuMzlWNDQuODRhMi4xOCwyLjE4LDAsMCwxLDEuMzYtMiwzMi44MiwzMi44MiwwLDAsMSwxMS0yYzguNTQsMCwxMy4yMyw0LjU4LDEzLjIzLDEyLjlWNzEuMjdhMS4zOSwxLjM5LDAsMCwxLTEuMzcsMS40MWgtMy40YTMuNTMsMy41MywwLDAsMS0zLjUtMy41M1oiLz48L3N2Zz4="  height="30"  class="d-inline-block align-top" alt="" style="background-color:#2c1942;"></a>
            <a class="navbar-brand" href="#" style="background-color:#2c1942;">
                <img src="https://www.phonepe.com/pulsestatic/pulse/pulse_header_logo.gif" height="30" class="d-inline-block align-top justify-content-center" alt="Pulse" style="background-color:#2c1942;">
            </a>
        </nav>
        <style>
        # *{
        #     # background-color:#ffff;
        #    margin: 0px;
        #    padding: 0px;
            
        # }
        nav{
            margin:-113px;
            padding:0px;
            width:auto;
        }
        MainMenu{
        visibility:hidden}
        footer{visibility:hidden}
        header{visibility:hidden}
        </style>
""", unsafe_allow_html=True)

#!Banner(nitish)

st.markdown('''
    <div style="position:relative;">
        <img src="https://www.phonepe.com/webstatic/static/6341d1762ac4ed98d04996c9b03b5eb5/eeb1b/hp-banner4wt.png" style="width:1280px;height:350px;margin-left:-80px;margin-top:-70px">
        <div style="position:absolute;top:30%;left:15%;transform:translate(-50%, -50%);font-size:35px;font-weight:bold;color:white;;">PhonePe <span style="color:#F7F000">Pulse</span> <br><p style="font-size:18px;font-weight:bold;font-style: italic;">Find out how money moves in a country of 140 Crore!</p></div>
    </div>
''', unsafe_allow_html=True)
#! title Name for india map
text = ":chart: ALL INDIA PHONEPE PAYMENTS :chart:"
st.write(
    f'<span style= "margin-top:30px;margin-bottom:20px; font-family: Montserrat, sans-serif; font-weight: 700; font-size: 22px; display: block; text-align: center; color:#5400ae">{text}</span>',
    unsafe_allow_html=True)


#!Add main
c1, c2 = st.columns(2)
with c1:
    Year = st.selectbox(
        '**Select Year**',
        ('2018', '2019', '2020', '2021', '2022'))
with c2:
    Quarter = st.selectbox(
        '**Select Quarter**',
        ('1', '2', '3', '4'))
year = int(Year)
quarter = int(Quarter)


#! CSV file data
Data_Aggregated_Transaction_df = pd.read_csv(
    r'data/Data_Aggregated_Transaction_Table.csv')
Data_Aggregated_User_Summary_df = pd.read_csv(
    r'data/Data_Aggregated_User_Summary_Table.csv')
Data_Aggregated_User_df = pd.read_csv(r'data/Data_Aggregated_User_Table.csv')
Scatter_Geo_Dataset = pd.read_csv(
    r'data/Data_Map_Districts_Longitude_Latitude.csv')
Coropleth_Dataset = pd.read_csv(r'data/Data_Map_IndiaStates_TU.csv')
Data_Map_Transaction_df = pd.read_csv(r'data/Data_Map_Transaction_Table.csv')
Data_Map_User_Table = pd.read_csv(r'data/Data_Map_User_Table.csv')
Indian_States = pd.read_csv(r'data/Longitude_Latitude_State_Table.csv')


Transaction_scatter_districts = Data_Map_Transaction_df.loc[(
    Data_Map_Transaction_df['Year'] == year) & (Data_Map_Transaction_df['Quarter'] == quarter)].copy()
Transaction_Coropleth_States = Transaction_scatter_districts[
    Transaction_scatter_districts["State"] == "india"]
Transaction_scatter_districts.drop(Transaction_scatter_districts.index[(
    Transaction_scatter_districts["State"] == "india")], axis=0, inplace=True)

# TODO ---- For districts
Transaction_scatter_districts = Transaction_scatter_districts.sort_values(
    by=['Place_Name'], ascending=False)


#! Total amount in india - Append in main file to show data on map  ---- For districts(nitish)
Total_Amount = []
for i in Transaction_scatter_districts['Total_Amount']:
    Total_Amount.append(i)
Scatter_Geo_Dataset['Total_Amount'] = Total_Amount


#! Total_Transaction in india - Append in main file to show data on map  ---- For districts
Total_Transaction = []
for i in Transaction_scatter_districts['Total_Transactions_count']:
    Total_Transaction.append(i)
Scatter_Geo_Dataset['Total_Transactions'] = Total_Transaction


#!year & Quarter - Append in main file to show data on map ---- For districts
Scatter_Geo_Dataset['Year_Quarter'] = str(year)+'-Q'+str(quarter)


# TODO ---- For Coropleth
Coropleth_Dataset = Coropleth_Dataset.sort_values(
    by=['state'], ascending=False)
Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(
    by=['Place_Name'], ascending=False)

#! Total amount in india - Append in main file to show data on map  ---- For Coropleth
Total_Amount = []
for i in Transaction_Coropleth_States['Total_Amount']:
    Total_Amount.append(i)
Coropleth_Dataset['Total_Amount'] = Total_Amount

#! Total Transaction in india - Append in main file to show data on map  ---- For Coropleth
Total_Transaction = []
for i in Transaction_Coropleth_States['Total_Transactions_count']:
    Total_Transaction.append(i)
Coropleth_Dataset['Total_Transactions'] = Total_Transaction


# TODO ---- For states

#!append all data from  Coropleth_DataSet to Indian_States -------- States Data Fig - first
Indian_States = Indian_States.sort_values(by=['state'], ascending=False)
Indian_States['Registered_Users'] = Coropleth_Dataset['Registered_Users']
Indian_States['Total_Amount'] = Coropleth_Dataset['Total_Amount']
Indian_States['Total_Transactions'] = Coropleth_Dataset['Total_Transactions']
Indian_States['Year_Quarter'] = str(year)+'-Q'+str(quarter)


# ? Plotting for states Fig 1
FirstFig = px.scatter_geo(Indian_States,
                          lon=Indian_States['Longitude'],
                          lat=Indian_States['Latitude'],
                          hover_name="state",
                          hover_data=['Total_Amount', "Total_Transactions", "Year_Quarter", "Registered_Users"],)
FirstFig.update_traces(marker=dict(color="#000", size=4))
FirstFig.update_geos(fitbounds="locations", visible=False,)


# ? Plotting for District Fig 2
SecondFig = px.scatter_geo(Scatter_Geo_Dataset,
                           lon=Scatter_Geo_Dataset['Longitude'],
                           lat=Scatter_Geo_Dataset['Latitude'],
                           size=Scatter_Geo_Dataset['Total_Transactions'],
                           hover_name="District",
                           hover_data=["State", "Total_Amount",
                                       "Total_Transactions", "Year_Quarter"],
                           title='District',
                           size_max=15,)

SecondFig.update_traces(marker=dict(color="#bbb", line_width=1.5))

# coropleth
fig_ch = px.choropleth(
    Coropleth_Dataset,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    locations='state',
    featureidkey='properties.ST_NM',
    color="Total_Transactions",
    color_continuous_scale=["#F9E6F1", "#E1B8F9",
                            "#C111E9", "#840CA8", "#2D033B"],

)
fig_ch.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                     geo=dict(
    showframe=False,
    showcoastlines=False,
    projection_type='equirectangular',
    bgcolor='rgba(0,0,0,0)'
))

fig_ch.update_geos(fitbounds="locations", visible=False,)


#! state Data plot
fig_ch.add_trace(FirstFig.data[0])


#! Dis plot data
fig_ch.add_trace(SecondFig.data[0])


Data_Map_User_df = Data_Aggregated_User_Summary_df.copy()
top_states = Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(
    Year)) & (Data_Map_User_df['Quarter'] == int(Quarter))]
top_states_r = top_states.sort_values(by=['Registered_Users'], ascending=False)
top_states_a = top_states.sort_values(by=['AppOpenings'], ascending=False)


top_states_T = Data_Aggregated_Transaction_df.loc[(Data_Aggregated_Transaction_df['Year'] == int(
    Year)) & (Data_Aggregated_Transaction_df['Quarter'] == int(Quarter))]
topst = top_states_T.groupby('State')

# x group by states

x = topst.sum().sort_values(by=['Total_Transactions_count'], ascending=False)
y = topst.sum().sort_values(by=['Total_Amount'], ascending=False)


Total_Transaction_value_india = x.iloc[0, 0]
df = pd.DataFrame({'Total Transaction Value (India)': [
                  Total_Transaction_value_india]})
Transaction_india_table = df.to_html(
    index=False, header=False, justify='center')

#!convert -> cr(nitish)
a = y.iloc[0, 1]
a1 = (int(a)/10000000)
a1 = round(a1)
Total_Amount_value_india = f"{a1} Cr."

# convert amount in dataframe
df = pd.DataFrame({'Total Amount Value (India)': [Total_Amount_value_india]})
Total_Amount_value_india = df.to_html(
    index=False, header=False, justify='center')


#! title Name for india map
text = ":world_map: INDIA MAP"
st.write(
    f'<span style="margin-top:20px;margin-bottom:20px;font-family: Montserrat, sans-serif; font-weight: 700; font-size:20px; display: block; text-align: center; color: #5400ae">{text}</span>',
    unsafe_allow_html=True
)

colT1, colT2 = st.columns([7, 3.1])

with colT1:

    colT111, colT222 = st.columns(2)
    with colT111:

        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:360px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Info:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-left:3px">Map shows total PhonePe transactions by state.</li>'
            f'<li style="font-size: 13px;margin-left:2px">State color shows transaction volume.</li>'
            f'<li style="font-size: 13px;margin-left:2px">Circle size shows transaction volume by district.</li>'
            f'<li style="font-size: 13px;margin-left:2px">Hover data shows more details.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )

    with colT222:
        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:360px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Observations:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-top:3px">Map shows PhonePe transactions statewise and district-wise.</li>'
            f'<li style="font-size: 13px;margin-left:2px">Top states for transactions are easy to see.</li>'
            f'<li style="font-size: 13px;margin-left:2px">District data gives insight into transaction patterns.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )
    st.plotly_chart(fig_ch, use_container_width=True)

with colT2:
    colT11, colT13 = st.columns([7, 4])
    with colT11:
        st.write(
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 600; font-size: 14px; display: block;color: #5400ae">Total Transaction In India &#10132;</span>',
            unsafe_allow_html=True
        )

    with colT13:
        st.markdown(Transaction_india_table, unsafe_allow_html=True)

    colT21, colT23 = st.columns([7, 4])
    with colT21:
        st.write(
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 600; font-size: 14px; display: block; color: #5400ae">Total Amount In India &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#10132;</span>',
            unsafe_allow_html=True
        )

    with colT23:
        st.markdown(Total_Amount_value_india, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(
        ["Registered Users", "Total Transactions", "Total Amount"])
    with tab1:
        rt = top_states_r[1:11]
        st.markdown(rt[['State', 'Registered_Users']].style.hide(
            axis="index").to_html(), unsafe_allow_html=True)

    with tab2:

        Top_Ten_T = Indian_States.sort_values(
            by=['Total_Transactions'], ascending=False)
        tt = Top_Ten_T[0:10]
        st.markdown(tt[['state', 'Total_Transactions']].style.hide(
            axis="index").to_html(), unsafe_allow_html=True)

    with tab3:
        Top_Ten_A = Indian_States.sort_values(
            by=['Total_Amount'], ascending=False)
        ta = Top_Ten_A[0:10]
        # convert to crore and round off to 2 decimal places
        ta['Total_Amount'] = (ta['Total_Amount'] / 10000000).round(2)
        ta['Total_Amount'] = ta['Total_Amount'].astype(
            str) + ' cr'  # add 'cr' suffix to indicate crore
        st.markdown(ta[['state', 'Total_Amount']].style.hide(
            axis="index").to_html(), unsafe_allow_html=True)


# ? transaction analysis


#! title Name for transactions (nitish)
text = ":moneybag: TRANSACTIONS ANALYSIS :moneybag:"
st.write(
    f'<span style="margin-top:10px;margin-bottom:20px;font-family: Montserrat, sans-serif; font-weight: 700; font-size: 20px; display: block; text-align: center; color: #5400ae">{text}</span>',
    unsafe_allow_html=True
)


tab1, tab2 = st.tabs(["STATE ANALYSIS", "OVERALL ANALYSIS"])
with tab1:
    Data_Aggregated_Transaction = Data_Aggregated_Transaction_df.copy()
    Data_Aggregated_Transaction.drop(Data_Aggregated_Transaction.index[(
        Data_Aggregated_Transaction["State"] == "india")], axis=0, inplace=True)
    State_PaymentMode = Data_Aggregated_Transaction.copy()
    st.write(
        f'<span style="font-family: Montserrat, sans-serif; font-weight: 600; font-size: 18px; display: block;color: #5400ae">State & Payment-Mode &#10132;</span>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        mode = st.selectbox(
            '**Mode Of Payments**',
            ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'), key='a')
    with col2:
        state = st.selectbox(
            '**States**',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
             'assam', 'bihar', 'chandigarh', 'chhattisgarh',
             'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
             'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
             'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
             'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
             'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
             'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
             'uttarakhand', 'west-bengal'), key='b')
    State = state
    Year_List = [2018, 2019, 2020, 2021, 2022]
    Mode = mode
    State_PaymentMode = State_PaymentMode.loc[(State_PaymentMode['State'] == State) & (State_PaymentMode['Year'].isin(Year_List)) &
                                              (State_PaymentMode['Payment_Mode'] == Mode)]
    State_PaymentMode = State_PaymentMode.sort_values(by=['Year'])
    State_PaymentMode["Quarter"] = "Q"+State_PaymentMode['Quarter'].astype(str)
    State_PaymentMode["Year_Quarter"] = State_PaymentMode['Year'].astype(
        str) + "-" + State_PaymentMode["Quarter"].astype(str)

    fig = px.bar(State_PaymentMode, x='Year_Quarter', y='Total_Transactions_count', color="Total_Transactions_count",
                 color_continuous_scale="Plasma")

    colT1, colT2 = st.columns([7, 3])
    with colT1:
        st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px">{State.upper()} &#10132;</div>', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
    with colT2:
        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:320px;margin-top:125px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Info:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-top:3px;">This entire data belongs to state selected by you.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">X Axis is  all years with all quarters.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">Y Axis represents total transactions.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:320px;margin-top:25px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Observations:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-top:3px;">User notes payment patterns in state through observation.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">Observe payment methods in a state to determine if they are increasing or decreasing in popularity.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )

#!New Change (nitish_sawant)
with tab2:
    years = Data_Aggregated_Transaction.groupby('Year')
    years_List = Data_Aggregated_Transaction['Year'].unique()
    transaction_summary = years.sum()
    del transaction_summary['Quarter']
    transaction_summary['year'] = years_List
    total_trans = transaction_summary['Total_Transactions_count'].sum()

    # Define custom color palette
    custom_palette = ['#8A00D4', '#DA07B7', '#F90CA8', '#FF82C3', '#FFCF9F']

    fig1 = px.pie(transaction_summary, values='Total_Transactions_count',
                  names='year', color_discrete_sequence=custom_palette,)
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    fig1.update_layout(showlegend=False, margin=dict(t=50, b=50))
    st.write(
        f'<span style="font-family: Montserrat, sans-serif; font-weight: 600; font-size: 18px;color: #5400ae;display:flex;position:absolute;margin-top:0px;z-index:1">Changes in Transactions (2018-2022) &#10132;</span>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
        st.write('<div style="border: 1px solid #ccc; border-radius: 5px; padding: 40px;margin-top: -35px;font-size:14px;font-weight:500">From the pie chart, it is clear that there has been a significant increase in the number of online transactions through PhonePe from 2018 to 2022. More than 50% of total PhonePe transactions in India happened in the year 2022 alone.</div>', unsafe_allow_html=True)
    with col2:
        st.write(f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:82px;margin-bottom:30px">Year Wise Transaction Analysis in India &#10132;</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin: 0px">' + transaction_summary.style.hide(
            axis="index").render() + '</div>', unsafe_allow_html=True)

        st.write('<div style="border: 1px solid #ccc; border-radius: 5px; padding: 30px;margin-top: 79px;font-size:14px;font-weight:500">From the table above, we can see the breakdown of transactions by year. Initially in 2018 and 2019, the number of transactions was less, but with time, the online payments increased at a high scale via PhonePe. It is clear that the majority of transactions occurred in the year 2022.</div>', unsafe_allow_html=True)


# ? User analysis

#! title Name for USERS DATA ANALYSIS (nitish)

text = ":bust_in_silhouette: USERS DATA ANALYSIS :iphone:"
st.write(
    f'<span style="margin-top:10px;margin-bottom:20px;font-family: Montserrat, sans-serif; font-weight: 700; font-size: 20px; display: block; text-align: center; color: #5400ae">{text}</span>',
    unsafe_allow_html=True
)
tab1, tab2 = st.tabs(["STATE ANALYSIS", "YEARLY ANALYSIS BY BRAND SHARE"])
with tab1:
    st.write(
        f'<span style="font-family: Montserrat, sans-serif; font-weight: 600; font-size: 18px; display: block;color: #5400ae">State & Userbase &#10132;</span>',
        unsafe_allow_html=True
    )
    state = st.selectbox(
        '**Select the State**',
        ('andhra-pradesh', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
         'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
         'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
         'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
         'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
         'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
         'uttarakhand', 'west-bengal'), key='W')
    app_opening = Data_Aggregated_User_Summary_df.groupby(['State', 'Year'])
    a_state = app_opening.sum()
    la = Data_Aggregated_User_Summary_df['State'] + " " + \
        Data_Aggregated_User_Summary_df["Year"].astype(str)
    a_state["state_year"] = la.unique()
    sta = a_state["state_year"].str[:-5]
    a_state["state"] = sta
    sout = a_state.loc[(a_state['state'] == state)]
    ta = sout['AppOpenings'].sum()
    tr = sout['Registered_Users'].sum()
    sout['AppOpenings'] = sout['AppOpenings'].mul(100/ta)
    sout['Registered_Users'] = sout['Registered_Users'].mul(100/tr).copy()
    fig = go.Figure(data=[
        go.Bar(name='AppOpenings %', y=sout['AppOpenings'], x=sout['state_year'], marker={
               'color': '#A459D1'}),
        go.Bar(name='Registered Users %',
               y=sout['Registered_Users'], x=sout['state_year'], marker={'color': '#F99417'})
    ])
    fig.update_layout(barmode='group', legend=dict(x=0, y=1.2))
    # Change the bar mode
    fig.update_layout(barmode='group', xaxis_title="State & Year")
    colT1, colT2 = st.columns([7, 3])
    with colT1:
        st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;text-align:left">{state.upper()} &#10132;</div>', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True, height=200)

    with colT2:
        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:320px;margin-top:100px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Info:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-top:3px;">First users will need to select a state to view the data.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">X Axis -Registered Users and App Openings.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">Y Axis -Percentage of Registered Users and App Openings.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:320px;margin-top:25px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Observations:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-top:3px;">The graph provides a clear visual representation of these two parameters and their trends.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">By comparing App Openings and Registered Users, users can observe how the user base is growing and identify areas for improvement.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )

with tab2:
    st.write(
        f'<span style="font-family: Montserrat, sans-serif; font-weight: 600; font-size: 18px; display: block;color: #5400ae">Mobile Brand Share Data &#10132;</span>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        state = st.selectbox(
            '**Select the State**',
            ('andhra-pradesh', 'andaman-&-nicobar-islands', 'arunachal-pradesh',
             'assam', 'bihar', 'chandigarh', 'chhattisgarh',
             'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
             'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
             'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
             'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
             'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
             'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
             'uttarakhand', 'west-bengal'), key='Z')
    with col2:
        Yearbrand = st.selectbox(
            '**Select the Year**',
            ('2018', '2019', '2020', '2021', '2022'), key='X')
    y = int(Yearbrand)
    s = state
    brand = Data_Aggregated_User_df.loc[(Data_Aggregated_User_df['Year'] == y) & (
        Data_Aggregated_User_df['State'] == s)]
    myb = brand['Brand_Name'].unique()
    x = sorted(myb).copy()
    b = brand.groupby('Brand_Name').sum()
    b['brand'] = x
    br = b['Registered_Users_Count'].sum()
    labels = b['brand']
    values = b['Registered_Users_Count']
    fig4 = px.bar(b, x='brand', y='Registered_Users_Count', color="Registered_Users_Count",
                  color_continuous_scale="purples")
    colT1, colT2 = st.columns([7, 3])
    with colT1:
        st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;text-align:left">{state.upper()} IN {Yearbrand} &#10132;</div>', unsafe_allow_html=True)
        st.plotly_chart(fig4, use_container_width=True)
    with colT2:
        st.write(
            f'<div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; width:320px;margin-top:180px">'
            f'<span style="font-family: Montserrat, sans-serif; font-weight: 550; font-size: 14px;">Observations:</span><br>'
            f'<ul style="list-style-type: disc; margin-left: -10px;">'
            f'<li style="font-size: 13px;margin-left:2px;margin-top:3px;">The chart above shows the top leading brands in the selected state and year.</li>'
            f'<li style="font-size: 13px;margin-left:2px;">You can use this data to make recommendations for app downloads, especially for growing brands.</li>'
            f'</ul>'
            f'</div>',
            unsafe_allow_html=True
        )

        # TODO -- nitish_sawant(49460)
        # TODO -- shreedhar_gehlot(49074)


#! title Name for TOP STATES DATA

text = ":bar_chart: TOP STATES DATA :clipboard:"
st.write(
    f'<span style="margin-top:10px;margin-bottom:20px;font-family: Montserrat, sans-serif; font-weight: 700; font-size: 20px; display: block; text-align: center; color: #5400ae">{text}</span>',
    unsafe_allow_html=True
)
c1,c2=st.columns(2)
with c1:
    Year = st.selectbox(
            '**Select Year**',
            ('2022', '2021','2020','2019','2018'),key='y1h2k')
with c2:
    Quarter = st.selectbox(
            '**Select Quarter**',
            ('1', '2', '3','4'),key='qgwe2')
Data_Map_User_df=Data_Aggregated_User_Summary_df.copy() 
top_states=Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(Year)) & (Data_Map_User_df['Quarter'] ==int(Quarter))]
top_states_r = top_states.sort_values(by=['Registered_Users'], ascending=False)
top_states_a = top_states.sort_values(by=['AppOpenings'], ascending=False) 

top_states_T=Data_Aggregated_Transaction_df.loc[(Data_Aggregated_Transaction_df['Year'] == int(Year)) & (Data_Aggregated_Transaction_df['Quarter'] ==int(Quarter))]
topst=top_states_T.groupby('State')
x=topst.sum().sort_values(by=['Total_Transactions_count'], ascending=False)
y=topst.sum().sort_values(by=['Total_Amount'], ascending=False)
col1, col2, col3, col4= st.columns([2.5,2.5,2.5,2.5])
with col1:
    rt=top_states_r[1:11]
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">Registered Users</div>', unsafe_allow_html=True)
    st.markdown(rt[[ 'State','Registered_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col2:
    at=top_states_a[1:11]
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">PhonePeApp Openings</div>', unsafe_allow_html=True)
    st.markdown(at[['State','AppOpenings']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col3:
    x1=x[1:11]
    x2=x1.reset_index()
    x2.rename(columns = {'Total_Transactions_count':'Total_Transactions'}, inplace = True)
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">Total Transactions</div>', unsafe_allow_html=True)
    st.write(x2[['State','Total_Transactions']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col4:
    y1=y[1:11]
    y1=y1.reset_index()
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">Total Amount</div>', unsafe_allow_html=True)
    st.write(y1[['State','Total_Amount']].style.hide(axis="index").to_html(), unsafe_allow_html=True)         

#! title Name for LEAST STATES DATA 

text = ":bar_chart: LEAST STATES DATA :clipboard:"
st.write(
    f'<span style="margin-top:50px;margin-bottom:20px;font-family: Montserrat, sans-serif; font-weight: 700; font-size: 20px; display: block; text-align: center; color: #5400ae">{text}</span>',
    unsafe_allow_html=True
)
c1,c2=st.columns(2)
with c1:
    Year = st.selectbox(
            '**Select Year**',
            ('2022', '2021','2020','2019','2018'),key='y1h2')
with c2:
    Quarter = st.selectbox(
            '**Select Quarter**',
            ('1', '2', '3','4'),key='qgw2')
Data_Map_User_df=Data_Aggregated_User_Summary_df.copy() 
top_states=Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(Year)) & (Data_Map_User_df['Quarter'] ==int(Quarter))]
top_states_r = top_states.sort_values(by=['Registered_Users'], ascending=True)
top_states_a = top_states.sort_values(by=['AppOpenings'], ascending=True) 

top_states_T=Data_Aggregated_Transaction_df.loc[(Data_Aggregated_Transaction_df['Year'] == int(Year)) & (Data_Aggregated_Transaction_df['Quarter'] ==int(Quarter))]
topst=top_states_T.groupby('State')
x=topst.sum().sort_values(by=['Total_Transactions_count'], ascending=True)
y=topst.sum().sort_values(by=['Total_Amount'], ascending=True)
col1, col2, col3, col4= st.columns([2.5,2.5,2.5,2.5])
with col1:
    rt=top_states_r[1:11]
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">Registered Users</div>', unsafe_allow_html=True)
    st.markdown(rt[[ 'State','Registered_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col2:
    at=top_states_a[1:11]
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">PhonePeApp Openings</div>', unsafe_allow_html=True)
    st.markdown(at[['State','AppOpenings']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col3:
    x1=x[1:11]
    x2=x1.reset_index()
    x2.rename(columns = {'Total_Transactions_count':'Total_Transactions'}, inplace = True)
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">Total Transactions</div>', unsafe_allow_html=True)
    st.write(x2[['State','Total_Transactions']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col4:
    y1=y[1:11]
    y1=y1.reset_index()
    st.write(
            f'<div style="color:#840CA8;font-size:16px; font-weight:700;margin-top:20px;margin-bottom:20px;text-align:center">Total Amount</div>', unsafe_allow_html=True)
    st.write(y1[['State','Total_Amount']].style.hide(axis="index").to_html(), unsafe_allow_html=True)    



        # TODO -- nitish_sawant(49460)
        # TODO -- shreedhar_gehlot(49074)