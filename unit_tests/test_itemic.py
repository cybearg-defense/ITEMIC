import unittest
import itemic
import copy


class MyTestCase(unittest.TestCase):
    def test_jdict(self):
        this_jdict = itemic.jdict({'a': 1, 'b': 2})
        self.assertEqual(this_jdict['a'], this_jdict.a)
        self.assertEqual(this_jdict['b'], this_jdict.b)

        this_jdict_copy = copy.deepcopy(this_jdict)
        self.assertEqual(this_jdict, this_jdict_copy)

        with self.assertRaises(KeyError):
            c = this_jdict.c

    # def test_itemic_core(self):
    #     this_itemic_core = itemic.ItemicCore({'a': 1, 'b': 2})
    #     self.assertEqual(this_itemic_core['a'], this_itemic_core.a)
    #     self.assertEqual(this_itemic_core['b'], this_itemic_core.b)


if __name__ == '__main__':
    unittest.main()
