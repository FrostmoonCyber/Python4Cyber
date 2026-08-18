#Trying to work with argparser

import sys
import argparse

BANNER = """                                                _                          _   
  __ _ _ __ __ _ _ __   __ _ _ __ ___  ___ _ __│ │_ _ __ _   _  ___  _   _│ │_ 
 ╱ _` │ '__╱ _` │ '_ ╲ ╱ _` │ '__╱ __│╱ _ ╲ '__│ __│ '__│ │ │ │╱ _ ╲│ │ │ │ __│
│ (_│ │ │ │ (_│ │ │_) │ (_│ │ │  ╲__ ╲  __╱ │  │ │_│ │  │ │_│ │ (_) │ │_│ │ │_ 
 ╲__,_│_│  ╲__, │ .__╱ ╲__,_│_│  │___╱╲___│_│___╲__│_│   ╲__, │╲___╱ ╲__,_│╲__│
           │___╱│_│                        │_____│       │___╱                 """


def main():
    parser = argparse.ArgumentParser(
                    prog='argparser_tryout',
                    description='Trying out argparser library and its funtionality',
                    epilog='Having fun')
    
    parser.add_argument("--target","-t", help = "Domain or checked IP", type= str)
    parser.add_argument("--version", "-v", action= "version", help = "Show version", version='%(prog)s 1.0.0' )
    args = parser.parse_args()
    
    print(BANNER)
    if args.target:
      print(f"[+] Starting audit in: {args.target}")
    else:
      parser.print_help()


if __name__ == '__main__':
    main()