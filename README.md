# [easy keyg3nme](https://crackmes.one/crackme/5da31ebc33c5d46f00e2c661)

Desafio simples (nivel 1) do site crackmes.one

Baixe o arquivo zipado e leia o FAQ para descobrir qual é a senha do zip.

## Pré-requisito:
- linux (ou algo compatível, foi feito e testando em um manjaro)
- python 3

## Informações sobre o binário:

```bash
$ file keyg3nme
keyg3nme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=01d8f2eefa63ea2a9dc6f6ceb2be2eac2ca22a67, for GNU/Linux 3.2.0, not stripped

$ readelf -a ./keyg3nme

ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x1080
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14816 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         11
  Size of section headers:           64 (bytes)
  Number of section headers:         29
  Section header string table index: 28

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         00000000000002a8  000002a8
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.gnu.build-i NOTE             00000000000002c4  000002c4
       0000000000000024  0000000000000000   A       0     0     4
  [ 3] .note.ABI-tag     NOTE             00000000000002e8  000002e8
       0000000000000020  0000000000000000   A       0     0     4
  [ 4] .gnu.hash         GNU_HASH         0000000000000308  00000308
       0000000000000024  0000000000000000   A       5     0     8
  [ 5] .dynsym           DYNSYM           0000000000000330  00000330
       00000000000000f0  0000000000000018   A       6     1     8
  [ 6] .dynstr           STRTAB           0000000000000420  00000420
       00000000000000bd  0000000000000000   A       0     0     1
  [ 7] .gnu.version      VERSYM           00000000000004de  000004de
       0000000000000014  0000000000000002   A       5     0     2
  [ 8] .gnu.version_r    VERNEED          00000000000004f8  000004f8
       0000000000000040  0000000000000000   A       6     1     8
  [ 9] .rela.dyn         RELA             0000000000000538  00000538
       00000000000000c0  0000000000000018   A       5     0     8
  [10] .rela.plt         RELA             00000000000005f8  000005f8
       0000000000000060  0000000000000018  AI       5    22     8
  [11] .init             PROGBITS         0000000000001000  00001000
       0000000000000017  0000000000000000  AX       0     0     4
  [12] .plt              PROGBITS         0000000000001020  00001020
       0000000000000050  0000000000000010  AX       0     0     16
  [13] .plt.got          PROGBITS         0000000000001070  00001070
       0000000000000008  0000000000000008  AX       0     0     8
  [14] .text             PROGBITS         0000000000001080  00001080
       0000000000000211  0000000000000000  AX       0     0     16
  [15] .fini             PROGBITS         0000000000001294  00001294
       0000000000000009  0000000000000000  AX       0     0     4
  [16] .rodata           PROGBITS         0000000000002000  00002000
       0000000000000047  0000000000000000   A       0     0     8
  [17] .eh_frame_hdr     PROGBITS         0000000000002048  00002048
       0000000000000044  0000000000000000   A       0     0     4
  [18] .eh_frame         PROGBITS         0000000000002090  00002090
       0000000000000128  0000000000000000   A       0     0     8
  [19] .init_array       INIT_ARRAY       0000000000003da0  00002da0
       0000000000000008  0000000000000008  WA       0     0     8
  [20] .fini_array       FINI_ARRAY       0000000000003da8  00002da8
       0000000000000008  0000000000000008  WA       0     0     8
  [21] .dynamic          DYNAMIC          0000000000003db0  00002db0
       00000000000001f0  0000000000000010  WA       6     0     8
  [22] .got              PROGBITS         0000000000003fa0  00002fa0
       0000000000000060  0000000000000008  WA       0     0     8
  [23] .data             PROGBITS         0000000000004000  00003000
       0000000000000010  0000000000000000  WA       0     0     8
  [24] .bss              NOBITS           0000000000004010  00003010
       0000000000000008  0000000000000000  WA       0     0     1
  [25] .comment          PROGBITS         0000000000000000  00003010
       0000000000000023  0000000000000001  MS       0     0     1
  [26] .symtab           SYMTAB           0000000000000000  00003038
       0000000000000648  0000000000000018          27    44     8
  [27] .strtab           STRTAB           0000000000000000  00003680
       000000000000025d  0000000000000000           0     0     1
  [28] .shstrtab         STRTAB           0000000000000000  000038dd
       00000000000000fe  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  l (large), p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  PHDR           0x0000000000000040 0x0000000000000040 0x0000000000000040
                 0x0000000000000268 0x0000000000000268  R      0x8
  INTERP         0x00000000000002a8 0x00000000000002a8 0x00000000000002a8
                 0x000000000000001c 0x000000000000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000658 0x0000000000000658  R      0x1000
  LOAD           0x0000000000001000 0x0000000000001000 0x0000000000001000
                 0x000000000000029d 0x000000000000029d  R E    0x1000
  LOAD           0x0000000000002000 0x0000000000002000 0x0000000000002000
                 0x00000000000001b8 0x00000000000001b8  R      0x1000
  LOAD           0x0000000000002da0 0x0000000000003da0 0x0000000000003da0
                 0x0000000000000270 0x0000000000000278  RW     0x1000
  DYNAMIC        0x0000000000002db0 0x0000000000003db0 0x0000000000003db0
                 0x00000000000001f0 0x00000000000001f0  RW     0x8
  NOTE           0x00000000000002c4 0x00000000000002c4 0x00000000000002c4
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_EH_FRAME   0x0000000000002048 0x0000000000002048 0x0000000000002048
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x10
  GNU_RELRO      0x0000000000002da0 0x0000000000003da0 0x0000000000003da0
                 0x0000000000000260 0x0000000000000260  R      0x1

 Section to Segment mapping:
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.gnu.build-id .note.ABI-tag .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt 
   03     .init .plt .plt.got .text .fini 
   04     .rodata .eh_frame_hdr .eh_frame 
   05     .init_array .fini_array .dynamic .got .data .bss 
   06     .dynamic 
   07     .note.gnu.build-id .note.ABI-tag 
   08     .eh_frame_hdr 
   09     
   10     .init_array .fini_array .dynamic .got 

Dynamic section at offset 0x2db0 contains 27 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x1000
 0x000000000000000d (FINI)               0x1294
 0x0000000000000019 (INIT_ARRAY)         0x3da0
 0x000000000000001b (INIT_ARRAYSZ)       8 (bytes)
 0x000000000000001a (FINI_ARRAY)         0x3da8
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x000000006ffffef5 (GNU_HASH)           0x308
 0x0000000000000005 (STRTAB)             0x420
 0x0000000000000006 (SYMTAB)             0x330
 0x000000000000000a (STRSZ)              189 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0x3fa0
 0x0000000000000002 (PLTRELSZ)           96 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0x5f8
 0x0000000000000007 (RELA)               0x538
 0x0000000000000008 (RELASZ)             192 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000000000001e (FLAGS)              BIND_NOW
 0x000000006ffffffb (FLAGS_1)            Flags: NOW PIE
 0x000000006ffffffe (VERNEED)            0x4f8
 0x000000006fffffff (VERNEEDNUM)         1
 0x000000006ffffff0 (VERSYM)             0x4de
 0x000000006ffffff9 (RELACOUNT)          3
 0x0000000000000000 (NULL)               0x0

Relocation section '.rela.dyn' at offset 0x538 contains 8 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000003da0  000000000008 R_X86_64_RELATIVE                    1160
000000003da8  000000000008 R_X86_64_RELATIVE                    1120
000000004008  000000000008 R_X86_64_RELATIVE                    4008
000000003fd8  000100000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_deregisterTMClone + 0
000000003fe0  000500000006 R_X86_64_GLOB_DAT 0000000000000000 __libc_start_main@GLIBC_2.2.5 + 0
000000003fe8  000600000006 R_X86_64_GLOB_DAT 0000000000000000 __gmon_start__ + 0
000000003ff0  000800000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_registerTMCloneTa + 0
000000003ff8  000900000006 R_X86_64_GLOB_DAT 0000000000000000 __cxa_finalize@GLIBC_2.2.5 + 0

Relocation section '.rela.plt' at offset 0x5f8 contains 4 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000003fb8  000200000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0
000000003fc0  000300000007 R_X86_64_JUMP_SLO 0000000000000000 __stack_chk_fail@GLIBC_2.4 + 0
000000003fc8  000400000007 R_X86_64_JUMP_SLO 0000000000000000 printf@GLIBC_2.2.5 + 0
000000003fd0  000700000007 R_X86_64_JUMP_SLO 0000000000000000 __isoc99_scanf@GLIBC_2.7 + 0

The decoding of unwind sections for machine type Advanced Micro Devices X86-64 is not currently supported.

Symbol table '.dynsym' contains 10 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __stack_chk_fail@GLIBC_2.4 (3)
     4: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.2.5 (2)
     5: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.2.5 (2)
     6: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     7: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __isoc99_scanf@GLIBC_2.7 (4)
     8: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
     9: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@GLIBC_2.2.5 (2)

Symbol table '.symtab' contains 67 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 00000000000002a8     0 SECTION LOCAL  DEFAULT    1 
     2: 00000000000002c4     0 SECTION LOCAL  DEFAULT    2 
     3: 00000000000002e8     0 SECTION LOCAL  DEFAULT    3 
     4: 0000000000000308     0 SECTION LOCAL  DEFAULT    4 
     5: 0000000000000330     0 SECTION LOCAL  DEFAULT    5 
     6: 0000000000000420     0 SECTION LOCAL  DEFAULT    6 
     7: 00000000000004de     0 SECTION LOCAL  DEFAULT    7 
     8: 00000000000004f8     0 SECTION LOCAL  DEFAULT    8 
     9: 0000000000000538     0 SECTION LOCAL  DEFAULT    9 
    10: 00000000000005f8     0 SECTION LOCAL  DEFAULT   10 
    11: 0000000000001000     0 SECTION LOCAL  DEFAULT   11 
    12: 0000000000001020     0 SECTION LOCAL  DEFAULT   12 
    13: 0000000000001070     0 SECTION LOCAL  DEFAULT   13 
    14: 0000000000001080     0 SECTION LOCAL  DEFAULT   14 
    15: 0000000000001294     0 SECTION LOCAL  DEFAULT   15 
    16: 0000000000002000     0 SECTION LOCAL  DEFAULT   16 
    17: 0000000000002048     0 SECTION LOCAL  DEFAULT   17 
    18: 0000000000002090     0 SECTION LOCAL  DEFAULT   18 
    19: 0000000000003da0     0 SECTION LOCAL  DEFAULT   19 
    20: 0000000000003da8     0 SECTION LOCAL  DEFAULT   20 
    21: 0000000000003db0     0 SECTION LOCAL  DEFAULT   21 
    22: 0000000000003fa0     0 SECTION LOCAL  DEFAULT   22 
    23: 0000000000004000     0 SECTION LOCAL  DEFAULT   23 
    24: 0000000000004010     0 SECTION LOCAL  DEFAULT   24 
    25: 0000000000000000     0 SECTION LOCAL  DEFAULT   25 
    26: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    27: 00000000000010b0     0 FUNC    LOCAL  DEFAULT   14 deregister_tm_clones
    28: 00000000000010e0     0 FUNC    LOCAL  DEFAULT   14 register_tm_clones
    29: 0000000000001120     0 FUNC    LOCAL  DEFAULT   14 __do_global_dtors_aux
    30: 0000000000004010     1 OBJECT  LOCAL  DEFAULT   24 completed.7963
    31: 0000000000003da8     0 OBJECT  LOCAL  DEFAULT   20 __do_global_dtors_aux_fin
    32: 0000000000001160     0 FUNC    LOCAL  DEFAULT   14 frame_dummy
    33: 0000000000003da0     0 OBJECT  LOCAL  DEFAULT   19 __frame_dummy_init_array_
    34: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS keyg3nm3.c
    35: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    36: 00000000000021b4     0 OBJECT  LOCAL  DEFAULT   18 __FRAME_END__
    37: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS 
    38: 0000000000003da8     0 NOTYPE  LOCAL  DEFAULT   19 __init_array_end
    39: 0000000000003db0     0 OBJECT  LOCAL  DEFAULT   21 _DYNAMIC
    40: 0000000000003da0     0 NOTYPE  LOCAL  DEFAULT   19 __init_array_start
    41: 0000000000002048     0 NOTYPE  LOCAL  DEFAULT   17 __GNU_EH_FRAME_HDR
    42: 0000000000003fa0     0 OBJECT  LOCAL  DEFAULT   22 _GLOBAL_OFFSET_TABLE_
    43: 0000000000001000     0 FUNC    LOCAL  DEFAULT   11 _init
    44: 0000000000001290     1 FUNC    GLOBAL DEFAULT   14 __libc_csu_fini
    45: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    46: 0000000000004000     0 NOTYPE  WEAK   DEFAULT   23 data_start
    47: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
    48: 0000000000004010     0 NOTYPE  GLOBAL DEFAULT   23 _edata
    49: 0000000000001294     0 FUNC    GLOBAL HIDDEN    15 _fini
    50: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __stack_chk_fail@@GLIBC_2
    51: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@@GLIBC_2.2.5
    52: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@@GLIBC_
    53: 0000000000004000     0 NOTYPE  GLOBAL DEFAULT   23 __data_start
    54: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    55: 0000000000004008     0 OBJECT  GLOBAL HIDDEN    23 __dso_handle
    56: 0000000000002000     4 OBJECT  GLOBAL DEFAULT   16 _IO_stdin_used
    57: 0000000000001230    93 FUNC    GLOBAL DEFAULT   14 __libc_csu_init
    58: 0000000000004018     0 NOTYPE  GLOBAL DEFAULT   24 _end
    59: 0000000000001080    43 FUNC    GLOBAL DEFAULT   14 _start
    60: 0000000000004010     0 NOTYPE  GLOBAL DEFAULT   24 __bss_start
    61: 0000000000001165   137 FUNC    GLOBAL DEFAULT   14 main
    62: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __isoc99_scanf@@GLIBC_2.7
    63: 0000000000004010     0 OBJECT  GLOBAL HIDDEN    23 __TMC_END__
    64: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    65: 00000000000011ee    59 FUNC    GLOBAL DEFAULT   14 validate_key
    66: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.2

Histogram for `.gnu.hash' bucket list length (total of 2 buckets):
 Length  Number     % of total  Coverage
      0  1          ( 50.0%)
      1  1          ( 50.0%)    100.0%

