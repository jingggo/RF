# -*- coding: utf-8 -*- 

import os,xlrd,xlwt,openpyxl,paramiko,types
import math,string,time,sys,zipfile
from pyPdf import PdfFileReader
from scp import SCPClient
from xlutils.copy import copy

def getValuesPerRow(fpath,tabName,rowIndex):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    rowValues=sheet.row_values(int(rowIndex))
    return rowValues

def getValuesPerCol(fpath,tabName,colIndex):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    colValues=sheet.col_values(int(colIndex))
    return colValues

def getColLength(fpath,tabName):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    colLen=sheet.ncols
    return int(colLen)

def getRowLength(fpath,tabName):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    rowLen=sheet.nrows
    return int(rowLen)

def getCellValue(fpath,tabName,rowx,colx):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    return sheet.cell_value(int(rowx),int(colx))

def getUserCount(fpath,tabName):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    count=sheet.nrows-3
    return count

def getSheetName(fpath):
    book=xlrd.open_workbook(fpath)
    return book.sheet_names()

def writeToExcel(fpath,sheetName,rowIndex,colIndex,content):
    rbook=xlrd.open_workbook(fpath,'w')
    wbook=copy(rbook)
    sheetIndex=rbook.sheet_names().index(sheetName)
    wbook.get_sheet(int(sheetIndex)).write(int(rowIndex),int(colIndex),content)
    wbook.save(fpath)
    print 'write file ok'
	
def sortListByNum(listToSort):
    iter_len = len(listToSort)
    if iter_len < 2:
        return listToSort
    for i in range(iter_len - 1):
        smallest = listToSort[i]
        location = i
        for j in range(i, iter_len):
            if listToSort[j] < smallest:
                smallest = listToSort[j]
                location = j
        if i != location:
            listToSort[i], listToSort[location] = listToSort[location], listToSort[i]
    return listToSort
	
def getDataNrows(fpath,tabName):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    nrows=sheet.nrows
    allData=[]
    for row in range(nrows):
        allData.append(sheet.row_values(row))
    return allData

def getDataNcols(fpath,tabName):
    book=xlrd.open_workbook(fpath)
    sheet=book.sheet_by_name(tabName)
    ncols=sheet.ncols
    allData=[]
    for col in range(ncols):
        allData.append(sheet.col_values(col))
    return allData

def getTemplateDatasDeleteBlankCols(fpath,tabName):
    #data=xlrd.open_workbook(r'C:\Users\jyang\Downloads\SecurityTemplateDownload_20170508-170257.xlsx')
    #sheet=data.sheet_by_name('Security Download')
    data=xlrd.open_workbook(fpath)
    sheet=data.sheet_by_name(tabName)
    nrows=sheet.nrows
    ncols=sheet.ncols
    lst=[]
    for row in range(nrows):
        lst.append(sheet.row_values(row))

    indexOfActionFlag=lst[0].index('Action Flag')
    indexOfUserName=lst[0].index('7thonline Username')-1
    indexOfLName=lst[0].index('User Last Name')-2
    indexOfFName=lst[0].index('User First Name')-3
    indexOfEmail=lst[0].index('User Email Address')-4
    indexOfTele=lst[0].index('User Telephone Number')-5

    lst2=[]
    for i in lst:
        i.pop(indexOfActionFlag)
        i.pop(indexOfUserName)
        i.pop(indexOfLName)
        i.pop(indexOfFName)
        i.pop(indexOfEmail)
        i.pop(indexOfTele)
        lst2.append(i)

    return lst2

def getAccessDataWithoutBlankColsInDw(fpath,tabName):
    '''Delete Action Flag column'''
    data=xlrd.open_workbook(fpath)
    sheet=data.sheet_by_name(tabName)
    nrows=sheet.nrows
    ncols=sheet.ncols
    lst=[]
    for row in range(nrows):
        lst.append(sheet.row_values(row))
    indexOfActionFlag=lst[0].index('Action Flag')
    lst2=[]
    for i in lst:
        i.pop(indexOfActionFlag)
        lst2.append(i)
    return lst2

def replaceFromList(lst,dic):
    '''replace list values through dictionary'''
    rep=[dic[x] if x in dic else x for x in lst]
    return rep

def sortedTwoDimList(lst):
    for i in range(len(lst)):
        lstSorted=sorted(lst,lambda x,y:cmp(x[i],y[i]))
    return lstSorted

def getDataNcolsFromList(lst,indexCol):
    '''The list is a multiple list. Return is a list of column data of certain index.'''
    ncols1=[x[indexCol] for x in lst]
    ncols=['' if x==None else x for x in ncols1]
    return ncols

if __name__ == "__main__":	
    getValuesPerRow()
    getValuesPerCol()
    getColLength()
    getRowLength()
    getCellValue()
    getSheetName()
    writeToExcel()
    sortListByNum()
    getDataNrows()
    getDataNcols()
    getTemplateDatasDeleteBlankCols()
    getAccessDataWithoutBlankColsInDw()
    replaceFromList()
    sortedTwoDimList()
    getDataNcolsFromList()

