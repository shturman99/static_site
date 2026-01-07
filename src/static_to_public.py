import os
import shutil

def static_to_public(static_dir='static', public_dir='public'):
    if not os.path.exists(public_dir):
        os.makedirs(public_dir, exist_ok=True)
    else:
        shutil.rmtree(public_dir)
        print(f"Removed existing directory {public_dir}")
        os.makedirs(public_dir, exist_ok=True)

    recursive_copy(static_dir, public_dir)

def recursive_copy(static_dir, public_dir):    
    if os.path.exists(static_dir):
        for item in os.listdir(static_dir):
            s = os.path.join(static_dir, item)
            p = os.path.join(public_dir, item)

            if os.path.isdir(s):
                os.makedirs(p, exist_ok=True)
                print(f"Copied dir {s} to {p}")
                recursive_copy(s, p)
            else:
                shutil.copy2(s, p)
                print(f"Copied {s} to {p}")
    
            
    