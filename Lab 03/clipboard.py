#!/usr/bin/python3

import subprocess
import time

look_for = ("cyberbezpieczeństwo", "cyberbezpieczenstwo", "CYBERBEZPIECZEŃSTWO", "CYBERBEZPIECZENSTWO")
change_to = "cyberprzestępczość"

def detect():
    while True:
        time.sleep(0.5)

        proc = subprocess.Popen(['xsel', '-b', '-o'], stdout = subprocess.PIPE)
        clip, _ = proc.communicate()
        clip = clip.decode('utf-8')

        for word in look_for:
            if word in clip:
                clip = clip.replace(word, change_to)

                proc = subprocess.Popen(['xsel', '-b', '-i'], stdin = subprocess.PIPE)
                proc.communicate(clip.encode('utf-8'))
                    

if __name__ == "__main__":
    detect()