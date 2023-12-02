all:
	g++ -O3 -DNDEBUG -fPIC -shared -o calSquareRootAndSquare_DLL_gcc.dll dllmain_dll.cpp
	strip calSquareRootAndSquare_DLL_gcc.dll
	# g++ -O3 -DNDEBUG -shared -o calSquareRootAndSquare_DLLG.dll calSquareRootAndSquare_DLLG.cpp

clean:
	del calSquareRootAndSquare_DLL_gcc.dll
	rm .\..\..\calSquareRootAndSquare_DLL_gcc.dll
    

