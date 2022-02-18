import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from textwrap import wrap

def app():
    # # --- Load Data From CSV ----
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    @st.cache()
    def get_data_from_csv():
        df = pd.read_csv('attrition.csv')
        return df

    df = get_data_from_csv()

    # plot 1 : Distribution of Monthly Income
    col1, col2 = st.columns([2,1])
    with col1:
        option = st.selectbox(
            'Choose one feature to plot',
            ('Monthly Income', 'Distance from Home', 'Years at Company'))
        if option == 'Monthly Income':
            option = 'MonthlyIncome'
            explanation = '''Average salary of employee is $6500 per month, median $4900 with minimum $1000 and maximum $20000. 
                             The distribution plot show that median salary of employee who attrition is $3200. 
                             This value is much lower than  overall  average salary, even only half of it. On the other hand, 
                             we also find some of employee attrition who have high salary.'''
        if option == 'Distance from Home':
            option = 'DistanceFromHome'
            explanation = '''Employee who are away from the company are more tending to attrition,
             than those whose house is near'''
        if option == 'Years at Company':
            option = 'YearsAtCompany'
            explanation = '''Employee who work in company less than 7 years have hight attrition rate, than who work more than  7 years.
                            We also found that employee who works more than 10 years is attrition. 
                            In this case, it is most likely because the employee has retired'''
        fig=px.histogram(df, x=option, color='Attrition', 
                 opacity=0.8, histnorm='density', barmode='relative', marginal='box',
                 color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'})
        fig.update_layout(title_text='Distribution of {} by Attrion'.format(option),
                        xaxis_title=option, yaxis_title='Density',font_color='#28221D',
                        paper_bgcolor='#F4F2F0', plot_bgcolor='#F4F2F0')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("<h4 style='text-align: center;'>Insight Related to {}</h4>".format(option), unsafe_allow_html=True)
        st.markdown('----------'*25)
        st.write(explanation)
    # Plot 2 & 3: distribution by attrition
    col3, col4 = st.columns(2)
    with col3:
        option1 = st.selectbox(
        'Which Feature do you wanna choose?',
        ('Over Time', 'Marital Status', 'Job Role','Gender','Department'))
        if option1 == 'Gender':
            column_name = 'Gender'
            title_two = 'We can see from the plot below, that male are more likely to attrition than female.'
        if option1 == 'Marital Status':
            column_name = 'MaritalStatus'
            title_two = 'Attrition rate of single employee is higher than married or divorced.'
        if option1 == 'Job Role':
            column_name = 'JobRole'
            title_two = 'Sales representative is job role with highest attrition rate, and research director is the lowest'
        if option1 == 'Over Time':
            column_name = 'OverTime'
            title_two = 'Employee who works overtime have highest rate of attrition than who are not overtime.'
        if option1 == 'Department':
            column_name = 'Department'
            title_two = 'Related to job role, sales department has highest attrition.'
        
        title_one = 'Attrition Rates by {}'.format(column_name)
        data_attrition_by = df.groupby([column_name])['Attrition'].value_counts(normalize=True)
        data_attrition_by = data_attrition_by.mul(100).rename('Percent').reset_index()
        fig = px.bar(data_attrition_by, 
                    x=column_name, 
                    y="Percent", 
                    color="Attrition", 
                    barmode="group",
                    text='Percent', opacity=.75,  category_orders={'Attrition': ['Yes', 'No']},
                    color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'}) 

        fig.update_traces(texttemplate='%{text:.3s}%', textposition='outside',
                        marker_line=dict(width=1, color='#28221D'),  width=.4)
        fig.update_layout(
                        # title_text='Attrition Rates by {}'.format(column_name), 
                        title=f'<b>{"<br>".join(wrap(title_one, 70))}</b><br><sub>{title_two}</sub>',
                        yaxis_ticksuffix = '%',
                        paper_bgcolor='#F4F2F0', 
                        plot_bgcolor='#F4F2F0', 
                        font_color='#28221D',
                        xaxis=dict(tickangle=30))
        fig.update_xaxes(showticklabels=True,tickangle=30,col=2)
        fig.update_yaxes(title = "", zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')

        st.plotly_chart(fig, use_container_width=True)

    with col4:
        option2 = st.selectbox(
            'Choose one feature above',
            ('Monthly Income', 'Distance from Home', 'Years at Company'))
        if option2 == 'Monthly Income':
            column_name2 = 'MonthlyIncome'
        if option2 == 'Distance from Home':
            column_name2 = 'DistanceFromHome'
        if option2 == 'Years at Company':
            column_name2 = 'YearsAtCompany'
 
        plot_df = df.groupby([column_name, 'Attrition'])[column_name2].mean()
        plot_df = plot_df.rename(option2).reset_index().sort_values(option2, ascending=False)
        fig = px.bar(plot_df, x=column_name, y=option2, color='Attrition', text=option2,  
                    barmode='group', opacity=0.75, color_discrete_map={'Yes': '#214D5C','No': '#ACBCC2'})
        fig.update_traces(texttemplate='%{text:,.1f}', textposition='outside',
                        marker_line=dict(width=1, color='#28221D'))
        fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')
        fig.update_layout( title_text ='Average {} by Attrition & {}'.format(option2, option1), font_color='#28221D',yaxis_title=option2, paper_bgcolor='#F4F2F0', plot_bgcolor='#F4F2F0')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>Insight Related to Performance and Satisfaction</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'> 1 (Low), 2 (Medium), 3 (High), 4 (Very High)</h5>", unsafe_allow_html=True)
    col5, col6, col7 = st.columns(3)
    with col5:
        title_one = 'Attrition Rates by {}'.format('JobSatisfaction')
        data_attrition_by = df.groupby(['JobSatisfaction'])['Attrition'].value_counts(normalize=True)
        data_attrition_by = data_attrition_by.mul(100).rename('Percent').reset_index()
        fig = px.bar(data_attrition_by, 
                    x='JobSatisfaction', 
                    y="Percent", 
                    color="Attrition", 
                    barmode="group",
                    text='Percent', opacity=.75,  category_orders={'Attrition': ['Yes', 'No']},
                    color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'}) 

        fig.update_traces(texttemplate='%{text:.3s}%', textposition='outside',
                        marker_line=dict(width=1, color='#28221D'),  width=.4)
        fig.update_layout(
                        # title_text='Attrition Rates by {}'.format(column_name), 
                        title=f'<b>{"<br>".join(wrap(title_one, 70))}</b><br>',
                        yaxis_ticksuffix = '%',
                        paper_bgcolor='#F4F2F0', 
                        plot_bgcolor='#F4F2F0', 
                        font_color='#28221D',
                        xaxis=dict(tickangle=30))
        fig.update_xaxes(showticklabels=True,tickangle=30,col=2)
        fig.update_yaxes(title = "", zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')

        st.plotly_chart(fig, use_container_width=True)
    
    with col6:
        title_one = 'Attrition Rates by {}'.format('RelationshipSatisfaction')
        data_attrition_by = df.groupby(['RelationshipSatisfaction'])['Attrition'].value_counts(normalize=True)
        data_attrition_by = data_attrition_by.mul(100).rename('Percent').reset_index()
        fig = px.bar(data_attrition_by, 
                    x='RelationshipSatisfaction', 
                    y="Percent", 
                    color="Attrition", 
                    barmode="group",
                    text='Percent', opacity=.75,  category_orders={'Attrition': ['Yes', 'No']},
                    color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'}) 

        fig.update_traces(texttemplate='%{text:.3s}%', textposition='outside',
                        marker_line=dict(width=1, color='#28221D'),  width=.4)
        fig.update_layout(
                        # title_text='Attrition Rates by {}'.format(column_name), 
                        title=f'<b>{"<br>".join(wrap(title_one, 70))}</b><br>',
                        yaxis_ticksuffix = '%',
                        paper_bgcolor='#F4F2F0', 
                        plot_bgcolor='#F4F2F0', 
                        font_color='#28221D',
                        xaxis=dict(tickangle=30))
        fig.update_xaxes(showticklabels=True,tickangle=30,col=2)
        fig.update_yaxes(title = "", zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')

        st.plotly_chart(fig, use_container_width=True)
    
    with col7:
        title_one = 'Attrition Rates by {}'.format('EnvironmentSatisfaction')
        data_attrition_by = df.groupby(['EnvironmentSatisfaction'])['Attrition'].value_counts(normalize=True)
        data_attrition_by = data_attrition_by.mul(100).rename('Percent').reset_index()
        fig = px.bar(data_attrition_by, 
                    x='EnvironmentSatisfaction', 
                    y="Percent", 
                    color="Attrition", 
                    barmode="group",
                    text='Percent', opacity=.75,  category_orders={'Attrition': ['Yes', 'No']},
                    color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'}) 

        fig.update_traces(texttemplate='%{text:.3s}%', textposition='outside',
                        marker_line=dict(width=1, color='#28221D'),  width=.4)
        fig.update_layout(
                        # title_text='Attrition Rates by {}'.format(column_name), 
                        title=f'<b>{"<br>".join(wrap(title_one, 70))}</b><br>',
                        yaxis_ticksuffix = '%',
                        paper_bgcolor='#F4F2F0', 
                        plot_bgcolor='#F4F2F0', 
                        font_color='#28221D',
                        xaxis=dict(tickangle=30))
        fig.update_xaxes(showticklabels=True,tickangle=30,col=2)
        fig.update_yaxes(title = "", zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')

        st.plotly_chart(fig, use_container_width=True)

    col8, col9 = st.columns(2)
    with col8:
        title_one = 'Attrition Rates by {}'.format('WorkLifeBalance')
        data_attrition_by = df.groupby(['WorkLifeBalance'])['Attrition'].value_counts(normalize=True)
        data_attrition_by = data_attrition_by.mul(100).rename('Percent').reset_index()
        fig = px.bar(data_attrition_by, 
                    x='WorkLifeBalance', 
                    y="Percent", 
                    color="Attrition", 
                    barmode="group",
                    text='Percent', opacity=.75,  category_orders={'Attrition': ['Yes', 'No']},
                    color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'}) 

        fig.update_traces(texttemplate='%{text:.3s}%', textposition='outside',
                        marker_line=dict(width=1, color='#28221D'),  width=.4)
        fig.update_layout(
                        # title_text='Attrition Rates by {}'.format(column_name), 
                        title=f'<b>{"<br>".join(wrap(title_one, 70))}</b><br>',
                        yaxis_ticksuffix = '%',
                        paper_bgcolor='#F4F2F0', 
                        plot_bgcolor='#F4F2F0', 
                        font_color='#28221D',
                        xaxis=dict(tickangle=30))
        fig.update_xaxes(showticklabels=True,tickangle=30,col=2)
        fig.update_yaxes(title = "", zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')

        st.plotly_chart(fig, use_container_width=True)
        
        
        with col9:
            title_one = 'Attrition Rates by {}'.format('JobInvolvement')
            data_attrition_by = df.groupby(['JobInvolvement'])['Attrition'].value_counts(normalize=True)
            data_attrition_by = data_attrition_by.mul(100).rename('Percent').reset_index()
            fig = px.bar(data_attrition_by, 
                        x='JobInvolvement', 
                        y="Percent", 
                        color="Attrition", 
                        barmode="group",
                        text='Percent', opacity=.75,  category_orders={'Attrition': ['Yes', 'No']},
                        color_discrete_map={'Yes': '#C02B34','No': '#CDBBA7'}) 

            fig.update_traces(texttemplate='%{text:.3s}%', textposition='outside',
                            marker_line=dict(width=1, color='#28221D'),  width=.4)
            fig.update_layout(
                            # title_text='Attrition Rates by {}'.format(column_name), 
                            title=f'<b>{"<br>".join(wrap(title_one, 70))}</b><br><sub>{title_two}</sub>',
                            yaxis_ticksuffix = '%',
                            paper_bgcolor='#F4F2F0', 
                            plot_bgcolor='#F4F2F0', 
                            font_color='#28221D',
                            xaxis=dict(tickangle=30))
            fig.update_xaxes(showticklabels=True,tickangle=30,col=2)
            fig.update_yaxes(title = "", zeroline=True, zerolinewidth=1, zerolinecolor='#28221D')

            st.plotly_chart(fig, use_container_width=True)
        