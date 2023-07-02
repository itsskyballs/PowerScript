Set Shell = CreateObject("wscript.shell")

Answer = MsgBox("Turn Off Computer?",vbYesNo+64,"PowerScript By Steven Kieth")
	If Answer = vbYes Then
		shell.run "shutdown -s"
		Ending = 1


End If
