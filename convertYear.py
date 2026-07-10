import streamlit as mg

mg.title("แอปพลิเคชั่นแปลงปี พ.ศ.เป็น ค.ศ.🤔")

bh_year=mg.number_input("กรอกปีพ.ศ.ที่ต้องการเปลี่ยนแปลง",value=2569)
ce_year=bh_year-543
mg.header(f"ปี ค.ศ. คือ : {ce_year}🤩")