Version symbols section '.gnu.version' contains 10 entries:
 Addr: 0x00000000000004de  Offset: 0x0004de  Link: 5 (.dynsym)
  000:   0 (*local*)       0 (*local*)       2 (GLIBC_2.2.5)   3 (GLIBC_2.4)  
  004:   2 (GLIBC_2.2.5)   2 (GLIBC_2.2.5)   0 (*local*)       4 (GLIBC_2.7)  
  008:   0 (*local*)       2 (GLIBC_2.2.5)

Version needs section '.gnu.version_r' contains 1 entry:
 Addr: 0x00000000000004f8  Offset: 0x0004f8  Link: 6 (.dynstr)
  000000: Version: 1  File: libc.so.6  Cnt: 3
  0x0010:   Name: GLIBC_2.7  Flags: none  Version: 4
  0x0020:   Name: GLIBC_2.4  Flags: none  Version: 3
  0x0030:   Name: GLIBC_2.2.5  Flags: none  Version: 2

Displaying notes found in: .note.gnu.build-id
  Owner                Data size 	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 01d8f2eefa63ea2a9dc6f6ceb2be2eac2ca22a67

Displaying notes found in: .note.ABI-tag
  Owner                Data size 	Description
  GNU                  0x00000010	NT_GNU_ABI_TAG (ABI version tag)
    OS: Linux, ABI: 3.2.0
  
