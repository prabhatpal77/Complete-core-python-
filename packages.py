# package is folder or dir which represent collection of python modules.
# syntax:- import packagename.modulename or
#          import packagename.subpackagename.modulename
# # we can import the properties of a module of a package or subpackage by using following import statement..
# syntax:- from package.modulename import property1, property2,.......
#          from package.subpackagename.modulename import property1, property2,.....
import pack1.a
from pack1.b import b,f2
import pack1.spack1.c as p
from pack1.spack1.d import*
print(pack1.a.a)
pack1.a.f1()
print(b)
f2()
print(p.c)
p.f3()
print(d)
f4()
#In 2.x version of python in order to make it recognize folder or directory of python package according to 2.x
# version of python we should define __init__.py file in that folder..
