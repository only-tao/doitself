// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include <stdio.h>
#include <math.h>
#include<stdlib.h>
#ifdef _MSC_VER
#define DLL_EXPORT extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT extern "C" 
#endif

#define DEBUGL

DLL_EXPORT void __stdcall calSquareRootAndSquare_DLL(int N,double* result) 
{
    //double* result = (double*)malloc(N * sizeof(double));
    for (int i = 0; i < N; i++)
    {
        result[i] = sqrt(i) + pow(i, 2);
    }
    return;
}
//DLL_EXPORT void __stdcall freeMemory(double* ptr) {
//    free(ptr);
//}
//BOOL APIENTRY DllMain( HMODULE hModule,
//                       DWORD  ul_reason_for_call,
//                       LPVOID lpReserved
//                     )
//{
//    switch (ul_reason_for_call)
//    {
//    case DLL_PROCESS_ATTACH:
//    case DLL_THREAD_ATTACH:
//    case DLL_THREAD_DETACH:
//    case DLL_PROCESS_DETACH:
//        break;
//    }
//    return TRUE;
//}

