import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu

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
        
        fig = px.histogram(df, x='Ins_Communication', color='College', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(rgt, x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(sht,  x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(ssk,  x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(apt,  x='Ins_Communication', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(df, x='Ins_Encouragement', color='College', barmode = 'group', text_auto=True)
        
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

        fig = px.histogram(sak, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(sat, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(srs, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(nkt, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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

        fig = px.histogram(rgt, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(sht, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(ssk, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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

        
        fig = px.histogram(msp, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(apt, x='Ins_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(df, x='Course_performance', color='College', barmode = 'group', text_auto=True)
        
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

        fig = px.histogram(sak, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(sat, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
    
        
        fig = px.histogram(srs, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
        


        fig = px.histogram(rgt, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
        

        fig = px.histogram(sht, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
          

        fig = px.histogram(ssk, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
    
        fig = px.histogram(msp, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
    
    
        
        fig = px.histogram(apt, x='Course_performance', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(df, x='Ins_Course_concept', color='College', barmode = 'group', text_auto=True)
        
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

        fig = px.histogram(sak, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(sat, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
    
        
        fig = px.histogram(srs, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
        


        fig = px.histogram(rgt, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
        

        fig = px.histogram(sht, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
          

        fig = px.histogram(ssk, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
    
        fig = px.histogram(msp, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
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
    
    
        
        fig = px.histogram(apt, x='Ins_Course_concept', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)

        #----------Helping_Student-----
        
    if options2 == "The instructor showed an interest in helping students learn" and side == "All":
        fig = px.histogram(df, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SAK":
        fig = px.histogram(sak, x='Helping_Student', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SAT":
        fig = px.histogram(sat, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SRS":
        fig = px.histogram(srs, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "NKT":
        fig = px.histogram(nkt, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "RGT":
        fig = px.histogram(rgt, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SHT":
        fig = px.histogram(sht, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "SSK":
        fig = px.histogram(ssk, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
   
    elif options2 == "The instructor showed an interest in helping students learn"and side == "MSP":
        fig = px.histogram(msp, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options2 == "The instructor showed an interest in helping students learn" and side == "APT":
        fig = px.histogram(apt, x='Helping_Student', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Imp_Topics', color='Imp_Topics', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sak, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        
          
        fig = px.histogram(srs, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(nkt, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
          

        
        fig = px.histogram(ssk, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Imp_Topics', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Theory_Practise',color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sht, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
          

        
        fig = px.histogram(ssk, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Theory_Practise', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='Learning_Material', color='Learning_Material', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
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
        
        fig = px.histogram(sat, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(rgt, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sht, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
          

        
        fig = px.histogram(ssk, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(msp, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Learning_Material', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
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
        
        fig = px.histogram(sat, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(rgt, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
          

        
        fig = px.histogram(ssk, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(apt, x='Course_Assignment', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
        
        
#----------------------perception/motivation----------------    
    
with tab3: 
    
    st.header("Perception About the course") 
        
    options5=st.selectbox('Select the Question', ["This course helps me improve my ability to interact with diverse groups of people", "The course challenges me to think deeply about the subject matter", "I attend classes regularly", "The course improves my communication and presentation skills"], key="options5")
    
    if options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="All":
            fig = px.histogram(df, x='College', y='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
        
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SAK":
            fig = px.histogram(sak, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SAT":
            fig = px.histogram(sat, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SRS":
            fig = px.histogram(srs, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="NKT":
            fig = px.histogram(nkt, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="RGT":
            fig = px.histogram(rgt, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SHT":
            fig = px.histogram(sht, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="SSK":
            fig = px.histogram(ssk, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="MSP":
            fig = px.histogram(msp, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "This course helps me improve my ability to interact with diverse groups of people" and side =="APT":
            fig = px.histogram(apt, x='Intract_people', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig) 
            
            
#2


    if options5 == "The course challenges me to think deeply about the subject matter" and side =="All":
            fig = px.histogram(df, x='College', y='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SAK":
            fig = px.histogram(sak, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
    elif options5 == "The course challenges me to think deeply about the subject matter" and  side =="SAT":
            fig = px.histogram(sat, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SRS":
            fig = px.histogram(srs, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="NKT":
            fig = px.histogram(nkt, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="RGT":
            fig = px.histogram(rgt, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SHT":
            fig = px.histogram(sht, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="SSK":
            fig = px.histogram(ssk, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="MSP":
            fig = px.histogram(msp, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course challenges me to think deeply about the subject matter" and side =="APT":
            fig = px.histogram(apt, x='Subject_Matters', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
#3
      
    if options5 == "I attend classes regularly" and side =="All":
            fig = px.histogram(df, x='Regular_Attendance', color='College', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)   
    elif options5 == "I attend classes regularly" and side =="SAK":
            fig = px.histogram(sak, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)        
    elif options5 == "I attend classes regularly" and side =="SAT":
            fig = px.histogram(sat, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="SRS":
            fig = px.histogram(srs, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="NKT":
            fig = px.histogram(nkt, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="RGT":
            fig = px.histogram(rgt, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="SHT":
            fig = px.histogram(sht, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 =="I attend classes regularly" and side =="SSK":
            fig = px.histogram(ssk, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="MSP":
            fig = px.histogram(msp, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "I attend classes regularly" and side =="APT":
            fig = px.histogram(apt, x='Regular_Attendance', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
#4

    if options5 == "The course improves my communication and presentation skills" and side =="All":
            fig = px.histogram(df, x='College', y='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
        
    elif options5 == "The course improves my communication and presentation skills" and side =="SAK":
            fig = px.histogram(sak, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
    elif options5 == "The course improves my communication and presentation skills" and side =="SAT":
            fig = px.histogram(sat, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="SRS":
            fig = px.histogram(srs, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="NKT":
            fig = px.histogram(nkt, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="RGT":
            fig = px.histogram(rgt, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="SHT":
            fig = px.histogram(sht, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="SSK":
            fig = px.histogram(ssk, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="MSP":
            fig = px.histogram(msp, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options5 == "The course improves my communication and presentation skills" and side =="APT":
            fig = px.histogram(apt, x='Communication_Skill', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
#motivation

with tab3: 
    
    st.header("Motivation") 
#1    
    options9=st.selectbox('Select the Question', ["What Influenced your Decision to take this course?", "How did you come to know about this course", "College Encouraged me to take up this course"],key='options9')
    
    if options9 == "What Influenced your Decision to take this course?" and side =="All":
            fig = px.histogram(df, x='College', color='Influence', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
        
    elif options9 == "What Influenced your Decision to take this course?" and side =="SAK":
            fig = px.histogram(sak, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
    elif options9 == "What Influenced your Decision to take this course?" and side =="SAT":
            fig = px.histogram(sat, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="SRS":
            fig = px.histogram(srs, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="NKT":
            fig = px.histogram(nkt, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="RGT":
            fig = px.histogram(rgt, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="SHT":
            fig = px.histogram(sht, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="SSK":
            fig = px.histogram(ssk, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="MSP":
            fig = px.histogram(msp, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "What Influenced your Decision to take this course?" and side =="APT":
            fig = px.histogram(apt, x='Influence', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig) 
            
#2

    if options9 == "How did you come to know about this course" and side =="All":
            fig = px.histogram(df, x='College', color='Course_Info', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
        
    elif options9 == "How did you come to know about this course" and side =="SAK":
            fig = px.histogram(sak, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
    elif options9 == "How did you come to know about this course" and side =="SAT":
            fig = px.histogram(sat, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="SRS":
            fig = px.histogram(srs, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="NKT":
            fig = px.histogram(nkt, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="RGT":
            fig = px.histogram(rgt, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="SHT":
            fig = px.histogram(sht, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="SSK":
            fig = px.histogram(ssk, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="MSP":
            fig = px.histogram(msp, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "How did you come to know about this course" and side =="APT":
            fig = px.histogram(apt, x='Course_Info', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
#3

    if options9 == "College Encouraged me to take up this course" and side =="All":
            fig = px.histogram(df, x='College', color='College_Encouragement', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
        
    elif options9 == "College Encouraged me to take up this course" and side =="SAK":
            fig = px.histogram(sak, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
            
    elif options9 == "College Encouraged me to take up this course" and side =="SAT":
            fig = px.histogram(sat, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="SRS":
            fig = px.histogram(srs, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="NKT":
            fig = px.histogram(nkt, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="RGT":
            fig = px.histogram(rgt, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="SHT":
            fig = px.histogram(sht, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="SSK":
            fig = px.histogram(ssk, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="MSP":
            fig = px.histogram(msp, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
            st.plotly_chart(fig)
    elif options9 == "College Encouraged me to take up this course" and side =="APT":
            fig = px.histogram(apt, x='College_Encouragement', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
        
        
        
        
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
        
        fig = px.histogram(sak, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(sat, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(srs, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        fig = px.histogram(rgt, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Recommend_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Recommend_Instructor', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Course_helpful', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Course_Impact', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='College', y='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Challenging', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(srs, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        
        fig = px.histogram(ssk, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Quality_Course', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Future_interest', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(df, x='College', y='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sak, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(sat, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(srs, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(nkt, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(rgt, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        
        fig = px.histogram(sht, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
          
        
        fig = px.histogram(ssk, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(msp, x='Experience', color='Branch', barmode = 'group', text_auto=True)
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
        
        fig = px.histogram(apt, x='Experience', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
        
        
 #-----------------overall score---------------   
with tab5:
    st.header("Overall Score")
    options7=st.selectbox('Select the Question', ["On a scale of 1-10 how would rate this program"], key="options7")
    
    #-----------Score---------
        
    if options7 == "On a scale of 1-10 how would rate this program" and side == "All":
        
        fig = px.histogram(df, x='College', y="Score", color='Score', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
        
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SAK":
        
        
        
        fig = px.histogram(sak, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SAT":
        fig = px.histogram(sat, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SRS":
        fig = px.histogram(srs, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "NKT":
        fig = px.histogram(nkt, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "RGT":
        fig = px.histogram(rgt, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SHT":
        fig = px.histogram(sht, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "SSK":
        fig = px.histogram(ssk, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
   
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "MSP":
        fig = px.histogram(msp, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
    elif options7 == "On a scale of 1-10 how would rate this program" and side == "APT":
        fig = px.histogram(apt, x='Score', color='Branch', barmode = 'group', text_auto=True)
        st.plotly_chart(fig)
    
        
       
    

    
    