$ strings -t d -d ./keyg3nme
    680 /lib64/ld-linux-x86-64.so.2
   1057 libc.so.6
   1067 __isoc99_scanf
   1082 puts
   1087 __stack_chk_fail
   1104 printf
   1111 __cxa_finalize
   1126 __libc_start_main
   1144 GLIBC_2.7
   1154 GLIBC_2.4
   1164 GLIBC_2.2.5
   1176 _ITM_deregisterTMCloneTable
   1204 __gmon_start__
   1219 _ITM_registerTMCloneTable
   4391 u/UH
   4738 []A\A]A^A_
   8200 Enter your key:  
   8224 Good job mate, now go keygen me.
   8257 nope.
   8439 ;*3$"
```

## Assembly extraido via objdump:

```bash
$ objdump -M intel -d -C ./keyg3nme
```

```asm
./keyg3nme:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 _init:
    1000:	48 83 ec 08          	sub    rsp,0x8
    1004:	48 8b 05 dd 2f 00 00 	mov    rax,QWORD PTR [rip+0x2fdd]        # 3fe8 <__gmon_start__>
    100b:	48 85 c0             	test   rax,rax
    100e:	74 02                	je     1012 <_init+0x12>
    1010:	ff d0                	call   rax
    1012:	48 83 c4 08          	add    rsp,0x8
    1016:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 .plt:
    1020:	ff 35 82 2f 00 00    	push   QWORD PTR [rip+0x2f82]        # 3fa8 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:	ff 25 84 2f 00 00    	jmp    QWORD PTR [rip+0x2f84]        # 3fb0 <_GLOBAL_OFFSET_TABLE_+0x10>
    102c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000001030 puts@plt:
    1030:	ff 25 82 2f 00 00    	jmp    QWORD PTR [rip+0x2f82]        # 3fb8 <puts@GLIBC_2.2.5>
    1036:	68 00 00 00 00       	push   0x0
    103b:	e9 e0 ff ff ff       	jmp    1020 <.plt>

