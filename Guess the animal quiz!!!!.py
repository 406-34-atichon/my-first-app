import time
import streamlit as st
score = 0
st.title("⏱️ เกมทายศัพท์จับเวลา(หมวดแอนิมอล)")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:
    st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
    st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:
    st.session_state.ans10_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans7_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.ans8_val = ""  # เคลียร์ค่าช่องข้อ 8
    st.session_state.ans9_val = ""  # เคลียร์ค่าช่องข้อ 9
    st.session_state.ans10_val = ""  # เคลียร์ค่าช่องข้อ 10
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()
    u_ans8 = ans8.strip().lower()
    u_ans9 = ans9.strip().lower()
    u_ans10 = ans10.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "หมา" or u_ans1 == "สุนัข" or u_ans1 == "Dog" or u_ans1 == "dog":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "แมว" or u_ans2 == "cat" or u_ans2 == "Cat":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
                 
          # ตรวจข้อ 3
    if u_ans3 == "ช้าง" or u_ans3 == "elephant" or u_ans3 == "Elephant":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 in ["ลิง", "monkey", "Monkey"]:
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # ตรวจข้อ 5
    if u_ans5 in ["Duck", "เป็ด", "duck"]:
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    # ตรวจข้อ 6
    if u_ans6 in ["bird", "Bird", "นก"]:
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")
                 
    # ตรวจข้อ 7
    if u_ans7 in ["Cow", "cow", "วัว", "วัวนม"]:
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")

    # ตรวจข้อ 8
    if u_ans8 in ["กระต่าย", "Rabbit", "rabbit"]:
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8 : ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")

    # ตรวจข้อ 9
    if u_ans9 in ["นกอินทรีย์", "อินทรีย์", "eagle", "Eagle"]:
        st.success("✅ ข้อ 9: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")

    # ตรวจข้อ 10
    if u_ans10 in ["Salmon", "salmon", "ปลาแซลม่อน", "แซลม่อน"]:
        st.success("✅ ข้อ 10: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")
                 

st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
if score >= 8:
    st.success("🎉 รอบรู้เรื่องสัตว์ขั้นเทพ!")
elif score >= 5:
    st.info("👍 ผ่านเกณฑ์รอบรู้สัตว์ทั่วไป")
else:
    st.error("💀 พยายามอีกนิด ไปศึกษาเรื่องสัตว์เพิ่มเติมนะ!")

# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(45 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1:  สัตว์อะไรเอ่ย ร้อง โฮ่งๆ ชอบเห่า เฝ้าบ้าน เป็นเพื่อนซี้มนุษย์?",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: สัตว์อะไรเอ่ย ร้อง เหมียวๆ ชอบจับหนู แถมชอบนอนทั้งวัน?",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3:สัตว์อะไรเอ่ย ตัวใหญ่ที่สุดบนบก มีงวงยาวๆ และมีงาขาวๆ?",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: สัตว์อะไรเอ่ย ชอบกินกล้วย ซุกซน โหนกิ่งไม้ไปมา ร้อง เจี๊ยกๆ? ",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5:สัตว์อะไรเอ่ย มี 2 ขา เดินเตาะแตะ ร้อง ก๊าบๆ ชอบว่ายน้ำ?",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: สัตว์อะไรเอ่ย มีปีก บินได้บนท้องฟ้า ร้อง จิ๊บๆ?",
    value=st.session_state.ans6_val,
)
ans7 = st.text_input(
    "ข้อ 7:สัตว์อะไรเอ่ย ตัวใหญ่ ร้อง มอๆ ให้นมสดอร่อยๆ ให้เราดื่ม?",
    value=st.session_state.ans7_val,
)
ans8 = st.text_input(
    "ข้อ 8:สัตว์อะไรเอ่ย หูยาว ขนปุกปุย กระโดดดุ๊กดิ๊ก ชอบกินแครอท?",
    value=st.session_state.ans8_val,
)
ans9 = st.text_input(
    "ข้อ 9: สัตว์อะไรเอ่ย เป็นสัตว์ตัวแทนแห่งอเมริกา เป็นนก ชื่ออยู่ในทะเล?",
    value=st.session_state.ans9_val,
)
ans10 = st.text_input(
    "ข้อ 10:สัตว์อะไรเอ่ยเนื้อสีส้ม นอเวย์มีเยอะ ฮาแลนด์ ว่ายทวนน้ำ โดนดองเกาหลีอร่อยๆ?",
    value=st.session_state.ans10_val,
)


# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
st.session_state.ans8_val = ans8
st.session_state.ans9_val = ans9
st.session_state.ans10_val = ans10


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)

st.divider()
st.write("นายอธิชนม์ จันทร์ต๊ะวงค์ เลขที่ 34 ม.4/6")


