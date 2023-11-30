#!/usr/bin/env python3

from numba import jit, njit
from timeit import timeit
from ctypes import *
from time import strftime,localtime

import numpy as np
import numpy.ctypeslib as npct


from calSquareRootAndSquare_CY import calSquareRootAndSquare_CY
from calSquareRootAndSquare_AOT import calSquareRootAndSquare_AOT
from calSquareRootAndSquare_PyC import calSquareRootAndSquare_PyC
from calSquareRootAndSquare_PyCG import calSquareRootAndSquare_PyC as calSquareRootAndSquare_PyCG

# from calMaCY   import calMaCY
# from calMaAOT  import calMaAOT
# from calMaPyC  import calMaPyC
# from calMaPyCG import calMaPyC as calMaPyCG


import math 
loop = 5
subloop = 5
# winsize = 100
length = 1000000
#length = 10000
# data = np.random.randint(1,2000000000,size=(length), dtype=np.int32)

dictTest ={
        'calSquareRootAndSquare'     : 'Standard Python',
        'calSquareRootAndSquare_OP'  : 'Python Numpy ',
        # 'calMaOpt'  : 'Numpy Optimized Ma',
        'calSquareRootAndSquare_JIT'  : 'Numba JIT',
        'calSquareRootAndSquare_AOT'  : 'Numba AOT',
        'calSquareRootAndSquare_CY'   : 'Cython Module',
        'calSquareRootAndSquare_PyC'  : 'C Module VC',
        'calSquareRootAndSquare_PyCG' : 'C Module GCC',
        'calSquareRootAndSquare_DLL'  : 'ctypes DLL VC',
        'calSquareRootAndSquare_DLL_gcc' : 'ctypes DLL GCC',
        'calSquareRootAndSquare_OMP'  : 'ctypes DLL VC OpenMP',
}


dlllib_DLL = npct.load_library("calSquareRootAndSquare_DLL",".")
dlllib.calSquareRootAndSquare_DLL.argtypes = [c_int]

dlllib_DLL_gcc = CDLL("./calSquareRootAndSquare_DLL_gcc.dll")
dlllib.calSquareRootAndSquare_DLL.argtypes = [c_int]

dlllib_OMP = CDLL("./calSRaddS_OMP.dll")
dlllib.calSquareRootAndSquare_DLL.argtypes = [c_int]

def calSquareRootAndSquare_OMP(N):
    global dlllib_OMP
    result = np.zeros(N, dtype=np.float64)
    result = dlllib_OMP.calSquareRootAndSquare_DLL(N)
    return result
    
def calSquareRootAndSquare_DLL_gcc(N):
    global dlllib_DLL_gcc
    result = dlllib_DLL_gcc.calSquareRootAndSquare_DLL(N)
    return result

def calSquareRootAndSquare_DLL(N):
    global dlllib
    result = dlllib.calSquareRootAndSquare_DLL(N)
    return result

@njit
def calSquareRootAndSquare_OP(N):
    result = np.zeros(N, dtype=np.float64)
    for i in range(N):
        result[i] = math.sqrt(i)+ math.pow(i,2)
    return result

# def calMaOpt(d, window): # 前n项和问题！ 
#     if d.size <= window:
#         return np.zeros(d.size, dtype=np.float64)
#     adjust = int(window/2)
#     n = d.size
#     m = np.zeros(n, dtype=np.float64)
#     s = np.sum(d[:window], dtype=np.int64)
#     m[adjust] = s/window
#     for i in range(1,n-window+1):
#         s = s - d[i-1] + d[i+window-1] # 3 times operations => 2 times operations
#         m[i+adjust] = s/window
#     return m

def calSquareRootAndSquare(N):
    for i in range(N):
        result = math.sqrt(i)+ math.pow(i,2)
    return result
'''
beforeCal=datetime.datetime.now()
for number in range(100000):
    result=math.sqrt(number )+math.pow(number,2)
afterCal=datetime.datetime .now()
calCost=afterCal-beforeCal
'''

def printDiff(d1,d2):
    n = d1.size
    for i in range(n):
        if d1[i] != d2[i]:
            print(i,d1[i],d2[i])
            