0000000000001040 __stack_chk_fail@plt:
    1040:	ff 25 7a 2f 00 00    	jmp    QWORD PTR [rip+0x2f7a]        # 3fc0 <__stack_chk_fail@GLIBC_2.4>
    1046:	68 01 00 00 00       	push   0x1
    104b:	e9 d0 ff ff ff       	jmp    1020 <.plt>

0000000000001050 printf@plt:
    1050:	ff 25 72 2f 00 00    	jmp    QWORD PTR [rip+0x2f72]        # 3fc8 <printf@GLIBC_2.2.5>
    1056:	68 02 00 00 00       	push   0x2
    105b:	e9 c0 ff ff ff       	jmp    1020 <.plt>

0000000000001060 __isoc99_scanf@plt:
    1060:	ff 25 6a 2f 00 00    	jmp    QWORD PTR [rip+0x2f6a]        # 3fd0 <__isoc99_scanf@GLIBC_2.7>
    1066:	68 03 00 00 00       	push   0x3
    106b:	e9 b0 ff ff ff       	jmp    1020 <.plt>

Disassembly of section .plt.got:

0000000000001070 __cxa_finalize@plt:
    1070:	ff 25 82 2f 00 00    	jmp    QWORD PTR [rip+0x2f82]        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1076:	66 90                	xchg   ax,ax

