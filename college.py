import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

import plotly.express as px
from PIL import Image


st.title('Course Review')

df=pd.read_csv("college-1.1.csv")



sak=df[df['College']=="SAK"]
sat=df[df['College']=="SAT"]
rgt=df[df['College']=="RGT"]
srs=df[df['College']=="SRS"]
nkt=df[df['College']=="NKT"]
sht=df[df['College']=="SHT"]
ssk=df[df['College']=="SSK"]
msp=df[df['College']=="MSP"]
apt=df[df['College']=="APT"]



st.sidebar.title('College')
side = st.sidebar.radio('Select the college:', ["All","SAK", "SAT", "SRS", "NKT", "RGT", "SHT", "SSK", "MSP","APT"], key="options")



tab1, tab2, tab3, tab4, tab5  = st.tabs(['Instructor Specific', 'Course Specific', 'Student Specific', 'Overall Evaluation', 'Overall Score'])

with tab1:
    st.header("Instructor Specific")
    options2=st.selectbox('Select the Question', ["The instructor communicated clearly and was easy to understand", "The instructor encouraged questions from students", "The standards of performance for the course were clearly communicated", "The instructor systematically relates course concepts, summarizes main points, and emphasizes material", "The instructor showed an interest in helping students learn"], key="options2")
    
    
