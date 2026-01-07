from textnode import *
from static_to_public  import *
import os

public_dir="./public"
static_dir="./static"


def main():

    static_to_public(static_dir, public_dir)

if __name__=="__main__":
    main()
