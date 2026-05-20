class Solution:
    def isProduct(self, arr, target):
        st = set()

        for x in arr:

            # Special case when target is 0
            if target == 0:
                if x == 0 and len(st) > 0:
                    return True

                for y in st:
                    if y == 0:
                        return True

            else:
                # Check if x divides target
                if x != 0 and target % x == 0:
                    need = target // x

                    if need in st:
                        return True

            st.add(x)

        return False
