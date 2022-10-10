#!/bin/sh
py_module=networkx
curl https://pypi.org/project/${py_module}/ 2>/dev/null |grep -A1 "package-header__name" |sed -ne "s,.*${py_module} ,,p"


