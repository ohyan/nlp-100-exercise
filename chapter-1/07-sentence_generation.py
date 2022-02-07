import argparse


parser = argparse.ArgumentParser()
parser.add_argument('x')
parser.add_argument('y')
parser.add_argument('z')
args = parser.parse_args()



def generate_sentence(x, y, z):
    return f"{x}時の{y}は{z}"


if __name__ == "__main__":
    print(generate_sentence(args.x, args.y, args.z))
