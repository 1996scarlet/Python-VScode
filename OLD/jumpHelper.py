import os

output = os.popen("adb start-server")
print(output.read())

while True:

    try:
        n = int(float(input("你想续多少毫秒啊：")) * 220)
    except:
        break

    print(n)
    os.popen("adb shell input swipe 400 400 400 400 %d" % n)

output = os.popen("adb kill-server")
print(output.read())

# n=850
# os.popen("adb shell input swipe 400 400 400 400 %d" %n)
#550-2.5
#900-4.2
#220-1cm