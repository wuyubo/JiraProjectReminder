# This is a sample Python script.
import sys
import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QSystemTrayIcon
import main_window
import login
import webbrowser
from jira import JIRA
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
import datetime
import images

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
version = "ProReminder v1.0"
jira = 0
issueslist = 0
name = 0
passwd = 0
task = 0
scheduler = 0
##########################
#openUrl
#########################
def openUrl(url):
    try:
        webbrowser.get('chrome').open_new_tab(url)
    except Exception as e:
        webbrowser.open_new_tab(url)

##########################
#print_hi
#########################
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

##########################
#openJira
#########################
def openJira(name, passwd):
    try:
        jira = JIRA(server='https://jira.cvte.com', basic_auth=(name, passwd))
        return jira
    except Exception as e:
        print(e)
        return 0

##########################
#searchIssues
#########################
def searchIssues(jira, jql, max_results=1000):
    try:
        issues = jira.search_issues(jql, maxResults=max_results)
        return issues
    except Exception as e:
        print(e)
        return 0

##########################
#showList
#########################

##########################
#analyze project
#########################

def getAllIssuesList(project):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\") ORDER BY assignee ASC"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getTodayFinishIssuesList(project):
    global jira
    global issueslist
    today = datetime.date.today()
    sql1 = "project ="
    sql2 = " AND issuetype in (任务, 新功能, 缺陷, 子任务, 子缺陷) AND  转测试日期 >= "+str(today)+" AND  转测试日期 <= "+str(today)+" ORDER BY assignee ASC, priority DESC, updated DESC"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getTodayCreateIssuesList(project):
    global jira
    global issueslist
    print("tommorow")
    today = datetime.date.today()
    delta = datetime.timedelta(days=1)
    n_days = today + delta
    tommorow = n_days.strftime('%Y-%m-%d')
    print(today)
    print(tommorow)
    sql1 = "project ="
    sql2 = " AND issuetype in ( 新功能, 缺陷, 子缺陷) AND created >= "+str(today)+" AND created <= "+str(tommorow)+" ORDER BY assignee ASC, priority DESC, updated DESC"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getTodayCreateIssuesList(project):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype in (新功能, 缺陷,  子缺陷) AND created >= -1d"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getCrashIssuesList(project):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\") AND text ~ \"死机\" ORDER BY assignee ASC"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getBlackPanelIssuesList(project):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\") AND text ~ \"黑屏\" ORDER BY assignee ASC"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getOtherIssuesList(project, text):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\") AND text ~ \""+text+"\" ORDER BY assignee ASC"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def analyzeProject():
    project = ui.lineEdit_project.text()
    issueslist = getAllIssuesList(project)
    todaylist = getTodayFinishIssuesList(project)
    createlist = getTodayCreateIssuesList(project)
    count = 0
    names = []
    for iss in issueslist:
        count = count+1

    result = project+"项目情况：\n"
    result = result+"剩余问题："+str(count)+"个\n"
    count = 0
    for iss in todaylist:
        count = count+1
        name = iss.fields.assignee
        names.append(name)
    result = result + "今天处理问题：" + str(count) + "个\n"
    count = 0
    for iss in createlist:
        count = count+1
    result = result + "今天新增问题：" + str(count) + "个\n"
    newNames = []
    num = 0
    result = result + "今天龙虎榜：\n"
    for i in range(len(names)):
        num = num + 1
        if names[i] not in newNames:
            if i != 0:
                result = result + str(num) + "个\n"
            result = result +"@" + str(names[i])
            newNames.append(names[i])
            num = 0
    result = result + str(num) + "个\n"
    return result

def getNextPointDay():
    version = ui.lineEdit_project_next.text()
    day = ui.dateEdit_projectPoint.text()
    today = datetime.date.today()
    d1 = datetime.datetime.strptime(str(day), '%Y-%m-%d')
    d2 = datetime.datetime.strptime(str(today), '%Y-%m-%d')

    delta = d1 - d2
    date = "距离"+version+"还有 "+str(delta.days)+" 天"
    return date

