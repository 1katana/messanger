
import subprocess

process=subprocess.Popen(['powershell'],stdout=subprocess.PIPE,stdin=subprocess.PIPE,text=True)

process.stdin.writelines(".\\djsite\\venv\\Scripts\\activate\n")
process.stdin.writelines("py .\\djsite\\manage.py runserver\n")
process.stdin.flush()

while True:
    print(process.stdout.readline())

