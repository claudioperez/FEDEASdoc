
import argparse, os
from pathlib import Path
import yaml

example_path = Path("docs/Examples")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",nargs="*")
    args = parser.parse_args()
    print(args)
    with open(args.filename[0],"r") as f:
        example_data = yaml.load(f,Loader=yaml.Loader)

    for example in example_data['references']:
        try:
            with open(example_path/example['id']/"meta.yaml","w+") as f:
                f.write(yaml.dump(example))
        except Exception as e: print(e)

if __name__ == "__main__":
    main()