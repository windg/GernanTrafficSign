def merge(nums1, nums2):

    pivot1 = 0
    pivot2 = 0
    leng1 = len(nums1)
    leng2 = len(nums2)
    combined = []
    while pivot1 < leng1 and pivot2 < leng2:

        if nums1[pivot1] < nums2[pivot2]:
            combined.append(nums1[pivot1])
            pivot1 += 1
        else:
            combined.append(nums2[pivot2])
            pivot2 += 1

    if pivot1 == leng1:
        combined += nums2[pivot2:]
    else:
        combined += nums1[pivot1:]

    midindex = 0.5 * (leng1 + leng2) - 0.5
    import math
    return 0.5 * (combined[math.floor(midindex)] + combined[math.ceil(midindex)])

a = [2]
b = [0]

print(merge(a,b))