Disassembly of section .text:

0000000000001080 _start:
    1080:	31 ed                	xor    ebp,ebp
    1082:	49 89 d1             	mov    r9,rdx
    1085:	5e                   	pop    rsi
    1086:	48 89 e2             	mov    rdx,rsp
    1089:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
    108d:	50                   	push   rax
    108e:	54                   	push   rsp
    108f:	4c 8d 05 fa 01 00 00 	lea    r8,[rip+0x1fa]        # 1290 <__libc_csu_fini>
    1096:	48 8d 0d 93 01 00 00 	lea    rcx,[rip+0x193]        # 1230 <__libc_csu_init>
    109d:	48 8d 3d c1 00 00 00 	lea    rdi,[rip+0xc1]        # 1165 <main>
    10a4:	ff 15 36 2f 00 00    	call   QWORD PTR [rip+0x2f36]        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    10aa:	f4                   	hlt    
    10ab:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000000010b0 deregister_tm_clones:
    10b0:	48 8d 3d 59 2f 00 00 	lea    rdi,[rip+0x2f59]        # 4010 <__TMC_END__>
    10b7:	48 8d 05 52 2f 00 00 	lea    rax,[rip+0x2f52]        # 4010 <__TMC_END__>
    10be:	48 39 f8             	cmp    rax,rdi
    10c1:	74 15                	je     10d8 <deregister_tm_clones+0x28>
    10c3:	48 8b 05 0e 2f 00 00 	mov    rax,QWORD PTR [rip+0x2f0e]        # 3fd8 <_ITM_deregisterTMCloneTable>
    10ca:	48 85 c0             	test   rax,rax
    10cd:	74 09                	je     10d8 <deregister_tm_clones+0x28>
    10cf:	ff e0                	jmp    rax
    10d1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    10d8:	c3                   	ret    
    10d9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

