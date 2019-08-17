#!/usr/bin/python
import os

lib='KSKUHLMAN'
tgtrls='*CURRENT'
dirname=''


def os400(cmd):
    """Usage:
    os400("sndmsg 'hello' tousr(kskuhlman)")
    How to get this?:
    system "CRTCMOD MODULE(KSKUHLMAN/scanners) SRCSTMF('/home/KSKUHLMAN/cython/Cython/Plex/Scanners.c') OUTPUT(*PRINT)"
    """
    os.system('system "%s"' % cmd)


def crtmod(modname, path, INCLUDE):
    include=':'.join([dirname] + INCLUDE)
    cmd = "chgenvvar envvar(INCLUDE) value('%s')"
    print(cmd)
    os.system(cmd)
    
    cmd = "CRTCMOD MODULE(%s/%s) " % (lib, modname) + \
      "SRCSTMF('%s') OUTPUT(*PRINT) OPTIMIZE(10) " % path + \
      "INLINE(*OFF) DBGVIEW(*ALL) SYSIFCOPT(*IFS64IO) " + \
      "LOCALETYPE(*LOCALEUTF) FLAG(10) TERASPACE(*YES *TSIFC) " + \
      "STGMDL(*TERASPACE) TGTRLS(%s) DTAMDL(*LLP64) " % tgtrls + \
      "INCDIR('%s') " % include
    print(cmd)

    if os400(cmd):
        #iSeriesPtyhon let you do this.. shall we clone that? 
        #os400.sndpgmmsg('*** F A I L E D ***')
        os400("sndpgmmsg '*** F A I L E D ***'")

include=['/QOpenSys/pkgs/include/python3.6m']
#I/QOpenSys/pkgs/include/python3.6m -c Cython/Plex/Scanners.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex/Scanners.o
crtmod('scanners', '/home/KSKUHLMAN/cython/Cython/Plex/Scanners.c', include)

#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Plex/Scanners.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Plex/Scanners.so
#crtsrvpgm('scanners')


#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Plex/Actions.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Plex/Actions.o
crtmod('actions', 'Cython/Plex/Actions.c', include)
 
#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Plex/Actions.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Plex/Actions.so
#crtsrvpgm('actions')


#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/Scanning.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/Scanning.o
crtmod('scanning','Cython/Compiler/Scanning.c', include)

#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Compiler/Scanning.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/Scanning.so
#crtsrvpgm('scanning')
 

#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/Visitor.c -o build/temp.os400-powerpc64-3.6/Cython/Compiler/Visitor.o
crtmod('visitor', 'Cython/Compiler/Visitor.c', include)
 
#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/Visitor.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/Visitor.so
#crtsrvpgm('visitor')


#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/FlowControl.c -o build/temp.os400-powerpc64-3.6/Cython/Compiler/FlowControl.o
crtmod('FlowControl', '/home/as500/cython/Cython/Compiler/FlowControl.c', include)

#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Compiler/FlowControl.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/FlowControl.so
#crtsrvpgm('FlowControl')

#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Runtime/refnanny.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Runtime/refnanny.o
#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Runtime/refnanny.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Runtime/refnanny.so
crtmod('refnanny','Cython/Runtime/refnanny.c', include) 
#crtsrvpgm('refnanny')

#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Compiler/FusedNode.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Compiler/FusedNode.o
#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Compiler/FusedNode.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Compiler/FusedNode.so
crtmod('FusedNode','/home/as500/cython/Cython/Compiler/FusedNode.c',include)
#crtsrvpgm('FusedNode')

#I/QOpenSys/pkgs/include/python3.6m -c /home/as500/cython/Cython/Tempita/_tempita.c -o build/temp.os400-powerpc64-3.6/home/as500/cython/Cython/Tempita/_tempita.o
#I:/QOpenSys/pkgs/lib/python3.6/config-3.6m/python.exp -Wl,-blibpath:/QOpenSys/pkgs/lib:/QOpenSys/usr/lib build/temp.os400-powerpc64-3.6/Cython/Tempita/_tempita.o -L/QOpenSys/pkgs/lib -o build/lib.os400-powerpc64-3.6/Cython/Tempita/_tempita.so
crtmod('_tempita','/home/as500/cython/Cython/Tempita/_tempita.c',include)
#crtsrvpgm('_tempita')
