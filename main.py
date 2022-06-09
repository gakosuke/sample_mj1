import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.header("点数")
point_a=st.sidebar.number_input('1着',-100000,100000,25000,step=100)
tba1=st.sidebar.checkbox('飛ばし1')
tbi1=st.sidebar.checkbox('飛び1')
y1=st.sidebar.checkbox('ヤキトリ1')

point_b=st.sidebar.number_input('2着',-100000,100000,25000,step=100)
tba2=st.sidebar.checkbox('飛ばし2')
tbi2=st.sidebar.checkbox('飛び2')
y2=st.sidebar.checkbox('ヤキトリ2')

point_c=st.sidebar.number_input('3着',-100000,100000,25000,step=100)
tba3=st.sidebar.checkbox('飛ばし3')
tbi3=st.sidebar.checkbox('飛び3')
y3=st.sidebar.checkbox('ヤキトリ3')

point_d=st.sidebar.number_input('4着',-100000,100000,25000,step=100)
tba4=st.sidebar.checkbox('飛ばし4')
tbi4=st.sidebar.checkbox('飛び4')
y4=st.sidebar.checkbox('ヤキトリ4')

st.sidebar.header("初期登録")
kijyun=st.sidebar.number_input('基準',20000,40000,30000,step=1000)
tobi=st.sidebar.number_input('飛び',0,100,10,step=5)
yakitori=st.sidebar.number_input('ヤキトリ',0,100,15,step=15)
uma1=st.sidebar.number_input('4位→1位',0,30,20,step=10)
uma2=st.sidebar.number_input('3位→2位',0,20,10,step=5)


st.header('点数表')
name_a='1位'
name_b='2位'
name_c='3位'
name_d='4位'

list=[point_a,point_b,point_c,point_d]
newlist=sorted(list,reverse=True)
rank4=(round(newlist[3],-3)-kijyun)/1000-uma1
rank3=(round(newlist[2],-3)-kijyun)/1000-uma2
rank2=(round(newlist[1],-3)-kijyun)/1000+uma2
rank1=-(rank4+rank3+rank2)
ycount=0

#飛ばしflag
tbaf1=0
tbaf2=0
tbaf3=0
tbaf4=0
#飛びflag
tbif1=0
tbif2=0
tbif3=0
tbif4=0
#ヤキトリflag
y1f=0
y2f=0
y3f=0
y4f=0

if tba1:
    rank1=rank1+tobi
    tbaf1=1
if tbi1:
    rank1=rank1-tobi
    tbif1=1
if y1:
    rank1=rank1-yakitori
    ycount +=1
    y1f=1
  
if tba2:
    rank2=rank2+tobi
    tbaf2=1
if tbi2:
    rank2=rank2-tobi
    tbif2=1
if y2:
    rank2=rank2-yakitori
    ycount +=1
    y2f=1

if tba3:
    rank3=rank3+tobi
    tbaf3=1
if tbi3:
    rank3=rank3-tobi
    tbif3=1
if y3:
    rank3=rank3-yakitori
    ycount +=1
    y3f=1

if tba4:
    rank4=rank4+tobi
    tbaf4=1
if tbi4:
    rank4=rank4-tobi
    tbif1=1
if y4:
    rank4=rank4-yakitori
    ycount +=1
    y4f=1

if ycount==1:
    if y1f==1 and y2f==0 and y3f==0 and y4f==0:
        #rank1=rank1+yakitori/3
        rank2=rank2+yakitori/3
        rank3=rank3+yakitori/3
        rank4=rank4+yakitori/3
    elif y1f==0 and y2f==1 and y3f==0 and y4f==0:
        rank1=rank1+yakitori/3
        #rank2=rank2+yakitori/3
        rank3=rank3+yakitori/3
        rank4=rank4+yakitori/3
    elif y1f==0 and y2f==0 and y3f==1 and y4f==0:
        rank1=rank1+yakitori/3
        rank2=rank2+yakitori/3
        #rank3=rank3+yakitori/3
        rank4=rank4+yakitori/3
    elif y1f==0 and y2f==0 and y3f==0 and y4f==1:
        rank1=rank1+yakitori/3
        rank2=rank2+yakitori/3
        rank3=rank3+yakitori/3
        #rank4=rank4+yakitori/3     
elif ycount==2:
    if y1f==0 and y2f==1 and y3f==1 and y4f==0:
        rank1=rank1+yakitori
        #rank2=rank2+yakitori
        #rank3=rank3+yakitori
        rank4=rank4+yakitori
    elif y1f==0 and y2f==1 and y3f==0 and y4f==1:
        rank1=rank1+yakitori
        #rank2=rank2+yakitori
        rank3=rank3+yakitori
        #rank4=rank4+yakitori
    elif y1f==0 and y2f==0 and y3f==1 and y4f==1:
        rank1=rank1+yakitori
        rank2=rank2+yakitori
        #rank3=rank3+yakitori
        #rank4=rank4+yakitori
        
df=pd.DataFrame({
    '点数' : pd.Series( [point_a,point_b,point_c,point_d ], index = [name_a,name_b,name_c,name_d] ),
    'ポイント' : pd.Series( [ rank1,rank2,rank3,rank4], index = [name_a,name_b,name_c,name_d] )
})

st.dataframe(df,width=1000,height=1000)
st.write(df)
#エラー確認

ch1=point_a+point_b+point_c+point_d
if ch1==100000:
    st.write('点数の合計が合っています')
else:
    st.write('<span style="color:red">エラー：点数を確かめてください</span>',unsafe_allow_html=True)

if tbaf1+tbaf2+tbaf3+tbaf4==tbif1+tbif2+tbif3+tbif4:
    st.write('飛びと飛ばしが同じです')
else:
    st.write('<span style="background:yellow">警告：飛びと飛ばしが異なります</span>',unsafe_allow_html=True)

if (tbaf1==1 and tbif1==1)or(tbaf2==1 and tbif2==1)or(tbaf3==1 and tbif3==1)or(tbaf4==1 and tbif4==1):
    st.write('<span style="color:red">エラー：飛びと飛ばしが重複しています</span>',unsafe_allow_html=True)


#result=st.button('登録')
#delete=st.button('削除')

#if result:
#    st.write('登録しました')
#if delete:
#    st.write('削除しました')