00000000000010e0 register_tm_clones:
    10e0:	48 8d 3d 29 2f 00 00 	lea    rdi,[rip+0x2f29]        # 4010 <__TMC_END__>
    10e7:	48 8d 35 22 2f 00 00 	lea    rsi,[rip+0x2f22]        # 4010 <__TMC_END__>
    10ee:	48 29 fe             	sub    rsi,rdi
    10f1:	48 c1 fe 03          	sar    rsi,0x3
    10f5:	48 89 f0             	mov    rax,rsi
    10f8:	48 c1 e8 3f          	shr    rax,0x3f
    10fc:	48 01 c6             	add    rsi,rax
    10ff:	48 d1 fe             	sar    rsi,1
    1102:	74 14                	je     1118 <register_tm_clones+0x38>
    1104:	48 8b 05 e5 2e 00 00 	mov    rax,QWORD PTR [rip+0x2ee5]        # 3ff0 <_ITM_registerTMCloneTable>
    110b:	48 85 c0             	test   rax,rax
    110e:	74 08                	je     1118 <register_tm_clones+0x38>
    1110:	ff e0                	jmp    rax
    1112:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    1118:	c3                   	ret    
    1119:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000001120 __do_global_dtors_aux:
    1120:	80 3d e9 2e 00 00 00 	cmp    BYTE PTR [rip+0x2ee9],0x0        # 4010 <__TMC_END__>
    1127:	75 2f                	jne    1158 <__do_global_dtors_aux+0x38>
    1129:	55                   	push   rbp
    112a:	48 83 3d c6 2e 00 00 	cmp    QWORD PTR [rip+0x2ec6],0x0        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1131:	00 
    1132:	48 89 e5             	mov    rbp,rsp
    1135:	74 0c                	je     1143 <__do_global_dtors_aux+0x23>
    1137:	48 8b 3d ca 2e 00 00 	mov    rdi,QWORD PTR [rip+0x2eca]        # 4008 <__dso_handle>
    113e:	e8 2d ff ff ff       	call   1070 <__cxa_finalize@plt>
    1143:	e8 68 ff ff ff       	call   10b0 <deregister_tm_clones>
    1148:	c6 05 c1 2e 00 00 01 	mov    BYTE PTR [rip+0x2ec1],0x1        # 4010 <__TMC_END__>
    114f:	5d                   	pop    rbp
    1150:	c3                   	ret    
    1151:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1158:	c3                   	ret    
    1159:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000001160 frame_dummy:
    1160:	e9 7b ff ff ff       	jmp    10e0 <register_tm_clones>

