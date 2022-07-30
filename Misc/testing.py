import List as cl
from List import List

def add(x, y):
    if type(y) is cl.List: return y.__add__(x)
    return x.__add__(y)

def sub(x, y):
    if type(y) is cl.List: return y.__add__(x)
    return x.__add__(y)

def mul(x, y):
    if type(y) is cl.List: return y.__add__(x)
    return x.__add__(y)

def div(x, y):
    if type(y) is cl.List: return y.__add__(x)
    return x.__add__(y)

# def update_depth_hashmap_debug(self, out=False):
#     if out:
#         print("before self.init_depth_hashmap()")
#         self.print_depth_hashmap()
#     self.depth_hashmap = self.init_depth_hashmap()
#     if out: print("self.init_depth_hashmap()")
#     self.print_depth_hashmap()
#     for d in range(0, self.depth_lim):
#         if out:
#             print("for d in range(...): d -> " + str(d))
#             self.print_depth_hashmap()
#         for dn in range(0, len(self.depth_hashmap[d])):
#             lr = [self.depth_hashmap[d][dn].left,
#                   self.depth_hashmap[d][dn].right]
#             # Store children in depth_hashmap against depth
#             left, right = lr[0], lr[1]
#             if left == right is None: continue
#             if left is None: lr.extend(self.depth_hashmap[right.eval_depth()])
#             else: lr.extend(self.depth_hashmap[left.eval_depth()])
#             self.depth_hashmap[left.eval_depth()] = lr
#     if out: self.print_depth_hashmap()
#     pass

    # def crossover(self, other, out=False):
    #     """
    #     >> Select random depth, 0 < d < self.depth_lim
    #     >> Select random node at depth, d, as n1
    #     >> Do the same for NodeStruc parameter, other, as n2
    #     >> if random() > 0.5:
    #             parent_ref = n1.parent
    #             n1.left = n2.left
    #             n1.parent = parent_ref
    #         else:
    #             parent_ref = n1.parent
    #             n1.right = n2.right
    #             n1.parent = parent_ref
    #     >> Limit max depth (if crossover made depth more than og_depth)
    #     >> Update self.depth_hashmap
    #     """
    #     pass

def main():
    # a, b, c = 5, 6, [2, 2, 2]
    # d = [4, 4, 4]
    # e = [1, 1, 1]
    #
    # c = List(c)
    # d = List(d)
    # e = List(e)
    #
    # print("c ->", c)
    # print("d ->", d)
    # print("e ->", e)
    # add(a, b)
    # add(b, a)
    # add(b, c)
    # add(c, b)
    # add(d, e)

    # arr1 = [1, 2, 3]
    # arr1 = List(arr1)
    # arr1c = arr1.__copy__()
    # arr1c[2] = 5
    #
    # print(arr1, arr1c, arr1)

    # for i in range(5):
    #     print(i)

    # d = {0: [1, 2, 3], 1: [2, 3, 4]}
    # print(d[0], d[1])
    # d[2] = [3, 4, 5]
    # print
    #
    #

    a = [1, 2, 3]
    a.append(4)
    print(a)

    a.extend([0, -1, -2])
    print(a)

    b = [1, 2, 3]
    be = [-2, -1, 0]
    be.extend(b)
    print(be, b)

    print(b.pop())


if __name__ == '__main__':
    main()
