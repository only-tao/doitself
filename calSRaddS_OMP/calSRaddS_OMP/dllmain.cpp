// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include <stdio.h>
#include <math.h>
#include <omp.h>
#ifdef _MSC_VER
#define DLL_EXPORT extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT extern "C" 
#endif

#define DEBUGL

DLL_EXPORT void __stdcall calSquareRootAndSquare_DLL(int N,double* result)
{
#pragma omp parallel for 
    for (int i = 0; i < N; i++)
    {
        result[i] = sqrt(i) + pow(i, 2);
    }
    return ;
}

