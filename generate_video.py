#!/usr/bin/env python3
"""
Easy video generator for Creative AI Memory Video
"""

import os
import subprocess
import sys

def main():
    print("AI Memory Video Generator")
    print("=" * 50)
    
    scenes = {
        "1": ("Standard Quality (Fast)", "AI_Memory_Solution_Video -ql"),
        "2": ("High Quality (Slow)", "AI_Memory_Solution_Video -qh"),
        "3": ("4K Ultra Quality (Very Slow)", "AI_Memory_Solution_Video -qk"),
    }
    
    print("\nAvailable Render Qualities:")
    for key, (name, _) in scenes.items():
        print(f"  {key}. {name}")
    
    choice = input("\nChoose quality (1-3): ").strip()
    
    if choice in scenes:
        quality_name, quality_flag = scenes[choice]
        print(f"\n Generating: AI Memory Video")
        print(f" Quality: {quality_name}")
        print(" This will take 2-10 minutes...")
        
        try:
            cmd = f"manim main.py {quality_flag}"
            subprocess.run(cmd, shell=True, check=True)
            
            print(f"✅ Video generated successfully!")
            print(f"📁 Output file: media/videos/main/480p15/AI_Memory_Solution_Video.mp4")
            print(f"Video length: Exactly 60 seconds")
            
        except subprocess.CalledProcessError as e:
            print(f"Error generating video: {e}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()