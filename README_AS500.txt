
Installing on IBM i under PASE is trivial.  Commands & results for that are below.

My goal, however, is to build this natively under OS400. 

See plat_as500.py for start of that attempt.

-k2uhl.

--------------------------------------------
#PASE-based build output:
bash-4.4$ git clone git@github.com:as500/cython.git
Cloning into 'cython'...
...
Checking out files: 100% (2015/2015), done.
bash-4.4$ alias python=python3
bash-4.4$ python setup.py build_ext --inplace
Unable to find pgen, not compiling formal grammar.
running build_ext
Compiling /home/as500/cython/Cython/Plex/Scanners.py because it changed.
Compiling /home/as500/cython/Cython/Plex/Actions.py because it changed.
Compiling /home/as500/cython/Cython/Compiler/Scanning.py because it changed.
Compiling /home/as500/cython/Cython/Compiler/Visitor.py because it changed.
Compiling /home/as500/cython/Cython/Compiler/FlowControl.py because it changed.
Compiling /home/as500/cython/Cython/Runtime/refnanny.pyx because it changed.
Compiling /home/as500/cython/Cython/Compiler/FusedNode.py because it changed.
Compiling /home/as500/cython/Cython/Tempita/_tempita.py because it changed.
[1/8] Cythonizing /home/as500/cython/Cython/Compiler/FlowControl.py
[2/8] Cythonizing /home/as500/cython/Cython/Compiler/FusedNode.py
[3/8] Cythonizing /home/as500/cython/Cython/Compiler/Scanning.py
[4/8] Cythonizing /home/as500/cython/Cython/Compiler/Visitor.py
[5/8] Cythonizing /home/as500/cython/Cython/Plex/Actions.py
[6/8] Cythonizing /home/as500/cython/Cython/Plex/Scanners.py
[7/8] Cythonizing /home/as500/cython/Cython/Runtime/refnanny.pyx
[8/8] Cythonizing /home/as500/cython/Cython/Tempita/_tempita.py
building 'Cython.Plex.Scanners' extension
creating build
creating build/temp.os400-powerpc64-3.6
creating build/temp.os400-powerpc64-3.6/home
creating build/temp.os400-powerpc64-3.6/home/as500
creating build/temp.os400-powerpc64-3.6/home/as500/cython
creating build/temp.os400-powerpc64-3.6/home/as500/cython/Cython
creating build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Plex/Scanners.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex/Scanners.o
creating build/lib.os400-powerpc64-3.6
creating build/lib.os400-powerpc64-3.6/Cython
creating build/lib.os400-powerpc64-3.6/Cython/Plex
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex/Scanners.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Plex/Scanners.so
building 'Cython.Plex.Actions' extension
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Plex/Actions.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex/Actions.o
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex/Actions.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Plex/Actions.so
building 'Cython.Compiler.Scanning' extension
creating build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/Scanning.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/Scanning.o
creating build/lib.os400-powerpc64-3.6/Cython/Compiler
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/Scanning.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/Scanning.so
building 'Cython.Compiler.Visitor' extension
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/Visitor.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/Visitor.o
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/Visitor.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/Visitor.so
building 'Cython.Compiler.FlowControl' extension
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/FlowControl.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/FlowControl.o
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/FlowControl.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/FlowControl.so
ld: 0711-319 WARNING: Exported symbol not defined: __pyx_module_is_main_Cython__Compiler(long)
ld: 0711-319 WARNING: Exported symbol not defined: __pyx_module_is_main_Cython__Compiler(long)
building 'Cython.Runtime.refnanny' extension
creating build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Runtime
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Runtime/refnanny.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Runtime/refnanny.o
creating build/lib.os400-powerpc64-3.6/Cython/Runtime
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Runtime/refnanny.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Runtime/refnanny.so
building 'Cython.Compiler.FusedNode' extension
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/FusedNode.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/FusedNode.o
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/FusedNode.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/FusedNode.so
building 'Cython.Tempita._tempita' extension
creating build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Tempita
gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -O2 -g -maix64 -O2 -g -maix64 -I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Tempita/_tempita.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Tempita/_tempita.o
creating build/lib.os400-powerpc64-3.6/Cython/Tempita
/QOpenSys/pkgs/lib/python3.6/config-3.6m/ld_so_aix gcc -pthread -bI:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Tempita/_tempita.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Tempita/_tempita.so
copying build/lib.os400-powerpc64-3.6/Cython/Plex/Scanners.so -> Cython/Plex
copying build/lib.os400-powerpc64-3.6/Cython/Plex/Actions.so -> Cython/Plex
copying build/lib.os400-powerpc64-3.6/Cython/Compiler/Scanning.so -> Cython/Compiler
copying build/lib.os400-powerpc64-3.6/Cython/Compiler/Visitor.so -> Cython/Compiler
copying build/lib.os400-powerpc64-3.6/Cython/Compiler/FlowControl.so -> Cython/Compiler
copying build/lib.os400-powerpc64-3.6/Cython/Runtime/refnanny.so -> Cython/Runtime
copying build/lib.os400-powerpc64-3.6/Cython/Compiler/FusedNode.so -> Cython/Compiler
copying build/lib.os400-powerpc64-3.6/Cython/Tempita/_tempita.so -> Cython/Tempita