0000000000001165 main:
    1165:	55                   	push   rbp
    1166:	48 89 e5             	mov    rbp,rsp
    1169:	48 83 ec 10          	sub    rsp,0x10
    116d:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    1174:	00 00 
    1176:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    117a:	31 c0                	xor    eax,eax
    117c:	48 8d 3d 85 0e 00 00 	lea    rdi,[rip+0xe85]        # 2008 <_IO_stdin_used+0x8>
    1183:	b8 00 00 00 00       	mov    eax,0x0
    1188:	e8 c3 fe ff ff       	call   1050 <printf@plt>
    118d:	48 8d 45 f4          	lea    rax,[rbp-0xc]
    1191:	48 89 c6             	mov    rsi,rax
    1194:	48 8d 3d 7f 0e 00 00 	lea    rdi,[rip+0xe7f]        # 201a <_IO_stdin_used+0x1a>
    119b:	b8 00 00 00 00       	mov    eax,0x0
    11a0:	e8 bb fe ff ff       	call   1060 <__isoc99_scanf@plt>
    11a5:	8b 45 f4             	mov    eax,DWORD PTR [rbp-0xc]
    11a8:	89 c7                	mov    edi,eax
    11aa:	b8 00 00 00 00       	mov    eax,0x0
    11af:	e8 3a 00 00 00       	call   11ee <validate_key>
    11b4:	83 f8 01             	cmp    eax,0x1
    11b7:	75 0e                	jne    11c7 <main+0x62>
    11b9:	48 8d 3d 60 0e 00 00 	lea    rdi,[rip+0xe60]        # 2020 <_IO_stdin_used+0x20>
    11c0:	e8 6b fe ff ff       	call   1030 <puts@plt>
    11c5:	eb 0c                	jmp    11d3 <main+0x6e>
    11c7:	48 8d 3d 73 0e 00 00 	lea    rdi,[rip+0xe73]        # 2041 <_IO_stdin_used+0x41>
    11ce:	e8 5d fe ff ff       	call   1030 <puts@plt>
    11d3:	b8 00 00 00 00       	mov    eax,0x0
    11d8:	48 8b 55 f8          	mov    rdx,QWORD PTR [rbp-0x8]
    11dc:	64 48 33 14 25 28 00 	xor    rdx,QWORD PTR fs:0x28
    11e3:	00 00 
    11e5:	74 05                	je     11ec <main+0x87>
    11e7:	e8 54 fe ff ff       	call   1040 <__stack_chk_fail@plt>
    11ec:	c9                   	leave  
    11ed:	c3                   	ret    