def checkRet(dictRet): # check the same answer!!
    listKey = list(dictRet.keys())
    number = len(listKey)
    for i in range(number-1):
        for n in range(i+1,number):
            keyi = listKey[i]
            keyn = listKey[n]
            if (dictRet[keyi].size != dictRet[keyn].size):
                print('checkRet size difference {} : {} != {} : {} '.format(keyi, dictRet[keyi].size, keyn, dictRet[keyn].size))
                return False
    print('checkRet size', dictRet[listKey[0]].size)
    for i in range(number-1):
        for n in range(i+1,number):
            keyi = listKey[i]
            keyn = listKey[n]
            if ((dictRet[keyi] == dictRet[keyn]).all() != True):            
                print('checkRet result False: {} {}'.format(keyi, keyn))
                print(type(dictRet[keyi][0]), type(dictRet[keyn][0]))
                printDiff(dictRet[keyi], dictRet[keyi])
                return False
    print('checkRet result True')
    return True

def getSysInfo():
    name = ''
    output = ''
    try:
        from SysInfo import sysinfo
        dictInfo = sysinfo()
    except:
        print('Please install wmi using:\npip install wmi\n')
        return name, output
    output = '###### System Information \n'
    output += '||| \n'
    output += '|:---|:---| \n'
    for key in dictInfo:
        if key == 'Name':
            name = dictInfo[key]
            continue
        output += '|{}|{}| \n'.format(key,dictInfo[key])
    date = strftime("%Y-%m-%d %H:%M:%S", localtime()) 
    output += '|{}|{}| \n'.format('TIME', date)
    return name, output

def getTestInfo():
    global loop, subloop, winsize, length, data
    datatype = type(data[0])
    output = '###### Test Information \n'
    output += '||| \n'
    output += '|:---|:---| \n'
    output += '|{}|{} * {}| \n'.format('Loop Number', loop, subloop)
    output += '|{}|{:,}| \n'.format('Data Size', length)
    output += '|{}|{}| \n'.format('Window Size', winsize)
    output += '|{}|{}| \n'.format('Data Type', str(datatype).lstrip('<class').rstrip('>').strip().strip("'"))
    return output

def saveResult(result, loop):
    output = ''
    name, sysinfo = getSysInfo()
    output += sysinfo
    output += getTestInfo()
    output += '###### Test Result \n'
    t = ''
    for i in range(loop):
        t += '|{}'.format(i+1)
    output += '|Name|Infomation'+t+'|Avg|Faster| \n'
    output += '|:---|:---:'+'|---:'*(loop+2)+'| \n'
    for key in result:
        info = '|{}|{}'.format(key, result[key][0])
        for data in result[key][1:]:
            info += '|{}'.format('%.3f'%data)
        info += '| \n'
        output += info
    if name != '':
        filename ='Result_{}.md'.format(name)
    else:
        filename = 'Result.md'
    f = open(filename, 'w', encoding='utf-8')
    f.write(output)
    f.close()
    return

def main():
    global loop, subloop, winsize

    dictRet = {}
    for key in dictTest:
        dictRet[key] = eval(key)(data,winsize)

    ret = checkRet(dictRet)
    if ret != True:
        return
    
    result = {}
    for key in dictTest:
        result[key] = [dictTest[key]]

    for i in range(loop): # begin test with 5 loops. 
        print('time : ', i+1)

        for key in dictTest:# each dict item: calMa or calMaCov
            strCmd = '{}(data,winsize)'.format(key) # 执行cmd
            strSetup = 'from __main__ import {},data,winsize'.format(key) # data,winsize是传入的参数
            ret = timeit(strCmd, setup=strSetup, number = subloop) # use timeit as the stand test lib function
            print('{:<10} : {} '.format(key, ret))
            result[key].append(ret)
            
    avgbase = sum(result['calMa'][1:])/loop
    for key in result:
        avg = sum(result[key][1:])/loop # count avg
        faster = avgbase/avg # count accelerate radio
        result[key].append(avg)
        result[key].append(faster)

    saveResult(result, loop) # draw pic
    return

if __name__ == '__main__':
    main()