def getFeatureList(project, version):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype = 新功能 AND status in (新建, 重新打开, \"In Progress\") AND (fixVersion is EMPTY OR fixVersion in ("+version+"))"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getProcessList(project, version):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND filter=45894 AND fixVersion in ("+version+")"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getTestingList(project):
    global jira
    global issueslist
    sql1 = "project ="
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (测试中, 待挂起,无效)"
    sql = sql1 + project + sql2
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getFilterList(sql):
    global jira
    issueslist = searchIssues(jira, sql, 1000)
    return issueslist

def getAllAssignee(issueslist):
    names = []
    newNames = []
    result = "  "

    for iss in issueslist:
        name = iss.fields.assignee
        names.append(name)
    num = 0
    if len(names) == 0:
        return result
    for i in range(len(names)):
        num = num + 1
        if names[i] not in newNames:
            if i != 0:
                result = result + str(num)+" "
            result = result + "@" + str(names[i]) + " "
            newNames.append(names[i])
            num = 0
    result = result + str(num+1) + "\n"
    return result

def getIssuesTitle(issueslist):
    result = ""
    num = 1
    for iss in issueslist:
        name = iss.fields.assignee
        title = iss.fields.summary
        status = iss.fields.status
        result = result + "(" + str(num)+"). " + str(title)+ " @" + str(name) +"("+ str(status)+")" +"\n"
        num = num+1
    return result

def getProjectDI(key):
    global jira
    global issueslist
    print("GET DI:")
    sql1 = "project = " + key
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\", 测试中, 待挂起) AND 缺陷级别 = Critical"
    sql = sql1 + sql2
    issueslist = searchIssues(jira, sql, 1000)
    Critical = len(issueslist)
    print(Critical)
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\", 测试中, 待挂起) AND 缺陷级别 = Major"
    sql = sql1 + sql2
    issueslist = searchIssues(jira, sql, 1000)
    Major = len(issueslist)
    print(Major)
    sql2 = " AND issuetype in (缺陷, 子缺陷) AND status in (新建, 重新打开, \"In Progress\", 测试中, 待挂起) AND 缺陷级别 = Normal"
    sql = sql1 + sql2
    issueslist = searchIssues(jira, sql, 1000)
    Normal = len(issueslist)
    print(Normal)
    DI = Critical*10 + Major*3 + Normal
    return DI

def projectStatus():
    projectID = ui.lineEdit_project.text()
    #name = ui.lineEdit_project_name.text()
    version = ui.lineEdit_project_next.text()
    nextPoint = getNextPointDay()
    project = jira.project(projectID)
    name = project.name
    result = name + " 项目情况如下：\n"
    DI = getProjectDI(projectID)
    result = result+"***"+nextPoint+", DI值："+str(DI)+"***\n"
    flag = 0
    isShowName = ui.checkBox_show_name.isChecked()
    isShowIssues = ui.checkBox_show_issuse.isChecked()
    num = 0
    if ui.checkBox_issues.isChecked() == 1:
        issueslist = getAllIssuesList(projectID)
        num = num + 1
        result = result+ "***"  + str(num) + "、系统剩余问题 " + str(len(issueslist)) + " 个***\n"
        if isShowName == 1:
            assigneeges = getAllAssignee(issueslist)
            result = result + assigneeges
            flag = 1
        result = result + "\n"

    if ui.checkBox_dead.isChecked() == 1:
        crashissueslist = getCrashIssuesList(projectID)
        num = num + 1
        result = result + "***" + str(num) + "、其中死机问题有 " + str(len(crashissueslist)) + " 个***\n"
        if isShowIssues == 1:
            issues = getIssuesTitle(crashissueslist)
            result = result + issues
            flag = 1
        result = result + "\n"

    if ui.checkBox_black.isChecked() == 1:
        blackissueslist = getBlackPanelIssuesList(projectID)
        num = num + 1
        result = result+ "***"  + str(num) + "、其中黑屏问题有 " + str(len(blackissueslist)) + " 个***\n"
        if isShowIssues == 1:
            issues = getIssuesTitle(blackissueslist)
            result = result + issues + "\n"
            flag = 1
        result = result + "\n"

    if ui.checkBox_other.isChecked() == 1:
        text = ui.lineEdit_note_2.text()
        otherissueslist = getOtherIssuesList(projectID, text)
        num = num + 1
        result = result + "***" + str(num) + "、其中"+text+"问题有 " + str(len(otherissueslist)) + " 个***\n"
        if isShowIssues == 1:
            issues = getIssuesTitle(otherissueslist)
            result = result + issues + "\n"
            flag = 1
        result = result + "\n"

    if ui.checkBox_feature.isChecked() == 1:
        featurelist = getFeatureList(projectID, version)
        num = num + 1
        result = result + "***" + str(num) + "、功能完成度剩余 " + str(len(featurelist)) + " 个***\n"
        if isShowName == 1:
            assigneeges = getAllAssignee(featurelist)
            result = result + assigneeges+"\n"
            flag = 1
        result = result + "\n"

    if ui.checkBox_process.isChecked() == 1:
        processlist = getProcessList(projectID, version)
        num = num + 1
        result = result + "***" + str(num) + "、过程待办剩余 " + str(len(processlist)) + " 个***\n"
        if isShowName == 1:
            assigneeges = getAllAssignee(processlist)
            result = result + assigneeges
            flag = 1
        result = result + "\n"

    if ui.checkBox_testing.isChecked() == 1:
        testlist = getTestingList(projectID)
        num = num + 1
        result = result + "***"  + str(num) + "、待关闭问题(测试中, 待挂起,无效) " + str(len(testlist)) + " 个***\n\n"


    if flag == 1:
        result = result + "请检查待办,按节点达成\n\n"

    if ui.checkBox_today.isChecked() == 1:
        todaylist = getTodayFinishIssuesList(projectID)
        num = num + 1
        result = result + "***"  + str(num) + "、今天处理问题或任务 " + str(len(todaylist)) + " 个***\n"
        assigneeges = getAllAssignee(todaylist)
        result = result + assigneeges+"\n"

    if ui.checkBox_create.isChecked() == 1:
        createlist = getTodayCreateIssuesList(projectID)
        num = num + 1
        result = result + "***"  + str(num) + "、今天新增问题 " + str(len(createlist)) + " 个***\n\n"

    if ui.checkBox_user_filter.isChecked() == 1:
        sql = ui.lineEdit_filter.text()
        name = ui.lineEdit_filter_name.text()
        filterlist = getFilterList(sql)
        num = num + 1
        result = result + "***"  + str(num) + "、" + name + "有 " + str(len(filterlist)) +" 个***\n"
        if ui.checkBox_user_filter_iss.isChecked() == 1:
            issues = getIssuesTitle(filterlist)
            result = result + issues + "\n"

    note = ui.textEdit_note.toPlainText()
    if note != "":
        num = num + 1
        result = result + "***" + str(num) + "、备注：***\n" + note + "\n\n"
    return result



##########################
#senMarkdownData
#########################

def sendTextData(url,contents,name):
    headers = {"Content-Type": "text/plain"}
    data ={
        "msgtype":"text",
        "text":{
            "content":contents,
            "mentioned_list":name,
            }
    }
    r = requests.post(url,headers=headers, json=data)

def senMarkdownData(url, contents):
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": contents,
        }
    }
    requests.post(url, headers=headers, json=data)
