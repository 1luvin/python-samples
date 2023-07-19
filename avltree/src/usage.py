from avltree import AVLTree


def main():
    tree = AVLTree()

    print('Tree:')
    for i in range(1, 6):
        tree.insert(i)

    tree.print()

    if tree.contains(2):
        print('Contains value - 2')

    tree.remove(2)

    if tree.contains(2):
        print('Contains value - 2')

    print('Min value - {}'.format(tree.get_min_value()))
    print('Max value - {}'.format(tree.get_max_value()))

    if not tree.is_empty():
        print('Hello, forest! I am a beautiful tree with many branches!')

    tree.clear()

    if tree.is_empty():
        print('Where have all my branches gone?')


if __name__ == '__main__':
    main()
