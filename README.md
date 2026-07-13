# -ndexDistance
My code scans a list and compares element indexes. If two control variables are equal, it returns the index sum. E.g., for [1,3,1] with pointer1 at index 0 and pointer2 at -1 (offset to check adjacent items), the first step (1 vs 3) is skipped. In the next iteration, it finds equal values and returns the index sum.
