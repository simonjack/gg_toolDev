
@echo on
SET _test=C:\SVNs\Art\Models
set C = bin\client\art

for /f "tokens=1* delims=Art" %%a in ("%_test%") do (
  set part1=%%a
  set part2=%%b
) 

set fpppath = %part1%%C%%part2%
echo %fpppath%