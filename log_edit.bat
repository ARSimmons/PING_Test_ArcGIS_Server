@echo off
setlocal enabledelayedexpansion
set hostIP=
:loop
set pingline=1
for /f "delims=" %%A in ('ping -n 1 -w 250 -l 255 %hostIP%') do (
	if !pingline! equ 2 (
		set logline=!date! !time! "%%A" 
		echo !logline! | find "TTL=">nul || (
			set logline=!logline:"=!
			echo !logline! >> pinglog.txt
			)
		)
	set /a pingline+=1
	)
:sleep 5000
goto loop