#ALL--    
    if options2 == "The instructor communicated clearly and was easy to understand" and side == "All":
        
        
        
        
        fig = px.line(df,x=list(range(535)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=df[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
        

#SAK---        
    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sak[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#---SAT       

    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "SAT":
        fig = px.line(sat,x=list(range(48)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sat[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#-----srs        
    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "SRS":

#line        
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=srs[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
#plot        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#---nkt--
        
    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "NKT":
        
#line        
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
#plot        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
        
        
#---rgt----        
        
    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "RGT":
        
        #line        
        fig = px.line(rgt,x=list(range(23)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        
#plot    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')    
        
        df_g = rgt.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
    
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#---sht-----

    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "SHT":
        
        #line        
        fig = px.line(sht,x=list(range(24)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=sht[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        
#plot        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
    
        df_g = sht.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#---ssk ----

    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "SSK":
        
        #line        
        fig = px.line(ssk,x=list(range(60)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=ssk[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        

#plot
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
    
        df_g = ssk.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#msp        
    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "MSP":
    #line        
        fig = px.line(msp,x=list(range(80)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=msp[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )    
#plot        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x))) 
        
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#apt

    elif options2 == "The instructor communicated clearly and was easy to understand" and side == "APT":
        
         #line        
        fig = px.line(apt,x=list(range(54)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=apt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
#plot   
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = apt.groupby(['Ins_Communication', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Ins_Communication', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Communication', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Communication', y=['Counts'], color='Branch',barmode = 'group', text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#---------ins_encouragement------------

#all
    if options2 == "The instructor encouraged questions from students" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=df[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
#plot        
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
    
        fig.update_layout(legend=dict(
        orientation="h",
        entrywidth=70,
        yanchor="bottom",
        y=1.00,
        xanchor="center",
        x=1
        ))
        st.plotly_chart(fig)
#sak        
    elif options2 == "The instructor encouraged questions from students" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sak[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
         
#plot
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#sat        
    elif options2 == "The instructor encouraged questions from students" and side == "SAT":
        fig = px.line(sat,x=list(range(48)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sat[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
#plot    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#srs        
    elif options2 == "The instructor encouraged questions from students" and side == "SRS":
    #line        
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=srs[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
    
#plot    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
    
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#nkt        
    elif options2 == "The instructor encouraged questions from students" and side == "NKT":
    
    #line        
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
#plot    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
    
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#rgt        
    elif options2 == "The instructor encouraged questions from students" and side == "RGT":
      #line        
        fig = px.line(rgt,x=list(range(23)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
#plot
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = rgt.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#sht        
    elif options2 == "The instructor encouraged questions from students" and side == "SHT":
       #line        
        fig = px.line(sht,x=list(range(24)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=sht[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
#plot
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sht.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
    
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#ssk        
    elif options2 == "The instructor encouraged questions from students" and side == "SSK":
        
      #line        
        fig = px.line(ssk,x=list(range(60)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=ssk[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
#plot
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = ssk.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
    
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#msp        
    elif options2 == "The instructor encouraged questions from students" and side == "MSP":
#line
        fig = px.line(msp,x=list(range(80)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=msp[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        
#plot
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = msp.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#apt        
    elif options2 == "The instructor encouraged questions from students" and side == "APT":
     #line        
        fig = px.line(apt,x=list(range(54)), y='ins_sum')
        st.plotly_chart(fig)
#table        
        t=apt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
    
    
#plot   
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = apt.groupby(['Ins_Encouragement', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Ins_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Encouragement', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
    
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#------------Course_performance---------------
#all
    if options2 == "The standards of performance for the course were clearly communicated" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=df[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#sak        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sak[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        
        st.plotly_chart(fig)
        
#sat        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "SAT":
        fig = px.line(sat,x=list(range(48)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sat[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#srs        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "SRS":
            
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=srs[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#nkt        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "NKT":
    
            
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=nkt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#rgt        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "RGT":
              
        fig = px.line(rgt,x=list(range(23)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=rgt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        

        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = rgt.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#sht        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "SHT":
              
        fig = px.line(sht,x=list(range(24)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sht[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')

        
        df_g = sht.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#ssk        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "SSK":
        
              
        fig = px.line(ssk,x=list(range(60)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g =ssk.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#msp        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "MSP":

        fig = px.line(msp,x=list(range(80)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=msp[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#apt        
    elif options2 == "The standards of performance for the course were clearly communicated" and side == "APT":
             
        fig = px.line(apt,x=list(range(54)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=apt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = apt.groupby(['Course_performance', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Course_performance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_performance', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_performance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#--------------Ins_Course_concept

    #all
    if options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=df[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#sak        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sak[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#sat        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "SAT":
        fig = px.line(sat,x=list(range(48)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sat[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#srs        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "SRS":
            
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=srs[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#nkt        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "NKT":
    
            
        fig = px.line(srs,x=list(range(75)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=nkt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#rgt        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "RGT":
              
        fig = px.line(rgt,x=list(range(23)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=rgt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')

        
        df_g = rgt.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#sht        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "SHT":
              
        fig = px.line(sht,x=list(range(24)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=sht[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sht.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
#ssk        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "SSK":
        
              
        fig = px.line(ssk,x=list(range(60)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied') 

        
        df_g = ssk.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#msp        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "MSP":

        fig = px.line(msp,x=list(range(80)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=msp[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
#apt        
    elif options2 == "The instructor systematically relates course concepts, summarizes main points, and emphasizes material" and side == "APT":
             
        fig = px.line(apt,x=list(range(54)), y='ins_sum')
        st.plotly_chart(fig)
        
        t=apt[['ins_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = apt.groupby(['Ins_Course_concept', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Ins_Course_concept', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Ins_Course_concept', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Ins_Course_concept', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)

        #----------Helping_Student-----
        
    if options2 == "The instructor showed an interest in helping students learn" and side == "All":
        
        df_g = df.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SAK":
        
        df_g = sak.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SAT":
        
        
        df_g = sat.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SRS":
        
        df_g = srs.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "NKT":
        
        df_g = nkt.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "RGT":
        
        df_g = rgt.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SHT":
        
        df_g = sht.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SSK":
        
        
        df_g = ssk.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
   
    elif options2 == "The instructor showed an interest in helping students learn"and side == "MSP":
        
        
        df_g = msp.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "APT":
        
        df_g = apt.groupby(['Helping_Student', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Helping_Student', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Helping_Student', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Helping_Student', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
        
        
 #------------------- tab2 begin------------    
with tab2:
    st.header("Course Specific")
    options3=st.selectbox('Select the Question', ["I believe the topics covered in this course are important", "This course provides a good balance of theory and practice"
, "The course provides learning materials that improves my understanding and increased my knowledge"
, "The course assignments  are reflective of the course content and syllabus"], key="options3")
    
 #----------- Imp_Topics----------------------
    if options3 == "I believe the topics covered in this course are important" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=df[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    elif options3 == "I believe the topics covered in this course are important" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sak[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
    elif options3 == "I believe the topics covered in this course are important" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sat[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "I believe the topics covered in this course are important" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
          
        
        df_g = srs.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "I believe the topics covered in this course are important" and side == "NKT":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "I believe the topics covered in this course are important" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = rgt.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "I believe the topics covered in this course are important" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=sht[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = sht.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "I believe the topics covered in this course are important" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=ssk[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = ssk.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
   
    elif options3 == "I believe the topics covered in this course are important"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=msp[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "I believe the topics covered in this course are important" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=apt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = apt.groupby(['Imp_Topics', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Imp_Topics', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Imp_Topics', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Imp_Topics', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
        
#---------- Theory_Practise---------

    if options3 == "This course provides a good balance of theory and practice" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=df[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    elif options3 == "This course provides a good balance of theory and practice" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sak[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        st.plotly_chart(fig)
    elif options3 == "This course provides a good balance of theory and practice" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sat[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "This course provides a good balance of theory and practice" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "This course provides a good balance of theory and practice" and side == "NKT":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "This course provides a good balance of theory and practice" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = rgt.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "This course provides a good balance of theory and practice" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=sht[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sht.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "This course provides a good balance of theory and practice" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=ssk[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = ssk.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
   
    elif options3 == "This course provides a good balance of theory and practice"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=msp[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "This course provides a good balance of theory and practice" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=apt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = apt.groupby(['Theory_Practise', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Theory_Practise', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Theory_Practise', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Theory_Practise', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
        #------------Learning_Material---------
        
    if options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=df[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sak[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        st.plotly_chart(fig)
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sat[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "NKT":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = rgt.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=sht[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sht.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=ssk[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = ssk.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
   
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=msp[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )    
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course provides learning materials that improves my understanding and increased my knowledge" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=apt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
       
        df_g = apt.groupby(['Learning_Material', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Learning_Material', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Learning_Material', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Learning_Material', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
        
        #---------------Course_Assignment----------
        
    if options3 == "The course assignments  are reflective of the course content and syllabus" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=df[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
        ))
        st.plotly_chart(fig)
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "SAK":
        
        
        
        fig = px.line(sak,x=list(range(97)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sak[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g =sak.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        st.plotly_chart(fig)
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=sat[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "NKT":
        
        fig = px.line(srs,x=list(range(75)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = rgt.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=sht[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = sht.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='cou_sum')
        st.plotly_chart(fig)
        
        t=ssk[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = ssk.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
   
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=msp[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )    
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
       
        df_g = msp.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
    
    elif options3 == "The course assignments  are reflective of the course content and syllabus" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='cou_sum')
        st.plotly_chart(fig)
#table        
        t=apt[['cou_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = apt.groupby(['Course_Assignment', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Course_Assignment', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Assignment', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Assignment', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
        ))
        st.plotly_chart(fig)
        
        
#----------------------perception/motivation----------------    
    
with tab3: 
    
    st.header("Perception About the course") 
        
    options5=st.selectbox('Select the Question', ["This course helps me improve my ability to interact with diverse groups of people", "The course challenges me to think deeply about the subject matter", "I attend classes regularly", "The course improves my communication and presentation skills"], key="options5")
    
    if options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="All":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = df.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
        
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SAK":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
           
            df_g = sak.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SAT":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sat.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SRS":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = srs.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="NKT":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = nkt.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="RGT":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = rgt.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SHT":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sht.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SSK":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = ssk.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="MSP":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = msp.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="APT":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = apt.groupby(['Intract_people', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['Intract_people', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Intract_people', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Intract_people', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig) 
            
            
#2


    if options5 == "The course challenges me to think deeply about the subject matter" and side =="All":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = df.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SAK":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sak.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
    elif options5 == "The course challenges me to think deeply about the subject matter" and  side =="SAT":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sat.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SRS":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = srs.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="NKT":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
           
            df_g = nkt.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="RGT":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = rgt.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SHT":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sht.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SSK":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = ssk.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="MSP":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = msp.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="APT":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = apt.groupby(['Subject_Matters', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['Subject_Matters', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Subject_Matters', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Subject_Matters', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
#3
      
    if options5 == "I attend classes regularly" and side =="All":
        
            
            
            df_g = df.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)   
    elif options5 == "I attend classes regularly" and side =="SAK":
        
            
            
            df_g = sak.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)        
    elif options5 == "I attend classes regularly" and side =="SAT":
            
            
            
            df_g = sat.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="SRS":
        
            
            
            df_g = srs.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="NKT":
        
            
            
            df_g = nkt.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="RGT":
            
            df_g = rgt.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="SHT":
            
            df_g = sht.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 =="I attend classes regularly" and side =="SSK":
            
            df_g = ssk.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="MSP":
            
            df_g = msp.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="APT":
           
            df_g = apt.groupby(['Regular_Attendance', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['Regular_Attendance', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Regular_Attendance', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Regular_Attendance', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
#4

    if options5 == "The course improves my communication and presentation skills" and side =="All":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = df.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
        
    elif options5 == "The course improves my communication and presentation skills" and side =="SAK":
        
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sak.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
    elif options5 == "The course improves my communication and presentation skills" and side =="SAT":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sat.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="SRS":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = srs.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="NKT":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = nkt.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="RGT":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = rgt.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="SHT":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = sht.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="SSK":
            
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = ssk.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="MSP":
           
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = msp.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="APT":
            st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
            
            df_g = apt.groupby(['Communication_Skill', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['Communication_Skill', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Communication_Skill', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Communication_Skill', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
#motivation

with tab3: 
    
    st.header("Motivation") 
#1    
    options9=st.selectbox('Select the Question', ["What Influenced your Decision to take this course?", "How did you come to know about this course", "College Encouraged me to take up this course"],key='options9')
    
    if options9 == "What Influenced your Decision to take this course?" and side =="All":
            
            df_g = df.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
        
    elif options9 == "What Influenced your Decision to take this course?" and side =="SAK":
            
            df_g = sak.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
    elif options9 == "What Influenced your Decision to take this course?" and side =="SAT":
            
            df_g = sat.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="SRS":
            
            df_g = srs.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="NKT":
            
            df_g = nkt.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="RGT":
            
            df_g = rgt.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="SHT":
            
            df_g = sht.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="SSK":
            
            df_g = ssk.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="MSP":
            
            df_g = msp.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="APT":
            
            df_g = apt.groupby(['Influence', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['Influence', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Influence', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Influence', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig) 
            
#2

    if options9 == "How did you come to know about this course" and side =="All":
            
            df_g = df.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
        
    elif options9 == "How did you come to know about this course" and side =="SAK":
            
            df_g = sak.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
    elif options9 == "How did you come to know about this course" and side =="SAT":
            
            df_g = sat.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="SRS":
            
            df_g = srs.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="NKT":
            
            df_g = nkt.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="RGT":
            
            df_g = rgt.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="SHT":
            
            df_g = sht.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="SSK":
            
            df_g = ssk.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="MSP":
            
            df_g = msp.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="APT":
            
            df_g = apt.groupby(['Course_Info', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['Course_Info', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['Course_Info', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='Course_Info', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
#3

    if options9 == "College Encouraged me to take up this course" and side =="All":
            
            df_g = df.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = df.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
        
    elif options9 == "College Encouraged me to take up this course" and side =="SAK":
            
            df_g = sak.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = sak.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
            
    elif options9 == "College Encouraged me to take up this course" and side =="SAT":
            
            df_g = sat.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = sat.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="SRS":
            
            df_g = srs.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = srs.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="NKT":
            
            df_g = nkt.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = nkt.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="RGT":
            
            df_g = rgt.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = rgt.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="SHT":
            
            df_g = sht.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = sht.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="SSK":
            
            df_g = ssk.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = ssk.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="MSP":
            
            df_g = msp.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = msp.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="APT":
            
            df_g = apt.groupby(['College_Encouragement', 'Branch']).size().reset_index()
            df_g['percentage'] = apt.groupby(['College_Encouragement', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
            df_g.columns = ['College_Encouragement', 'Branch', 'Counts', 'Percentage']
            fig= px.bar(df_g, x='College_Encouragement', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
            
            fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
            st.plotly_chart(fig)


    
            
            
            

#--------------------overall evaluation---------------------------------    
with tab4:
    
    
    st.header("Overall Evaluation")
    options6=st.selectbox('Select the Question', ["I would highly recommend this course to other students", "I would highly recommend this instructor to other students", "The course is helpful in progress toward my career", 
"This course has a high educational value and impact", "This course was challenging", "Overall, this course is meeting my expectations for the quality of the course", "Would you be interested in such Programs in the Future?", "How would you describe your experience?"], key="options6")
    
     #------------Recommend_Course---------
        
    if options6 == "I would highly recommend this course to other students" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = df.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "I would highly recommend this course to other students" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sak.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "I would highly recommend this course to other students" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sat.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this course to other students" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = srs.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this course to other students" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = nkt.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 =="I would highly recommend this course to other students" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = rgt.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this course to other students" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sht.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this course to other students" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = ssk.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "I would highly recommend this course to other students" and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = msp.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this course to other students" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = apt.groupby(['Recommend_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Recommend_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
  #------------Recommend_Instructor---------
        
    if options6 == "I would highly recommend this instructor to other students" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = df.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "I would highly recommend this instructor to other students" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sak.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "I would highly recommend this instructor to other students" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sat.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this instructor to other students" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = srs.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this instructor to other students" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = nkt.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this instructor to other students" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = rgt.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this instructor to other students" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        
        df_g = sht.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this instructor to other students" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree') 
        
        
        df_g = ssk.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "I would highly recommend this instructor to other students"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = msp.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "I would highly recommend this instructor to other students" and side == "APT":
        
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = apt.groupby(['Recommend_Instructor', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Recommend_Instructor', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Recommend_Instructor', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Recommend_Instructor', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)      
        
#------------Course_helpful---------
        
    if options6 == "The course is helpful in progress toward my career" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = df.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "The course is helpful in progress toward my career" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sak.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "The course is helpful in progress toward my career" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sat.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "The course is helpful in progress toward my career" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = srs.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "The course is helpful in progress toward my career" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = nkt.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "The course is helpful in progress toward my career" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = rgt.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "The course is helpful in progress toward my career" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        
        df_g = sht.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "The course is helpful in progress toward my career" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree') 
        
        
        df_g = ssk.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "The course is helpful in progress toward my career"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = msp.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "The course is helpful in progress toward my career" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        fig = px.histogram(apt, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
        df_g = apt.groupby(['Course_helpful', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Course_helpful', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_helpful', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_helpful', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)        
        
#------------Course_Impact---------
        
    if options6 == "This course has a high educational value and impact" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = df.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "This course has a high educational value and impact" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sak.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "This course has a high educational value and impact" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        fig = px.histogram(sat, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
        df_g = sat.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course has a high educational value and impact" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = srs.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course has a high educational value and impact" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = nkt.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course has a high educational value and impact" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = rgt.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course has a high educational value and impact" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sht.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course has a high educational value and impact" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = ssk.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "This course has a high educational value and impact"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = msp.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course has a high educational value and impact" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = apt.groupby(['Course_Impact', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Course_Impact', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Course_Impact', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Course_Impact', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
 
 #------------Challenging---------
        
    if options6 == "This course was challenging" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = df.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "This course was challenging" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sak.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "This course was challenging" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sat.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course was challenging" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = srs.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course was challenging" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = nkt.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course was challenging" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = rgt.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course was challenging" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sht.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course was challenging" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = ssk.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "This course was challenging"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = msp.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "This course was challenging" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = apt.groupby(['Challenging', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Challenging', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Challenging', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Challenging', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)

#-----------Quality_Course---------
        
    if options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = df.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = sak.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sat.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "SRS":
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = srs.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = nkt.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = rgt.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        df_g = sht.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = ssk.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course"and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = msp.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Overall, this course is meeting my expectations for the quality of the course" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Strongly disagree 2-Disagree 3-Neutral 4-Agree 5-Strongly Agree')
        
        df_g = apt.groupby(['Quality_Course', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Quality_Course', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Quality_Course', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Quality_Course', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
      
 
 #-----------Future_interest---------
        
    if options6 == "Would you be interested in such Programs in the Future?" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = df.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = sak.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = sat.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = srs.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = nkt.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = rgt.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        
        df_g = sht.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely') 
        
        
        df_g = ssk.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "MSP":
        
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = msp.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "Would you be interested in such Programs in the Future?" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Extremely Likely 2-Unlikely 3-Neutral 4-Likely 5-Extremely Likely')
        
        df_g = apt.groupby(['Future_interest', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Future_interest', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Future_interest', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Future_interest', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
 
 #-----------Experience---------
        
    if options6 == "How would you describe your experience?" and side == "All":
        
        fig = px.line(df,x=list(range(535)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=df[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = df.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = df.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
    elif options6 == "How would you describe your experience?" and side == "SAK":
        
        fig = px.line(sak,x=list(range(97)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sak[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sak.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = sak.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    elif options6 == "How would you describe your experience?" and side == "SAT":
        
        fig = px.line(sat,x=list(range(48)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sat[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = sat.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = sat.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "How would you describe your experience?" and side == "SRS":
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = srs.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = srs.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "How would you describe your experience?" and side == "NKT":
        
        
        fig = px.line(srs,x=list(range(75)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=nkt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = nkt.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = nkt.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "How would you describe your experience?" and side == "RGT":
        
        fig = px.line(rgt,x=list(range(23)), y='ovral_sum')
        st.plotly_chart(fig)
#table        
        t=rgt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
#download        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = rgt.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = rgt.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "How would you describe your experience?" and side == "SHT":
        
        fig = px.line(sht,x=list(range(24)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=sht[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        
        df_g = sht.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = sht.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "How would you describe your experience?" and side == "SSK":
        
        fig = px.line(ssk,x=list(range(60)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=ssk[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )
          
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = ssk.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = ssk.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
   
    elif options6 == "How would you describe your experience?" and side == "MSP":
        
        fig = px.line(msp,x=list(range(80)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=msp[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
        
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        )  
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = msp.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = msp.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
    
    elif options6 == "How would you describe your experience?" and side == "APT":
        
        fig = px.line(apt,x=list(range(54)), y='ovral_sum')
        st.plotly_chart(fig)
        
        t=apt[['ovral_sum']].aggregate(['mean','min','max'])
        st.table(t)
       
        @st.cache
        def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(t)

        st.download_button(
            label="Download",
            data=csv,
            file_name='t.csv',
            mime='text/csv',
        ) 
        st.markdown('1-Very Unsatisfied 2-Unsatisfied 3-Neutral 4-Satisfied 5-Satisfied')
        
        df_g = apt.groupby(['Experience', 'Branch']).size().reset_index()
        df_g['percentage'] = apt.groupby(['Experience', 'Branch']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
        df_g.columns = ['Experience', 'Branch', 'Counts', 'Percentage']
        fig= px.bar(df_g, x='Experience', y=['Counts'], color='Branch',barmode = 'group',  text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
 #-----------------overall score---------------   
with tab5:
    st.header("Overall Score")
    options7=st.selectbox('Select the Question', ["On a scale of 1-10 how would rate this program"], key="options7")
    
    #-----------Score---------
        
    if options7 == "On a scale of 1-10 how would rate this program" and side == "All":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(df, x='Score', color='Score', barnorm='percent')
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=1.00
            ))
        st.plotly_chart(fig)
        
        
        
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SAK":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        
        fig = px.histogram(sak, x='Score', color='Score', barnorm='percent')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
        
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SAT":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(sat, x='Score', color='Score', barnorm='percent')
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SRS":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        
        fig = px.histogram(srs, x='Score', color='Score', barnorm='percent')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "NKT":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(nkt, x='Score', color='Score', barnorm='percent')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "RGT":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(rgt, x='Score', color='Score', barnorm='percent')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SHT":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(sht, x='Score', color='Score', barnorm='percent')
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SSK":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(ssk, x='Score', color='Score', barnorm='percent')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
   
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "MSP":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(msp, x='Score', color='Score', barnorm='percent')
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="right",
            x=0.5
            ))
        st.plotly_chart(fig)
        
        
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "APT":
        
        st.markdown('1 = Poor, 10  =  Good')
        
        fig = px.histogram(apt, x='Score', color='Score', barnorm='percent')
        
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.00,
            xanchor="center",
            x=0.90
            ))
        st.plotly_chart(fig)
    
    
       

    
    