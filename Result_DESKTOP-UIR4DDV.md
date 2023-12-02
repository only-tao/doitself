###### System Information 
||| 
|:---|:---| 
|OS|Microsoft Windows 10 专业版 19045 64 位| 
|CPU|Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz # Threads : 12| 
|GPU 0|NVIDIA Quadro T2000 with Max-Q Design # 31.0.15.2908| 
|GPU 1|Intel(R) UHD Graphics # 27.20.100.9316| 
|MEM|16384 MB  = 16384 MB| 
|TIME|2023-12-02 12:58:14| 
###### Test Information 
||| 
|:---|:---| 
|Loop Number|5 * 5| 
|Data Size|1,000,000| 
###### Test Result 
|Name|Infomation|1|2|3|4|5|Avg|Faster| 
|:---|:---:|---:|---:|---:|---:|---:|---:|---:| 
|calSquareRootAndSquare|Standard Python|3.408|3.251|3.295|3.200|2.990|3.229|1.000| 
|calSquareRootAndSquare_OP|Python Numpy |1.268|1.320|1.220|1.134|1.107|1.210|2.669| 
|calSquareRootAndSquare_JIT|Numba JIT|0.019|0.019|0.021|0.026|0.018|0.021|155.229| 
|calSquareRootAndSquare_AOT|Numba AOT|0.022|0.024|0.027|0.024|0.021|0.024|136.127| 
|calSRaddS_CY|Cython Module|2.642|2.613|2.704|2.432|2.381|2.554|1.264| 
|calSRaddS_PyC|C Module VC|0.262|0.252|0.253|0.228|0.233|0.245|13.157| 
|calSRaddS_PyCG|C Module GCC|0.228|0.259|0.259|0.233|0.252|0.246|13.111| 
|calSquareRootAndSquare_DLL|ctypes DLL VC|0.230|0.218|0.244|0.233|0.232|0.231|13.950| 
|calSquareRootAndSquare_DLL_gcc|ctypes DLL GCC|0.018|0.018|0.020|0.021|0.024|0.020|159.810| 
|calSquareRootAndSquare_OMP|ctypes DLL VC OpenMP|0.224|0.204|0.217|0.212|0.289|0.229|14.092| 
