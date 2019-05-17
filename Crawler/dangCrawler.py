#!/usr/bin/env python
# author by teamboy
# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import pandas
import xlwt
class url_Open():
    def __init__(self):
        self.problem_datas = []
        self.option_A_datas = []
        self.option_B_datas = []
        self.option_C_datas = []
        self.option_D_datas = []
        self.answer_datas = []
    def getHtml(self,url):
        page = urllib.request.urlopen(url)
        htmlcode = page.read().decode('utf-8')
        return htmlcode
    def getSoup(self,html):
        get_Soup = BeautifulSoup(html,'html.parser')
        # /html/body/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/span
        # /html/body/div[4]/div/div/div[2]/div[2]
        # /html/body/div[4]/div/div/div[2]/div[2]/div[759]/div[2]/div[1]/div[2]/span/b
        # body > div.yiban-content > div > div > div.ec_sider > div.ec_content.ep_content > div:nth-child(759) > div.eh_t_solution > div.eh_ts_a > div.eh_uanswer > span > b
        get_problem_list = get_Soup.find(class_='ec_content ep_content')
        return get_problem_list
    def write_word(self,problem_list):
        # file_name = 'test1.csv'
        all_probream = problem_list.find_all(class_='ep_topic')
        for con in all_probream:
            # body > div.yiban-content > div > div > div.ec_sider > div.ec_content.ep_content > div:nth-child(758) > div.eh_t_solution > div.eh_ts_a > div.eh_uanswer > span > b
            # body > div.yiban-content > div > div > div.ec_sider > div.ec_content.ep_content > div:nth-child(759) > div.ep_t_topic > div.ep_tt_topic.eh_tt_topic > span
            self.problem_datas.append(con.find(attrs={'class':'ep_tt_topic eh_tt_topic'}).get_text())
            self.option_A_datas.append(con.find(attrs={'class':'ep_t_ul'}).find_all('li')[0].get_text())
            self.option_B_datas.append(con.find(attrs={'class':'ep_t_ul'}).find_all('li')[1].get_text())
            self.option_C_datas.append(con.find(attrs={'class':'ep_t_ul'}).find_all('li')[2].get_text())
            self.option_D_datas.append(con.find(attrs={'class':'ep_t_ul'}).find_all('li')[3].get_text())
            self.answer_datas.append(con.find(attrs={'eh_uanswer'}).find('b').get_text())
        Data = {'题目':self.problem_datas,'A':self.option_A_datas,'B':self.option_B_datas ,'C':self.option_C_datas ,'D':self.option_D_datas ,'正确答案':self.answer_datas}
        problem_datas = pandas.Series(self.problem_datas,name='problem_datas')
        option_A_datas = pandas.Series(self.option_A_datas, name='option_A_datas')
        option_B_datas = pandas.Series(self.option_B_datas, name='option_B_datas')
        option_C_datas = pandas.Series(self.option_C_datas, name='option_C_datas')
        option_D_datas = pandas.Series(self.option_D_datas, name='option_D_datas')
        answer_datas = pandas.Series(self.answer_datas, name='answer_datas')
        # Data = {'problem_datas': problem_datas, 'option_A_datas': option_A_datas, 'option_B_datas': option_B_datas, 'option_C_datas': option_C_datas,'option_D_datas': option_D_datas, 'answer_datas': answer_datas}
        # f = open("C:\\Users\\admin\\Desktop\\problem.csv",'r+',encoding="utf-8")
        # save = pandas.DataFrame(list(Data))
        dataset = list(zip(Data['题目'], Data['A'], Data['B'], Data['C'], Data['D'], Data['正确答案']))
        df = pandas.DataFrame(data=dataset, columns=['题目','A', 'B', 'C', 'D', '正确答案'])
        print(dataset)
        df.to_csv("C:\\Users\\admin\\Desktop\\problem.csv", index=False)

        return self.problem_datas

        #







if __name__=='__main__':
    url = 'file:///C:/Users/admin/Desktop/%E6%88%91%E7%9A%84%E9%94%99%E9%A2%98%E4%B8%80A.html'
    # getHTMLText(url)
    urlopen = url_Open()
    get_html = urlopen.getHtml(url)
    get_Soup = urlopen.getSoup(get_html)
    write_word = urlopen.write_word(get_Soup)
    print(write_word)
