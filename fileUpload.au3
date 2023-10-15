WinWaitActive("Open") ; Wait for the file dialog to appear
Sleep(1000) ; Add a short delay to ensure the dialog is ready

; Replace "File path" with the full path of the file you want to upload
ControlSetText("Open", "", "Edit1", "C:\Users\mike2\Desktop\vzls\crops\output_image.jpg")
ControlClick("Open", "", "Button1") ; Click the Open button