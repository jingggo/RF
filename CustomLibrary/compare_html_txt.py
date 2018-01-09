from bs4 import BeautifulSoup
import difflib
import os, re, xlwt

def should_be_equal_as_html(ptext, stext):
    '''Return True if equal, or else return False'''
    if ptext == stext:
        return True
    else:
        return False

def html_contents(dir, file_name):
    '''return as list'''
    file_name_escape = r'\\' + file_name
    with open(dir+file_name_escape, 'r+') as pfile:
        contents = pfile.readlines()
        return contents
    
def wrap(string, tag):
    '''If with th/td/option tag, del wrap th would display failed, so need to wrap after the tag'''
    tag_start = '<' + tag + ' class="diff">'
    tag_end = '</' + tag + '>'
    se = re.search('<th.*?>.*</th>|<td.*?>.*</td>|<option.*?>', string)
    if se is not None:
        soup = BeautifulSoup(string, 'html.parser')
        tag_s = soup.new_tag(tag)
        tag_s.attrs['class'] = 'diff'
        if soup.th is not None:
            if(soup.th.has_attr('class')):
                soup.th['class'].append('diff')
            else:
                soup.th['class'] = 'diff'
        if soup.td is not None:
            if(soup.td.has_attr('class')):
                soup.td['class'].append('diff')
            else:
                soup.td['class'] = 'diff'
        if soup.option is not None:
            if (soup.option.has_attr('class')):
                soup.option['class'].append('diff')
            else:
                soup.option['class'] = 'diff'
        return str(soup)
    else:
        string = tag_start + string + tag_end
    return string

def hndiff(p_contents, s_contents):
    '''parameter should be list, for string, need to split to lines. Return as string with html text'''
    ndiffs = list(difflib.ndiff(p_contents, s_contents))
    prod_temp = []
    for pdiff in ndiffs:
        if pdiff[0:1] == '-':
            pdiff = wrap(pdiff[2:], 'del')
            prod_temp.append(pdiff)
        elif pdiff[0:1] == ' ':
            prod_temp.append(pdiff[2:])
    stag_temp = []
    for sdiff in ndiffs:
        if sdiff[0:1] == '+':
            sdiff = wrap(sdiff[2:], 'ins')
            stag_temp.append(sdiff)
        elif sdiff[0:1] == ' ':
            stag_temp.append(sdiff[2:])

    p_content = ''.join(prod_temp)
    s_content = ''.join(stag_temp)

    pre_html = '''
    <html><head>
    <style>.diff { color: #FF0000; background-color:#ADD8E6;}
    </style></head><body><table width="98%" cellspacing="0" cellpadding="1" border="1"><tbody><tr><th>Production</th><th>Stage</th></tr>
    '''
    end_html = '''
    </tbody></table></body></html>
    '''
    html = pre_html + '<tr><td>' + p_content + '</td><td>' + s_content + '</td></tr>' + end_html
    return html

pd = r'Z:\QA\QA Material\TD\TD comparison\test07\prod'
sd = r'Z:\QA\QA Material\TD\TD comparison\test07\stag'
pf = r'\AP Main_asliter.htm'
sf = r'\AP Main_asliter.htm'

def compare_html_dir():
    parent_dir = r'Z:\QA\QA Material\TD\TD comparison\test07'
    for file_name in os.listdir(parent_dir + r'\prod'):
        print file_name
        file_name_escape = r'\\' + file_name
        p_contents = html_contents(pd, file_name)
        s_contents = html_contents(sd, file_name)
        html = hndiff(p_contents, s_contents)
        with open(parent_dir+'\diff_html_result3'+file_name_escape, 'w+') as result:
            result.write(html)
        print "\tDone"

def writeListToExcel(lst, path):
    '''Support one dimension and two dimension list, path is the excel you want to save as'''
    if not(isinstance(lst[0],list)):
        print('One Dimension')
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'Sheet1', cell_overwrite_ok=True)
        for colx, value in enumerate(lst):
            sheet1.write(0, colx, value)
        f.save(path)
    else:
        print('Two Dimension')
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'Sheet1', cell_overwrite_ok=True)
        for rowx in range(len(lst)):
            for colx, value in enumerate(lst[rowx]):
                sheet1.write(rowx, colx, value)
        f.save(path)
# lst=[[1,2,3],[1,2,3]]
# path=r'E:\\text.xls'
# writeListToExcel(lst, path)
