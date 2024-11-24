import streamlit as s


dict = {'con cho' : 'co Xu hướng thích khám phá những cái mới hay thích sự ổn định' ,
        'con meo' : 'nguoi huong ngoai',
       'con ga' : 'nguoi huong noi',
       'con lon' : 'nguoi co tham vong',
       'con chuot' : 'nguoi thong minh'}
s.title("chon con vat ban yeu thich")
col1,col2,col3,col4,col5 = s.columns(5)
with col1:
  a1 = s.button("con cho")
with col2:
  a2 =s.button("con meo")
with col3:
  a3 = s.button("con ga")
with col4:
  a4 = s.button("con heo")
with col5:
  a5 = s.button("con chuot")
convat = 'con cho'
if a1:
  s.sidebar.title("con vat ban thich la: con cho")
  convat = "con cho"
if a2:
  s.sidebar.title("con vat ban thich la: con meo")
  convat = "con meo"
if a3:
  s.sidebar.title("con vat ban thich la: con ga")
  convat = "con ga"
if a4:
  s.sidebar.title("con vat ban thich la: con lon")
  convat = "con lon"
if a5:
  s.sidebar.title("con vat ban thich la: con chuot")
  convat = "con chuot"

s.write(dict[convat])


  