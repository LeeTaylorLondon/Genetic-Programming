    # def _crossover(self, sarr):
    #     """ :param sarr: Selection Array contains index values for which
    #     population members are to be selected. """
    #     # Unpack selection array & assign values
    #     s1, s2 = sarr
    #     p1, p2 = self.population[s1], self.population[s2]
    #     sn1 = selected_node1 = p1.rand_node()
    #     sn2 = selected_node2 = p2.rand_node(ntype=sn1.eval_type())
    #     if sn1.eval_type() != sn2.eval_type(): return
    #     print('term_set', term_set)
    #     try:
    #         print('term_set.index', term_set.index(sn2.val))
    #     except ValueError:
    #         pass
    #     print("sn1.val & sn2.val")
    #     print(sn1.val, sn2.val)
    #     print("======================================")
    #     # Debug
    #     print("p1 BEFORE")
    #     p1.print_depth_hashmap()
    #     print("p2 BEFORE")
    #     p2.print_depth_hashmap()
    #     # Overwrite sn1.val
    #     if sn2.val in func_set: sn1.val = sn2.val
    #     elif sn2.val in term_set and term_set.index(sn2.val) != 0:
    #         sn1.val = term_set.index(sn2.val)
    #     else: sn1.val = term_set[0]
    #     # Reset computed-value
    #     sn1.cval = None
    #     p1.reset_cval_all_c()
    #     # Overwrite left & right
    #     sn1.left  = sn2.left
    #     sn1.right = sn2.right
    #     # Debug
    #     print('p1 AFTER')
    #     p1.print_depth_hashmap()
