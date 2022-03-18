#time:2022/2/14  20:26
#author:Hu_Guangliang
#
import time
import tkinter as tk
from tkinter import ttk,messagebox as msg
import tkinter.font as tkfont
import random

##########################——————————主要全局变量——————————###############################
DISTANCE=10
DISPLAY_MAX=8
ROW=0
EN_VISIABLE=0
tran_visi_flag=0
word_count=0
dis_trans_cnt=0
word_list_origin=[]
word_list_random=[]
class WordClass:
    def __init__(self,only,all):
        self.word_only=only
        self.word_all=all
############################-----------主要函数------------#############################
def ReadInytextBox():
    global dis_trans_cnt
    dis_trans_cnt = 0
    outText.delete(1.0,'end')
    file=inText.get('1.0','end')
    #默认第一个字符就是第一个单词的开始
    global word_count
    global word_list_random
    global tran_visi_flag
    # 如果outtext里有内容就读取，没有就显示已经读取的内容
    if len(inText.get('1.0','end'))>=10:
        word_count=0
        start_i = 0
        sum_of_str = file.count('');  # 统计字符个数，‘’为空字符，即任意字符都计数
        print('字符个数总计：', sum_of_str);
        for i in range(0, sum_of_str-2, 1):
            print(i,file[i])
            if file[i]=='\n':
                j=start_i
                print('    ',i,j)
                while file[j]!='/' and file[j]!=' ':
                    print(j,' ',file[j])
                    j=j+1
                end_i=j-1
                word_count+=1
                print('word_count:',word_count)
                if len(word_list_origin)<word_count:
                    word_list_origin.append(WordClass(file[start_i:end_i+1], file[start_i:i]))
                else:
                    word_list_origin[word_count - 1].word_only= file[start_i:end_i+1]
                    word_list_origin[word_count - 1].word_all = file[start_i:i]
                start_i=i+1
    outText.delete('1.0','end')
    word_list_random=word_list_origin[:]
    # for i in range(0,word_count):
    #     outText.insert('end', word_list_origin[i].word_all + word_list_origin[i].word_only + '\n')
    DisplayTabels(word_list_origin, 'all')
    tran_visi_flag=1
    return 0;
def ShuffleWords():
    global dis_trans_cnt
    dis_trans_cnt = 0
    if len(word_list_random)==0:
        ReadInytextBox()
    word_list_temp=word_list_random[0:word_count]
    random.shuffle(word_list_temp)
    word_list_random[0:word_count]=word_list_temp[0:word_count]
    global tran_visi_flag
    tran_visi_flag=0
    outText.delete('1.0', 'end')
    print('random函数')
    print(word_count)
    # for i in range(0, word_count):
    #     outText.insert('end', word_list_random[i].word_only  + '\n')
    DisplayTabels(word_list_random, 'only_word')
    return 0
def SwitchTranslateVisity():
    global tran_visi_flag
    global dis_trans_cnt
    dis_trans_cnt = 0
    if len(word_list_origin)==0:
        ReadInytextBox()
    outText.delete('1.0', 'end')
    print('cover_words函数')
    print(word_count)
    # for i in range(0, word_count):
    #     outText.insert('end', word_list_origin[i].word_only  + '\n')
    if tran_visi_flag==0:
        DisplayTabels(word_list_random, 'all')
    else:
        DisplayTabels(word_list_random, 'only_word')
    tran_visi_flag = 1 - tran_visi_flag
    return 0
def DisplayTabels(dis_list_class, mode):
    global v_list
    global label_word_list
    if mode=='all':
        for i in range(0,DISPLAY_MAX):
            if i<word_count:
                label_word_list[i] = dis_list_class[i].word_all
                v_list[i].set(label_word_list[i])
            else:
                v_list[i].set(' ')
    elif mode=='only_word':
        for i in range(0,DISPLAY_MAX):
            if i<word_count:
                label_word_list[i] = dis_list_class[i].word_only
                v_list[i].set(label_word_list[i])
            else:
                v_list[i].set(' ')
    elif mode=='OneNextOne':
        for i in range(0,DISPLAY_MAX):
            if i<word_count:
                if i<dis_trans_cnt:
                    label_word_list[i] = dis_list_class[i].word_all
                    v_list[i].set(label_word_list[i])
                else:
                    label_word_list[i] = dis_list_class[i].word_only
                    v_list[i].set(label_word_list[i])
            else:
                v_list[i].set(' ')
    #输入、输出TEXT不可见
    if EN_VISIABLE==0:
        outText.delete('1.0', 'end')
        inText.delete('1.0','end')
    outText.insert('end','当前读取单词个数    ','%s',word_count)
    return 0