def sendProjectDataTorobot():
    global jira
    global name
    global passwd
    jira = openJira(name, passwd)
    url = ui.lineEdit_robot.text()
    data = projectStatus()
    senMarkdownData(url, data)
    if ui.checkBox_all.isChecked() == 1:
        sendTextData(url,"","@all")

def timertask():
    print("task test")
    sendProjectDataTorobot()

def setTimer():
    print("set scheduler")
    global scheduler
    scheduler = BlockingScheduler()
    timer = ui.timeEdit.text()
    timers = timer.split(":",1)

    dayofweek = ""
    if ui.checkBox_week_0.isChecked() == 1:
        dayofweek = "0"
    if ui.checkBox_week_1.isChecked() == 1:
        if dayofweek != "":
            dayofweek = dayofweek + ","
        dayofweek =dayofweek + "1"
    if ui.checkBox_week_2.isChecked() == 1:
        if dayofweek != "":
            dayofweek = dayofweek + ","
        dayofweek = dayofweek + "2"
    if ui.checkBox_week_3.isChecked() == 1:
        if dayofweek != "":
            dayofweek = dayofweek + ","
        dayofweek = dayofweek + "3"
    if ui.checkBox_week_4.isChecked() == 1:
        if dayofweek != "":
            dayofweek = dayofweek + ","
        dayofweek = dayofweek + "4"
    if ui.checkBox_week_5.isChecked() == 1:
        if dayofweek != "":
            dayofweek = dayofweek + ","
        dayofweek = dayofweek + "5"
    if ui.checkBox_week_6.isChecked() == 1:
        if dayofweek != "":
            dayofweek = dayofweek + ","
        dayofweek = dayofweek + "6"
    print(dayofweek)
    print(timers)
    scheduler.add_job(timertask, 'cron', day_of_week=dayofweek, hour=timers[0], minute=timers[1])
    scheduler.start()

def createTask():
    global task
    task = threading.Thread(target=setTimer, args=())
    task.start()

def destroyTask():
    global task
    global scheduler
    if scheduler != 0:
        scheduler.shutdown(True)
    if task != 0:
        task.join()

################################
# Press the green button in the gutter to run the script.

def click_dlg_login():
    global jira
    global name
    global passwd
    name = loginUi.lineEdit_login_user.text()
    passwd = loginUi.lineEdit_login_passwd.text()
    jira = openJira(name, passwd)

    if jira == 0:
        print("登录失败")
        return
    print("登录成功")
    MainWindow.show()
    loginDlg.hide()


def click_send_robot():
    url = ui.lineEdit_robot.text()
    content = ui.textEdit_analyze.toPlainText()
    senMarkdownData(url, content)
    if ui.checkBox_all.isChecked() == 1:
        sendTextData(url,"","@all")

task_flag = False
def click_set_Timer():
    global task_flag
    if task_flag == True:
        task_flag = False
        destroyTask()
        ui.ptn_timer_start.setText("定时发送")
        return
    createTask()
    timer = ui.timeEdit.text()
    tips = "已设置定时" + timer + "发送项目数据"
    ui.label_timer.setText(tips)
    task_flag = True
    ui.ptn_timer_start.setText("取消")

def click_preview():
    data = projectStatus()
    ui.textEdit_analyze.setText(data)

if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    loginDlg = QDialog()
    loginUi = login.Ui_Dialog()
    loginUi.setupUi(loginDlg)
    loginDlg.show()

    #set title and icon
    loginDlg.setWindowTitle(version)
    MainWindow.setWindowTitle(version)
    loginDlg.setWindowIcon(QIcon(':/icon.png'))
    MainWindow.setWindowIcon(QIcon(':/icon.png'))

    loginUi.ptn_login.clicked.connect(click_dlg_login)
    ui.ptn_send_robot.clicked.connect(click_send_robot)
    ui.ptn_timer_start.clicked.connect(click_set_Timer)
    ui.ptn_preview.clicked.connect(click_preview)
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