00000000000011ee validate_key:
    11ee:	55                   	push   rbp
    11ef:	48 89 e5             	mov    rbp,rsp
    11f2:	89 7d fc             	mov    DWORD PTR [rbp-0x4],edi
    11f5:	8b 4d fc             	mov    ecx,DWORD PTR [rbp-0x4]
    11f8:	ba ad 0a cb 1a       	mov    edx,0x1acb0aad
    11fd:	89 c8                	mov    eax,ecx
    11ff:	f7 ea                	imul   edx
    1201:	c1 fa 07             	sar    edx,0x7
    1204:	89 c8                	mov    eax,ecx
    1206:	c1 f8 1f             	sar    eax,0x1f
    1209:	29 c2                	sub    edx,eax
    120b:	89 d0                	mov    eax,edx
    120d:	69 c0 c7 04 00 00    	imul   eax,eax,0x4c7
    1213:	29 c1                	sub    ecx,eax
    1215:	89 c8                	mov    eax,ecx
    1217:	85 c0                	test   eax,eax
    1219:	75 07                	jne    1222 <validate_key+0x34>
    121b:	b8 01 00 00 00       	mov    eax,0x1
    1220:	eb 05                	jmp    1227 <validate_key+0x39>
    1222:	b8 00 00 00 00       	mov    eax,0x0
    1227:	5d                   	pop    rbp
    1228:	c3                   	ret    
    1229:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000001230 __libc_csu_init:
    1230:	41 57                	push   r15
    1232:	49 89 d7             	mov    r15,rdx
    1235:	41 56                	push   r14
    1237:	49 89 f6             	mov    r14,rsi
    123a:	41 55                	push   r13
    123c:	41 89 fd             	mov    r13d,edi
    123f:	41 54                	push   r12
    1241:	4c 8d 25 58 2b 00 00 	lea    r12,[rip+0x2b58]        # 3da0 <__frame_dummy_init_array_entry>
    1248:	55                   	push   rbp
    1249:	48 8d 2d 58 2b 00 00 	lea    rbp,[rip+0x2b58]        # 3da8 <__do_global_dtors_aux_fini_array_entry>
    1250:	53                   	push   rbx
    1251:	4c 29 e5             	sub    rbp,r12
    1254:	48 83 ec 08          	sub    rsp,0x8
    1258:	e8 a3 fd ff ff       	call   1000 <_init>
    125d:	48 c1 fd 03          	sar    rbp,0x3
    1261:	74 1b                	je     127e <__libc_csu_init+0x4e>
    1263:	31 db                	xor    ebx,ebx
    1265:	0f 1f 00             	nop    DWORD PTR [rax]
    1268:	4c 89 fa             	mov    rdx,r15
    126b:	4c 89 f6             	mov    rsi,r14
    126e:	44 89 ef             	mov    edi,r13d
    1271:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
    1275:	48 83 c3 01          	add    rbx,0x1
    1279:	48 39 dd             	cmp    rbp,rbx
    127c:	75 ea                	jne    1268 <__libc_csu_init+0x38>
    127e:	48 83 c4 08          	add    rsp,0x8
    1282:	5b                   	pop    rbx
    1283:	5d                   	pop    rbp
    1284:	41 5c                	pop    r12
    1286:	41 5d                	pop    r13
    1288:	41 5e                	pop    r14
    128a:	41 5f                	pop    r15
    128c:	c3                   	ret    
    128d:	0f 1f 00             	nop    DWORD PTR [rax]

0000000000001290 __libc_csu_fini:
    1290:	c3                   	ret    

Disassembly of section .fini:

0000000000001294 _fini:
    1294:	48 83 ec 08          	sub    rsp,0x8
    1298:	48 83 c4 08          	add    rsp,0x8
    129c:	c3                   	ret    
```

## Ponto de entrada do binário

Através do resultado do readelf, podemos ver que a entrada do binário está em: `Entry point address: 0x1080`

## Análise e RE:

Nesse desafio, a parte mais chata é descobrir todos os bitwise que foram usados.

Existe uma função com o nome validate_key, então, foi bem tranquilo entender onde era feita a checagem do valor fornecido.

A primeira coisa que complicou foi entender que o comando IMUL separa o resultado entre os registradores EAX e EDX caso ultrapasse 8 bytes. (bom, ao menos eu não sabia disso)
Então, se o valor for 0xaaaabbbbcccc, edx=0xaaaa e eax=0xbbbbcccc

SAR representa shift right.

O primeiro shift right encontrado representa edx >> 0x7 e, depois, eax >> 0x1f, como eax contém o valor fornecido, para que o shift right produza algo superior a zero, é necessário ter um valor com 3 digitos.

Após entender o IMUL, SAR e TEST (procura saber se a comparação é igual a zero), foi bem tranquilo escrever o keygen, já que, para identificar se a chave está certa basta comparar se o valor das operações resulta em zero.

## Keygen

Rode o arquivo [keygen.py](keygen.py), receba uma key e coloque como input do keyg3nme ou, se preferir, redirecione o stdin do script em python para o executável através do comando abaixo:

```bash
./keyg3nme <<< $(python3 ./keygen.py)
Enter your key:  Good job mate, now go keygen me.
```