##########################——————————初始化——————————##################################
root=tk.Tk()
root.title('背单词V20220303')
root.resizable(0,0)
Label1=tk.Label
#Label
label_list=[]
v_list=[]
label_word_list=[]
for i in range(0,DISPLAY_MAX):
    label_word_list.append('word: void')
    v_list.append(tk.StringVar())
    v_list[i].set(label_word_list[i])
    ft_label = tkfont.Font(family='Times New Roman', size=30, weight=tkfont.NORMAL)
    label_list.append(tk.Label(root,textvariable=v_list[i], font=ft_label,fg='green',justify='left',anchor='w',padx=0,width=40,relief='raised',borderwidth=0))
    # label_list[i].
    label_list[i].grid(row=ROW,padx=80,ipady=10)
    ROW += 1
# 输入窗口
global inText
global outText
inText = tk.Text(root, height=10, width=60)
inText.insert(0.0,
"accessory / æk’sesәri/n.配件、同谋 a.附属的\n"
"accommodate / ә’kɔmәdeit/vt.容纳；供应，供给\n"
"accord / ә’kɔ:d/n.条约vt.与…一致(~ with)；给予\n"
"acknowledge / әk’nɔlidʒ/vt.承认；告知收到\n"
"acquaint / ә’kweint/vt.使认识，使了解\n"
"acquisition / ‘ækwi’ziʃәn/n. 收获\n"
"activate / ‘æktiveit/vt. 刺激,使活动\n")
inText.grid(row=ROW + 1, padx=DISTANCE, pady=DISTANCE, sticky='w')

# 输出窗口
outText = tk.Text(root, height=10, width=60)
outText.insert(0.0, "输出单词567890")
outText.grid(row=ROW + 1, padx=DISTANCE, pady=DISTANCE, sticky='e')
# 设置 tag(暂时没用)
# outText.tag_config("tag_1", backgroun="yellow", foreground="red")
# ft=tkfont.Font(family='微软雅黑',size=10)
# outText.configure(ft)
# # outText.tag_add('tag_1',a1)
def NextDisTrans():
    if len(word_list_origin)==0:
        ReadInytextBox()
    global dis_trans_cnt
    if dis_trans_cnt<=word_count :
        dis_trans_cnt+=1
    if dis_trans_cnt>word_count or dis_trans_cnt>DISPLAY_MAX:
        dis_trans_cnt=0
        ShuffleWords()
    print(dis_trans_cnt)
    DisplayTabels(word_list_random, 'OneNextOne')

nextButton= ttk.Button(root, text='显示下一个单词的翻译', width=20, command=NextDisTrans)
nextButton.grid(row=ROW + 1, padx=DISTANCE, pady=DISTANCE, sticky=' ', ipady=10)

readButton = ttk.Button(root, text='读取/顺序显示', width=40, command=ReadInytextBox)
readButton.grid(row=ROW + 3, padx=DISTANCE, pady=DISTANCE, sticky='w', ipady=10)
ranButton = ttk.Button(root, text='随机顺序测试', width=40, command=ShuffleWords)
ranButton.grid(row=ROW + 3, padx=DISTANCE, pady=DISTANCE, sticky=' ', ipady=10)
coverButton = ttk.Button(root, text='打开/关闭翻译', width=40, command=SwitchTranslateVisity)
coverButton.grid(row=ROW + 3, padx=DISTANCE, pady=DISTANCE, sticky='e', ipady=10)

root.mainloop()