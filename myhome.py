import streamlit as st
from PIL import Image

page = st.sidebar.radio('阿短首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区', '我的网站推荐', '我的博物馆推荐'])

def page_1():
    st.write(":red[2025年电影大赏：]")
    pic = ["哪吒2.jpg", "熊出没.png", "唐探1900.jpg", "封神二.jpg"]
    imgs_lst = []
    for i in pic:
        img = Image.open(i)
        img = img.resize((200, 300))
        imgs_lst.append(img)
    col10, col11 = st.columns([1, 1])
    with col10:
        st.write("哪吒之魔童闹海")
        st.image(imgs_lst[0])
    with col11:
        st.write("熊出没之重启未来")
        st.image(imgs_lst[1])
    col12, col13 = st.columns([1, 1])
    with col12:
        st.write("唐探1900")
        st.image(imgs_lst[2])
    with col13:
        st.write("封神二")
        st.image(imgs_lst[3])
    
def page_2():
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    st.write(":five::two::zero:")
    uploaded_file = st.file_uploader("上传图片", type = ["png", "jpeg", "jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img,1, 0, 2))
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)

def page_3():
    st.write("智慧词典")
    with open("words_space.txt", "r", encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split("#")
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]), i[2]]
    with open("check_out_times.txt", "r", encoding='utf-8') as f:
        time_list = f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i] = time_list[i].split("#")
    time_dict = {}
    for i in time_list:
        time_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词")
    st.write("可以试着输入“雪花”，“今天是我的生日”, “python”（有小彩蛋哦:sparkles:）")
    if word:
        if word in word_dict:
            st.write(word_dict[word])
            n = word_dict[word][0]
            if n in time_dict:
                time_dict[n] += 1
            else:
                time_dict[n] = 1
            with open("check_out_times.txt", "w", encoding='utf-8') as f:
                message = ''
                for k, v in time_dict.items():
                    message += str(k) + "#" + str(v) + "\n"
                message = message[:-1]
                f.write(message)
            st.write('查询次数:', time_dict[n])
        elif word == "python":
            st.write("小彩蛋")
            st.code('''
                print(hello world)
                ''' )
        elif word == "雪花":
            st.snow()
        elif word == "今天是我的生日":
            st.balloons()
        else:
            st.write("您所查找的单词不存在或单词拼写有问题")
    
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌚'):
                # st.write(i[1],':',i[2])
                st.write(':red[{}:{}]'.format(i[1],i[2]))
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                # st.write(i[1],':',i[2])
                st.text(i[1]+':'+i[2])
    # 进行留言
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message) 



def page_5():
    st.write(":red[网站推荐]")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("百度.jpg")
        st.link_button('百度一下', 'https://www.baidu.com/')
    with col2:
        st.image("新闻网.jpg")
        st.link_button('中国新闻网', 'http://www.chinanews.com/')
    col3, col4 = st.columns([1, 1])
    with col3:
        st.image("腾讯.jpg")
        st.link_button('腾讯视频', 'https://v.qq.com/')
        col5, col6 = st.columns([1, 1])
        with col5:
            st.image("微博.jpg")
            st.link_button('微博', 'https://weibo.com/')
        with col6:
            st.image("优酷.jpg")
            st.link_button('优酷', 'https://www.youku.com/')
    with col4:
        st.image("billbill.jpg")
        st.link_button('billbill', 'https://www.bilibili.com/')
        col7, col8 = st.columns([1, 1])
        with col7:
            st.image("编程猫社区.jpg")
            st.link_button('编程猫社区', 'https://shequ.codemao.cn/')
        with col8:
            st.image("中国教育在线.jpg")
            st.link_button('中国教育在线', 'https://www.eol.cn/')
    
def page_6():
    st.write("在河南，最出名的博物馆不过是河南博物院，以下是我这个寒假去那里游玩拍下来的河南博物院十大镇馆之宝，供大家欣赏，希望有更多的人了解河南，也希望有更多的人来河南游玩:exclamation::exclamation::exclamation:")
    st.write(":red[河南博物院十大镇馆之宝：]")
    picu = ["白玉萝卜.jpg", "贾湖骨笛.jpg", "杜岭方鼎.jpg", "妇好鴞尊.jpg", "莲鹤方壶.jpg", "汝窑天蓝釉刻花.jpg", "四神云气图.jpg", "武则天金简.jpg", "玉柄铁剑.jpg", "云纹铜禁.jpg"]
    imgs_lsts = []
    for i in picu:
        img = Image.open(i)
        img = img.resize((300, 400))
        imgs_lsts.append(img)
    col14, col15 = st.columns([1, 1])
    with col14:
        st.write("白玉萝卜")
        st.image(imgs_lsts[0])
    with col15:
        st.write("贾湖骨笛")
        st.image(imgs_lsts[1])
    col16, col17 = st.columns([1, 1])
    with col16:
        st.write("杜岭方鼎")
        st.image(imgs_lsts[2])
    with col17:
        st.write("妇好鴞尊")
        st.image(imgs_lsts[3])
    col18, col19 = st.columns([1, 1])
    with col18:
        st.write("莲鹤方壶")
        st.image(imgs_lsts[4])
    with col19:
        st.write("汝窑天蓝釉刻花鹅颈瓶")
        st.image(imgs_lsts[5])
    col20, col21 = st.columns([1, 1])
    with col20:
        st.write("四神云气图壁画")
        st.image(imgs_lsts[6])
    with col21:
        st.write("武则天金简")
        st.image(imgs_lsts[7])
    col22, col23 = st.columns([1, 1])
    with col22:
        st.write("玉柄铁剑")
        st.image(imgs_lsts[8])
    with col23:
        st.write("云纹铜禁")
        st.image(imgs_lsts[9])
    
    

def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的网站推荐':
    page_5()
elif page =='我的博物馆推荐':
    page_6()

#python -m streamlit run C:\Users\Administrator\Desktop\my_home\myhome.py